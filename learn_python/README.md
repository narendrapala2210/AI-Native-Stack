# 🐍 Complete Python Mastery Curriculum

> **An exhaustive, industry-grade reference manual and curriculum covering Python from fundamental syntax to deep OOP architecture and standard library modules, organized cleanly into domain categories.**

---

## 📚 Curriculum Structure & Domain Map

### 01. Python Basics & Fundamental Syntax

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.intro_and_python_architecture.md`](01_basics/01.intro_and_python_architecture.md) | **Introduction to Programming & Python Architecture** | Software, syntax, CPython, PVM bytecode execution | 3 Examples |
| [`02.variables_literals_and_constants.md`](01_basics/02.variables_literals_and_constants.md) | **Variables, Literals & Constants** | Dynamic typing, references, PEP 8 constants, literal types | 3 Examples |
| [`03.input_output_print_comments.md`](01_basics/03.input_output_print_comments.md) | **Input, Output, Print Formatting & Comments** | print() sep/end/flush, input(), comments, syntax errors | 3 Examples |
| [`04.type_conversion_and_casting.md`](01_basics/04.type_conversion_and_casting.md) | **Type Conversion & Casting** | Implicit coercion, int/float/str/bool casting, ValueError traps | 3 Examples |

### 02. Core Data Types & Structures (`02_datatypes/{s.no}.{typename}.md`)

| Module File | Topic & Concept Description | Key Concepts Covered & Built-in Methods | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.integers.md`](02_datatypes/01.integers.md) | **Integers (`int`)** | Arbitrary precision, radix bases (bin/hex/oct), interning, bit_length, bit_count, to_bytes, from_bytes | 3 Examples |
| [`02.floats.md`](02_datatypes/02.floats.md) | **Floats (`float`)** | IEEE 754 precision traps, math.isclose, nan/inf, Decimal, is_integer, as_integer_ratio, hex, fromhex | 3 Examples |
| [`03.complex_numbers.md`](02_datatypes/03.complex_numbers.md) | **Complex Numbers (`complex`)** | $a+bj$, real/imag attributes, conjugate(), cmath, Euler's formula | 3 Examples |
| [`04.booleans.md`](02_datatypes/04.booleans.md) | **Booleans (`bool`)** | int subclassing, truthiness matrix, short-circuit fallbacks, sentinels | 3 Examples |
| [`05.strings.md`](02_datatypes/05.strings.md) | **Strings (`str`)** | Immutability, slicing [start:stop:step], f-strings, Unicode & **ALL 45+ string methods** | 3 Examples |
| [`06.lists.md`](02_datatypes/06.lists.md) | **Lists (`list`)** | Dynamic arrays, mutability, slicing, matrices & **ALL 11 list methods** | 3 Examples |
| [`07.tuples.md`](02_datatypes/07.tuples.md) | **Tuples (`tuple`)** | Immutability, packing/unpacking (*rest), namedtuple, count, index | 3 Examples |
| [`08.sets.md`](02_datatypes/08.sets.md) | **Sets (`set` & `frozenset`)** | Hash tables, uniqueness, Venn algebra & **ALL 17 set methods** | 3 Examples |
| [`09.dictionaries.md`](02_datatypes/09.dictionaries.md) | **Dictionaries (`dict`)** | Hash tables, insertion order, JSON trees, merge ops (\|) & **ALL 11 dict methods** | 3 Examples |
| [`10.bytes_and_bytearray.md`](02_datatypes/10.bytes_and_bytearray.md) | **Bytes, Bytearray & Memoryview** | Binary sequences, mutable buffers, zero-copy memoryview, magic numbers | 3 Examples |
| [`11.none_type.md`](02_datatypes/11.none_type.md) | **The None Type (`NoneType`)** | Singleton identity (is None), mutable default argument trap, null coalescing | 3 Examples |

