# Test-Driven Development with Large Language Models

Large Language Models (LLMs) can generate lots of (mostly) working code very quickly. If you're not careful, LLMs can make you a sloppy programmer and slow down your progress in the long run. If you use LLMs carefully, you can learn more quickly and become a more efficient developer. This workshop covers one strategy for collaborating with LLMs to go from a blank page to finished code that is readable, documented, and well-tested.

- [Prerequisites](#prerequisites)
- [Learning Objectives](#learning-objectives)
- [Prep Work](#prep-work)
- [Workshop Outline](#workshop-outline)

---

## Prerequisites

- [Documenting and Testing](https://github.com/MIT-Emerging-Talent/documenting-and-testing)
- [Debugging](https://github.com/MIT-Emerging-Talent/debugging)

---

## Learning Objectives

<details><summary>Priorities: 🥚🐣🐥🐔 (click for more info)</summary>
<br />

Learning objectives for this workshop are labeled so you can prioritize your study time. The emojis show the _minimum_ mastery you are expected to achieve for each skill, but there is no maximum! If you have the time you should aim to master all of the skills introduced in this workshop.

- 🥚 You are expected to master these skills. They are the foundations you will need to move forward.
- 🐣 You are expected to be comfortable with these skills. It's ok if you still need help sometimes.
- 🐥 You are expected to be familiar with these skills. It's enough to recognize them in practice and apply them with help.
- 🐔 You are not expected to know these skills, but they are important if you want to excel. You should only focus on these after mastering the 🥚, 🐣 and 🐥 objectives.

---

</details>

### TDD with LLMs

- 🥚 You can translate an open-ended problem into a complete docstring.
- 🥚 You can use an LLM to generate code by providing a clear prompt and code for context.
- 🥚 You can comment, understand and review code generated by an LLM, judging if it is correct or not.
- 🥚 You run your unit tests every time you make any change to your function, making sure they still pass.
- 🥚 Every time you want to change a function's behavior, you first update the tests before changing the function.
- 🐣 When a test fails, you can determine if it was the test or the function that is not correct.
- 🐣 You can collaborate with an LLM to find and fix bugs in your code.
- 🐣 You can collaborate with an LLM to _refactor_ a program's strategy or implementation without modifying its behavior.
- 🐣 You can polish and personalize your final code to showcase your understanding instead of just another program generated from an LLM.

### Situating LLMs

- 🥚 You are aware of concerns that LLMs may generate responses in violation of copyright law, or that violate data privacy.
- 🥚 You are aware that training and running LLMs [consumes more energy](https://ai.stackexchange.com/questions/38970/how-much-energy-consumption-is-involved-in-chat-gpt-responses-being-generated) than older tools like [internet search](https://arxiv.org/pdf/2307.01135.pdf).
- 🥚 You are aware that LLMs can _hallucinate_ - they can produce responses that feel correct but are actually untrue.
- 🥚 You are aware that LLMs can, despite many guardrails, produce responses that perpetuate stereotypes and misconceptions.

### Non-Objective: Prompt Engineering

This workshop does not cover _prompt engineering_: how to carefully construct sentences and questions for the LLM to get better results. Prompt engineering is a whole topic of it's own. You can learn more about it online by following [tutorials](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/), reading [articles](https://en.wikipedia.org/wiki/Prompt_engineering), and [practicing](https://phind.com/).

Instead we will zoom out from specific LLM prompts and focus on how you can integrate LLMs into your development workflow.

---

## Prep Work

Read through these two documents:

- [Test-Driven Development](./test_driven_development.md)
- [CoAIthoring Workflow](./coaithoring_workflow.md)

Read through the examples:

- `examples/stepped`: This folder contains worked examples of developing with an LLM. Each of the files is a snapshot of a different step the development process. The final product is in one file, not two files like yours should be.
- `examples/separated`: This folder contains examples of the finished product _after_ you have developed a solution with an LLM. You should notice that the finished code is no different from what you wrote in [Documenting and Testing](https://github.com/MIT-Emerging-Talent/documenting-and-testing), that's on purpose! LLMs may improve your development _process_, but they do not change the need for well tested, documented, and understandable code.
  - [/examples/separated/add_two_numbers](./examples/separated/add_two_numbers) has a guide video explaining how the code was developed.

---

## Workshop Outline

### Workshop Overview _(all together)_

The workshop instructor will introduce the main concepts of this workshop:

- Introduce the workshop's [learning objectives](#learning-objectives).
- Discuss some trade-offs to consider when studying and developing with an LLM.
- Talk through the [CoAIthoring Workflow](./coaithoring-workflow.md).
- Demonstrate how to do TDD with an LLM by developing a function that adds two numbers
  - We will use [phind](https://phind.com) because you do not need to create an account.
- Introduce the group exercises.

### Practice CoAIthoring _(small groups)_

Each small group will choose one of the [/exercises](./exercises/) and develop tests + a solution using [phind](https://phind.com) for support.

You can start with any exercise you like, and move on to another if you finish.

### Discussion _(all together)_

Back together, you will have an informal discussion with the other groups and the workshop leader.

1. Each group will have 2-3 minutes to share:
   - One thing they couldn't figure out
   - One surprising thing they learned
   - One thing they'd like to discuss with the full class
2. Discuss!
