# noSaasTrust

noSaasTrust is a multimodal backup framework

Because no provider should ever be trusted, people should manage their own
backups.

It uses a yaml description to launch various synchronizations and run a backend
(defaults to borg) to encrypt and store the data.

## License

BSD-2-Clause-Patent

## Requirements

- python-yaml
- python-cryptography
- (optional) rsync
- (optional) borg
- (optional) git

## Installation

```
python -m build
python -m installer dist/*.whl
```

## Usage

``` bash
nost sync <desc.yaml>
nost list
nost retrieve [ARCHIVE_ID]
nost delete [ARCHIVE_ID]
```

## Configuration

### Global configuration

The framework requires a Toml configuration file named ``nost.toml``.

The framework will look by order in :

1. in the environment ``NOSTDIR`` if defined
1. ``~/.config``
1. ``/etc``
1. ``/usr/share/nost``

A configuration template can be found in <resources/nost-user.toml>.

### Backup description

The Yaml backup description is used to describe the required backup
fetch. Options are desribed in <docs/backup_description.md>

## Prerequisites

The framework may require a group nosaastrust. Add your user to this group to
gain permissions to backups.

All path given in the TOML configuration must be created. As per default:

- `/usr/backup` for backup storage
- `/var/cache/nosaastrust` for cached date and vaults
- `/var/lib/nosaastrust` for sensitive permanent data such as SSH and Fernet keys

## Daemon mode

A systemd service is provided as an example to use in daemon mode. If the
backend is borg, a passphrase may be given using the environment variable
BORG_PASSPHRASE, or more securely, one shall use the systemd-creds:

```
# systemd-ask-password -n | systemd-creds encrypt --name=borgpw -p - -
```

and create the systemd config file `nost.service.d/borg.conf` with the result:

```
[Service]
SetCredentialEncrypted=borgpw: \
        k6iUCUh0RJCQyvL8k8q1UyAAAAABAAAADAAAABAAAABODbSDtNZ8+PtlN3IAAAAAgAAAA \
        AAAAAALACMA8AAAACAAAAAAngAgRKW32QRYMvWeTcwb4SbbvK/QDF4tihGlL8OHlLKa86 \
        AAEHwr8IDsdxBmuRIXWSBGoFu8la+lTclW0/GN3OZwbvfeymJhqSoa3+76kJ1aRumQVul \
        Wvc9KxykzPhVoqFN3adVujhUkfeUmD/IMwzscsOh0hsOd8d1r2v3K8WyVv9ebk0hS1mVC \
        UzSTCNMsuKrPF2wXUP2QK5+WIjL1AE4ACAALAAAAEgAgY9RHOefBR+mMgV/Frr+UzQX1S \
        IsLFItIbfB6Ep76It0AEAAgNyMB30ZJ2HiqikmhgZfvFRZqxNRhXluH/cxMiohBDKRj1E \
        c558FH6YyBX8Wuv5TNBfVIiwsUi0ht8HoSnvoi3QAAAADffR0SV5WlPlCnJtJrhVnIXp3 \
        IO36xjF4iBmXjBfjaWhpFJ6yyY0HzHF9O1J7eNgls5aJX6Skh
Environment=BORG_PASSCOMMAND="cat %d/borgpw"
```

## Testing

Run `tox` to run all tests. Non installed python versions shall be skipped.

Run `tox -e py3xx` to run tests for a specific python version

Run `tox -e lint` for code formating check

## Contribute

Before submitting, please run `flake8 src/nost`. One can also use pre-commit:
`pre-commit install`.

## Auto generated documentation

Install dependency `pip install sphinx`.

Run `sphinx-build noSaasTrust/docs path/to/doc`.
