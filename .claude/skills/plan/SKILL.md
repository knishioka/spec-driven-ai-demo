---
name: plan
description: Create plan.md from spec.md defining PR scope (will/won't do, files, verification). Use before implementation.
user-invocable: true
---

# Plan Skill

Creates an implementation plan from spec.md, defining the exact scope of 1 PR.

## Process

1. **Read spec.md**
2. **Define PR scope** - what will/won't be in this PR
3. **Identify files** - which files likely need changes
4. **Define verification** - how to prove it works
5. **Generate plan.md**

## Output File

### plan.md

```markdown
# Implementation Plan: [Feature/Fix Name]

## This PR will
- [Action 1 - be specific]
- [Action 2]
- [Max 5 items]

## This PR will NOT
- [Explicitly out of scope - helps prevent scope creep]
- [Max 4 items]

## Files likely to change
- `src/demoapp/text_utils.py` - add new function
- `tests/test_text_utils.py` - add test cases
- [Max 6 files]

## Verification
- **Required**: `make test` - all tests pass
- [Optional: 1 additional verification if needed]

## Risk & Rollback
**Risk**: [1-2 line description]
**Rollback**: [1-2 line plan]

## PR Summary
[Short summary suitable for PR description - 2-3 lines]
```

## Rules

- **Keep PR small** - if scope is too large, suggest splitting into multiple PRs
- **Be explicit about non-goals** - prevents scope creep during implementation
- **Verification must be runnable** - `make test` is required, others must be concrete commands
- **No vague statements** - "improve code quality" is not a valid item

## Example

Input (spec.md):
```markdown
# Add snake_case to camelCase conversion

## Acceptance Criteria
- [ ] to_camel_case("hello_world") returns "helloWorld"
- [ ] to_camel_case("") returns ""
- [ ] All tests pass with make test
```

Output (plan.md):
```markdown
# Implementation Plan: Add to_camel_case function

## This PR will
- Add to_camel_case() function in text_utils.py
- Add test cases for basic conversion and edge cases
- Update existing tests if needed

## This PR will NOT
- Add kebab-case or PascalCase conversion
- Refactor existing to_snake_case function
- Add documentation beyond docstrings

## Files likely to change
- `src/demoapp/text_utils.py` - new function
- `tests/test_text_utils.py` - new tests

## Verification
- **Required**: `make test` - all tests pass in <1s

## Risk & Rollback
**Risk**: New function might have edge cases with special characters.
**Rollback**: Remove new function and tests - no impact on existing code.

## PR Summary
Adds to_camel_case() utility function to convert snake_case strings to camelCase format, needed for API payload formatting.
```
