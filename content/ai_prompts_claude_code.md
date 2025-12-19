Title: AI Prompts - Claude Code
Date: 2025-11-09
Category: AI
Slug: ai_prompts_claude_code
Summary: Claude Code configuration, commands, and workflow prompts

### What is Claude.md?

Claude.md is your AI team member's persistent memory - essential context available in every prompt. Like onboarding a new developer, you provide Claude Code with institutional knowledge to work effectively.

### The CONTEXT Framework for Claude.md

| Letter | Principle |
|--------|-----------|
| C | Clear and Concise Instructions |
| O | Operational Processes |
| N | Naming and Standards |
| T | Testing and Quality Gates |
| E | Examples and References |
| X | Expectations and Boundaries |
| T | Tools and Dependencies |

### Core Principles

**Essential Information Only** - Global information that applies to every task. Don't overwhelm with project-specific details.

**Specificity Creates Better Targets** - "Write solid code" is vague; "Follow SOLID design principles for all object-oriented code" is actionable.

**Process Over Micromanagement** - Define workflows and checks, not implementation details.

### Claude.md Best Practices

**Do's:**
- Use clear, actionable language
- Provide specific tools and frameworks
- Define quality gates and testing requirements
- Include workflow processes
- Specify naming conventions

**Don'ts:**
- Include task-specific details that only apply sometimes
- Write 1000-page documentation dumps
- Use vague instructions like "write good code"
- Micromanage implementation details

### Claude.md Example

```text
# Project: TaskFlow Web Application

## Core Principles
IMPORTANT: All code MUST follow SOLID design principles.

## Development Workflow
1. Create and checkout feature branch: feature-[brief-description]
2. Write comprehensive tests for all new functionality
3. Compile code and run all tests before committing
4. Write detailed commit messages explaining changes
5. Commit all changes to the feature branch

## Architecture Overview
- Frontend: Next.js 14 with TypeScript and Tailwind CSS
- State Management: Zustand for client state, React Query for server state
- Backend: Node.js with Express and Prisma ORM
- Database: PostgreSQL
- Testing: Jest for unit tests, Playwright for E2E

## Quality Gates
- All code must compile without warnings
- Test coverage must remain above 80%
- All tests must pass before committing
- ESLint and Prettier must pass without errors
```

---

## Creating Claude Commands

Commands deliver targeted context for specific, repeatable tasks. They're specialized instruction sets stored in `.claude/commands/` directory.

### The TARGETED Framework

| Letter | Principle |
|--------|-----------|
| T | Task-Specific Instructions |
| A | Arguments and Placeholders |
| R | Reusable Process Steps |
| G | Guided Examples and References |
| E | Explicit Output Requirements |
| T | Template-Based Naming |
| E | Error Handling and Edge Cases |
| D | Documentation and Context |

### Command Location

- **Project-specific**: `.claude/commands/` (versioned with project)
- **Global commands**: `~/.claude/commands/` (available across all projects)

### Organization Strategies

- **By Function**: `plan-feature.md`, `impl-api.md`, `test-unit.md`
- **By Domain**: `auth-login.md`, `user-profile.md`, `payment-process.md`
- **By Role**: `dev-review.md`, `qa-automation.md`, `ops-deploy.md`

---

## Example Commands

### Code Review Command

File: `.claude/commands/code-review.md`

```text
# Code Review Command

Carefully perform a comprehensive code review of $ARGUMENTS.

## Review Standards
Examples of excellent code to match:
- src/components/UserProfile/UserProfile.tsx (React components)
- src/utils/dataValidation.ts (utility functions)
- src/hooks/useUserData.ts (custom hooks)

## Process
1. Read example files to understand patterns and conventions
2. Analyze $ARGUMENTS against these standards
3. Create detailed critique covering:
   - Code structure and organization
   - Adherence to established patterns
   - Performance considerations
   - Security implications
   - Test coverage gaps

## Output Requirements
- Save review as ai-code-reviews/{filename}.review.md
- Include specific line references for issues
- Rate quality: Excellent/Good/Needs Improvement/Poor
- Estimate refactoring effort: Low/Medium/High
```

### Parallel Work Command

File: `.claude/commands/parallel-work.md`

```text
I want to develop features in parallel using Git worktrees: $ARGUMENTS

Think about how to divide the work into separate features.

Please help me set up the worktree environment:
1. For each feature, create worktree at ../project-[feature-name]
   with branch feature/[feature-name]
2. Set up development environment in each worktree
3. List all worktrees to confirm creation
4. Explain what each worktree contains and how they're isolated

I want to work on all features simultaneously without conflicts.
```

Usage: `/parallel-work budget-tracking notifications user-settings`

### Integrate Parallel Work Command

File: `.claude/commands/integrate-parallel-work.md`

```text
I have features developed in parallel worktrees to integrate: $ARGUMENTS

Please help me integrate these features:
1. Create integration branch: integration/parallel-features
2. For each feature, merge branch feature/[feature-name]
3. Resolve any merge conflicts
4. Test that all features work together
5. Run all tests to ensure nothing is broken
6. Once successful, merge to main and clean up branches

I want to integrate safely before merging to main.
```

Usage: `/integrate-parallel-work budget-tracking notifications user-settings`

### API Test Command

File: `.claude/commands/api-test.md`

```text
# API Testing Command

Create comprehensive API tests for: $ARGUMENTS

## Testing Strategy

1. Happy Path Testing:
   - Valid request formats
   - Expected response structures
   - Proper HTTP status codes

2. Error Handling Testing:
   - Invalid request payloads
   - Authentication failures
   - Rate limiting scenarios

3. Edge Cases:
   - Boundary value testing
   - Large payload handling
   - Concurrent request handling

## Test Structure
Create tests in /tests/api/{endpoint-name}.test.ts
```
