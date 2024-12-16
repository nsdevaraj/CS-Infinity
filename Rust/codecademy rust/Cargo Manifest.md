


Cargo uses a **manifest file** (`Cargo.toml`) to manage dependencies, compilation options, and package metadata. It's essential for dependency management and publishing to [crates.io](https://crates.io/).

---

## Basic Structure

When you create a new project using `cargo new`, the default `Cargo.toml` looks like this:
(https://toml.io/en/)


```toml
[package]
name = "mybinary"
version = "0.1.0"
edition = "2021"

[dependencies]
# External dependencies go here
```

---

## Metadata Fields

The `[package]` section contains important details about your crate:

```toml
[package]
name = "mybinary"          # Crate name
version = "0.1.0"        # Current version
edition = "2021"         # Rust Edition version

description = ""         # Crate description for crates.io
keywords = []            # Search keywords
documentation = ""       # URL to documentation
homepage = ""            # Homepage URL
repository = ""          # Source repository URL
authors = [""]           # Author(s) of the crate
license = ""             # Licensing information
rust-version = ""        # Minimum supported Rust version
```

---

## Dependencies

Dependencies are defined under `[dependencies]`. Cargo fetches these from crates.io by default.

### Semantic Versioning

```toml
[dependencies]
serde = "1.0.2"          # Specific version
serde_derive = "1.0"   # Compatible with 1.0.X
heck = "*"             # Latest version
```

more : https://doc.rust-lang.org/cargo/reference/resolver.html

### Git Repository Dependency

```toml
serde = { git = "https://github.com/serde-rs/serde" }
# A specific branch
serde = { git = "https://github.com/serde-rs/serde", branch = "next" }
# A specific commit hash
serde = { git = "https://github.com/serde-rs/serde", rev = "7e19ae8c9486a3bbbe51f1befb05edee94c454f9" }
```

### Local Path Dependency

```toml
my_library = { path = "../my_library" }
```

---

## Features

Enable/disable features in external crates using the `features` field:

```toml
uuid = { version = "0.8", features = ["serde", "v4"] }
wee_alloc = { version = "0.4.5", default_features = false }
```

---

## Advanced Configuration

You can extend the manifest file with:

- `[dev-dependencies]`: Dependencies only for development.
- `[features]`: Define your crate's features.
- `[profile]`: Custom compilation settings.
- `[workspace]`: Manage multiple crates within a single workspace.

For more, see the [Cargo Manifest Reference](https://doc.rust-lang.org/cargo/reference/manifest.html).



