# Master Python Learning Curriculum

Welcome to the **Comprehensive, Enterprise-Grade Python Engineering Curriculum**. This curriculum covers modern Python from foundational basics through systems-level C extensions, asynchronous concurrency, and Python 3.13 innovations.

Every module is organized with **architectural deep dives**, **concrete syntax tables**, and **at least 3 real-world, runnable code examples** complete with step-by-step explanations and expected outputs.

## Curriculum Table of Contents

### [Python Basics & Core Fundamentals](01_basics/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. Introduction to Programming & Python Architecture | [01.intro_and_python_architecture.md](01_basics/01.intro_and_python_architecture.md) |
| 02 | 02. Variables, Literals and Constants | [02.variables_literals_and_constants.md](01_basics/02.variables_literals_and_constants.md) |
| 03 | 03. Input, Output, Print Formatting and Comments | [03.input_output_print_comments.md](01_basics/03.input_output_print_comments.md) |
| 04 | 04. Type Conversion and Casting | [04.type_conversion_and_casting.md](01_basics/04.type_conversion_and_casting.md) |
| 05 | Memory Management, Garbage Collection & Bytecode | [05.garbage_collection_and_memory_internals.md](01_basics/05.garbage_collection_and_memory_internals.md) |

### [Data Types & Collections Deep Dive](02_datatypes/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. The Integer (`int`) Data Type | [01.integers.md](02_datatypes/01.integers.md) |
| 02 | 02. The Floating-Point (`float`) Data Type | [02.floats.md](02_datatypes/02.floats.md) |
| 03 | 03. The Complex Number (`complex`) Data Type | [03.complex_numbers.md](02_datatypes/03.complex_numbers.md) |
| 04 | 04. The Boolean (`bool`) Data Type | [04.booleans.md](02_datatypes/04.booleans.md) |
| 05 | 05. The String (`str`) Data Type | [05.strings.md](02_datatypes/05.strings.md) |
| 06 | Lists (`list`) | [06.lists.md](02_datatypes/06.lists.md) |
| 07 | Tuples (`tuple`) | [07.tuples.md](02_datatypes/07.tuples.md) |
| 08 | Sets (`set` & `frozenset`) | [08.sets.md](02_datatypes/08.sets.md) |
| 09 | Dictionaries (`dict`) | [09.dictionaries.md](02_datatypes/09.dictionaries.md) |
| 10 | Bytes, Bytearray & Memoryview | [10.bytes_and_bytearray.md](02_datatypes/10.bytes_and_bytearray.md) |
| 11 | The None Type (`NoneType`) | [11.none_type.md](02_datatypes/11.none_type.md) |
| 12 | Decimals & Fractions (`decimal.Decimal`, `fractions.Fraction`) | [12.decimal_and_fractions.md](02_datatypes/12.decimal_and_fractions.md) |
| 13 | Enumerations (`enum.Enum`, `Flag`, `auto`) | [13.enumerations.md](02_datatypes/13.enumerations.md) |

### [Operators & Expressions](03_operators/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. Arithmetic Operators & Precedence (BODMAS) | [01.arithmetic_and_precedence_bodmas.md](03_operators/01.arithmetic_and_precedence_bodmas.md) |
| 02 | 02. Relational & Comparison Operators | [02.relational_and_comparison_operators.md](03_operators/02.relational_and_comparison_operators.md) |
| 03 | 03. Logical Operators & Short-Circuit Evaluation | [03.logical_operators_and_short_circuit.md](03_operators/03.logical_operators_and_short_circuit.md) |
| 04 | 04. Membership & Identity Operators | [04.membership_and_identity_operators.md](03_operators/04.membership_and_identity_operators.md) |
| 05 | Bitwise Operators & The Walrus Operator (`:=`) | [05.bitwise_and_walrus_operators.md](03_operators/05.bitwise_and_walrus_operators.md) |

