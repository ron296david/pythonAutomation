# Design Rules

Rules for architecture, UI/UX, and design decisions in this project.

<!-- Add rules below, one per bullet. -->

- The project is built in layers. Layers 1-4 each call only the layer(s) directly below them; layer 5 is shared by all:
  1. **Test layer**: contains the tests. Tests call building blocks only. They never use selectors or Playwright directly.
  2. **Building blocks layer**: reusable business actions and flows used by tests. Building blocks get UI selectors from the repository layer and interact with the page only through the web access layer.
  3. **Repository layer**: holds UI selectors and similar static data. It contains no logic and no Playwright calls.
  4. **Web access layer**: wraps the actual Playwright actions (read, write, click, etc.). This is the only layer that calls Playwright.
  5. **Entities layer** (`entities` folder): all entities (objects such as `User`), both the entity definition and its data (e.g. a test user's details). Entities never live in another layer's folder. Any layer may use them.