### 03. Operators & Expressions

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.arithmetic_and_precedence_bodmas.md`](03_operators/01.arithmetic_and_precedence_bodmas.md) | **Arithmetic Operators & Precedence (BODMAS)** | +, -, *, /, //, %, **, right-to-left power associativity | 3 Examples |
| [`02.relational_and_comparison_operators.md`](03_operators/02.relational_and_comparison_operators.md) | **Relational & Comparison Operators** | ==, !=, <, >, <=, >=, chained range comparisons | 3 Examples |
| [`03.logical_operators_and_short_circuit.md`](03_operators/03.logical_operators_and_short_circuit.md) | **Logical Operators & Short-Circuit** | and, or, not, truth tables, short-circuit shielding | 3 Examples |
| [`04.membership_and_identity_operators.md`](03_operators/04.membership_and_identity_operators.md) | **Membership & Identity Operators** | in, not in, is, is not, identity vs equality, sentinels | 3 Examples |

### 04. Control Flow & Loops

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.conditional_statements_if_elif_else.md`](04_control_flow/01.conditional_statements_if_elif_else.md) | **Conditional Statements: if, elif, else** | Indentation blocks, grade classifier, ternary expression | 3 Examples |
| [`02.nested_conditionals_and_decision_trees.md`](04_control_flow/02.nested_conditionals_and_decision_trees.md) | **Nested Conditionals & Decision Trees** | Multi-factor authentication, guard clauses, early returns | 3 Examples |
| [`03.while_loops_and_iteration_patterns.md`](04_control_flow/03.while_loops_and_iteration_patterns.md) | **While Loops & Iteration Patterns** | Condition check, exponential backoff, digit reversal | 3 Examples |
| [`04.for_loops_and_range_function.md`](04_control_flow/04.for_loops_and_range_function.md) | **For Loops & The range() Function** | range(start, stop, step), batching, zip & enumerate | 3 Examples |
| [`05.nested_loops_and_grid_patterns.md`](04_control_flow/05.nested_loops_and_grid_patterns.md) | **Nested Loops & Grid Patterns** | 2D distance matrix, asterisk diamonds, pair combinations | 3 Examples |
| [`06.loop_control_break_continue_pass_else.md`](04_control_flow/06.loop_control_break_continue_pass_else.md) | **Loop Control: break, continue, pass, else** | Early termination, skipping iterations, loop-else clause | 3 Examples |

### 05. Functions, Scope & Recursion

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.function_definition_and_return.md`](05_functions/01.function_definition_and_return.md) | **Function Definition & Return Values** | def keyword, multiple returns, dead code, pure functions | 3 Examples |
| [`02.positional_keyword_and_default_arguments.md`](05_functions/02.positional_keyword_and_default_arguments.md) | **Positional, Keyword & Default Arguments** | Order rules, mutable default trap (None sentinel), / and * | 3 Examples |
| [`03.arbitrary_arguments_args_and_kwargs.md`](05_functions/03.arbitrary_arguments_args_and_kwargs.md) | **Arbitrary Arguments: *args & **kwargs** | Tuple packing, dict packing, decorators, argument unpacking | 3 Examples |
| [`04.variable_scope_and_legb_rule.md`](05_functions/04.variable_scope_and_legb_rule.md) | **Variable Scope & The LEGB Rule** | Local, Enclosing, Global, Built-in, UnboundLocalError | 3 Examples |
| [`05.global_and_nonlocal_keywords.md`](05_functions/05.global_and_nonlocal_keywords.md) | **The global and nonlocal Keywords** | Rebinding module names, stateful closures, rate limiters | 3 Examples |
| [`06.function_call_stack_and_execution_frames.md`](05_functions/06.function_call_stack_and_execution_frames.md) | **Function Call Stack & Execution Frames** | LIFO frames, inspect module, stack introspection | 3 Examples |
| [`07.recursion_mechanics_and_call_tree.md`](05_functions/07.recursion_mechanics_and_call_tree.md) | **Recursion Mechanics & Call Trees** | Base case, reduction step, directory tree walking | 3 Examples |
| [`08.lambda_functions_map_filter_reduce.md`](05_functions/08.lambda_functions_map_filter_reduce.md) | **Lambda Functions, map, filter & reduce** | Anonymous functions, in-line sorting keys, ETL pipelines | 3 Examples |

### 06. Built-in Utility Functions

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.mathematical_and_numeric_functions.md`](06_builtin_functions/01.mathematical_and_numeric_functions.md) | **Mathematical & Numeric Functions** | abs, round (bankers' rounding), pow modular, divmod | 3 Examples |
| [`02.sequence_and_aggregation_functions.md`](06_builtin_functions/02.sequence_and_aggregation_functions.md) | **Sequence & Aggregation Functions** | len, min, max with custom key, sum, sorted, all, any | 3 Examples |
| [`03.iteration_tools_enumerate_zip_reversed.md`](06_builtin_functions/03.iteration_tools_enumerate_zip_reversed.md) | **Iteration Tools: enumerate, zip, reversed** | Index tracking, parallel streams, strict=True, reversed() | 3 Examples |

### 07. Object-Oriented Programming (OOP)

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.classes_objects_and_init_constructor.md`](07_oop/01.classes_objects_and_init_constructor.md) | **Classes, Objects & __init__ Constructor** | State and behavior, self parameter, instance __dict__ | 3 Examples |
| [`02.instance_attributes_and_methods.md`](07_oop/02.instance_attributes_and_methods.md) | **Instance Attributes & Methods** | Instance methods, method chaining fluent interface | 3 Examples |
| [`03.class_attributes_and_class_methods.md`](07_oop/03.class_attributes_and_class_methods.md) | **Class Attributes & Class Methods (@classmethod)** | Shared class state, alternative constructors via cls | 3 Examples |
| [`04.static_methods_and_utility_helpers.md`](07_oop/04.static_methods_and_utility_helpers.md) | **Static Methods & Utilities (@staticmethod)** | Pure utility functions, comparison table | 3 Examples |
| [`05.inheritance_single_and_multilevel.md`](07_oop/05.inheritance_single_and_multilevel.md) | **Inheritance: Single & Multilevel** | IS-A hierarchy, subclassing, isinstance/issubclass | 3 Examples |
| [`06.super_delegation_and_method_overriding.md`](07_oop/06.super_delegation_and_method_overriding.md) | **super() Delegation & Method Overriding** | C3 MRO, cooperative super() calls, method overriding | 3 Examples |
| [`07.composition_has_a_vs_inheritance_is_a.md`](07_oop/07.composition_has_a_vs_inheritance_is_a.md) | **Composition: HAS-A vs Inheritance (IS-A)** | Loose coupling, swappable components, order modeling | 3 Examples |

### 08. Error & Exception Handling

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.syntax_errors_vs_runtime_exceptions.md`](08_exceptions/01.syntax_errors_vs_runtime_exceptions.md) | **Syntax Errors vs Runtime Exceptions** | Parsing phase vs execution phase, common exception catalog | 3 Examples |
| [`02.try_except_blocks_and_built_in_exceptions.md`](08_exceptions/02.try_except_blocks_and_built_in_exceptions.md) | **try-except Blocks & Specific Exceptions** | Catching multiple exceptions, grouped tuples, LookupError | 3 Examples |
| [`03.try_except_else_finally_clauses.md`](08_exceptions/03.try_except_else_finally_clauses.md) | **try, except, else & finally Clauses** | else success block, finally clean-up guarantee | 3 Examples |
| [`04.raising_exceptions_and_custom_exceptions.md`](08_exceptions/04.raising_exceptions_and_custom_exceptions.md) | **Raising Exceptions & Custom Classes** | raise keyword, domain hierarchy, exception chaining (from) | 3 Examples |

