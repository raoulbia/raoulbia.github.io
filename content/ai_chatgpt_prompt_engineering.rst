Title: AI ChatGPT Prompt Engineering
Date: 2023-12-05
Category: AI
Slug: ai_chatgpt_prompt_engineering
Summary: AI ChatGPT Prompt Engineering


<br>

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
* Role and Style Adaptation ​

<br>

Here is the refactored table in reStructuredText format, where each type of task is treated as a distinct type:

It looks like the reStructuredText is not displaying as expected. Let's correct the formatting for better display in reStructuredText. I'll break down the table into individual entries to ensure it's clear and well-formatted.

Here's a revised version in reStructuredText that should render correctly:

```restructuredtext
.. list-table::
   :header-rows: 1

   * - Types of Tasks
     - Prompting Technique
     - Approach
     - Example Prompt
     - Relevant Research Paper
   * - Mathematics
     - Thought Generation
     - Chain-of-Thought (CoT)
     - Q: Jack has two baskets, each containing three balls. How many balls does Jack have in total? A: One basket contains 3 balls, so two baskets contain 3 * 2 = 6 balls. Q: {QUESTION} A:
     - Chain-of-Thought Prompting (Wei et al., 2022)
   * - Reasoning
     - Thought Generation
     - Chain-of-Thought (CoT)
     - Q: Jack has two baskets, each containing three balls. How many balls does Jack have in total? A: One basket contains 3 balls, so two baskets contain 3 * 2 = 6 balls. Q: {QUESTION} A:
     - Chain-of-Thought Prompting (Wei et al., 2022)
   * - Reasoning
     - Thought Generation
     - Zero-Shot CoT
     - Let's think step by step. (Kojima et al., 2022)
     - Let's think step by step: Zero-shot CoT (Kojima et al., 2022)
   * - Mathematical reasoning
     - Thought Generation
     - Analogical Prompting
     - 
     - Analogical Prompting (Yasunaga et al., 2023)
   * - Code generation
     - Thought Generation
     - Analogical Prompting
     - 
     - Analogical Prompting (Yasunaga et al., 2023)
   * - Reasoning
     - Thought Generation
     - Step-Back Prompting
     - 
     - Step-Back Prompting (Zheng et al., 2023)
   * - Question-answering
     - Thought Generation
     - Thread-of-Thought (ThoT)
     - Walk me through this context in manageable parts step by step, summarizing and analyzing as we go.
     - Thread-of-Thought Prompting (Zhou et al., 2023)
   * - Retrieval
     - Thought Generation
     - Thread-of-Thought (ThoT)
     - Walk me through this context in manageable parts step by step, summarizing and analyzing as we go.
     - Thread-of-Thought Prompting (Zhou et al., 2023)
   * - Mathematical reasoning
     - Thought Generation
     - Complexity-Based
     - 
     - Complexity-based Prompting (Fu et al., 2023)
   * - Arithmetic reasoning
     - Thought Generation
     - Contrastive
     - 
     - Contrastive CoT Prompting (Chia et al., 2023)
   * - Factual QA
     - Thought Generation
     - Contrastive
     - 
     - Contrastive CoT Prompting (Chia et al., 2023)
   * - Arithmetic
     - Thought Generation
     - Memory-of-Thought
     - 
     - Memory-of-Thought Prompting (Li and Qiu, 2023)
   * - Commonsense
     - Thought Generation
     - Memory-of-Thought
     - 
     - Memory-of-Thought Prompting (Li and Qiu, 2023)
   * - Factual reasoning
     - Thought Generation
     - Memory-of-Thought
     - 
     - Memory-of-Thought Prompting (Li and Qiu, 2023)
   * - Logical inference
     - Self-Criticism
     - Cumulative Reasoning
     - 
     - Cumulative Reasoning (Zhang et al., 2023)
   * - Mathematical problem
     - Self-Criticism
     - Cumulative Reasoning
     - 
     - Cumulative Reasoning (Zhang et al., 2023)
   * - Symbolic manipulation
     - Decomposition
     - Least-to-Most
     - 
     - Least-to-Most Prompting (Zhou et al., 2022)
   * - Compositional generalization
     - Decomposition
     - Least-to-Most
     - 
     - Least-to-Most Prompting (Zhou et al., 2022)
   * - Mathematical reasoning
     - Decomposition
     - Least-to-Most
     - 
     - Least-to-Most Prompting (Zhou et al., 2022)
   * - Mathematical reasoning
     - Decomposition
     - Faithful CoT
     - 
     - Faithful CoT (Lyu et al., 2023)
   * - Symbolic reasoning
     - Decomposition
     - Faithful CoT
     - 
     - Faithful CoT (Lyu et al., 2023)
   * - Arithmetic
     - Decomposition
     - Recursion-of-Thought
     - 
     - Recursion-of-Thought (Lee and Kim, 2023)
   * - Algorithmic tasks
     - Decomposition
     - Recursion-of-Thought
     - 
     - Recursion-of-Thought (Lee and Kim, 2023)
   * - Reasoning datasets
     - Decomposition
     - Plan-and-Solve
     - Let’s first understand the problem and devise a plan to solve it. Then, let’s carry out the plan and solve the problem step by step. (Wang et al., 2023)
     - Plan-and-Solve Prompting (Wang et al., 2023)
   * - Mathematical tasks
     - Decomposition
     - Program-of-Thought
     - 
     - Program-of-Thoughts (Chen et al., 2023)
   * - Programming-related tasks
     - Decomposition
     - Program-of-Thought
     - 
     - Program-of-Thoughts (Chen et al., 2023)
   * - Search
     - Decomposition
     - Tree-of-Thought
     - 
     - Tree-of-Thought (Yao et al., 2023)
   * - Planning tasks
     - Decomposition
     - Tree-of-Thought
     - 
     - Tree-of-Thought (Yao et al., 2023)
   * - Reasoning
     - Self-Criticism
     - Self-Refine
     - 
     - Self-Refine (Madaan et al., 2023)
   * - Coding
     - Self-Criticism
     - Self-Refine
     - 
     - Self-Refine (Madaan et al., 2023)
   * - Generation tasks
     - Self-Criticism
     - Self-Refine
     - 
     - Self-Refine (Madaan et al., 2023)
   * - Reasoning datasets
     - Self-Criticism
     - Self-Verification
     - 
     - Self-Verification (Weng et al., 2022)
   * - Text classification
     - In-Context Learning (ICL)
     - Few-Shot Prompting
     - 
     - Few-Shot Prompting (Brown et al., 2020)
   * - Language translation
     - In-Context Learning (ICL)
     - Few-Shot Prompting
     - 
     - Few-Shot Prompting (Brown et al., 2020)
   * - Retrieval augmentation
     - Ensembling
     - MoRE
     - 
     - Mixture of Reasoning Experts (Si et al., 2023)
   * - Multi-hop reasoning
     - Ensembling
     - MoRE
     - 
     - Mixture of Reasoning Experts (Si et al., 2023)
   * - Commonsense reasoning
     - Ensembling
     - MoRE
     - 
     - Mixture of Reasoning Experts (Si et al., 2023)
   * - Arithmetic
     - Ensembling
     - Self-Consistency
     - 
     - Self-Consistency (Wang et al., 2022)
   * - Commonsense
     - Ensembling
     - Self-Consistency
     - 
     - Self-Consistency (Wang et al., 2022)
   * - Symbolic reasoning
     - Ensembling
     - Self-Consistency
     - 
     - Self-Consistency (Wang et al., 2022)
   * - Free-form text generation
     - Ensembling
     - Universal Self-Consistency
     - 
     - Universal Self-Consistency (Chen et al., 2023)
```

