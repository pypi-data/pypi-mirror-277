# Conception

Because no provider should ever be trusted, people need to own backups.

Therefore, the goal is to have an application that automates several backups
listed in a YaML description file and place them somewhere after encryption.

In a second step, the application may list and retrieve backups.

```sh
$ nost backups.yml
```

The description of the backup may look like:

```yaml
backuplist: ["serviceA", "serviceB"]

services:
  serverA:
    type: ssh
    host: some.where
    fingerprint: ABCD
    credentials:
      user: me
      pass: secret
  serverB:
    type: rsync
    host: else.where
    credentials:
      sshid: blablabla
  serverC:
    type: rsync
    host: any.where
    credentials:
      file: name
```

## Configuration

The application will be configured along two axis:

1. the description file as above shared among users and robots that describes
   services to be backuped.
1. a local configuration file that gives some configuration specific to the
   user/robot.

As an example, details about periodicity, rotations, storage will be in the
local configuration.

## Credentials

We must provide utils to avoid unencrypted credentials in the description.

Below is the process to retrieve secrets (password, private ssh key, tokens...)

1. if it's defined in the description, use it
1. if not, the plugin should ask for an identifier into a list of vaults:
   1. look in the local vault (see below)
   1. look into a bitwarden vault (this is not in the scope yet)

As an example, if the description has `user: itsme` and no password, the plugin
should ask each vault for the identifier `itsme`.

The list of accepted vaults must be configured in the local configuration.

### Local vault

To keep things easy so far, the local vault can be a local storage
(`/var/lib/nosaastrust` by default). An identifier should match a file in that
storage. It should have strict permissions and encrypted/hashed data.

## Considerations

1. credentials (user/pass, ssh keys, tokens...) are sensitive.
1. we might require support for OAuth
1. the app must be maintainable and should not rely on a specific package
1. the code must be accessible to the most, and so the python language is chosen
1. it may be nice to raise a warning when backuped data is old
1. use a logger
1. we will need a daemon with a timer
1. we need tests

## Commandline

The command line shall accept following commands:

- `nost sync desc.yaml`: fetch and store all services given in the yaml description
- `nost list`: list backups (with an unique ID) managed by the backend
- `nost retrieve all|ID`: retrieve backup ID
