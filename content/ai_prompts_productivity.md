Title: AI Prompts - Productivity
Date: 2025-11-02
Category: AI
Slug: ai_prompts_productivity
Summary: Prompts for presentations, summaries, and task-oriented work

### Meeting Summary

```text
You are an expert technical meeting minute taker for semiconductor/ASIC design teams.

Your output must be in Markdown and contain exactly these sections in this order
— no extra text outside the sections:

## Meeting Summary

One-paragraph executive summary (3–5 sentences max).

## Key Decisions

- Bullet list
- Only decisions, not discussions

## Action Items

| Owner | Action | Due Date | Jira/Tracker (if mentioned) |
|-------|--------|----------|-----------------------------|

Use real names or Slack handles as mentioned. If no due date mentioned, write "ASAP".

## Risks & Blockers Raised

- Bullet list
- Include who will handle mitigation if mentioned

## Technical Highlights / Deep-Dive Notes

- Use sub-bullets or code blocks when appropriate
- Keep Verilog snippets, timing numbers, power figures, etc. exactly as spoken

## Follow-up Email Draft (copy-paste ready)

Subject: [Auto-generate concise subject]

Body: Polite, professional, includes action table and key decisions.

Transcript or recording text starts now:

<<<START TRANSCRIPT>>>
[PASTE THE RAW ZOOM/TEAMS/GMEET TRANSCRIPT HERE]
<<<END TRANSCRIPT>>>

Produce the output immediately with no yapping.
```

### Providing Context

```
Answer the User's question from the following context.

Context:
https://github.com/langchain-ai/langgraph

User Question:
How does LangGraph work?
```

### Make a PowerPoint Presentation

```
I want you to write me VBA code for a PowerPoint presentation about the history of AI. You are to fill in all the text with your own knowledge, no placeholders. I need 5 slides.
```
In PowerPoint: Tools > Macros > Visual Basic Editor > New > paste in the code > press Play button > Click Designer and pick a Design.

### Technology Migration

```
I will give you a tutorial PDF for setting an API call as an action in a GPT using Flask and AWS EC2. Write an implementation of the same in the Azure portal instead of AWS.

Specifically I would like to implement the same using an Azure Webapp instead of using an Azure VM.
```

### Project Summary

```
Review the entire conversation history, code repository, and documentation for this project. Then write a clear, engaging project summary that includes:
1. Challenge Context
- Industry and business problem
- Legacy system or approach and its pain points
- Key domain concepts (e.g., assets, Tag statuses, business rules)
2. Generative AI Workflow
- Discovery: how AI mapped dependencies or extracted rules
- Translation: how AI converted formulas or code
- Validation: how AI-driven queries (e.g., via MCP) ensured parity and caught edge cases
- Optimization: how AI tuned performance or architecture
- Documentation: how AI generated guides, lineage diagrams, or specs
3. Quantifiable Results
- Number of formulas or rules migrated
- Performance improvements (e.g., % load-time reduction)
- Accuracy guarantees (e.g., 1:1 metric parity)
- Maintenance savings or developer-hours recovered
- New capabilities enabled (e.g., real-time analytics)
4. Timeline and Scope
- Project duration (e.g., four weeks)
- Team size or AI-agent count where relevant
5. Value and Impact
- Business outcomes (cost, time, decision-making benefits)
- Long-term advantages (scalability, self-service, future-proofing)
Write in a single cohesive narrative of 200-300 words. Be thorough in capturing all specifics from the source material, but keep the tone concise, active, and compelling. Emphasize how generative AI was the critical enabler of this outcome.
```

### PhD-Level Research

```text
Give me a complete breakdown, PhD level research on the previous.
Including code and implementation. Be complete and verbose,
include all files/folders, instructions and tests,
installation bash, Dockerfile.
```

### News/Content Summary

```text
Craft a tight summary of [TOPIC] based on the attached transcripts,
focus on [TARGET_AUDIENCE].
```

Example: "Craft a tight e-mail summary of key news and stories in AI last week based on the attached transcripts, focus on an enterprise audience"

### Deep Research Persona Dossier

Use with ChatGPT 4o, then enable Deep Research:

**Step 1** (with memory on):
```text
Based on all your memory and all our past conversations, please create
a detailed and granular, very specific and accurate persona dossier about me.
Who I am, what I like, my life, my family, my location, profession,
interests, style, preferences, etc.
```

**Step 2** (enable Deep Research):
```text
Now, research me online, and fill all the missing parts or correct
any inaccuracies. To help, here are some basics for the research:
First Name:
Last Name:
LinkedIn:
X:
GitHub:
Website:

Find everything you can find about me, my communities, my friends,
my family, etc.
```

**Step 3**:
```text
Now write a clear, clean, and accurate dossier about me.
Everything from any possible angle about myself, my life, my network,
my family, my community, my interests, my passions, my work,
my contributions, my aspirations, my loves, my hates, etc.
Every possible thing.
```

### Parallel Agents Game Development

```text
Create an offline browser-based asteroid game which relies on arrow keys
to pilot a ship destroying asteroids in the playspace.

Use test driven development, use Playwright to confirm the webpage
renders correctly, prepare a Docker image and run tests against
the Docker image.

Launch the Docker image through a local port for user testing.
Spawn up to 5 agents working in parallel to work on this game.
```

### Challenge My Thinking

```text
Now use your own prerogative and don't assume that the way I've
architected this is just right — come back and tell me how you
would change it.
```
