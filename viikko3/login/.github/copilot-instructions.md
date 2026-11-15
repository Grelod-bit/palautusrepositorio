# Copilot instructions

## Project shape

This directory is an independent Flask exercise. Use its own
`pyproject.toml` and `uv.lock`; run commands from `viikko3/login`, not from
the repository root. The project targets Python 3.14 and uses `uv` for
environment and dependency management.

The application starts through `src/index.py`. Flask routes live in
`src/app.py`, render the Jinja templates in `src/templates`, and use the
service and repository modules under `src/services` and `src/repositories`.
Browser acceptance tests are Robot Framework suites under `src/tests`.

## Architecture

- `src/app.py` defines the HTTP routes. Registration and login handlers call
  the singleton `user_service`, redirect on success, and flash error messages
  before redirecting back to the form on failure.
- `UserService.validate` owns username and password registration validation,
  while `UserService.check_credentials` handles login authentication. The
  service delegates process-local persistence to the singleton
  `user_repository`; there is no database or durable user store.
- `src/index.py` starts the Flask app on `http://localhost:5001`.
- Robot tests drive the running app with Browser/Chromium. `AppLibrary.py`
  uses HTTP requests to reset the in-memory repository and seed users between
  scenarios.

## Install, run, and test

This is a `uv` project: run project commands in the form `uv run ...` from
`viikko3/login`:

```bash
uv sync
uv run python src/index.py
```

Keep the application running in another terminal while executing Robot tests:

```bash
uv run robot src/tests
uv run robot src/tests/login.robot
uv run robot --test "Login With Correct Credentials" src/tests/login.robot
```

The Robot suites expect port 5001 and Chromium through Robot Framework
Browser. The `${HEADLESS}` variable in `src/tests/resource.robot` defaults to
`false`; change it to `true` for a headless run. The `POST /tests/reset`
endpoint clears the in-memory users before scenarios.

## Conventions

- Keep changes inside this project unless the exercise explicitly requires a
  repository-wide change. Keep `uv.lock` aligned with dependency changes in
  `pyproject.toml`.
- Preserve the service/repository split and process-local state model.
- Preserve the exact user-facing error strings because Robot tests assert
  visible messages.
- Use the existing HTTP reset endpoint and `AppLibrary.py` setup flow to keep
  acceptance tests isolated.
