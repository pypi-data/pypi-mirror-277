// SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
//
// SPDX-License-Identifier: MPL-2.0

#pragma once

// main model class

// main include
#include "batch_parameter.hpp"
#include "calculation_parameters.hpp"
#include "container.hpp"
#include "topology.hpp"

// common
#include "common/common.hpp"
#include "common/exception.hpp"
#include "common/timer.hpp"

// component include
#include "all_components.hpp"
#include "auxiliary/dataset.hpp"
#include "auxiliary/input.hpp"
#include "auxiliary/output.hpp"

// math model include
#include "math_solver/math_solver.hpp"

#include "optimizer/optimizer.hpp"

// main model implementation
#include "main_core/calculation_info.hpp"
#include "main_core/input.hpp"
#include "main_core/math_state.hpp"
#include "main_core/output.hpp"
#include "main_core/topology.hpp"
#include "main_core/update.hpp"

// stl library
#include <memory>
#include <span>
#include <thread>

namespace power_grid_model {

// solver output type to output type getter meta function

template <solver_output_type SolverOutputType> struct output_type_getter;
template <short_circuit_solver_output_type SolverOutputType> struct output_type_getter<SolverOutputType> {
    template <class T> using type = meta_data::sc_output_getter_s<T>;
};
template <> struct output_type_getter<SolverOutput<symmetric_t>> {
    template <class T> using type = meta_data::sym_output_getter_s<T>;
};
template <> struct output_type_getter<SolverOutput<asymmetric_t>> {
    template <class T> using type = meta_data::asym_output_getter_s<T>;
};

// main model implementation template
template <class T, class U> class MainModelImpl;

template <class... ExtraRetrievableType, class... ComponentType>
class MainModelImpl<ExtraRetrievableTypes<ExtraRetrievableType...>, ComponentList<ComponentType...>> {
  private:
    // internal type traits
    // container class
    using ComponentContainer = Container<ExtraRetrievableTypes<ExtraRetrievableType...>, ComponentType...>;
    using MainModelState = main_core::MainModelState<ComponentContainer>;
    using MathState = main_core::MathState;

    template <class CT>
    static constexpr size_t index_of_component = container_impl::get_cls_pos_v<CT, ComponentType...>;

    // trait on type list
    // struct of entry
    // name of the component, and the index in the list
    struct ComponentEntry {
        char const* name;
        size_t index;
    };

    static constexpr size_t n_types = sizeof...(ComponentType);

    using SequenceIdx = std::array<std::vector<Idx2D>, n_types>;

    using OwnedUpdateDataset = std::tuple<std::vector<typename ComponentType::UpdateType>...>;

    static constexpr Idx ignore_output{-1};

    // run functors with all component types
    template <class Functor> static constexpr void run_functor_with_all_types_return_void(Functor functor) {
        (functor.template operator()<ComponentType>(), ...);
    }
    template <class Functor> static constexpr auto run_functor_with_all_types_return_array(Functor functor) {
        return std::array{functor.template operator()<ComponentType>()...};
    }

  public:
    struct cached_update_t : std::true_type {};

    struct permanent_update_t : std::false_type {};

    struct Options {
        static constexpr Idx sequential = -1;

        CalculationMethod calculation_method{CalculationMethod::default_method};
        OptimizerType optimizer_type{OptimizerType::no_optimization};
        OptimizerStrategy optimizer_strategy{OptimizerStrategy::any};

        double err_tol{1e-8};
        Idx max_iter{20};
        Idx threading{sequential};

        ShortCircuitVoltageScaling short_circuit_voltage_scaling{ShortCircuitVoltageScaling::maximum};
    };

    // constructor with data
    explicit MainModelImpl(double system_frequency, ConstDataset const& input_data, Idx pos = 0)
        : system_frequency_{system_frequency}, meta_data_{&input_data.meta_data()} {
        assert(input_data.get_description().dataset->name == std::string_view("input"));
        auto const add_func = [this, pos, &input_data]<typename CT>() {
            this->add_component<CT>(input_data.get_buffer_span<meta_data::input_getter_s, CT>(pos));
        };
        run_functor_with_all_types_return_void(add_func);
        set_construction_complete();
    }

    // constructor with only frequency
    explicit MainModelImpl(double system_frequency, meta_data::MetaData const& meta_data)
        : system_frequency_{system_frequency}, meta_data_{&meta_data} {}

    // get number
    template <class CompType> Idx component_count() const {
        assert(construction_complete_);
        return state_.components.template size<CompType>();
    }

    // all component count
    std::map<std::string, Idx> all_component_count() const {
        auto const get_comp_count = [this]<typename CT>() -> std::pair<std::string, Idx> {
            return make_pair(std::string{CT::name}, this->component_count<CT>());
        };
        auto const all_count = run_functor_with_all_types_return_array(get_comp_count);
        std::map<std::string, Idx> result;
        for (auto const& [name, count] : all_count) {
            if (count > 0) {
                // only add if count is greater than 0
                result[name] = count;
            }
        }
        return result;
    }

    // helper function to add vectors of components
    template <class CompType> void add_component(std::vector<typename CompType::InputType> const& components) {
        add_component<CompType>(components.begin(), components.end());
    }
    template <class CompType> void add_component(std::span<typename CompType::InputType const> components) {
        add_component<CompType>(components.begin(), components.end());
    }

    // template to construct components
    // using forward interators
    // different selection based on component type
    template <std::derived_from<Base> CompType, std::forward_iterator ForwardIterator>
    void add_component(ForwardIterator begin, ForwardIterator end) {
        assert(!construction_complete_);
        main_core::add_component<CompType>(state_, begin, end, system_frequency_);
    }

    // template to update components
    // using forward interators
    // different selection based on component type
    // if sequence_idx is given, it will be used to load the object instead of using IDs via hash map.
    template <class CompType, class CacheType, std::forward_iterator ForwardIterator>
    void update_component(ForwardIterator begin, ForwardIterator end, std::vector<Idx2D> const& sequence_idx) {
        constexpr auto comp_index = index_of_component<CompType>;

        assert(construction_complete_);
        assert(static_cast<ptrdiff_t>(sequence_idx.size()) == std::distance(begin, end));

        if constexpr (CacheType::value) {
            main_core::update_inverse<CompType>(
                state_, begin, end, std::back_inserter(std::get<comp_index>(cached_inverse_update_)), sequence_idx);
        }

        UpdateChange const changed = main_core::update_component<CompType>(
            state_, begin, end, std::back_inserter(std::get<comp_index>(parameter_changed_components_)), sequence_idx);

        // update, get changed variable
        update_state(changed);
        if constexpr (CacheType::value) {
            cached_state_changes_ = cached_state_changes_ || changed;
        }
    }

    // helper function to update vectors of components
    template <class CompType, class CacheType>
    void update_component(std::vector<typename CompType::UpdateType> const& components,
                          std::vector<Idx2D> const& sequence_idx) {
        if (!components.empty()) {
            update_component<CompType, CacheType>(components.begin(), components.end(), sequence_idx);
        }
    }
    template <class CompType, class CacheType>
    void update_component(std::span<typename CompType::UpdateType const> components,
                          std::vector<Idx2D> const& sequence_idx) {
        if (!components.empty()) {
            update_component<CompType, CacheType>(components.begin(), components.end(), sequence_idx);
        }
    }

