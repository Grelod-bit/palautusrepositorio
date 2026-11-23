# Copilot instructions

## Project commands

- Install the development dependency group with `uv sync`.
- Run the full test suite from the project root with `uv run pytest -q`.
- Run the existing test module with `uv run pytest -q src/tests/ostoskori_test.py`.
- Run one test with `uv run pytest -q src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa`.
- There is no configured lint or format command in `pyproject.toml`.

The project targets Python 3.14, as specified by `.python-version` and
`pyproject.toml`.

## Architecture

This is a small shopping-cart domain model implemented as flat modules under
`src/`:

- `Tuote` represents a product and owns its name and integer price.
- `Ostos` represents one product line in a cart. It starts with quantity one,
  calculates its line total, and prevents quantity from becoming negative.
- `Ostoskori` is the aggregate that owns cart lines and exposes cart-level
  operations: adding/removing products, clearing the cart, counting items,
  calculating the total, and returning purchases.
- `src/tests/ostoskori_test.py` contains the behavior tests. Tests use
  `unittest.TestCase` assertions but are run through pytest.

## Repository-specific conventions

- Keep the flat-module import style used by the source and tests, such as
  `from tuote import Tuote`; run commands from the project root so pytest's
  current import behavior remains consistent.
- Prices are represented as `int` values (euros), not floating-point amounts.
- Product identity and cart-line behavior should remain separate: product data
  belongs in `Tuote`, quantity and line totals in `Ostos`, and collection-level
  behavior in `Ostoskori`.
- Quantity changes are incremental through `Ostos.muuta_lukumaaraa`; preserve
  its invariant that quantity never falls below zero.
- Use the existing Finnish public names and method names when extending the
  model; they are the domain API exercised by the tests.
- Do not change `src/ostos.py` or `src/tuote.py`.
- Do not edit tests unless the user explicitly asks for test changes.
- Implement the absolute minimum code needed to make the tests pass; avoid
  unrelated behavior or refactoring.
