# Public configuration schemas

These schemas are public contracts between Recipe authors and Hakoniwa
Conductor implementations.

- `eu-input-v1.schema.json` describes the `eu-input.json` consumed by a
  Conductor configuration generator.
- A Recipe may require a private generator for regeneration while publishing
  its schema-valid input and generated runtime configuration.
- Published generated artifacts should record the input SHA-256 and generator
  product revision. The generator source does not need to be published.

Version 1 is selected by the schema file name; no version property is added to
existing `eu-input.json` documents.