### [Control Flow & Pattern Matching](04_control_flow/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | if, elif, else | [01.conditional_statements_if_elif_else.md](04_control_flow/01.conditional_statements_if_elif_else.md) |
| 02 | 02. Nested Conditionals & Decision Trees | [02.nested_conditionals_and_decision_trees.md](04_control_flow/02.nested_conditionals_and_decision_trees.md) |
| 03 | 03. While Loops & Iteration Patterns | [03.while_loops_and_iteration_patterns.md](04_control_flow/03.while_loops_and_iteration_patterns.md) |
| 04 | 04. For Loops & The `range()` Function | [04.for_loops_and_range_function.md](04_control_flow/04.for_loops_and_range_function.md) |
| 05 | 05. Nested Loops & Grid Patterns | [05.nested_loops_and_grid_patterns.md](04_control_flow/05.nested_loops_and_grid_patterns.md) |
| 06 | break, continue, pass, and loop-else | [06.loop_control_break_continue_pass_else.md](04_control_flow/06.loop_control_break_continue_pass_else.md) |
| 07 | Structural Pattern Matching (`match - case`) | [07.structural_pattern_matching_match_case.md](04_control_flow/07.structural_pattern_matching_match_case.md) |

### [Functions, Scopes & Closures](05_functions/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. Function Definition & Return Values | [01.function_definition_and_return.md](05_functions/01.function_definition_and_return.md) |
| 02 | 02. Positional, Keyword & Default Arguments | [02.positional_keyword_and_default_arguments.md](05_functions/02.positional_keyword_and_default_arguments.md) |
| 03 | `*args` and `**kwargs` | [03.arbitrary_arguments_args_and_kwargs.md](05_functions/03.arbitrary_arguments_args_and_kwargs.md) |
| 04 | 04. Variable Scope & The LEGB Rule | [04.variable_scope_and_legb_rule.md](05_functions/04.variable_scope_and_legb_rule.md) |
| 05 | 05. The `global` and `nonlocal` Keywords | [05.global_and_nonlocal_keywords.md](05_functions/05.global_and_nonlocal_keywords.md) |
| 06 | 06. Function Call Stack & Execution Frames | [06.function_call_stack_and_execution_frames.md](05_functions/06.function_call_stack_and_execution_frames.md) |
| 07 | 07. Recursion Mechanics & Call Trees | [07.recursion_mechanics_and_call_tree.md](05_functions/07.recursion_mechanics_and_call_tree.md) |
| 08 | 08. Lambda Functions, `map()`, `filter()` & `reduce()` | [08.lambda_functions_map_filter_reduce.md](05_functions/08.lambda_functions_map_filter_reduce.md) |
| 09 | Closures, Advanced Parameters & Metadata | [09.closures_and_advanced_parameters.md](05_functions/09.closures_and_advanced_parameters.md) |

### [Essential Built-in Functions](06_builtin_functions/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. Mathematical & Numeric Built-in Functions | [01.mathematical_and_numeric_functions.md](06_builtin_functions/01.mathematical_and_numeric_functions.md) |
| 02 | 02. Sequence & Aggregation Functions | [02.sequence_and_aggregation_functions.md](06_builtin_functions/02.sequence_and_aggregation_functions.md) |
| 03 | `enumerate()`, `zip()` & `reversed()` | [03.iteration_tools_enumerate_zip_reversed.md](06_builtin_functions/03.iteration_tools_enumerate_zip_reversed.md) |

### [Object-Oriented Programming (OOP) & Metaclasses](07_oop/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. Classes, Objects & The `__init__` Constructor | [01.classes_objects_and_init_constructor.md](07_oop/01.classes_objects_and_init_constructor.md) |
| 02 | 02. Instance Attributes & Methods | [02.instance_attributes_and_methods.md](07_oop/02.instance_attributes_and_methods.md) |
| 03 | 03. Class Attributes & Class Methods (`@classmethod`) | [03.class_attributes_and_class_methods.md](07_oop/03.class_attributes_and_class_methods.md) |
| 04 | 04. Static Methods & Utility Helpers (`@staticmethod`) | [04.static_methods_and_utility_helpers.md](07_oop/04.static_methods_and_utility_helpers.md) |
| 05 | Single & Multilevel | [05.inheritance_single_and_multilevel.md](07_oop/05.inheritance_single_and_multilevel.md) |
| 06 | 06. `super()` Delegation & Method Overriding | [06.super_delegation_and_method_overriding.md](07_oop/06.super_delegation_and_method_overriding.md) |
| 07 | HAS-A vs Inheritance (IS-A) | [07.composition_has_a_vs_inheritance_is_a.md](07_oop/07.composition_has_a_vs_inheritance_is_a.md) |
| 08 | Encapsulation, Name Mangling & Property Decorators | [08.encapsulation_and_property_decorators.md](07_oop/08.encapsulation_and_property_decorators.md) |
| 09 | Multiple Inheritance & MRO (C3 Linearization) | [09.multiple_inheritance_and_mro_c3.md](07_oop/09.multiple_inheritance_and_mro_c3.md) |
| 10 | Abstract Base Classes (`abc.ABC`) & Protocols | [10.abstract_base_classes_and_protocols.md](07_oop/10.abstract_base_classes_and_protocols.md) |
| 11 | The Complete Dunder (Magic) Methods Matrix | [11.dunder_methods_matrix.md](07_oop/11.dunder_methods_matrix.md) |
| 12 | Memory Optimization with `__slots__` & Dataclasses | [12.slots_and_dataclasses.md](07_oop/12.slots_and_dataclasses.md) |
| 13 | The `copy` Module & Object Cloning Mechanics | [13.copy_module_and_object_cloning.md](07_oop/13.copy_module_and_object_cloning.md) |

