# Predictive Stepping

Programming is communication. It's also a lot of other things, but this
introduction will focus on the different ways you communicate with your code.

When you write code you are really just writing a text document, exactly like
you might write an email or a note. The biggest difference between an email and
a computer program is _who you are writing for_.

When you write an email you're writing for the person who will be reading it.
When you write a computer program you are writing for 3 very different audiences
at the same time! One single document (your code) needs to be understandable to:

- **Developers**: A developer needs to read your code and understand what you
  were trying to do and why.
- **Computers**: Your code needs to have _perfect_ syntax so the computer can
  parse it, and you must write instructions that are allowed by the programming
  language or the computer will throw an error.
- **Users**: The instructions you give to the computer must create an intuitive
  and pleasant experience for the user.

Being a developer means understanding how all these characters interact, and
then communicating with everyone involved to deliver quality software within
your project's constraints. This diagram shows the different channels of
communication in a simple Python program:

![a program](./computers_and_developers.png)

> PS. In the examples and exercises for this chapter you will be both the developer and the user, running the program and interacting with it from command line.

## Stepping Through Programs

This chapter has a few small programs that showcase different Python language features. Use these programs to practice:

- Stepping through programs with your debugger
- Finding variables' values in the scope pane
- Understanding a program's _callstack_

To carefully study a program, practice following these steps. You know you understand a program when you can predict each step without mistakes:

1. Predict which line will execute next and how it will change program state (variables & callstack)
2. Step forward in the program.
3. Check your prediction.
4. Investigate if you were wrong: Is this a bug in the program, or is it something you did not understand?

> PS. You can write all the comments you want!

## Learning Objectives

- 🥚 **Using Breakpoints**:
  - You can add and remove breakpoints, before and while you are debugging a program.
  - You can enable and disable breakpoints without removing them.
- 🥚 **Launching the Debugger**: You can open the debugger pane and launch a single-file Python program.
- **Debugger Buttons**
  - 🥚 **Skip Ahead**: You can skip ahead to the next breakpoint or the end of the program.
  - 🥚 **Step Over**: You can step _over_ a function call to ignore its implementation.
  - 🥚 **Step In**: You can step _into_ a function call to debug it's implementation.
  - 🥚 **Step Out**: You can step _out of_ a function call to resume debugging the main program.
  - 🥚 **Restart**: You can restart your debugger at the beginning of the program.
  - 🥚 **Exiting**: You can exit the debugger at any point of execution.
- 🥚 **Reading State**: At each point in a program's execution, you can find the value of any declared variable in the Variables pane.
- **The Call Stack**:
  - 🥚 You understand the relationship to between the _callstack_ pane, _local variables_ and _function calls_.
  - 🥚 You can view the local variables for each level of the callstack by clicking on it.
- 🐣 **Variable Categories**: You can explain the difference between _Locals_, _Globals_, _Function Variables_, _Class Variables_, and _Special Variables_
- 🐣 You can _predict_ a program's behavior while stepping through in the debugger:
  - Which line will execute next?
  - What will change in memory (_callstack_ and _variables_)?
- 🐣 You can identify steps of execution that surprise you. This will help understand the gap between what a program _does_ do, and what it _should_ do.
- 🐥 **Watch Expressions**: You can create helpful _watch expressions_ and use them to track information about your program that is not explicitly declared in the code.
- 🐔 **Backtracing** You can trace a program backwards from a surprising step to understand how the program reached this state (either mentally or on paper, VSCode's debugger only goes forward).
