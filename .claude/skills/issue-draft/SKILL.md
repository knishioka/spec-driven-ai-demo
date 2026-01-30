---
name: issue-draft
description: Create GitHub Issue draft with AC/Non-goals/Tasks. Use when starting from vague requirements - asks clarifying questions if needed. Also used internally by create-issue skill.
user-invocable: true
---

# Issue Draft Skill

Creates a well-structured GitHub Issue draft from vague user requirements.

**Note**: This skill is also used as part of the `/create-issue` workflow for learning purposes.

## Process

1. **Gather context** from user input (1-3 lines of what they want)
2. **Identify gaps** - if information is insufficient, ask up to 4 clarifying questions using AskUserQuestion:
   - Who has what problem? (Background/Why)
   - What defines success? (Acceptance Criteria)
   - What are we NOT doing? (Non-goals)
   - Any constraints or impacts? (Constraints)
3. **Generate draft** with all sections filled

## Output Files

### ISSUE_TITLE.txt
A short, actionable title (1 line).

Example:
```
Add snake_case to camelCase conversion function
```

### ISSUE_DRAFT.md
Complete GitHub Issue body in this format:

```markdown
## Problem / Why
[2-4 lines explaining the background and motivation]

## Acceptance Criteria
- [ ] [Observable outcome with example if possible]
- [ ] [Given/When/Then format preferred]
- [ ] [3-5 specific, testable criteria]

## Non-goals
- [What we explicitly won't do - 2-4 items]

## Constraints
- [Technical or business constraints - 1-3 items if applicable]

## Tasks
- [ ] Run /spec to create spec.md
- [ ] Run /plan to create plan.md
- [ ] Implement changes
- [ ] Run make test
- [ ] Create PR
```

## Rules

- **Acceptance Criteria MUST be observable** - avoid "can do X", prefer "when Y, then Z"
- **Do NOT write code** - focus only on creating the Issue
- **Keep it concise** - don't inflate bullet points unnecessarily
- **Ask questions** if requirements are vague - better to clarify upfront

## Example Usage

User: "Add a function to convert text to camelCase"

Skill asks:
- Who needs this? (Background)
- What inputs/outputs? (AC)
- What won't we support? (Non-goals)
- Any constraints? (Performance, compatibility)

Then generates ISSUE_TITLE.txt and ISSUE_DRAFT.md.
