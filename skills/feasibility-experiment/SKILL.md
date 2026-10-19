---
name: feasibility-experiment
description: Run minimal, isolated experiments to determine whether uncertain technical behavior is actually feasible. Use when the user asks for an empirical feasibility check, proof-of-concept probe, or spike and wants direct observed evidence rather than production-quality code. Do not use for normal feature implementation, refactoring, or production hardening.
---

# Feasibility Experiment

Answer one sharply stated feasibility question with the smallest direct experiment that can distinguish success from failure.

## Experiment workspace

Create a fresh directory under `research/` in the current working directory for every experiment. Choose a short descriptive kebab-case name, such as `research/aspen-save-as-probe/`. Never reuse or overwrite an earlier experiment; add a short suffix if the name already exists.

Keep new code, dependency files, generated evidence, and the experiment record inside that directory. Read existing project files when useful, but do not turn the probe into a project feature or modify unrelated source and shared dependency files.

## Design the smallest discriminating probe

- State the question and an observable success criterion before writing code.
- Exercise the real uncertain boundary whenever possible; a mock does not establish that the actual API, application, file format, or integration works.
- Prefer one direct script with hard-coded test values. Inline logic and small amounts of duplication are acceptable.
- Skip reusable abstractions, package layouts, configuration layers, command-line interfaces, broad test suites, refactors, production logging, defensive plumbing, and extensibility unless one is necessary to answer the question.
- Add only the checks needed to interpret the result unambiguously. If a failure could merely be a setup mistake, use the smallest control or follow-up probe that separates setup failure from unsupported behavior.
- Stop when the success criterion has been observed or the remaining blocker is clear. Do not continue into production implementation.

## Isolate added dependencies

Run package-manager commands from the new experiment directory and keep their manifests, lockfiles, and installed packages there.

For Python, default to:

```text
uv init --bare --no-workspace
uv add <needed-packages>
uv run python probe.py
```

For JavaScript or TypeScript, default to:

```text
npm init -y
npm install <needed-packages>
node probe.mjs
```

Use `npm exec` for locally installed command-line packages. For another language, use its local project environment and native package manager. Do not use global `pip`, global `npm` installs, a shared virtual environment, or the parent project's dependency manifest. Using an already installed runtime or the application being probed is fine; the isolation rule applies to experiment code and newly added dependencies.

If the preferred package manager is unavailable, use another available option only when it preserves local isolation. Do not install a global tool merely to run the probe without the user's approval.

## Preserve evidence

Keep a concise `README.md` in the experiment directory, written in the user's language, with this structure:

```markdown
# [Experiment title]

## Question
[One falsifiable feasibility question]

## Success criterion
[The exact observable result that counts as success]

## Environment
[Only relevant application, runtime, package, OS, or API versions]

## Commands
[Exact commands that reproduce the run]

## Raw evidence
[Verbatim short output, or paths to unedited logs, generated files, and screenshots]

## Findings
[What each observed result establishes]

## Conclusion
[Feasible under tested conditions / not demonstrated / inconclusive, with scope]
```

Run the probe rather than stopping after writing it. Save material stdout and stderr without rewriting them, for example in `result.log`; if the evidence is a generated file or UI state, preserve the file or a screenshot when possible. Keep failed attempts only when they explain the conclusion.

A successful observation establishes feasibility only under the recorded conditions. A failed attempt does not establish universal impossibility. Use `not demonstrated` when the tested approach failed, `inconclusive` when execution was blocked, and `not feasible within <specific constraint>` only when the evidence directly rules out that bounded case.

## Report back

Lead with the feasibility conclusion in plain language. Link the experiment directory and the strongest evidence, state the tested conditions and remaining limits, and avoid proposing a production rewrite unless the user asks for one.
