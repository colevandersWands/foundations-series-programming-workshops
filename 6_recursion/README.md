# Recursion

## Template Recursive Solution

```py
def _func_name_(__: __) -> __:
    is_base_case = __ # must use argument(s)
    if is_base_case:
        turn_around = __
        return turn_around

    break_down = __ # must use argument(s)
    recursion = _func_name_(break_down)
    build_up = __ # must use recursion variable
    return build_up
```

## Learning Objectives

- 🥚 **The Callstack**: You can inspect, explain, and predict a program's callstack using the debugger.
- 🥚 **Stack Overflow**: You can inspect and explain stack overflow errors.
- 🥚 **Parts of a Recursive Solution**: You can explain how the 5 parts of a recursion solution work together:
  - _Base Case_
  - _Turn-Around_
  - _Break-Down_
  - _Recursion_
  - _Build-Up_
- 🥚 **Labeling Recursive Solutions**: You can use comments to identify and label the 5 parts of a recursive solution written in Python.
- 🥚 **(semi)Formal Definition**: You can write a (semi)formal recursive definition to describe a recursive solution written in Python.
- 🐣 **Visualizing Implementation**: You can use the debugger and print statements to visualize a recursive solution's implementation.
- 🐣 **Visualizing Strategy**: You can visualize a recursive solution's strategy using the tool(s) of your choice:
  - The `recursion_tracer` decorator in this repository.
  - Python Packages: [`rcviz`](https://github.com/carlsborg/rcviz?tab=readme-ov-file), [recursion-visualizer](https://pypi.org/project/recursion-visualizer/), [Recursion-Tree-Visualizer](https://github.com/Bishalsarang/Recursion-Tree-Visualizer?tab=readme-ov-file)
  - Websites: [recursionvisualizer.com](https://www.recursionvisualizer.com), [recursion.vercel.app](https://recursion.vercel.app), [recursion-visualizer.vercel.app](https://recursion-visualizer.vercel.app), [visualgo.net] (https://visualgo.net/en/recursion)
- 🐣 **Debugging Recursion**: You can use the 5 parts of recursion to help find and fix bugs in a recursive solution.
- 🐥**Writing Recursion**: You can plan a recursive solution using the 5 parts as a guide, then can implement your strategy as a Python function.