    // update all components
    template <class CacheType>
    void update_component(ConstDataset const& update_data, Idx pos, SequenceIdx const& sequence_idx_map) {
        assert(construction_complete_);
        assert(update_data.get_description().dataset->name == std::string_view("update"));
        auto const update_func = [this, pos, &update_data, &sequence_idx_map]<typename CT>() {
            this->update_component<CT, CacheType>(update_data.get_buffer_span<meta_data::update_getter_s, CT>(pos),
                                                  sequence_idx_map[index_of_component<CT>]);
        };
        run_functor_with_all_types_return_void(update_func);
    }

    // update all components
    template <class CacheType> void update_component(ConstDataset const& update_data, Idx pos = 0) {
        update_component<CacheType>(update_data, pos, get_sequence_idx_map(update_data));
    }

    template <typename CompType> void restore_component(SequenceIdx const& sequence_idx) {
        constexpr auto component_index = index_of_component<CompType>;

        auto& cached_inverse_update = std::get<component_index>(cached_inverse_update_);
        auto const& component_sequence = std::get<component_index>(sequence_idx);

        if (!cached_inverse_update.empty()) {
            update_component<CompType, permanent_update_t>(cached_inverse_update, component_sequence);
            cached_inverse_update.clear();
        }
    }

    // restore the initial values of all components
    void restore_components(SequenceIdx const& sequence_idx) {
        (restore_component<ComponentType>(sequence_idx), ...);

        update_state(cached_state_changes_);
        cached_state_changes_ = {};
    }

    // set complete construction
    // initialize internal arrays
    void set_construction_complete() {
        assert(!construction_complete_);
#ifndef NDEBUG
        // set construction_complete for debug assertions
        construction_complete_ = true;
#endif // !NDEBUG
        state_.components.set_construction_complete();
        construct_topology();
    }

    void construct_topology() {
        ComponentTopology comp_topo;
        main_core::register_topology_components<Node>(state_, comp_topo);
        main_core::register_topology_components<Branch>(state_, comp_topo);
        main_core::register_topology_components<Branch3>(state_, comp_topo);
        main_core::register_topology_components<Source>(state_, comp_topo);
        main_core::register_topology_components<Shunt>(state_, comp_topo);
        main_core::register_topology_components<GenericLoadGen>(state_, comp_topo);
        main_core::register_topology_components<GenericVoltageSensor>(state_, comp_topo);
        main_core::register_topology_components<GenericPowerSensor>(state_, comp_topo);
        main_core::register_topology_components<Regulator>(state_, comp_topo);
        state_.comp_topo = std::make_shared<ComponentTopology const>(std::move(comp_topo));
    }

    void reset_solvers() {
        assert(construction_complete_);
        is_topology_up_to_date_ = false;
        is_sym_parameter_up_to_date_ = false;
        is_asym_parameter_up_to_date_ = false;
        n_math_solvers_ = 0;
        main_core::clear(math_state_);
        state_.math_topology.clear();
        state_.topo_comp_coup.reset();
        state_.comp_coup = {};
    }

    /*
    the the sequence indexer given an input array of ID's for a given component type
    */
    void get_indexer(std::string_view component_type, ID const* id_begin, Idx size, Idx* indexer_begin) const {
        auto const get_index_func = [&state = this->state_, component_type, id_begin, size,
                                     indexer_begin]<typename CT>() {
            if (component_type == CT::name) {
                std::transform(id_begin, id_begin + size, indexer_begin,
                               [&state](ID id) { return main_core::get_component_idx_by_id<CT>(state, id).pos; });
            }
        };
        run_functor_with_all_types_return_void(get_index_func);
    }

    // get sequence idx map of a certain batch scenario
    SequenceIdx get_sequence_idx_map(ConstDataset const& update_data, Idx scenario_idx) const {

        auto const get_seq_idx_func = [&state = this->state_, &update_data,
                                       scenario_idx]<typename CT>() -> std::vector<Idx2D> {
            auto const buffer_span = update_data.get_buffer_span<meta_data::update_getter_s, CT>(scenario_idx);
            auto const it_begin = buffer_span.begin();
            auto const it_end = buffer_span.end();
            return main_core::get_component_sequence<CT>(state, it_begin, it_end);
        };
        return run_functor_with_all_types_return_array(get_seq_idx_func);
    }

    // get sequence idx map of an entire batch for fast caching of component sequences
    // (only applicable for independent update dataset)
    SequenceIdx get_sequence_idx_map(ConstDataset const& update_data) const {
        assert(is_update_independent(update_data));
        return get_sequence_idx_map(update_data, 0);
    }

  private:
    void update_state(const UpdateChange& changes) {
        // if topology changed, everything is not up to date
        // if only param changed, set param to not up to date
        is_topology_up_to_date_ = is_topology_up_to_date_ && !changes.topo;
        is_sym_parameter_up_to_date_ = is_sym_parameter_up_to_date_ && !changes.topo && !changes.param;
        is_asym_parameter_up_to_date_ = is_asym_parameter_up_to_date_ && !changes.topo && !changes.param;
    }

    template <solver_output_type SolverOutputType, typename MathSolverType, typename YBus, typename InputType,
              typename PrepareInputFn, typename SolveFn>
        requires std::invocable<std::remove_cvref_t<PrepareInputFn>, Idx /*n_math_solvers*/> &&
                 std::invocable<std::remove_cvref_t<SolveFn>, MathSolverType&, YBus const&, InputType const&> &&
                 std::same_as<std::invoke_result_t<PrepareInputFn, Idx /*n_math_solvers*/>, std::vector<InputType>> &&
                 std::same_as<std::invoke_result_t<SolveFn, MathSolverType&, YBus const&, InputType const&>,
                              SolverOutputType>
    std::vector<SolverOutputType> calculate_(PrepareInputFn&& prepare_input, SolveFn&& solve) {
        using sym = typename SolverOutputType::sym;

        assert(construction_complete_);
        calculation_info_ = CalculationInfo{};
        // prepare
        auto const& input = [this, &prepare_input] {
            Timer const timer(calculation_info_, 2100, "Prepare");
            prepare_solvers<sym>();
            assert(is_topology_up_to_date_ && is_parameter_up_to_date<sym>());
            return prepare_input(n_math_solvers_);
        }();
        // calculate
        return [this, &input, &solve] {
            Timer const timer(calculation_info_, 2200, "Math Calculation");
            auto& solvers = get_solvers<sym>();
            auto& y_bus_vec = get_y_bus<sym>();
            std::vector<SolverOutputType> solver_output;
            solver_output.reserve(n_math_solvers_);
            for (Idx i = 0; i != n_math_solvers_; ++i) {
                solver_output.emplace_back(solve(solvers[i], y_bus_vec[i], input[i]));
            }
            return solver_output;
        }();
    }

    template <symmetry_tag sym> auto calculate_power_flow_(double err_tol, Idx max_iter) {
        return [this, err_tol, max_iter](MainModelState const& state,
                                         CalculationMethod calculation_method) -> std::vector<SolverOutput<sym>> {
            return calculate_<SolverOutput<sym>, MathSolver<sym>, YBus<sym>, PowerFlowInput<sym>>(
                [&state](Idx n_math_solvers) { return prepare_power_flow_input<sym>(state, n_math_solvers); },
                [this, err_tol, max_iter, calculation_method](MathSolver<sym>& solver, YBus<sym> const& y_bus,
                                                              PowerFlowInput<sym> const& input) {
                    return solver.run_power_flow(input, err_tol, max_iter, calculation_info_, calculation_method,
                                                 y_bus);
                });
        };
    }

