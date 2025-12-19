Title: AI Prompting Techniques
Date: 2023-12-05
Category: AI
Slug: ai_prompting_techniques
Summary: LLM prompting techniques, methods, and research papers

### Types of Tasks LLMs Can Be Used For

* Text Generation and Completion
* Question Answering
* Information Retrieval and Summarization
* Language Translation
* Mathematical Reasoning
* Sentiment Analysis
* Logical and Commonsense Reasoning
* Task Decomposition
* Code Generation
* Role and Style Adaptation

### LLM Task Prompts and Text-based Techniques

#### Table 1: Type of Task, Prompting Technique, Description

| Task Type                             | Prompting Technique | Description                                                                            |
|---------------------------------------|---------------------|----------------------------------------------------------------------------------------|
| Mathematics and Reasoning             | Chain-of-Thought    | A technique that involves breaking down a problem into a series of intermediate steps to reach the solution. |
| Mathematics and Reasoning             | Zero-Shot CoT       | A technique where the model generates a step-by-step solution without prior examples.   |
| Mathematics and Reasoning             | Complexity-Based    | A technique that adapts the complexity of the prompt based on the task requirements.    |
| Mathematics and Reasoning             | Memory-of-Thought   | A technique that involves recalling previous thoughts to aid current problem-solving.   |
| Mathematics and Reasoning             | Least-to-Most       | A technique that breaks down a complex task into simpler, sequential steps.             |
| Mathematics and Reasoning             | Faithful CoT        | A technique that ensures each step logically follows from the previous one.             |
| Mathematics and Reasoning             | Recursion-of-Thought| A technique that involves recursive steps to handle complex problems.                   |
| Mathematics and Reasoning             | Self-Consistency    | A technique that ensures consistency in the model's responses across different prompts. |
| Mathematics and Reasoning             | Universal Self-Consistency | An advanced form of self-consistency applied to various tasks.                          |
| Mathematical and Code Generation      | Analogical Prompting| A technique that leverages analogies to facilitate problem-solving.                     |
| Question Answering and Retrieval      | Thread-of-Thought   | A technique that prompts the model to summarize and analyze a context step by step.     |
| Mathematics and Factual QA            | Contrastive         | A technique that compares different possible answers to improve reasoning accuracy.     |
| Mathematics and Logical Inference     | Cumulative Reasoning| A technique that builds upon previous steps to draw logical conclusions.                |
| Mathematics and Symbolic Manipulation | Least-to-Most       | A technique that breaks down a complex task into simpler, sequential steps.             |
| Mathematics and Symbolic Reasoning    | Faithful CoT        | A technique that ensures each step logically follows from the previous one.             |
| Mathematics and Algorithmic Tasks     | Recursion-of-Thought| A technique that involves recursive steps to handle complex problems.                   |
| Reasoning                             | Step-Back Prompting | A technique that involves periodically reviewing and revising previous steps to ensure accuracy. |
| Reasoning                             | Self-Verification   | A technique where the model verifies its own answers through internal checks.           |
| Reasoning                             | Plan-and-Solve      | A technique that involves planning a solution path before execution.                    |
| Reasoning                             | Self-Consistency    | A technique that ensures consistency in the model's responses across different prompts. |
| Reasoning                             | Universal Self-Consistency | An advanced form of self-consistency applied to various tasks.                          |
| Mathematics and Programming           | Program-of-Thought  | A technique that uses programming-like structures for problem-solving.                  |
| Search and Planning                   | Tree-of-Thought     | A technique that explores multiple possible solution paths in parallel.                 |
| Reasoning, Coding, and Generation     | Self-Refine         | A technique where the model iteratively refines its own answers.                        |
| Text Classification and Translation   | Few-Shot Prompting  | A technique that uses a few examples to guide the model's response.                     |
| Retrieval and Reasoning               | MoRE                | A technique that combines multiple reasoning paths to reach a conclusion.               |
| Text Generation                       | Universal Self-Consistency | An advanced form of self-consistency applied to various tasks.                          |

#### Table 2: Prompting Technique, Method, Research Paper Title & Authors

