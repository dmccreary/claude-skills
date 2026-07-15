# README Validator Closing-Fence Investigation

## Status

RESOLVED

## Incident

The `book-publisher` README validator reports valid closing Markdown fences as
code blocks without language specifications. The representative X Marketing
README contains four fenced examples, and every opening fence names a language,
but the validator reports four unlabeled blocks and deducts points from the
publication score.

## Impact

- Publication reports contain a false formatting failure.
- A valid README cannot reach the score its content actually earns.
- Authors are encouraged to "fix" closing fences that are already correct.
- The book-publisher parent task cannot use the validator as trustworthy
  completion evidence until this reusable source defect is remediated.

## Reproduction

Current implementation:

```python
code_blocks = re.findall(r'```(\w*)\n', content)
unnamed_blocks = sum(1 for lang in code_blocks if not lang)
```

Minimal valid Markdown:

````markdown
```bash
echo hello
```
````

The regular expression returns both `bash` and an empty string. The empty
string is the closing fence, but the validator treats it as a second opening
fence without a language.

## Evidence

- Source: `skills/book-publisher/scripts/validate-readme.py`
- Affected exercise:
  `/home/agent-tomas/worktrees/x-marketing-book-publisher/README.md`
- Observed report: `93/100`, including
  `Found 4 code block(s) without language specification`
- Manual inspection: all four opening fences are labeled; the four matches are
  the closing fences.

## Initial hypotheses

| Hypothesis | Initial probability | Evidence |
|---|---:|---|
| The regex does not distinguish opening from closing fences. | 90% | Each closing ````` line satisfies the same regex with an empty capture. |
| The README contains genuinely unlabeled opening fences. | 5% | Direct inspection found none. |
| Mixed line endings or trailing spaces corrupt language capture. | 3% | The reported count exactly equals the number of valid closing fences. |
| The cause is not represented above. | 2% | Reserved for an unlisted parser or fixture interaction. |

## Root cause

The validator treats fenced-code syntax as independent regex matches rather
than a stateful opening/closing construct. A closing fence has no info string by
design, so every valid closing fence is classified as an unlabeled opening.

This is a semantic-validation anti-pattern: a local pattern match is being used
for syntax whose meaning depends on parser state.

## Experiments

### Regression tests against the original implementation

Five focused tests were added in
`skills/book-publisher/tests/test_validate_readme.py`. Before the source fix,
four failed:

- one labeled backtick block was reported as one unlabeled block;
- three labeled examples were reported as four unlabeled blocks because a
  four-backtick wrapper added another closing fence;
- an unlabeled backtick block was reported twice;
- an unlabeled tilde block was not reported at all.

The unclosed-unlabeled case passed because the old regex happened to count its
single opening fence. This negative control was important: it proved that the
replacement must preserve valid findings rather than merely suppressing the
false positives.

### Stateful scanner

`count_unlabeled_fenced_code_blocks()` now tracks whether a fence is open, the
opening marker character, and its length. A bare matching marker of at least
the opening length closes the block. Only a fence encountered outside a block
can be classified as an unlabeled opening. The scanner handles backtick and
tilde fences and ignores invalid backtick openers whose info string contains a
backtick.

### Verification

- Book-publisher fence regression suite: 5/5 passed.
- Adjacent book-installer regression suite: 4/4 passed.
- Existing book-metrics layout suite: 6/6 passed.
- Python compilation and `git diff --check`: passed.
- Representative X Marketing README: `100/100`, with 4/4 required sections,
  5/5 recommended sections, 28 valid links, 4 badges, zero formatting issues,
  and zero header issues.

`ruff` and `black` were not installed in this environment, so no formatter or
linter result is claimed.

## Remediation plan

1. Add regression tests that prove labeled openings plus their closing fences
   produce no issue.
2. Prove a genuinely unlabeled opening still produces exactly one issue.
3. Cover longer backtick fences and tilde fences so the scanner follows normal
   Markdown fenced-code forms rather than only one literal token.
4. Replace the independent regex count with a stateful fence scanner.
5. Run the validator against the representative README and the source tests.
6. Record the reusable learning with CE Compound.
7. Merge the source fix, verify it is on `origin/main`, and restore the blocked
   book-publisher task.

## Closure criteria

- Regression tests fail on the old implementation and pass on the fix.
- Valid labeled blocks produce no unlabeled-block finding.
- A genuinely unlabeled opening produces one finding, not two.
- The representative README reaches an honest `100/100` after its independent
  README content fixes.
- Source validation passes, CE Compound is recorded, and the fix is merged.

## Closure status

All closure criteria are satisfied. The source fix and CE Compound learning
merged in PR #3, whose merged state was verified against GitHub before closure.
The representative README scored `100/100`, every source and adjacent test
passed, and the blocked book-publisher task was independently verified in the
Trello `Next` list before this investigation was closed.