    template <symmetry_tag sym> auto calculate_state_estimation_(double err_tol, Idx max_iter) {
        return [this, err_tol, max_iter](MainModelState const& state,
                                         CalculationMethod calculation_method) -> std::vector<SolverOutput<sym>> {
            return calculate_<SolverOutput<sym>, MathSolver<sym>, YBus<sym>, StateEstimationInput<sym>>(
                [&state](Idx n_math_solvers) { return prepare_state_estimation_input<sym>(state, n_math_solvers); },
                [this, err_tol, max_iter, calculation_method](MathSolver<sym>& solver, YBus<sym> const& y_bus,
                                                              StateEstimationInput<sym> const& input) {
                    return solver.run_state_estimation(input, err_tol, max_iter, calculation_info_, calculation_method,
                                                       y_bus);
                });
        };
    }

    template <symmetry_tag sym> auto calculate_short_circuit_(ShortCircuitVoltageScaling voltage_scaling) {
        return [this,
                voltage_scaling](MainModelState const& /*state*/,
                                 CalculationMethod calculation_method) -> std::vector<ShortCircuitSolverOutput<sym>> {
            return calculate_<ShortCircuitSolverOutput<sym>, MathSolver<sym>, YBus<sym>, ShortCircuitInput>(
                [this, voltage_scaling](Idx /* n_math_solvers */) {
                    assert(is_topology_up_to_date_ && is_parameter_up_to_date<sym>());
                    return prepare_short_circuit_input<sym>(voltage_scaling);
                },
                [this, calculation_method](MathSolver<sym>& solver, YBus<sym> const& y_bus,
                                           ShortCircuitInput const& input) {
                    return solver.run_short_circuit(input, calculation_info_, calculation_method, y_bus);
                });
        };
    }

    /*
    run the calculation function in batch on the provided update data.

    The calculation function should be able to run standalone.
    It should output to the provided result_data if the trailing argument is not ignore_output.

    threading
        < 0 sequential
        = 0 parallel, use number of hardware threads
        > 0 specify number of parallel threads
    raise a BatchCalculationError if any of the calculations in the batch raised an exception
    */
    template <typename Calculate>
        requires std::invocable<std::remove_cvref_t<Calculate>, MainModelImpl&, MutableDataset const&, Idx>
    BatchParameter batch_calculation_(Calculate&& calculation_fn, MutableDataset const& result_data,
                                      ConstDataset const& update_data, Idx threading = -1) {
        // if the update dataset is empty without any component
        // execute one power flow in the current instance, no batch calculation is needed
        if (update_data.empty()) {
            calculation_fn(*this, result_data, 0);
            return BatchParameter{};
        }

        // get batch size
        Idx const n_scenarios = update_data.batch_size();

        // if the batch_size is zero, it is a special case without doing any calculations at all
        // we consider in this case the batch set is independent and but not topology cachable
        if (n_scenarios == 0) {
            return BatchParameter{};
        }

        // calculate once to cache topology, ignore results, all math solvers are initialized
        try {
            calculation_fn(*this,
                           {
                               false,
                               1,
                               "sym_output",
                               *meta_data_,
                           },
                           ignore_output);
        } catch (const SparseMatrixError&) {
            // missing entries are provided in the update data
        } catch (const NotObservableError&) {
            // missing entries are provided in the update data
        }

        // error messages
        std::vector<std::string> exceptions(n_scenarios, "");
        std::vector<CalculationInfo> infos(n_scenarios);

        // lambda for sub batch calculation
        auto sub_batch = sub_batch_calculation_(calculation_fn, result_data, update_data, exceptions, infos);

        batch_dispatch(sub_batch, n_scenarios, threading);

        handle_batch_exceptions(exceptions);
        calculation_info_ = main_core::merge_calculation_info(infos);

        return BatchParameter{};
    }

    template <typename Calculate>
        requires std::invocable<std::remove_cvref_t<Calculate>, MainModelImpl&, MutableDataset const&, Idx>
    auto sub_batch_calculation_(Calculate&& calculation_fn, MutableDataset const& result_data,
                                ConstDataset const& update_data, std::vector<std::string>& exceptions,
                                std::vector<CalculationInfo>& infos) {
        // const ref of current instance
        MainModelImpl const& base_model = *this;

        // cache component update order if possible
        bool const is_independent = MainModelImpl::is_update_independent(update_data);

        return [&base_model, &exceptions, &infos, &calculation_fn, &result_data, &update_data,
                is_independent](Idx start, Idx stride, Idx n_scenarios) {
            assert(n_scenarios <= narrow_cast<Idx>(exceptions.size()));
            assert(n_scenarios <= narrow_cast<Idx>(infos.size()));

            Timer const t_total(infos[start], 0000, "Total in thread");

            auto copy_model = [&base_model, &infos](Idx scenario_idx) {
                Timer const t_copy_model(infos[scenario_idx], 1100, "Copy model");
                return MainModelImpl{base_model};
            };
            auto model = copy_model(start);

            SequenceIdx scenario_sequence = is_independent ? model.get_sequence_idx_map(update_data) : SequenceIdx{};

            auto [setup, winddown] =
                scenario_update_restore(model, update_data, is_independent, scenario_sequence, infos);

            auto calculate_scenario = MainModelImpl::call_with<Idx>(
                [&model, &calculation_fn, &result_data, &infos](Idx scenario_idx) {
                    calculation_fn(model, result_data, scenario_idx);
                    infos[scenario_idx].merge(model.calculation_info_);
                },
                std::move(setup), std::move(winddown), scenario_exception_handler(model, exceptions, infos),
                [&model, &copy_model](Idx scenario_idx) { model = copy_model(scenario_idx); });

            for (Idx scenario_idx = start; scenario_idx < n_scenarios; scenario_idx += stride) {
                Timer const t_total_single(infos[scenario_idx], 0100, "Total single calculation in thread");

                calculate_scenario(scenario_idx);
            }
        };
    }

    // run sequential if
    //    specified threading < 0
    //    use hardware threads, but it is either unknown (0) or only has one thread (1)
    //    specified threading = 1
    template <typename RunSubBatchFn>
        requires std::invocable<std::remove_cvref_t<RunSubBatchFn>, Idx /*start*/, Idx /*stride*/, Idx /*n_scenarios*/>
    static void batch_dispatch(RunSubBatchFn sub_batch, Idx n_scenarios, Idx threading) {
        // run batches sequential or parallel
        auto const hardware_thread = static_cast<Idx>(std::thread::hardware_concurrency());
        if (threading < 0 || threading == 1 || (threading == 0 && hardware_thread < 2)) {
            // run all in sequential
            sub_batch(0, 1, n_scenarios);
        } else {
            // create parallel threads
            Idx const n_thread = std::min(threading == 0 ? hardware_thread : threading, n_scenarios);
            std::vector<std::thread> threads;
            threads.reserve(n_thread);
            for (Idx thread_number = 0; thread_number < n_thread; ++thread_number) {
                // compute each sub batch with stride
                threads.emplace_back(sub_batch, thread_number, n_thread, n_scenarios);
            }
            for (auto& thread : threads) {
                thread.join();
            }
        }
    }