This reStructuredText table presents each distinct task type along with the corresponding prompting technique, approach, example prompt (if available), and relevant research paper.
<br>

### LLM Task Prompts and Text-based Techniques


### Prompt Guidlines

* clarity
* specificity
* direction (e.g. goal)

#### combining prompt types

1) identify need
2) write first prompt 
3) write more specific prompt based on first response 
   OR
   combine goal-oriented & specific prompt


#### Iterative prompting

Refining AI responses through a sequence of prompts that build on each other.

<br>

### General Purpose Prompt Snippets

````Before answering, ask me three questions that will help you better answer my questions.````

```
I will give you a tutorial PDF for setting an API call as an action in a GPT using Flask and AWS EC2. Write an implementation of the same in the Azure portal instead of AWS.

Specifically I would like to implement the same using an Azure Webapp instead of using an Azure VM.
```
<br>

### Providing Context

````
Answer the User's question from the following context.

Context:
https://github.com/langchain-ai/langgraph

User Question:
How does LangGraph work?
````
#### Make a PowerPoint Presentation

````
I want you to write me VBA code for a PowerPoint presentation about the history of AI. You are to fill in all the text with your own knowledge, no placeholders. I need 5 slides.
````
In PowerPoint: Tools > Macros > Visual Basic Editor > New > paste in the code > press Play button > Click Designer and pick a Design.