| Prompting Technique | Method         | Research Paper Title & Authors                                      |
|---------------------|----------------|---------------------------------------------------------------------|
| Chain-of-Thought    | Thought Generation | Chain-of-Thought Prompting (Wei et al., 2022)                        |
| Zero-Shot CoT       | Thought Generation | Let's think step by step: Zero-shot CoT (Kojima et al., 2022)        |
| Analogical Prompting| Thought Generation | Analogical Prompting (Yasunaga et al., 2023)                         |
| Step-Back Prompting | Thought Generation | Step-Back Prompting (Zheng et al., 2023)                             |
| Thread-of-Thought   | Thought Generation | Thread-of-Thought Prompting (Zhou et al., 2023)                      |
| Complexity-Based    | Thought Generation | Complexity-based Prompting (Fu et al., 2023)                         |
| Contrastive         | Thought Generation | Contrastive CoT Prompting (Chia et al., 2023)                        |
| Memory-of-Thought   | Thought Generation | Memory-of-Thought Prompting (Li and Qiu, 2023)                       |
| Cumulative Reasoning| Self-Criticism | Cumulative Reasoning (Zhang et al., 2023)                            |
| Least-to-Most       | Decomposition  | Least-to-Most Prompting (Zhou et al., 2022)                          |
| Faithful CoT        | Decomposition  | Faithful CoT (Lyu et al., 2023)                                      |
| Recursion-of-Thought| Decomposition  | Recursion-of-Thought (Lee and Kim, 2023)                             |
| Plan-and-Solve      | Decomposition  | Plan-and-Solve Prompting (Wang et al., 2023)                         |
| Program-of-Thought  | Decomposition  | Program-of-Thoughts (Chen et al., 2023)                              |
| Tree-of-Thought     | Decomposition  | Tree-of-Thought (Yao et al., 2023)                                   |
| Self-Refine         | Self-Criticism | Self-Refine (Madaan et al., 2023)                                    |
| Self-Verification   | Self-Criticism | Self-Verification (Weng et al., 2022)                                |
| Few-Shot Prompting  | In-Context Learning (ICL) | Few-Shot Prompting (Brown et al., 2020)                              |
| MoRE                | Ensembling     | Mixture of Reasoning Experts (Si et al., 2023)                       |
| Self-Consistency    | Ensembling     | Self-Consistency (Wang et al., 2022)                                 |
| Universal Self-Consistency | Ensembling     | Universal Self-Consistency (Chen et al., 2023)                       |

#### Table 3: Prompting Technique and Prompt Example

| Prompting Technique | Example Prompt                                                                                   |
|---------------------|--------------------------------------------------------------------------------------------------|
| Chain-of-Thought    | Q: Jack has two baskets, each containing three balls. How many balls does Jack have in total? A: One basket contains 3 balls, so two baskets contain 3 * 2 = 6 balls. Q: {QUESTION} A:  |
| Zero-Shot CoT       | Let's think step by step. |
| Thread-of-Thought   | Walk me through this context in manageable parts step by step, summarizing and analyzing as we go. |
| Plan-and-Solve      | Let's first understand the problem and devise a plan to solve it. Then, let's carry out the plan and solve the problem step by step. |
| Few-Shot Prompting  | Provide 2-3 examples of the desired input/output format before your actual query. |
| Self-Consistency    | Generate multiple reasoning paths and select the most consistent answer. |
| Tree-of-Thought     | Explore multiple solution branches in parallel before converging on the best path. |
| Self-Refine         | Review your response and improve it based on self-identified weaknesses. |

### Prompt Guidelines

* clarity
* specificity
* direction (e.g. goal)

#### Combining prompt types

1) identify need
2) write first prompt
3) write more specific prompt based on first response
   OR
   combine goal-oriented & specific prompt

#### Iterative prompting

Refining AI responses through a sequence of prompts that build on each other.

### Papers

* [Few Shots - [2001.08361] Scaling Laws for Neural Language Models (arxiv.org)](https://arxiv.org/abs/2001.08361)
* [Chain of Thought - [2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (arxiv.org)](https://arxiv.org/abs/2201.11903)
* [Self Consistency aka CoT@k - [2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models (arxiv.org)](https://arxiv.org/abs/2203.11171)
* [Tree of Thought - [2305.10601] Tree of Thoughts: Deliberate Problem Solving with Large Language Models (arxiv.org)](https://arxiv.org/abs/2305.10601)
* [ReAct - [2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models (arxiv.org)](https://arxiv.org/abs/2210.03629)