    template <typename... Args, typename RunFn, typename SetupFn, typename WinddownFn, typename HandleExceptionFn,
              typename RecoverFromBadFn>
        requires std::invocable<std::remove_cvref_t<RunFn>, Args const&...> &&
                 std::invocable<std::remove_cvref_t<SetupFn>, Args const&...> &&
                 std::invocable<std::remove_cvref_t<WinddownFn>, Args const&...> &&
                 std::invocable<std::remove_cvref_t<HandleExceptionFn>, Args const&...> &&
                 std::invocable<std::remove_cvref_t<RecoverFromBadFn>, Args const&...>
    static auto call_with(RunFn run, SetupFn setup, WinddownFn winddown, HandleExceptionFn handle_exception,
                          RecoverFromBadFn recover_from_bad) {
        return [setup_ = std::move(setup), run_ = std::move(run), winddown_ = std::move(winddown),
                handle_exception_ = std::move(handle_exception),
                recover_from_bad_ = std::move(recover_from_bad)](Args const&... args) {
            try {
                setup_(args...);
                run_(args...);
                winddown_(args...);
            } catch (...) {
                handle_exception_(args...);
                try {
                    winddown_(args...);
                } catch (...) {
                    recover_from_bad_(args...);
                }
            }
        };
    }

    static auto scenario_update_restore(MainModelImpl& model, ConstDataset const& update_data,
                                        bool const is_independent, SequenceIdx& scenario_sequence,
                                        std::vector<CalculationInfo>& infos) {
        return std::make_pair(
            [&model, &update_data, &scenario_sequence, is_independent, &infos](Idx scenario_idx) {
                Timer const t_update_model(infos[scenario_idx], 1200, "Update model");
                if (!is_independent) {
                    scenario_sequence = model.get_sequence_idx_map(update_data, scenario_idx);
                }
                model.template update_component<cached_update_t>(update_data, scenario_idx, scenario_sequence);
            },
            [&model, &scenario_sequence, is_independent, &infos](Idx scenario_idx) {
                Timer const t_update_model(infos[scenario_idx], 1201, "Restore model");
                model.restore_components(scenario_sequence);
                if (!is_independent) {
                    std::ranges::for_each(scenario_sequence, [](auto& comp_seq_idx) { comp_seq_idx.clear(); });
                }
            });
    }

    // Lippincott pattern
    static auto scenario_exception_handler(MainModelImpl& model, std::vector<std::string>& messages,
                                           std::vector<CalculationInfo>& infos) {
        return [&model, &messages, &infos](Idx scenario_idx) {
            std::exception_ptr const ex_ptr = std::current_exception();
            try {
                std::rethrow_exception(ex_ptr);
            } catch (std::exception const& ex) {
                messages[scenario_idx] = ex.what();
            } catch (...) {
                messages[scenario_idx] = "unknown exception";
            }
            infos[scenario_idx].merge(model.calculation_info_);
        };
    }

    static void handle_batch_exceptions(std::vector<std::string> const& exceptions) {
        std::string combined_error_message;
        IdxVector failed_scenarios;
        std::vector<std::string> err_msgs;
        for (Idx batch = 0; batch < static_cast<Idx>(exceptions.size()); ++batch) {
            // append exception if it is not empty
            if (!exceptions[batch].empty()) {
                combined_error_message += "Error in batch #" + std::to_string(batch) + ": " + exceptions[batch];
                failed_scenarios.push_back(batch);
                err_msgs.push_back(exceptions[batch]);
            }
        }
        if (!combined_error_message.empty()) {
            throw BatchCalculationError(combined_error_message, failed_scenarios, err_msgs);
        }
    }

  public:
    template <class Component> using UpdateType = typename Component::UpdateType;

    static bool is_update_independent(ConstDataset const& update_data) {
        // If the batch size is (0 or) 1, then the update data for this component is 'independent'
        if (update_data.batch_size() <= 1) {
            return true;
        }

        auto const is_component_update_independent = [&update_data]<typename CT>() -> bool {
            // get span of all the update data
            auto const all_spans = update_data.get_buffer_span_all_scenarios<meta_data::update_getter_s, CT>();
            // Remember the first batch size, then loop over the remaining batches and check if they are of the same
            // length
            auto const elements_per_scenario = static_cast<Idx>(all_spans.front().size());
            bool const uniform_batch = std::ranges::all_of(all_spans, [elements_per_scenario](auto const& span) {
                return static_cast<Idx>(span.size()) == elements_per_scenario;
            });
            if (!uniform_batch) {
                return false;
            }
            if (elements_per_scenario == 0) {
                return true;
            }
            // Remember the begin iterator of the first scenario, then loop over the remaining scenarios and check the
            // ids
            auto const first_span = all_spans[0];
            // check the subsequent scenarios
            // only return true if all scenarios match the ids of the first batch
            return std::all_of(all_spans.cbegin() + 1, all_spans.cend(), [&first_span](auto const& current_span) {
                return std::ranges::equal(
                    current_span, first_span,
                    [](UpdateType<CT> const& obj, UpdateType<CT> const& first) { return obj.id == first.id; });
            });
        };

        // check all components
        auto const update_independent = run_functor_with_all_types_return_array(is_component_update_independent);
        return std::ranges::all_of(update_independent, [](bool const is_independent) { return is_independent; });
    }

    template <symmetry_tag sym> auto calculate_power_flow(Options const& options) {
        return optimizer::get_optimizer<MainModelState, ConstDataset>(
                   options.optimizer_type, options.optimizer_strategy,
                   calculate_power_flow_<sym>(options.err_tol, options.max_iter),
                   [this](ConstDataset update_data) { this->update_component<permanent_update_t>(update_data); },
                   *meta_data_)
            ->optimize(state_, options.calculation_method);
    }

    // Single load flow calculation, propagating the results to result_data
    template <symmetry_tag sym>
    void calculate_power_flow(Options const& options, MutableDataset const& result_data, Idx pos = 0) {
        assert(construction_complete_);
        auto const math_output = calculate_power_flow<sym>(options);

        if (pos != ignore_output) {
            output_result(math_output, result_data, pos);
        }
    }

    // Batch load flow calculation, propagating the results to result_data
    template <symmetry_tag sym>
    BatchParameter calculate_power_flow(Options const& options, MutableDataset const& result_data,
                                        ConstDataset const& update_data) {
        return batch_calculation_(
            [&options](MainModelImpl& model, MutableDataset const& target_data, Idx pos) {
                auto sub_opt = options; // copy
                sub_opt.err_tol = pos != ignore_output ? options.err_tol : std::numeric_limits<double>::max();
                sub_opt.max_iter = pos != ignore_output ? options.max_iter : 1;

                model.calculate_power_flow<sym>(sub_opt, target_data, pos);
            },
            result_data, update_data, options.threading);
    }

    // Single state estimation calculation, returning math output results
    template <symmetry_tag sym> auto calculate_state_estimation(Options const& options) {
        return MathOutput<std::vector<SolverOutput<sym>>>{
            .solver_output =
                calculate_state_estimation_<sym>(options.err_tol, options.max_iter)(state_, options.calculation_method),
            .optimizer_output = {}};
    }

    // Single state estimation calculation, propagating the results to result_data
    template <symmetry_tag sym>
    void calculate_state_estimation(Options const& options, MutableDataset const& result_data, Idx pos = 0) {
        assert(construction_complete_);
        auto const solver_output = calculate_state_estimation<sym>(options);

        if (pos != ignore_output) {
            output_result(solver_output, result_data, pos);
        }
    }