### [Exception Handling & Resource Management](08_exceptions/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. Syntax Errors vs Runtime Exceptions | [01.syntax_errors_vs_runtime_exceptions.md](08_exceptions/01.syntax_errors_vs_runtime_exceptions.md) |
| 02 | 02. `try-except` Blocks & Catching Multiple Exceptions | [02.try_except_blocks_and_built_in_exceptions.md](08_exceptions/02.try_except_blocks_and_built_in_exceptions.md) |
| 03 | 03. `try`, `except`, `else` & `finally` Clauses | [03.try_except_else_finally_clauses.md](08_exceptions/03.try_except_else_finally_clauses.md) |
| 04 | 04. Raising Exceptions & Custom Exception Classes | [04.raising_exceptions_and_custom_exceptions.md](08_exceptions/04.raising_exceptions_and_custom_exceptions.md) |
| 05 | Exception Chaining & ExceptionGroups | [05.exception_chaining_and_exception_groups.md](08_exceptions/05.exception_chaining_and_exception_groups.md) |
| 06 | Context Managers & the `contextlib` Standard Library | [06.context_managers_and_contextlib.md](08_exceptions/06.context_managers_and_contextlib.md) |

### [Standard Library Power Tools](09_standard_library/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | 01. Modules, Imports & Aliasing | [01.modules_imports_and_aliasing.md](09_standard_library/01.modules_imports_and_aliasing.md) |
| 02 | 02. The `math` Module & Mathematical Operations | [02.math_module_and_mathematical_functions.md](09_standard_library/02.math_module_and_mathematical_functions.md) |
| 03 | 03. The `random` Module & Simulations | [03.random_module_and_randomized_simulations.md](09_standard_library/03.random_module_and_randomized_simulations.md) |
| 04 | Dates & Times | [04.datetime_module_dates_and_times.md](09_standard_library/04.datetime_module_dates_and_times.md) |
| 05 | Durations & Date Arithmetic | [05.timedelta_durations_and_date_arithmetic.md](09_standard_library/05.timedelta_durations_and_date_arithmetic.md) |
| 06 | Formatting and Parsing Dates | [06.strftime_and_strptime_formatting_parsing.md](09_standard_library/06.strftime_and_strptime_formatting_parsing.md) |
| 07 | Regular Expressions (`re`) | [07.regular_expressions_re_module.md](09_standard_library/07.regular_expressions_re_module.md) |
| 08 | Professional Logging (`logging`) | [08.logging_module.md](09_standard_library/08.logging_module.md) |
| 09 | Operating System, Sys & Subprocesses | [09.os_sys_and_subprocess.md](09_standard_library/09.os_sys_and_subprocess.md) |
| 10 | Command-Line Parsing (`argparse`) | [10.argparse_cli_parsing.md](09_standard_library/10.argparse_cli_parsing.md) |
| 11 | Hashlib & Cryptographic Tools | [11.hashlib_and_cryptographic_tools.md](09_standard_library/11.hashlib_and_cryptographic_tools.md) |
| 12 | The `warnings` Module & System Diagnostics | [12.warnings_module.md](09_standard_library/12.warnings_module.md) |

