# Supply-chain review

## Inspect

- Repository owner and exact source URL.
- Skill or plugin directory, manifest and metadata.
- Scripts, hooks, MCP servers and app definitions.
- Dependencies, install commands and post-install steps.
- Network and filesystem scope.
- Authentication and secrets.
- Binary, generated, minified or encoded files.
- Destructive commands and persistence mechanisms.
- License, version/tag/commit and maintenance signals.

## Risk language

Use `Lower observed risk` when scope is limited, content is readable, source is official/known, no unexpected scripts or secrets appear, and version pinning exists.

Use `Moderate observed risk` for maintained external code with explainable scripts/dependencies and bounded permissions.

Use `Higher observed risk` for obfuscation, binaries, post-install scripts, broad filesystem/network access, secret collection, destructive behavior, unknown ownership or unverifiable installation.

Never write “safe” or “trusted” as a guarantee. State what was and was not inspected.

## Installation authorization

Authorization must identify source, destination, scope and material permissions. A request to find options is not permission to install.