    // Batch state estimation calculation, propagating the results to result_data
    template <symmetry_tag sym>
    BatchParameter calculate_state_estimation(Options const& options, MutableDataset const& result_data,
                                              ConstDataset const& update_data) {
        return batch_calculation_(
            [&options](MainModelImpl& model, MutableDataset const& target_data, Idx pos) {
                auto sub_opt = options; // copy

                sub_opt.err_tol = pos != ignore_output ? options.err_tol : std::numeric_limits<double>::max();
                sub_opt.max_iter = pos != ignore_output ? options.max_iter : 1;

                model.calculate_state_estimation<sym>(sub_opt, target_data, pos);
            },
            result_data, update_data, options.threading);
    }

    // Single short circuit calculation, returning short circuit math output results
    template <symmetry_tag sym> auto calculate_short_circuit(Options const& options) {
        return MathOutput<std::vector<ShortCircuitSolverOutput<sym>>>{
            .solver_output = calculate_short_circuit_<sym>(options.short_circuit_voltage_scaling)(
                state_, options.calculation_method),
            .optimizer_output = {}};
    }

    // Single short circuit calculation, propagating the results to result_data
    void calculate_short_circuit(Options const& options, MutableDataset const& result_data, Idx pos = 0) {
        assert(construction_complete_);
        if (std::all_of(state_.components.template citer<Fault>().begin(),
                        state_.components.template citer<Fault>().end(),
                        [](Fault const& fault) { return fault.get_fault_type() == FaultType::three_phase; })) {
            auto const solver_output = calculate_short_circuit<symmetric_t>(options);
            output_result(solver_output, result_data, pos);
        } else {
            auto const solver_output = calculate_short_circuit<asymmetric_t>(options);
            output_result(solver_output, result_data, pos);
        }
    }

    // Batch load flow calculation, propagating the results to result_data
    BatchParameter calculate_short_circuit(Options const& options, MutableDataset const& result_data,
                                           ConstDataset const& update_data) {
        return batch_calculation_(
            [&options](MainModelImpl& model, MutableDataset const& target_data, Idx pos) {
                if (pos != ignore_output) {
                    model.calculate_short_circuit(options, target_data, pos);
                }
            },
            result_data, update_data, options.threading);
    }

    template <typename Component, typename MathOutputType, std::forward_iterator ResIt>
        requires solver_output_type<typename MathOutputType::SolverOutputType::value_type>
    ResIt output_result(MathOutputType const& math_output, ResIt res_it) const {
        assert(construction_complete_);
        return main_core::output_result<Component, ComponentContainer>(state_, math_output, res_it);
    }

    template <solver_output_type SolverOutputType>
    void output_result(MathOutput<std::vector<SolverOutputType>> const& math_output, MutableDataset const& result_data,
                       Idx pos = 0) {
        auto const output_func = [this, &math_output, &result_data, pos]<typename CT>() {
            // output
            auto const span = result_data.get_buffer_span<output_type_getter<SolverOutputType>::template type, CT>(pos);
            if (span.empty()) {
                return;
            }
            this->output_result<CT>(math_output, span.begin());
        };
        Timer const t_output(calculation_info_, 3000, "Produce output");
        run_functor_with_all_types_return_void(output_func);
    }

    CalculationInfo calculation_info() const { return calculation_info_; }

  private:
    CalculationInfo calculation_info_; // needs to be first due to padding override

    double system_frequency_;
    meta_data::MetaData const* meta_data_;

    MainModelState state_;
    // math model
    MathState math_state_;
    Idx n_math_solvers_{0};
    bool is_topology_up_to_date_{false};
    bool is_sym_parameter_up_to_date_{false};
    bool is_asym_parameter_up_to_date_{false};
    bool is_accumulated_component_updated_{true};
    bool last_updated_calculation_symmetry_mode_{false};

    OwnedUpdateDataset cached_inverse_update_{};
    UpdateChange cached_state_changes_{};
    std::array<std::vector<Idx2D>, n_types> parameter_changed_components_{};
#ifndef NDEBUG
    // construction_complete is used for debug assertions only
    bool construction_complete_{false};
#endif // !NDEBUG

    template <symmetry_tag sym> bool& is_parameter_up_to_date() {
        if constexpr (is_symmetric_v<sym>) {
            return is_sym_parameter_up_to_date_;
        } else {
            return is_asym_parameter_up_to_date_;
        }
    }

    template <symmetry_tag sym> std::vector<MathSolver<sym>>& get_solvers() {
        if constexpr (is_symmetric_v<sym>) {
            return math_state_.math_solvers_sym;
        } else {
            return math_state_.math_solvers_asym;
        }
    }

    template <symmetry_tag sym> std::vector<YBus<sym>>& get_y_bus() {
        if constexpr (is_symmetric_v<sym>) {
            return math_state_.y_bus_vec_sym;
        } else {
            return math_state_.y_bus_vec_asym;
        }
    }

    void rebuild_topology() {
        assert(construction_complete_);
        // clear old solvers
        reset_solvers();
        // get connection info
        ComponentConnections comp_conn;
        comp_conn.branch_connected.resize(state_.comp_topo->branch_node_idx.size());
        comp_conn.branch_phase_shift.resize(state_.comp_topo->branch_node_idx.size());
        comp_conn.branch3_connected.resize(state_.comp_topo->branch3_node_idx.size());
        comp_conn.branch3_phase_shift.resize(state_.comp_topo->branch3_node_idx.size());
        comp_conn.source_connected.resize(state_.comp_topo->source_node_idx.size());
        std::transform(
            state_.components.template citer<Branch>().begin(), state_.components.template citer<Branch>().end(),
            comp_conn.branch_connected.begin(), [](Branch const& branch) {
                return BranchConnected{static_cast<IntS>(branch.from_status()), static_cast<IntS>(branch.to_status())};
            });
        std::transform(state_.components.template citer<Branch>().begin(),
                       state_.components.template citer<Branch>().end(), comp_conn.branch_phase_shift.begin(),
                       [](Branch const& branch) { return branch.phase_shift(); });
        std::transform(
            state_.components.template citer<Branch3>().begin(), state_.components.template citer<Branch3>().end(),
            comp_conn.branch3_connected.begin(), [](Branch3 const& branch3) {
                return Branch3Connected{static_cast<IntS>(branch3.status_1()), static_cast<IntS>(branch3.status_2()),
                                        static_cast<IntS>(branch3.status_3())};
            });
        std::transform(state_.components.template citer<Branch3>().begin(),
                       state_.components.template citer<Branch3>().end(), comp_conn.branch3_phase_shift.begin(),
                       [](Branch3 const& branch3) { return branch3.phase_shift(); });
        std::transform(state_.components.template citer<Source>().begin(),
                       state_.components.template citer<Source>().end(), comp_conn.source_connected.begin(),
                       [](Source const& source) { return source.status(); });
        // re build
        Topology topology{*state_.comp_topo, comp_conn};
        std::tie(state_.math_topology, state_.topo_comp_coup) = topology.build_topology();
        n_math_solvers_ = static_cast<Idx>(state_.math_topology.size());
        is_topology_up_to_date_ = true;
        is_sym_parameter_up_to_date_ = false;
        is_asym_parameter_up_to_date_ = false;
    }

