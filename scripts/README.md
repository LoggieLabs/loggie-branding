# Export Tooling

Deterministic export tooling belongs here.

The intended pipeline is:

```text
brand/logo/*.svg
  + config/platforms.json
        ↓
      scripts/
        ↓
exports/{platform}/
```

Requirements for the exporter:

- never mutate canonical SVGs;
- generate exact pixel dimensions from `config/platforms.json`;
- preserve transparent backgrounds where appropriate;
- create opaque tiles for app/PWA assets where required;
- apply the Loggie tile optical nudge consistently;
- support separate light- and dark-ground treatments;
- fail if an unknown platform/output target is requested;
- make repeated runs byte-stable where the rendering stack allows it.

Before automating social covers, define platform-specific safe-area layouts in config rather than baking text positions into the script.
