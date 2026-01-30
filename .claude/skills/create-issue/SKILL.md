---
name: create-issue
description: Create GitHub Issue with complete specification (Background/AC/Non-goals/Constraints). Asks clarifying questions, outputs ISSUE_TITLE.txt and ISSUE_WITH_SPEC.md ready to post.
user-invocable: true
---

# Create Issue Skill

Creates a complete GitHub Issue with specification in one workflow.

## Purpose

Transforms vague requirements into a well-defined Issue with:
- Clear background and motivation
- Observable acceptance criteria
- Explicit non-goals
- Technical constraints

## Process

1. **Gather requirements** - Ask up to 4 clarifying questions:
   - Background/Why (business context)
   - Acceptance Criteria (observable outcomes)
   - Non-goals (what we won't do)
   - Constraints (technical/business limits)

2. **Generate Issue** - Create two files:
   - `ISSUE_TITLE.txt` - Short, actionable title
   - `ISSUE_WITH_SPEC.md` - Complete Issue body

## Output: ISSUE_WITH_SPEC.md

Use this exact structure:

```markdown
## Background / Why

[2-3 sentences: Business context, motivation, user need]

## Acceptance Criteria

- [ ] AC1: [Observable outcome with input/output example]
- [ ] AC2: [Observable outcome with Given/When/Then]
- [ ] AC3: [Observable outcome]

[3-5 criteria. Make them testable and observable.]

## Non-goals

- [Thing we explicitly won't do in this Issue]
- [Feature/refactor deferred to future]

[2-4 items. Clarifies scope boundaries.]

## Constraints

[Only if applicable]
- [Technical constraint: framework version, compatibility]
- [Business constraint: timeline, resources]

[1-3 items. Omit if none.]

## Tasks

- [ ] Review specification
- [ ] Run `/resolve-issue` to implement
- [ ] Create PR with verification results
```

## Rules

- **Ask questions when unclear** - Don't assume requirements
- **Make ACs observable** - "Function returns X" not "Function is good"
- **Be explicit about Non-goals** - Future enhancements go here
- **No code yet** - Focus on "what" not "how"
- **Keep it concise** - 3-5 ACs, 2-4 Non-goals

## Example Questions

**Q1: What is the background and motivation for this feature?**
[User answers business context]

**Q2: What are the observable success criteria? (e.g., input → output)**
[User provides examples]

**Q3: What should we explicitly NOT include in this Issue?**
[User clarifies scope boundaries]

**Q4: Are there any technical or business constraints?**
[User mentions framework versions, timelines, etc.]

## Example Output

```markdown
## Background / Why

API responses use camelCase, but our Python codebase uses snake_case. Manual conversion is error-prone and slows development.

## Acceptance Criteria

- [ ] AC1: `to_camel_case('hello_world')` returns `'helloWorld'`
- [ ] AC2: `to_camel_case('user_id')` returns `'userId'`
- [ ] AC3: Empty string returns empty string
- [ ] AC4: Function has type hints and docstring

## Non-goals

- Reverse conversion (camelCase → snake_case)
- Handling special characters or Unicode
- Configuration for custom naming schemes

## Constraints

- Must work with Python 3.9+
- No external dependencies

## Tasks

- [ ] Review specification
- [ ] Run `/resolve-issue` to implement
- [ ] Create PR with verification results
```

## Next Steps

After generating `ISSUE_WITH_SPEC.md`:

1. User reviews the specification
2. User posts it to GitHub as an Issue
3. User runs `/resolve-issue` to implement

## Notes

- This skill replaces the 2-step workflow (`/issue-draft` → `/spec`)
- For learning the process step-by-step, use the individual skills instead
- Can be used by the `resolve-issue` skill if no Issue exists yet