    template <symmetry_tag sym> std::vector<MathModelParam<sym>> get_math_param() {
        std::vector<MathModelParam<sym>> math_param(n_math_solvers_);
        for (Idx i = 0; i != n_math_solvers_; ++i) {
            math_param[i].branch_param.resize(state_.math_topology[i]->n_branch());
            math_param[i].shunt_param.resize(state_.math_topology[i]->n_shunt());
            math_param[i].source_param.resize(state_.math_topology[i]->n_source());
        }
        // loop all branch
        for (Idx i = 0; i != static_cast<Idx>(state_.comp_topo->branch_node_idx.size()); ++i) {
            Idx2D const math_idx = state_.topo_comp_coup->branch[i];
            if (math_idx.group == -1) {
                continue;
            }
            // assign parameters
            math_param[math_idx.group].branch_param[math_idx.pos] =
                state_.components.template get_item_by_seq<Branch>(i).template calc_param<sym>();
        }
        // loop all branch3
        for (Idx i = 0; i != static_cast<Idx>(state_.comp_topo->branch3_node_idx.size()); ++i) {
            Idx2DBranch3 const math_idx = state_.topo_comp_coup->branch3[i];
            if (math_idx.group == -1) {
                continue;
            }
            // assign parameters, branch3 param consists of three branch parameters
            auto const branch3_param =
                state_.components.template get_item_by_seq<Branch3>(i).template calc_param<sym>();
            for (size_t branch2 = 0; branch2 < 3; ++branch2) {
                math_param[math_idx.group].branch_param[math_idx.pos[branch2]] = branch3_param[branch2];
            }
        }
        // loop all shunt
        for (Idx i = 0; i != static_cast<Idx>(state_.comp_topo->shunt_node_idx.size()); ++i) {
            Idx2D const math_idx = state_.topo_comp_coup->shunt[i];
            if (math_idx.group == -1) {
                continue;
            }
            // assign parameters
            math_param[math_idx.group].shunt_param[math_idx.pos] =
                state_.components.template get_item_by_seq<Shunt>(i).template calc_param<sym>();
        }
        // loop all source
        for (Idx i = 0; i != static_cast<Idx>(state_.comp_topo->source_node_idx.size()); ++i) {
            Idx2D const math_idx = state_.topo_comp_coup->source[i];
            if (math_idx.group == -1) {
                continue;
            }
            // assign parameters
            math_param[math_idx.group].source_param[math_idx.pos] =
                state_.components.template get_item_by_seq<Source>(i).template math_param<sym>();
        }
        return math_param;
    }
    template <symmetry_tag sym> std::vector<MathModelParamIncrement> get_math_param_increment() {
        using AddToIncrement = void (*)(std::vector<MathModelParamIncrement>&, MainModelState const&, Idx2D const&);

        static constexpr std::array<AddToIncrement, n_types> add_to_increments{
            [](std::vector<MathModelParamIncrement>& increments, MainModelState const& state,
               Idx2D const& changed_component_idx) {
                if constexpr (std::derived_from<ComponentType, Branch>) {
                    Idx2D const math_idx =
                        state.topo_comp_coup
                            ->branch[main_core::get_component_sequence<Branch>(state, changed_component_idx)];
                    if (math_idx.group == -1) {
                        return;
                    }
                    // assign parameters
                    increments[math_idx.group].branch_param_to_change.push_back(math_idx.pos);
                } else if constexpr (std::derived_from<ComponentType, Branch3>) {
                    Idx2DBranch3 const math_idx =
                        state.topo_comp_coup
                            ->branch3[main_core::get_component_sequence<Branch3>(state, changed_component_idx)];
                    if (math_idx.group == -1) {
                        return;
                    }
                    // assign parameters, branch3 param consists of three branch parameters
                    // auto const branch3_param =
                    //   get_component<Branch3>(state, changed_component_idx).template calc_param<sym>();
                    for (size_t branch2 = 0; branch2 < 3; ++branch2) {
                        increments[math_idx.group].branch_param_to_change.push_back(math_idx.pos[branch2]);
                    }
                } else if constexpr (std::same_as<ComponentType, Shunt>) {
                    Idx2D const math_idx =
                        state.topo_comp_coup
                            ->shunt[main_core::get_component_sequence<Shunt>(state, changed_component_idx)];
                    if (math_idx.group == -1) {
                        return;
                    }
                    // assign parameters
                    increments[math_idx.group].shunt_param_to_change.push_back(math_idx.pos);
                }
            }...};

        std::vector<MathModelParamIncrement> math_param_increment(n_math_solvers_);

        for (size_t i = 0; i < n_types; ++i) {
            auto const& changed_type_components = parameter_changed_components_[i];
            auto const& add_type_to_increment = add_to_increments[i];
            for (auto const& changed_component : changed_type_components) {
                add_type_to_increment(math_param_increment, state_, changed_component);
            }
        }

        return math_param_increment;
    }

    static constexpr auto include_all = [](Idx) { return true; };

    /** This is a heavily templated member function because it operates on many different variables of many
     *different types, but the essence is ever the same: filling one member (vector) of the calculation calc_input
     *struct (soa) with the right calculation symmetric or asymmetric calculation parameters, in the same order as
     *the corresponding component are stored in the component topology. There is one such struct for each sub graph
     * / math model and all of them are filled within the same function call (i.e. Notice that calc_input is a
     *vector).
     *
     *  1. For each component, check if it should be included.
     *     By default, all component are included, except for some cases, like power sensors. For power sensors, the
     *     list of component contains all power sensors, but the preparation should only be done for one type of
     *power sensors at a time. Therefore, `included` will be a lambda function, such as:
     *
     *       [this](Idx i) { return state_.comp_topo->power_sensor_terminal_type[i] == MeasuredTerminalType::source;
     *}
     *
     *  2. Find the original component in the topology and retrieve its calculation parameters.
     *
     *  3. Fill the calculation parameters of the right math model.
     *
     *  @tparam CalcStructOut
     *      The calculation input type (soa) for the desired calculation (e.g. PowerFlowInput<sym> or
     *StateEstimationInput<sym>).
     *
     * @tparam CalcParamOut
     *      The data type for the desired calculation for the given ComponentIn (e.g. SourceCalcParam<sym> or
     *      VoltageSensorCalcParam<sym>).
     *
     * @tparam comp_vect
     *      The (pre-allocated and resized) vector of CalcParamOuts which shall be filled with component specific
     *      calculation parameters. Note that this is a pointer to member
     *
     * @tparam ComponentIn
     * 	    The component type for which we are collecting calculation parameters
     *
     * @tparam PredicateIn
     * 	    The lambda function type. The actual type depends on the captured variables, and will be
     *automatically deduced.
     *
     * @param component[in]
     *      The vector of component math indices to consider (e.g. state_.topo_comp_coup->source).
     *      When idx.group = -1, the original component is not assigned to a math model, so we can skip it.
     *
     * @param calc_input[out]
     *		Although this variable is called `input`, it is actually the output of this function, it stored
     *the calculation parameters for each math model, for each component of type ComponentIn.
     *
     * @param include
     *      A lambda function (Idx i -> bool) which returns true if the component at Idx i should be included.
     * 	    The default lambda `include_all` always returns `true`.
     */
    template <calculation_input_type CalcStructOut, typename CalcParamOut,
              std::vector<CalcParamOut>(CalcStructOut::*comp_vect), class ComponentIn,
              std::invocable<Idx> PredicateIn = decltype(include_all)>
        requires std::convertible_to<std::invoke_result_t<PredicateIn, Idx>, bool>
    static void prepare_input(MainModelState const& state, std::vector<Idx2D> const& components,
                              std::vector<CalcStructOut>& calc_input, PredicateIn include = include_all) {
        for (Idx i = 0, n = narrow_cast<Idx>(components.size()); i != n; ++i) {
            if (include(i)) {
                Idx2D const math_idx = components[i];
                if (math_idx.group != -1) {
                    auto const& component = get_component_by_sequence<ComponentIn>(state, i);
                    CalcStructOut& math_model_input = calc_input[math_idx.group];
                    std::vector<CalcParamOut>& math_model_input_vect = math_model_input.*comp_vect;
                    math_model_input_vect[math_idx.pos] = calculate_param<CalcStructOut>(component);
                }
            }
        }
    }