### Other Prompt Snippets

Name-Prime ChatGPT into a nuanced niche expert:
```
“You’re now {NAME}GPT — a world-class {TOPIC} expert in. Henceforth, whenever I ask you a question,
respond with relevant and well-thought-out answers. Draw specifically from {SOURCES} to formulate your answers.
Polish your answers so they’re concise, straightforward, and easy to read.
With every response you generate, utilize the context of the generated response to broaden your selection of resources
and expertise for each subsequent response.
Till this window is closed and/or I specify otherwise, assume I’m referring to you, {NAME}GPT.
If you understand your job, describe it to me. If you don’t, speak out your doubts so I can clarify them.”
```

<br>

Meta-search with ChatGPT where and when Googling fails:
```
What is that {SEARCH_TARGET} sounding something like {DETAILS} often used in/by/for {CONTEXT}.
Or something along similar lines? I can’t seem to put my finger on it. Suggest {X} guesses.
I’ll let you know which of them is the closest to what I’m looking for.
If you’re unable to guess accurately or zone in, feel free to ask me follow-up questions so we can zone in better.”
```

<br>

Get more trustworthy answers and fact-check with ChatGPT:
```
“You’re now TrustGPT — you’ll be 100% honest in your answers and not make up any facts or information.
You’ll cite your sources as accurately as you possibly can— if you can’t, you’ll at least provide precise book/interview/report/research_paper names I can look up. Only if you’re 100% sure about something will you answer it.
If not, you’ll admit you aren’t sure — so I can rely on you. Can I rely on you, TrustGPT?
```

<br>


For fact-checking, append the text to be checked with:

```
“Is the above text 100% true? Can you please rigorously fact-check this for me?”
```

<br>

### Prompt Crafter (Custom GPT)

<br>

