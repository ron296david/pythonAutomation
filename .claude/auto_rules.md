# Automation Rules

Rules for automated workflows, scripts, and agent behavior in this project.

<!-- Add rules below, one per bullet. -->

- Never hide failures. Tests are deterministic: there is no "maybe", "almost", or partial pass. If something is missing or wrong, the test fails. Do not swallow errors, skip checks, loosen assertions, or add fallbacks or silent retries that mask a problem.
- Tests are independent. Each test prepares everything it needs and cleans up after itself. No test relies on another test's data, state, or run order.
- When an API is available, use it for setup (before) and cleanup (after). Use the UI only for the part the test is actually checking.
- Every building block verifies its own result. After performing its action, a block checks that the expected outcome actually happened. If the check fails, the test fails immediately with a clear error message that says which block failed, what was expected, and what was found.
- Never skip anything on your own: no tab, page, element, step, or check. Not even when it looks external, unreliable, or out of scope. Always stop and ask the user first, explain the options, and wait for a decision. Never skip!
- When running tests, run them once, in UI mode (a visible browser: `--headed`), so the user can watch. Do not repeat runs unless the user asks.