    template <calculation_input_type CalcStructOut, typename CalcParamOut,
              std::vector<CalcParamOut>(CalcStructOut::*comp_vect), class ComponentIn,
              std::invocable<Idx> PredicateIn = decltype(include_all)>
        requires std::convertible_to<std::invoke_result_t<PredicateIn, Idx>, bool>
    static void prepare_input(MainModelState const& state, std::vector<Idx2D> const& components,
                              std::vector<CalcStructOut>& calc_input,
                              std::invocable<ComponentIn const&> auto extra_args, PredicateIn include = include_all) {
        for (Idx i = 0, n = narrow_cast<Idx>(components.size()); i != n; ++i) {
            if (include(i)) {
                Idx2D const math_idx = components[i];
                if (math_idx.group != -1) {
                    auto const& component = get_component_by_sequence<ComponentIn>(state, i);
                    CalcStructOut& math_model_input = calc_input[math_idx.group];
                    std::vector<CalcParamOut>& math_model_input_vect = math_model_input.*comp_vect;
                    math_model_input_vect[math_idx.pos] =
                        calculate_param<CalcStructOut>(component, extra_args(component));
                }
            }
        }
    }

    template <calculation_input_type CalcInputType>
    static auto calculate_param(auto const& c, auto const&... extra_args)
        requires requires {
                     { c.calc_param(extra_args...) };
                 }
    {
        return c.calc_param(extra_args...);
    }

    template <calculation_input_type CalcInputType>
    static auto calculate_param(auto const& c, auto const&... extra_args)
        requires requires {
                     { c.template calc_param<typename CalcInputType::sym>(extra_args...) };
                 }
    {
        return c.template calc_param<typename CalcInputType::sym>(extra_args...);
    }

    template <symmetry_tag sym, IntSVector(StateEstimationInput<sym>::*component), class Component>
    static void prepare_input_status(MainModelState const& state, std::vector<Idx2D> const& objects,
                                     std::vector<StateEstimationInput<sym>>& input) {
        for (Idx i = 0, n = narrow_cast<Idx>(objects.size()); i != n; ++i) {
            Idx2D const math_idx = objects[i];
            if (math_idx.group == -1) {
                continue;
            }
            (input[math_idx.group].*component)[math_idx.pos] =
                main_core::get_component_by_sequence<Component>(state, i).status();
        }
    }

    template <symmetry_tag sym>
    static std::vector<PowerFlowInput<sym>> prepare_power_flow_input(MainModelState const& state, Idx n_math_solvers) {
        std::vector<PowerFlowInput<sym>> pf_input(n_math_solvers);
        for (Idx i = 0; i != n_math_solvers; ++i) {
            pf_input[i].s_injection.resize(state.math_topology[i]->n_load_gen());
            pf_input[i].source.resize(state.math_topology[i]->n_source());
        }
        prepare_input<PowerFlowInput<sym>, DoubleComplex, &PowerFlowInput<sym>::source, Source>(
            state, state.topo_comp_coup->source, pf_input);

        prepare_input<PowerFlowInput<sym>, ComplexValue<sym>, &PowerFlowInput<sym>::s_injection, GenericLoadGen>(
            state, state.topo_comp_coup->load_gen, pf_input);

        return pf_input;
    }

    template <symmetry_tag sym>
    static std::vector<StateEstimationInput<sym>> prepare_state_estimation_input(MainModelState const& state,
                                                                                 Idx n_math_solvers) {
        std::vector<StateEstimationInput<sym>> se_input(n_math_solvers);

        for (Idx i = 0; i != n_math_solvers; ++i) {
            se_input[i].shunt_status.resize(state.math_topology[i]->n_shunt());
            se_input[i].load_gen_status.resize(state.math_topology[i]->n_load_gen());
            se_input[i].source_status.resize(state.math_topology[i]->n_source());
            se_input[i].measured_voltage.resize(state.math_topology[i]->n_voltage_sensor());
            se_input[i].measured_source_power.resize(state.math_topology[i]->n_source_power_sensor());
            se_input[i].measured_load_gen_power.resize(state.math_topology[i]->n_load_gen_power_sensor());
            se_input[i].measured_shunt_power.resize(state.math_topology[i]->n_shunt_power_power_sensor());
            se_input[i].measured_branch_from_power.resize(state.math_topology[i]->n_branch_from_power_sensor());
            se_input[i].measured_branch_to_power.resize(state.math_topology[i]->n_branch_to_power_sensor());
            se_input[i].measured_bus_injection.resize(state.math_topology[i]->n_bus_power_sensor());
        }

        prepare_input_status<sym, &StateEstimationInput<sym>::shunt_status, Shunt>(state, state.topo_comp_coup->shunt,
                                                                                   se_input);
        prepare_input_status<sym, &StateEstimationInput<sym>::load_gen_status, GenericLoadGen>(
            state, state.topo_comp_coup->load_gen, se_input);
        prepare_input_status<sym, &StateEstimationInput<sym>::source_status, Source>(
            state, state.topo_comp_coup->source, se_input);

        prepare_input<StateEstimationInput<sym>, VoltageSensorCalcParam<sym>,
                      &StateEstimationInput<sym>::measured_voltage, GenericVoltageSensor>(
            state, state.topo_comp_coup->voltage_sensor, se_input);
        prepare_input<StateEstimationInput<sym>, PowerSensorCalcParam<sym>,
                      &StateEstimationInput<sym>::measured_source_power, GenericPowerSensor>(
            state, state.topo_comp_coup->power_sensor, se_input,
            [&state](Idx i) { return state.comp_topo->power_sensor_terminal_type[i] == MeasuredTerminalType::source; });
        prepare_input<StateEstimationInput<sym>, PowerSensorCalcParam<sym>,
                      &StateEstimationInput<sym>::measured_load_gen_power, GenericPowerSensor>(
            state, state.topo_comp_coup->power_sensor, se_input, [&state](Idx i) {
                return state.comp_topo->power_sensor_terminal_type[i] == MeasuredTerminalType::load ||
                       state.comp_topo->power_sensor_terminal_type[i] == MeasuredTerminalType::generator;
            });
        prepare_input<StateEstimationInput<sym>, PowerSensorCalcParam<sym>,
                      &StateEstimationInput<sym>::measured_shunt_power, GenericPowerSensor>(
            state, state.topo_comp_coup->power_sensor, se_input,
            [&state](Idx i) { return state.comp_topo->power_sensor_terminal_type[i] == MeasuredTerminalType::shunt; });
        prepare_input<StateEstimationInput<sym>, PowerSensorCalcParam<sym>,
                      &StateEstimationInput<sym>::measured_branch_from_power, GenericPowerSensor>(
            state, state.topo_comp_coup->power_sensor, se_input, [&state](Idx i) {
                using enum MeasuredTerminalType;
                return state.comp_topo->power_sensor_terminal_type[i] == branch_from ||
                       // all branch3 sensors are at from side in the mathematical model
                       state.comp_topo->power_sensor_terminal_type[i] == branch3_1 ||
                       state.comp_topo->power_sensor_terminal_type[i] == branch3_2 ||
                       state.comp_topo->power_sensor_terminal_type[i] == branch3_3;
            });
        prepare_input<StateEstimationInput<sym>, PowerSensorCalcParam<sym>,
                      &StateEstimationInput<sym>::measured_branch_to_power, GenericPowerSensor>(
            state, state.topo_comp_coup->power_sensor, se_input, [&state](Idx i) {
                return state.comp_topo->power_sensor_terminal_type[i] == MeasuredTerminalType::branch_to;
            });
        prepare_input<StateEstimationInput<sym>, PowerSensorCalcParam<sym>,
                      &StateEstimationInput<sym>::measured_bus_injection, GenericPowerSensor>(
            state, state.topo_comp_coup->power_sensor, se_input,
            [&state](Idx i) { return state.comp_topo->power_sensor_terminal_type[i] == MeasuredTerminalType::node; });

        return se_input;
    }