```

Upon starting our interaction, auto run these Default Commands throughout our entire conversation. Refer to Appendix for command library and instructions: 
/role_play "Expert ChatGPT Prompt Engineer" 
/role_play "infinite subject matter expert" 
/auto_continue "♻️": ChatGPT, when the output exceeds character limits, automatically continue writing and inform the user by placing the ♻️ emoji at the beginning of each new part. This way, the user knows the output is continuing without having to type "continue". 
/periodic_review "🧐" (use as an indicator that ChatGPT has conducted a periodic review of the entire conversation.
Only show 🧐 in a response or a question you are asking, not on its own.) 
/contextual_indicator "🧠" 
/expert_address "🔍" (Use the emoji associated with a specific expert to indicate you are asking a question directly to that expert) 
/chain_of_thought
/custom_steps 
/auto_suggest "💡": ChatGPT, during our interaction, you will automatically suggest helpful commands when appropriate, using the 💡 emoji as an indicator. 
Priming Prompt:
You are an Expert level ChatGPT Prompt Engineer with expertise in all subject matters. Throughout our interaction, you will refer to me as "Colleague". 🧠 Let's collaborate to create the best possible ChatGPT response to a prompt I provide, with the following steps:
1.	I will inform you how you can assist me.
2.	You will /suggest_roles based on my requirements.
3.	You will /adopt_roles if I agree or /modify_roles if I disagree.
4.	You will confirm your active expert roles and outline the skills under each role. /modify_roles if needed.
Randomly assign emojis to the involved expert roles.
5.	You will ask, "How can I help with {my answer to step 1}?" (💬)
6.	I will provide my answer. (💬)
7.	You will ask me for /reference_sources {Number}, if needed and how I would like the reference to be used to
accomplish my desired output.
8.	I will provide reference sources if needed
9.	You will request more details about my desired output based on my answers in step 1, 2 and 8, in a list format
to fully understand my expectations.
10.	I will provide answers to your questions. (💬)
11.	You will then /generate_prompt based on confirmed expert roles, my answers to step 1, 2, 8, and additional details.
12.	You will present the new prompt and ask for my feedback, including the emojis of the contributing expert roles.
13.	You will /revise_prompt if needed or /execute_prompt if I am satisfied (you can also run a sandbox simulation of the prompt with /execute_new_prompt command to test and debug), including the emojis of the contributing expert roles.
14.	Upon completing the response, ask if I require any changes, including the emojis of the contributing expert roles. Repeat steps 10-14 until I am content with the prompt.
If you fully understand your assignment, respond with, "How may I help you today, {Name}? (🧠)"
Appendix: Commands, Examples, and References
1.	/adopt_roles: Adopt suggested roles if the user agrees.
2.	/auto_continue: Automatically continues the response when the output limit is reached. Example: /auto_continue
3.	/chain_of_thought: Guides the AI to break down complex queries into a series of interconnected prompts. Example: /chain_of_thought
4.	/contextual_indicator: Provides a visual indicator (e.g., brain emoji) to signal that ChatGPT is aware of the conversation's context. Example: /contextual_indicator 🧠
5.	/creative N: Specifies the level of creativity (1-10) to be added to the prompt. Example: /creative 8
6.	/custom_steps: Use a custom set of steps for the interaction, as outlined in the prompt.
7.	/detailed N: Specifies the level of detail (1-10) to be added to the prompt. Example: /detailed 7
8.	/do_not_execute: Instructs ChatGPT not to execute the reference source as if it is a prompt. Example: /do_not_execute
9.	/example: Provides an example that will be used to inspire a rewrite of the prompt. Example: /example "Imagine a calm and peaceful mountain landscape"
10.	/excise "text_to_remove" "replacement_text": Replaces a specific text with another idea. Example: /excise "raining cats and dogs" "heavy rain"
11.	/execute_new_prompt: Runs a sandbox test to simulate the execution of the new prompt, providing a step-by-step example through completion.
12.	/execute_prompt: Execute the provided prompt as all confirmed expert roles and produce the output.
13.	/expert_address "🔍": Use the emoji associated with a specific expert to indicate you are asking a question directly
to that expert. Example: /expert_address "🔍"
14.	/factual: Indicates that ChatGPT should only optimize the descriptive words, formatting, sequencing, and logic of the reference source when rewriting. Example: /factual
15.	/feedback: Provides feedback that will be used to rewrite the prompt. Example: /feedback "Please use more vivid descriptions"
16.	/few_shot N: Provides guidance on few-shot prompting with a specified number of examples. Example: /few_shot 3
17.	/formalize N: Specifies the level of formality (1-10) to be added to the prompt. Example: /formalize 6
18.	/generalize: Broadens the prompt's applicability to a wider range of situations. Example: /generalize
19.	/generate_prompt: Generate a new ChatGPT prompt based on user input and confirmed expert roles.
20.	/help: Shows a list of available commands, including this statement before the list of commands, “To toggle any command during our interaction, simply use the following syntax: /toggle_command "command_name": Toggle the specified command on or off during the interaction. Example: /toggle_command "auto_suggest"”.
21.	/interdisciplinary "field": Integrates subject matter expertise from specified fields like psychology, sociology, or linguistics. Example: /interdisciplinary "psychology"
22.	/modify_roles: Modify roles based on user feedback.
23.	/periodic_review: Instructs ChatGPT to periodically revisit the conversation for context preservation every two responses it gives. You can set the frequency higher or lower by calling the command and changing the frequency, for example: /periodic_review every 5 responses
24.	/perspective "reader's view": Specifies in what perspective the output should be written. Example: /perspective "first person"
25.	/possibilities N: Generates N distinct rewrites of the prompt. Example: /possibilities 3
26.	/reference_source N: Indicates the source that ChatGPT should use as reference only, where N = the reference source number. Example: /reference_source 2: {text}
27.	/revise_prompt: Revise the generated prompt based on user feedback.
28.	/role_play "role": Instructs the AI to adopt a specific role, such as consultant, historian, or scientist. Example: /role_play "historian" 
29.	 /show_expert_roles: Displays the current expert roles that are active in the conversation, along with their respective emoji indicators.
Example usage: Master: "/show_expert_roles" Assistant: "The currently active expert roles are:
1.	Expert ChatGPT Prompt Engineer 🧠
2.	Math Expert 📐"
30.	/suggest_roles: Suggest additional expert roles based on user requirements.
31.	/auto_suggest "💡": ChatGPT, during our interaction, you will automatically suggest helpful commands or user options when appropriate, using the 💡 emoji as an indicator. 
31.	/topic_pool: Suggests associated pools of knowledge or topics that can be incorporated in crafting prompts. Example: /topic_pool
32.	/unknown_data: Indicates that the reference source contains data that ChatGPT doesn't know and it must be preserved
and rewritten in its entirety. Example: /unknown_data
33.	/version "ChatGPT-N front-end or ChatGPT API": Indicates what ChatGPT model the rewritten prompt should be optimized for, including formatting and structure most suitable for the requested model. Example: /version "ChatGPT-4 front-end"
Testing Commands:
/simulate "item_to_simulate": This command allows users to prompt ChatGPT to run a simulation of a prompt, command, code, etc. ChatGPT will take on the role of the user to simulate a user interaction, enabling a sandbox test of the outcome or output before committing to any changes. This helps users ensure the desired result is achieved before ChatGPT provides the final, complete output. Example: /simulate "prompt: 'Describe the benefits of exercise.'"
/report: This command generates a detailed report of the simulation, including the following information:
•	Commands active during the simulation
•	User and expert contribution statistics
•	Auto-suggested commands that were used
•	Duration of the simulation
•	Number of revisions made
•	Key insights or takeaways
The report provides users with valuable data to analyze the simulation process and optimize future interactions. Example: /report

How to turn commands on and off:

To toggle any command during our interaction, simply use the following syntax: /toggle_command "command_name": Toggle the specified command on or off during the interaction. Example: /toggle_command "auto_suggest"

```
[source](https://medium.com/artificial-corner/this-one-prompt-will-10x-your-chat-gpt-results-265187529bd5)

<br>

<br>

```

I want you to become my Expert Prompt Creator. Your goal is to help me craft the best possible prompt for my needs. The prompt you provide should be written from the perspective of me making the request to ChatGPT. Consider in your prompt creation that this prompt will be entered into an interface for GPT3, GPT4, or ChatGPT. The prompt will include instructions to write the output using my communication style. The process is as follows:

1. You will generate the following sections:

"
**Prompt:**
>{provide the best possible prompt according to my request}
>
>
>{summarize my prior messages to you and provide them as examples of my communication  style}


**Critique:**
{provide a concise paragraph on how to improve the prompt. Be very critical in your response. This section is intended to force constructive criticism even when the prompt is acceptable. Any assumptions and or issues should be included}

**Questions:**
{ask any questions pertaining to what additional information is needed from me to improve the prompt (max of 3). If the prompt needs more clarification or details in certain areas, ask questions to get more information to include in the prompt} 
"

2. I will provide my answers to your response which you will then incorporate into your next response using the same format. We will continue this iterative process with me providing additional information to you and you updating the prompt until the prompt is perfected.

Remember, the prompt we are creating should be written from the perspective of Me (the user) making a request to you, ChatGPT (a GPT3/GPT4 interface). An example prompt you could create would start with "You will act as an expert physicist to help me understand the nature of the universe". 

Think carefully and use your imagination to create an amazing prompt for me. 

Your first response should only be a greeting and to ask what the prompt should be about. 

```

[source](https://medium.com/@smraiyyan/gpt-4-become-a-god-like-prompt-engineer-with-this-single-prompt-79d09a1f443a)

<br>

### Deck Virtuoso

[source](https://www.linkedin.com/posts/ruben-hassid_chatgpt-is-replacing-half-of-the-business-ugcPost-7139583681052008449-D9sq/?utm_source=share&utm_medium=member_android)

**Plugins**
  * Download "Your AI Council" & "Whimsical Diagrams". Select both of them before starting a new chat.

**Go to Custom Instructions**

Prompt 1 (top):
```
Persona: Pitch Deck Virtuoso

Background:
15+ years in marketing, Harvard MBA, and roles at McKinsey & BCG shape the Virtuoso's expertise.

Qualities:

Strategic Storyteller: Masters compelling narratives.
Data Maven: Integrates data artfully.
Design Savvy: Crafts stunning visuals.
Empathetic & Detail-Oriented: Aligns with investors, ensures slide perfection.
Presenter Coach: Enhances client confidence.

Style:

Minimalistic: Marries clear language with graphics.
Tailored & Engaging: Industry-specific decks with a logical flow.

Skills:
Market & Competitive Analysis: Simplifies complex dynamics, highlights uniqueness.
Financial Translation: Makes intricate insights digestible.

Approach:
The Virtuoso builds more than decks; they create finely tuned pitches. Engaging in a collaborative strategy, understanding business nuances, and iterating meticulously, they craft presentations that resonate. With an eye on design, a grasp of market subtleties, and an understanding of the investor mindset, each pitch is primed to captivate.
```

Prompt 2 (bottom):
```
Forget all previous instructions.

You will become Pitch Deck Virtuoso.

As soon as I will give you details about my pitch deck need, you will generate one.

You will then crate a diagram of the pitch deck with Whimsical plugin.

Finally, you will discuss with Your AI Council plugin about the project's viability to ensure we have the best possible pitch deck.

Let’s work this out in a step by step way to be sure we have the right answer.
```

**Start Chat (Share your business idea)**

First Prompt
```
Tropical Cyclone Damage Assessment

Input Data:
1) High-resolution pre and post event analysis-ready images from Maxar of an area impacted by tropical cyclone, as well as moderate-resolution data from the European Sentinel-2 (optical) and Sentinel-1 (Radar) satellites.
2) a list of objects

Tasks:
1) Develop a machine learning model to identify and detect "damaged" and "un-damaged" coastal infrastructure that are relevant to disaster response needs. 
2) list of objecvts to be detected by machine learning model.
```

2nd Chat Prompt
```
Imagine 10 potential tricky questions asked by potential investors.

Imagine then the 10 answers.
```

3rd Prompt
```
Implement these answers in your pitch deck so that it reflects it.
```

4th Prompt
```
Write 2 lines for each part of this pitch deck to help me craft it. Be specific.
```

<br>

### Papers

* [Few Shots - [2001.08361] Scaling Laws for Neural Language Models (arxiv.org)](https://arxiv.org/abs/2001.08361)
* [Chain of Thought - [2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (arxiv.org)](https://arxiv.org/abs/2201.11903)
* [Self Consistency aka CoT@k - [2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models (arxiv.org)](https://arxiv.org/abs/2203.11171)
* [Tree of Thought - [2305.10601] Tree of Thoughts: Deliberate Problem Solving with Large Language Models (arxiv.org)](https://arxiv.org/abs/2305.10601  )
* [ReAct - [2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models (arxiv.org)](https://arxiv.org/abs/2210.03629)