### 09. Python Standard Library Modules

| Module File | Topic & Concept Description | Key Concepts Covered | Practical Examples |
| :--- | :--- | :--- | :---: |
| [`01.modules_imports_and_aliasing.md`](09_standard_library/01.modules_imports_and_aliasing.md) | **Modules, Imports & Aliasing** | import, from ... import, aliasing, __name__ == '__main__' | 3 Examples |
| [`02.math_module_and_mathematical_functions.md`](09_standard_library/02.math_module_and_mathematical_functions.md) | **The math Module & Mathematical Operations** | sqrt, ceil, floor, pi, hypot, factorial | 3 Examples |
| [`03.random_module_and_randomized_simulations.md`](09_standard_library/03.random_module_and_randomized_simulations.md) | **The random Module & Simulations** | randint, choice, shuffle, sample, seed, Monte Carlo | 3 Examples |
| [`04.datetime_module_dates_and_times.md`](09_standard_library/04.datetime_module_dates_and_times.md) | **The datetime Module: Dates & Times** | date, time, datetime objects, ISO 8601 parsing | 3 Examples |
| [`05.timedelta_durations_and_date_arithmetic.md`](09_standard_library/05.timedelta_durations_and_date_arithmetic.md) | **timedelta: Durations & Date Arithmetic** | Durations, SLA deadlines, launch countdowns | 3 Examples |
| [`06.strftime_and_strptime_formatting_parsing.md`](09_standard_library/06.strftime_and_strptime_formatting_parsing.md) | **strftime & strptime: Formatting & Parsing** | Date formatting specifiers (%Y, %m, %d, %B), multi-format parser | 3 Examples |

---
**Total Concept Modules**: 54 across 9 categories.
Every module contains in-depth conceptual theory, syntax rules, memory models, and **at least 3 complete real-world hands-on code examples with outputs**.
