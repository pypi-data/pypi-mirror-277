# Services authentification

For some backups, you probably require some authentication. As this framework is
intended to run automatically, it brings helpers to avoid credentials
exhibition (called vaults).

## Basic dumb authentication

Credentials may be provided in the YAML service description.

```yaml
service:
  type: type
  auth:
    user: user
    password: password
    token: token
```

Refer to the plugin to know which key is expected.

## Local vaults

Local vaults are local encrypted data files in directories with restricted
permissions.

Each file should be named after the service it deserves, and its encrypted
content should match a (user, password) tuple per line.

```
userA passwordA
userB passwordB
```

In such a situation, the password may be retrieved if a service has the
following YAML description:

```yaml
service:
  type: type
  auth:
    user: userA
```

### Encryption

So far two encryptions methods are available: base64 and fernet

### How to create a local vault

The local vault must be defined in the TOML configuration. As default:

``` toml
[vaults]
order = ["localb64", "localfernet"]

[vaults.localb64]
mode = "local"
path = "/var/cache/nosaastrust/.vault/localb64"
encryption = "b64"

[vaults.localfernet]
mode = "local"
path = "/var/cache/nosaastrust/.vault/localfernet"
encryption = "fernet"
# Default path to store fernet key
keypath = "/var/lib/nosaastrust/.fernet/vault.key"
```

The path must be created with restricted permissions:

``` bash
sudo install -d -m 0770 -g nosaastrust /path/to/local/vault
```

Then you may use the helper `nost-add-password` to add an encrypted entry in the
vault.

### `nost-vault` helper

Local vaults and password files may be created throught the `nost-vault` helper:

``` bash
nost-vault init <vaultname> | all
nost-vault add-password <vaultname> <service> <user>
```

With `nost-vault`, vaults will be created with permissions for the current user.

## Remote vaults

This aims to support the bitwarden API to retrieve passwords from a remote
vault.