### [Iterators, Generators & Comprehensions](10_iterators_and_generators/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Comprehensions Deep Dive | [01.comprehensions_deep_dive.md](10_iterators_and_generators/01.comprehensions_deep_dive.md) |
| 02 | The Iterator Protocol (`__iter__`, `__next__`) | [02.iterator_protocol.md](10_iterators_and_generators/02.iterator_protocol.md) |
| 03 | Generator Functions & `yield from` | [03.generators_and_yield.md](10_iterators_and_generators/03.generators_and_yield.md) |
| 04 | Generator Coroutines (`send`, `throw`, `close`) | [04.generator_coroutines.md](10_iterators_and_generators/04.generator_coroutines.md) |
| 05 | The `itertools` Standard Library Power Tools | [05.itertools_power_tools.md](10_iterators_and_generators/05.itertools_power_tools.md) |

### [Decorators & Functional Programming](11_decorators_and_functional/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Mechanics & Preserving Metadata with `@functools.wraps` | [01.decorator_mechanics_and_wraps.md](11_decorators_and_functional/01.decorator_mechanics_and_wraps.md) |
| 02 | Parameterized Decorators & Stacking Order | [02.parameterized_and_stacked_decorators.md](11_decorators_and_functional/02.parameterized_and_stacked_decorators.md) |
| 03 | Class Decorators & Class-Based Decorators | [03.class_decorators.md](11_decorators_and_functional/03.class_decorators.md) |
| 04 | Built-in Functional Decorators (`lru_cache`, `singledispatch`) | [04.builtin_decorators.md](11_decorators_and_functional/04.builtin_decorators.md) |

### [Metaprogramming, Descriptors & AST Internals](12_metaprogramming/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | The Descriptor Protocol (`__get__`, `__set__`, `__delete__`) | [01.descriptor_protocol.md](12_metaprogramming/01.descriptor_protocol.md) |
| 02 | Dynamic `type()` & Custom Metaclasses | [02.dynamic_type_creation_and_metaclasses.md](12_metaprogramming/02.dynamic_type_creation_and_metaclasses.md) |
| 03 | `__init_subclass__` & Dynamic Attribute Hooks | [03.init_subclass_and_hooks.md](12_metaprogramming/03.init_subclass_and_hooks.md) |
| 04 | Runtime Introspection (`inspect`) & AST Parsing (`ast`) | [04.runtime_inspection_and_ast.md](12_metaprogramming/04.runtime_inspection_and_ast.md) |

### [File I/O, Serialization & Storage Systems](13_file_io_and_persistence/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | File Handling & Object-Oriented Paths (`pathlib.Path`) | [01.file_handling_and_pathlib.md](13_file_io_and_persistence/01.file_handling_and_pathlib.md) |
| 02 | Structured Data (CSV & JSON) | [02.structured_data_csv_json.md](13_file_io_and_persistence/02.structured_data_csv_json.md) |
| 03 | Binary Serialization & `pickle` Security | [03.binary_serialization_and_pickle.md](13_file_io_and_persistence/03.binary_serialization_and_pickle.md) |
| 04 | Embedded Relational Databases (`sqlite3`) | [04.embedded_databases_sqlite3.md](13_file_io_and_persistence/04.embedded_databases_sqlite3.md) |
| 05 | High-Level File Management (`shutil`, `tempfile`, `zipfile`) | [05.file_management_shutil_tempfile_zipfile.md](13_file_io_and_persistence/05.file_management_shutil_tempfile_zipfile.md) |

### [Modules, Packages & Distribution Standards](14_modules_and_packaging/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | The Import System & `sys.path` Resolution | [01.import_system_and_sys_path.md](14_modules_and_packaging/01.import_system_and_sys_path.md) |
| 02 | Packages, `__init__.py` & Relative Imports | [02.packages_init_and_relative_imports.md](14_modules_and_packaging/02.packages_init_and_relative_imports.md) |
| 03 | Virtual Environments (`venv`) & `pyproject.toml` | [03.virtual_environments_and_pyproject.md](14_modules_and_packaging/03.virtual_environments_and_pyproject.md) |

### [Modern Typing & Data Validation](15_modern_typing_and_validation/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Type Hints & Generic Primitives | [01.type_hints_and_primitives.md](15_modern_typing_and_validation/01.type_hints_and_primitives.md) |
| 02 | Advanced Typing (`Callable`, `Literal`, `TypedDict`, `Protocol`) | [02.advanced_typing_protocols.md](15_modern_typing_and_validation/02.advanced_typing_protocols.md) |
| 03 | Generics & Python 3.12 Type Parameter Syntax (PEP 695) | [03.generics_and_pep_695.md](15_modern_typing_and_validation/03.generics_and_pep_695.md) |
| 04 | Data Validation & Schemas with Pydantic v2 | [04.pydantic_v2_validation.md](15_modern_typing_and_validation/04.pydantic_v2_validation.md) |

