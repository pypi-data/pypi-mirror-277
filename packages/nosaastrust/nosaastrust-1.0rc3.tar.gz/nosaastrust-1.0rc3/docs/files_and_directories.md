# Files and directories

This is a document to list all files and directories required to run the default
configuration.

This aims to spot incoherences and vulnaribilities

## User and group

On a secure server, the backup process should be ran by a specific `nosaastrust`
user. Other users may be added to the associated group to retrieve backups.

On personal machines, users should also be added to the `nosaastrust` group so
the download cache and the backup keys remain private.

In the following, permission modes will be given considering user and group
`nosaastrust`.

## List of files and directories

| Path                     | Mode | Description        | Security concern     |
|--------------------------|------|--------------------|----------------------|
| `/lib/systemd/system`    | 0755 | system services    | Hashed borg pw       |
| `/lib/systemd/user`      | 0755 | user services      |                      |
| `/etc/nost.toml`         | 0750 | configuration file |                      |
| `/etc/nost.d/`           | 0750 | descriptions files |                      |
| `/var/cache/nosaastrust` | 0770 | download cache     | Plain sensitive data |
| `/var/lib/nosaastrust`   | 0750 | encrypted backups  |                      |
| `/etc/nost.d`            | 0750 | encryption key     | Data encryption key  |
| `/srv/nost-vaults`       | 0750 | password vaults    | Access to passwords  |
| `/var/lib/nosaastrust`   | 0750 | vaults enc key     | Vault encryption key |
| `/var/lib/nosaastrust/`  | 0700 | gpg key            | Vault encryption key |
| `/var/lib/nosaastrust/`  | 0700 | ssh keys           | Access keys          |

## Details

### Configuration

Read permission may be permissive for configuration but write permission must be
restricted as changing the configuration may corrupt the backups.

### Download cache

Downloads are plain data but they are made to a temporary directory with rwx
permission restricted to the user, it's ok for any user of the `nosaastrust`
group to make use of it.

### Backups

Backups are stored in `/srv`. Read permission is given to `nosaastrust` group
but write shall be reserved to `nosaastrust` user to preserve the integrity in
case a user of the group is corrupted.

### Backup encryption key

The backup encryption key must be accessible for the `nosaastrust` group for
data retrieving. Write permission must be restricted to the `nosaastrust` user
to protect the key from corruption.

### Local vaults

Local vaults may store credentials for the services to backup. Read permission
is grant to the `nosaastrust` group so any user of this group can run a backup.

### Local vaults keys

Some vaults use a unique envryption key which must be known from other users of
the vault and may be stored in a group shared directory. That is different for
gpg encryption (pass). As gpg ids are stored in a private `.gnupg` directory, it
is fine to have it the group shared directory.

### ssh keys

For the same reason it is fine to have the `.ssh` directory in a group shared
directory.

## Security concerns

| Storage        | Data and encryption key must be on different partitions | OK |
| Download cache | Must no be on RAM, must be cleaned after use            | OK |
| Vaults         | Vaults and their keys must be on different partitions   | OK |
