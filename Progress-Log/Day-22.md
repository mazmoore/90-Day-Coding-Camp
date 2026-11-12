
# Day 22 — Variable Scope

**Language:** Python  
**Topic:** Variable Scope  
**Status:** Review pending

## Learning Objectives

- Understand what variable scope means.
- Learn Python's LEGB lookup rule.
- Create local variables inside functions.
- Understand local variable accessibility.
- Create and read global variables.
- Understand variable shadowing.
- Recognize that function parameters are local names.
- Use return values to transfer information.
- Reduce unnecessary global dependencies.
- Understand the `global` statement.
- Understand why reading globals does not require `global`.
- Create nested functions.
- Understand enclosing scope.
- Use `nonlocal` to reassign enclosing variables.
- Create closures.
- Create independent closure instances.
- Recognize Python's built-in names.
- Avoid shadowing built-in functions.
- Understand common scope errors.
- Recognize `UnboundLocalError`.
- Understand mutable argument side effects.
- Use copies to avoid unwanted mutation.
- Understand loop and conditional block scope.
- Understand comprehension scope.
- Recognize local variables in recursive calls.
- Use uppercase naming conventions for constants.
- Pass configuration values explicitly.
- Apply scope concepts to business calculations.
- Apply scope concepts to cybersecurity analysis.
- Build reusable functions without shared global state.

## Lesson Files

- `Python/Fundamentals/day22_scope.py`
- `Python/Exercises/day22_exercises.py`

## Exercises

- [ ] Create a local variable.
- [ ] Create separate local variables.
- [ ] Explore local variable lifetime.
- [ ] Create a global variable.
- [ ] Read a global variable.
- [ ] Compare local and global names.
- [ ] Demonstrate variable shadowing.
- [ ] Use a local parameter.
- [ ] Reuse parameter names.
- [ ] Return a local value.
- [ ] Avoid unnecessary global variables.
- [ ] Update a value using return.
- [ ] Use `global`.
- [ ] Read a global without `global`.
- [ ] Replace global state with parameters.
- [ ] Explore enclosing scope.
- [ ] Shadow an enclosing variable.
- [ ] Use `nonlocal`.
- [ ] Create a nested function.
- [ ] Return a nested function.
- [ ] Create a closure.
- [ ] Create a closure with `nonlocal`.
- [ ] Create independent closures.
- [ ] Explore built-in scope.
- [ ] Avoid shadowing built-in names.
- [ ] Demonstrate LEGB resolution.
- [ ] Read a global as a fallback.
- [ ] Explain `UnboundLocalError`.
- [ ] Correct a scope problem.
- [ ] Modify a mutable list argument.
- [ ] Avoid unwanted list mutation.
- [ ] Modify a dictionary argument.
- [ ] Return a modified dictionary copy.
- [ ] Explore loop scope.
- [ ] Explore conditional scope.
- [ ] Explore comprehension scope.
- [ ] Test separate function calls.
- [ ] Practice recursion and local scope.
- [ ] Use uppercase constant conventions.
- [ ] Pass configuration through parameters.
- [ ] Calculate remaining flower inventory.
- [ ] Calculate bouquet pricing.
- [ ] Calculate a customer order total.
- [ ] Count failed logins using local state.
- [ ] Create a security configuration summary.
- [ ] Create independent event counters.
- [ ] Generate independent event reports.
- [ ] Test independent function calls.
- [ ] Create nested security report functions.
- [ ] Build an independent security event analyzer.

## Practical Applications

Variable scope determines where names can be accessed and how information moves between different parts of a Python program.

Understanding local, enclosing, global, and built-in scope helps prevent naming conflicts and unexpected changes to program state.

In business applications, functions can use local variables and parameters to calculate inventory quantities, product pricing, and customer order totals without relying on shared global variables.

In cybersecurity, explicit parameters and returned results help organize security event analysis, configuration handling, event counting, and reporting.

Closures can maintain independent counters or other state when appropriate, while local variables and return values support predictable, reusable functions.

## Reflection

**What did I learn?**

To be completed after reviewing the lesson.

**What was challenging?**

To be completed after completing the exercises.

**What would I like to practice again?**

To be completed after completing the exercises.

## Next Lesson

Day 23 — Boolean Logic