### [Concurrency, Parallelism & AsyncIO](16_concurrency_and_async/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Concurrency Models & The Global Interpreter Lock (GIL) | [01.concurrency_fundamentals_and_gil.md](16_concurrency_and_async/01.concurrency_fundamentals_and_gil.md) |
| 02 | Threading & Synchronization Primitives | [02.threading_and_synchronization.md](16_concurrency_and_async/02.threading_and_synchronization.md) |
| 03 | Multiprocessing & Worker Pools | [03.multiprocessing_and_pools.md](16_concurrency_and_async/03.multiprocessing_and_pools.md) |
| 04 | High-Level `concurrent.futures` Executors | [04.concurrent_futures_executors.md](16_concurrency_and_async/04.concurrent_futures_executors.md) |
| 05 | `asyncio` Fundamentals & Modern `TaskGroup` | [05.asyncio_fundamentals.md](16_concurrency_and_async/05.asyncio_fundamentals.md) |
| 06 | Advanced AsyncIO (Iterators, Context Managers, Queues) | [06.advanced_asyncio.md](16_concurrency_and_async/06.advanced_asyncio.md) |

### [Python CLI, Flags & Runtime Environment](17_python_cli_and_runtime/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Command-Line Flags & Execution Modes | [01.cli_flags_and_execution_modes.md](17_python_cli_and_runtime/01.cli_flags_and_execution_modes.md) |
| 02 | Critical Environment Variables | [02.runtime_environment_variables.md](17_python_cli_and_runtime/02.runtime_environment_variables.md) |

### [Enterprise Design Patterns in Python](18_design_patterns/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Creational (Singleton, Factory, Builder) | [01.creational_patterns.md](18_design_patterns/01.creational_patterns.md) |
| 02 | Structural (Adapter, Facade, Proxy) | [02.structural_patterns.md](18_design_patterns/02.structural_patterns.md) |
| 03 | Behavioral (Strategy, Observer, Command) | [03.behavioral_patterns.md](18_design_patterns/03.behavioral_patterns.md) |

### [Testing, Mocking & Code Quality](19_testing_and_quality/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Unittest & Doctest Frameworks | [01.unittest_and_doctest.md](19_testing_and_quality/01.unittest_and_doctest.md) |
| 02 | Mocking & Patching (`unittest.mock`) | [02.mocking_and_patching.md](19_testing_and_quality/02.mocking_and_patching.md) |
| 03 | Modern Testing with Pytest | [03.modern_testing_with_pytest.md](19_testing_and_quality/03.modern_testing_with_pytest.md) |

### [Profiling, Memory & Optimization](20_profiling_and_performance/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | CPU Profiling with `cProfile` | [01.cpu_profiling_cprofile.md](20_profiling_and_performance/01.cpu_profiling_cprofile.md) |
| 02 | Memory Profiling with `tracemalloc` | [02.memory_profiling_tracemalloc.md](20_profiling_and_performance/02.memory_profiling_tracemalloc.md) |
| 03 | Weak References (`weakref` Module) | [03.weak_references_weakref.md](20_profiling_and_performance/03.weak_references_weakref.md) |
| 04 | Microbenchmarking with `timeit` | [04.microbenchmarking_timeit.md](20_profiling_and_performance/04.microbenchmarking_timeit.md) |

### [AI, Vectorization & Data Foundations](21_ai_and_data_foundations/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | NumPy Vectorization vs. Python Loops | [01.numpy_vectorization_vs_python_loops.md](21_ai_and_data_foundations/01.numpy_vectorization_vs_python_loops.md) |
| 02 | Columnar Data & DataFrames | [02.columnar_data_and_dataframes.md](21_ai_and_data_foundations/02.columnar_data_and_dataframes.md) |
| 03 | Configuration & Dotenv | [03.configuration_and_dotenv.md](21_ai_and_data_foundations/03.configuration_and_dotenv.md) |

