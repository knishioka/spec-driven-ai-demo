---
name: ship
description: Implement from plan.md, run tests, generate PR_DRAFT.md with actual verification results. Use when ready to code.
user-invocable: true
---

# Ship Skill

Implements the plan, runs tests, and generates a PR draft with actual results.

## Prerequisites

Before running this skill, ensure:
- Dependencies are installed: `make install`
- Baseline tests pass: `make test`

If not already done, the skill will check and prompt for installation.

## Process

1. **Read plan.md**
2. **Implement changes** - minimal diff following the plan
3. **Add/update tests** as needed
4. **Run `make test`** - fix until all tests pass
5. **Execute verification** - run all commands from plan.md
6. **Generate PR_DRAFT.md** - include actual results

## Output File

### PR_DRAFT.md

```markdown
## Summary
[1-2 line description of what this PR does]

## Why
[Background/motivation from spec - 2-3 lines]

## Changes
- [Concrete change 1]
- [Concrete change 2]
- [Max 5 items]

## Verification

### Automated Tests
- [x] `make test` - ✅ 5 passed in 0.01s

### Manual Testing
[If applicable, with actual commands run and results]
- [x] `python -c "from demoapp.text_utils import to_camel_case; print(to_camel_case('hello_world'))"` - ✅ Returns "helloWorld"

## Risk & Rollback
**Risk**: [From plan.md - 1-2 lines]
**Rollback**: [From plan.md - 1-2 lines]

## Related Issue
Fixes # [leave blank for user to fill]

---
Generated with /ship
```

## Rules

- **ONLY check items actually done** - no fake ✅ marks
- **Include actual results** - not just "make test passed", show timing and counts
- **Minimal changes only** - no refactoring, no unrelated formatting
- **Test must pass** - don't generate PR_DRAFT.md until `make test` succeeds
- **PR creation optional** - generating PR_DRAFT.md is sufficient, actual `gh pr create` not required

## Example Output

```markdown
## Summary
Add to_camel_case() function to convert snake_case strings to camelCase.

## Why
API payloads require camelCase formatting, but internal code uses snake_case. This utility function enables easy conversion.

## Changes
- Added to_camel_case() in src/demoapp/text_utils.py
- Added 4 test cases in tests/test_text_utils.py
- Updated module docstring

## Verification

### Automated Tests
- [x] `make test` - ✅ 7 passed in 0.01s (4 new tests added)

### Manual Testing
- [x] `python -c "from demoapp.text_utils import to_camel_case; print(to_camel_case('hello_world'))"` - ✅ Returns "helloWorld"
- [x] `python -c "from demoapp.text_utils import to_camel_case; print(to_camel_case(''))"` - ✅ Returns ""

## Risk & Rollback
**Risk**: New function might have edge cases with special characters or Unicode.
**Rollback**: Remove to_camel_case() function and its tests - no impact on existing functionality.

## Related Issue
Fixes #

---
Generated with /ship
```

## Notes

- The skill implements code changes, so it may take longer than other skills
- If tests fail, the skill should fix issues and retry
- If stuck, ask user for guidance rather than generating incomplete PR_DRAFT.md
