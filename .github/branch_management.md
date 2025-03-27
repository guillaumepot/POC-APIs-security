```
We follow a clear branching model for development:

- **main**: The main branch containing stable releases.
- **build**: For building releases from development branches.
- **debug**: For debugging, branched from build.
- **dev**: Where new features are developed.

Branch naming convention:

- `dev-<version>-<stack>` for feature branches.
- `debug-<version>-<issue_number>` for debug branches.

Example:  
If version `1.1.0` is the latest release, then the build branch would be `build-1.1.0` and feature branches might include `dev-1.1.0-API`, `dev-1.1.0-AIRFLOW`, etc.

Bug fixes create a `debug-1.1.z-<issue_number>` branch, leading to a new build and eventually an update on `main`.

_Note_: Bug fixes increment the `z` in the versioning (x.y.z).

### Versions

Our versioning follows a `x.y.z` pattern:

- **x**: Major changes or UI overhauls.
- **y**: New significant features (e.g., new API routes).
- **z**: Bug fixes or minor updates.

Examples:

- `1.0.0` - Initial release
- `1.1.0` - Feature update.
- `1.1.1` - Minor update

```