### [Low-Level Systems & Binary Protocols](22_low_level_systems_and_protocols/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Socket Programming (TCP & UDP) | [01.socket_programming_tcp_udp.md](22_low_level_systems_and_protocols/01.socket_programming_tcp_udp.md) |
| 02 | Binary Protocols & the `struct` Module | [02.binary_protocols_struct.md](22_low_level_systems_and_protocols/02.binary_protocols_struct.md) |
| 03 | Primitive Arrays & `memoryview` | [03.primitive_arrays.md](22_low_level_systems_and_protocols/03.primitive_arrays.md) |

### [Algorithmic Data Structures](23_algorithmic_data_structures/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Heaps & Priority Queues (`heapq`) | [01.heaps_and_priority_queues.md](23_algorithmic_data_structures/01.heaps_and_priority_queues.md) |
| 02 | Binary Search with `bisect` | [02.binary_search_bisect.md](23_algorithmic_data_structures/02.binary_search_bisect.md) |
| 03 | Fast Extractors with the `operator` Module | [03.fast_extractors_operator.md](23_algorithmic_data_structures/03.fast_extractors_operator.md) |

### [C Extensions & Foreign Function Interface (FFI)](24_c_extensions_and_ffi/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Calling Shared Libraries with `ctypes` | [01.ctypes_shared_libraries.md](24_c_extensions_and_ffi/01.ctypes_shared_libraries.md) |
| 02 | Modern Interop with CFFI & PyBind11 | [02.cffi_and_pybind11.md](24_c_extensions_and_ffi/02.cffi_and_pybind11.md) |
| 03 | Python C-API Foundations | [03.python_c_api_foundations.md](24_c_extensions_and_ffi/03.python_c_api_foundations.md) |

### [Web Architecture (WSGI, ASGI & Middleware)](25_web_architecture/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | WSGI Protocol (PEP 3333) | [01.wsgi_protocol_pep_3333.md](25_web_architecture/01.wsgi_protocol_pep_3333.md) |
| 02 | ASGI Protocol (Asynchronous Server Gateway Interface) | [02.asgi_protocol.md](25_web_architecture/02.asgi_protocol.md) |
| 03 | Middleware Pipelines & Request-Response Cycles | [03.middleware_pipelines.md](25_web_architecture/03.middleware_pipelines.md) |

### [Application Security & Vulnerability Hardening](26_security_hardening/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Injection Defenses (SQLi & Command Injection) | [01.injection_defenses.md](26_security_hardening/01.injection_defenses.md) |
| 02 | Path Traversal & Insecure Deserialization | [02.path_traversal_and_deserialization.md](26_security_hardening/02.path_traversal_and_deserialization.md) |
| 03 | ReDoS & Timing Attacks (`secrets` Module) | [03.redos_and_timing_attacks.md](26_security_hardening/03.redos_and_timing_attacks.md) |

### [Modern Tooling & Python 3.12 / 3.13 Innovations](27_modern_tooling_and_python_312_313/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Fast Workflows with uv, Ruff & Mypy | [01.modern_tooling_uv_ruff_mypy.md](27_modern_tooling_and_python_312_313/01.modern_tooling_uv_ruff_mypy.md) |
| 02 | Python 3.12 Cutting-Edge Language Features | [02.python_312_cutting_edge.md](27_modern_tooling_and_python_312_313/02.python_312_cutting_edge.md) |
| 03 | Python 3.13 JIT Compiler & Free-Threaded No-GIL | [03.python_313_jit_and_no_gil.md](27_modern_tooling_and_python_312_313/03.python_313_jit_and_no_gil.md) |

### [Practical Case Studies & Capstone Challenges](28_practical_case_studies_and_challenges/)

| S.No | Topic / Concept | Direct Module Link |
|---|---|---|
| 01 | Chai Business Billing & Inventory Engine | [01.chai_business_billing_and_inventory.md](28_practical_case_studies_and_challenges/01.chai_business_billing_and_inventory.md) |
| 02 | Production Log Analyzer & Rate Limiter | [02.log_analyzer_and_rate_limiter.md](28_practical_case_studies_and_challenges/02.log_analyzer_and_rate_limiter.md) |
| 03 | Concurrent Web Crawler & Async Pipeline | [03.concurrent_web_crawler_and_pipeline.md](28_practical_case_studies_and_challenges/03.concurrent_web_crawler_and_pipeline.md) |

---

**Total Curriculum Coverage:** 27 Comprehensive Categories | 140 Production-Grade Engineering Modules.
