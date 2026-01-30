---
name: spec
description: Convert GitHub Issue to spec.md with Why/AC/Non-goals/Constraints. Use after Issue is created or /issue-draft is done.
user-invocable: true
---

# Spec Skill

Converts a GitHub Issue (or ISSUE_DRAFT.md) into a structured spec.md.

## Process

1. **Read input** - ISSUE_DRAFT.md if exists, or user-provided Issue text
2. **Extract structure** - parse Problem/Why, AC, Non-goals, Constraints
3. **Clarify ambiguities** - if AC is vague, add improvement notes
4. **Generate spec.md**

## Output File

### spec.md

```markdown
# [Feature/Fix Name]

## Summary
[1-2 line overview of what this is]

## Why
[Background and motivation - keep it short]

## Acceptance Criteria
- [ ] [Copied from Issue, or improved if vague]
- [ ] [Observable outcomes preferred]
- [ ] [3-5 specific criteria]

## Non-goals
- [What we won't do - 2-4 items]

## Constraints
- [Technical/business constraints - 1-3 items]

## Open Questions
- [Any remaining ambiguities to resolve]
```

## Rules

- **Keep it short** - don't add unnecessary text
- **Improve vague AC** - if AC says "can do X", suggest observable alternative
- **Flag ambiguities** - add to Open Questions if something is unclear
- **No implementation details** - this is specification, not design

## Example

Input (ISSUE_DRAFT.md):
```
## Problem / Why
Users need to convert snake_case to camelCase for API payloads.

## Acceptance Criteria
- [ ] Function converts "hello_world" to "helloWorld"
- [ ] Handles empty strings
- [ ] Make test passes
```

Output (spec.md):
```markdown
# Add snake_case to camelCase conversion

## Summary
Utility function to convert snake_case strings to camelCase.

## Why
API payloads require camelCase formatting, but our internal code uses snake_case.

## Acceptance Criteria
- [ ] to_camel_case("hello_world") returns "helloWorld"
- [ ] to_camel_case("") returns ""
- [ ] All tests pass with make test

## Non-goals
- kebab-case conversion
- PascalCase conversion

## Constraints
- Must work with Python 3.9+
```