    template <symmetry_tag sym>
    std::vector<ShortCircuitInput> prepare_short_circuit_input(ShortCircuitVoltageScaling voltage_scaling) {
        // TODO(mgovers) split component mapping from actual preparing
        std::vector<IdxVector> topo_fault_indices(state_.math_topology.size());
        std::vector<IdxVector> topo_bus_indices(state_.math_topology.size());

        for (Idx fault_idx{0}; fault_idx < state_.components.template size<Fault>(); ++fault_idx) {
            auto const& fault = state_.components.template get_item_by_seq<Fault>(fault_idx);
            if (fault.status()) {
                auto const node_idx = state_.components.template get_seq<Node>(fault.get_fault_object());
                auto const topo_bus_idx = state_.topo_comp_coup->node[node_idx];

                if (topo_bus_idx.group >= 0) { // Consider non-isolated objects only
                    topo_fault_indices[topo_bus_idx.group].push_back(fault_idx);
                    topo_bus_indices[topo_bus_idx.group].push_back(topo_bus_idx.pos);
                }
            }
        }

        auto fault_coup = std::vector<Idx2D>(state_.components.template size<Fault>(), Idx2D{-1, -1});
        std::vector<ShortCircuitInput> sc_input(n_math_solvers_);

        for (Idx i = 0; i != n_math_solvers_; ++i) {
            auto map = build_dense_mapping(topo_bus_indices[i], state_.math_topology[i]->n_bus());

            for (Idx reordered_idx{0}; reordered_idx < static_cast<Idx>(map.reorder.size()); ++reordered_idx) {
                fault_coup[topo_fault_indices[i][map.reorder[reordered_idx]]] = Idx2D{i, reordered_idx};
            }

            sc_input[i].fault_buses = {from_dense, std::move(map.indvector), state_.math_topology[i]->n_bus()};
            sc_input[i].faults.resize(state_.components.template size<Fault>());
            sc_input[i].source.resize(state_.math_topology[i]->n_source());
        }

        state_.comp_coup = ComponentToMathCoupling{.fault = std::move(fault_coup)};

        prepare_input<ShortCircuitInput, FaultCalcParam, &ShortCircuitInput::faults, Fault>(
            state_, state_.comp_coup.fault, sc_input, [this](Fault const& fault) {
                return state_.components.template get_item<Node>(fault.get_fault_object()).u_rated();
            });
        prepare_input<ShortCircuitInput, DoubleComplex, &ShortCircuitInput::source, Source>(
            state_, state_.topo_comp_coup->source, sc_input, [this, voltage_scaling](Source const& source) {
                return std::pair{state_.components.template get_item<Node>(source.node()).u_rated(), voltage_scaling};
            });

        return sc_input;
    }

    template <symmetry_tag sym> void prepare_y_bus() {
        std::vector<YBus<sym>>& y_bus_vec = get_y_bus<sym>();
        // also get the vector of other Y_bus (sym -> asym, or asym -> sym)
        std::vector<YBus<other_symmetry_t<sym>>>& other_y_bus_vec = get_y_bus<other_symmetry_t<sym>>();
        // If no Ybus exists, build them
        if (y_bus_vec.empty()) {
            bool const other_y_bus_exist = (!other_y_bus_vec.empty());
            y_bus_vec.reserve(n_math_solvers_);
            auto math_params = get_math_param<sym>();

            // Check the branch and shunt indices
            constexpr auto branch_param_in_seq_map =
                std::array{index_of_component<Line>, index_of_component<Link>, index_of_component<Transformer>};
            constexpr auto shunt_param_in_seq_map = std::array{index_of_component<Shunt>};

            for (Idx i = 0; i != n_math_solvers_; ++i) {
                // construct from existing Y_bus structure if possible
                if (other_y_bus_exist) {
                    y_bus_vec.emplace_back(state_.math_topology[i],
                                           std::make_shared<MathModelParam<sym> const>(std::move(math_params[i])),
                                           other_y_bus_vec[i].get_y_bus_structure());
                } else {
                    y_bus_vec.emplace_back(state_.math_topology[i],
                                           std::make_shared<MathModelParam<sym> const>(std::move(math_params[i])));
                }

                y_bus_vec.back().set_branch_param_idx(
                    IdxVector{branch_param_in_seq_map.begin(), branch_param_in_seq_map.end()});
                y_bus_vec.back().set_shunt_param_idx(
                    IdxVector{shunt_param_in_seq_map.begin(), shunt_param_in_seq_map.end()});
            }
        }
    }

    template <symmetry_tag sym> void prepare_solvers() {
        std::vector<MathSolver<sym>>& solvers = get_solvers<sym>();
        // rebuild topology if needed
        if (!is_topology_up_to_date_) {
            rebuild_topology();
        }
        prepare_y_bus<sym>();

        if (n_math_solvers_ != static_cast<Idx>(solvers.size())) {
            assert(solvers.empty());
            assert(n_math_solvers_ == static_cast<Idx>(state_.math_topology.size()));
            assert(n_math_solvers_ == static_cast<Idx>(get_y_bus<sym>().size()));

            solvers.clear();
            solvers.reserve(n_math_solvers_);
            std::ranges::transform(state_.math_topology, std::back_inserter(solvers),
                                   [](auto math_topo) { return MathSolver<sym>{std::move(math_topo)}; });
            for (Idx idx = 0; idx < n_math_solvers_; ++idx) {
                get_y_bus<sym>()[idx].register_parameters_changed_callback(
                    [solver = std::ref(solvers[idx])](bool changed) { solver.get().parameters_changed(changed); });
            }
        } else if (!is_parameter_up_to_date<sym>()) {
            std::vector<MathModelParam<sym>> const math_params = get_math_param<sym>();
            std::vector<MathModelParamIncrement> const math_param_increments = get_math_param_increment<sym>();
            if (last_updated_calculation_symmetry_mode_ == is_symmetric_v<sym>) {
                main_core::update_y_bus(math_state_, math_params, math_param_increments);
            } else {
                main_core::update_y_bus(math_state_, math_params);
            }
        }
        // else do nothing, set everything up to date
        is_parameter_up_to_date<sym>() = true;
        std::ranges::for_each(parameter_changed_components_, [](auto& comps) { comps.clear(); });
        last_updated_calculation_symmetry_mode_ = is_symmetric_v<sym>;
    }
};

using MainModel =
    MainModelImpl<ExtraRetrievableTypes<Base, Node, Branch, Branch3, Appliance, GenericLoadGen, GenericLoad,
                                        GenericGenerator, GenericPowerSensor, GenericVoltageSensor, Regulator>,
                  AllComponents>;

} // namespace power_grid_model
