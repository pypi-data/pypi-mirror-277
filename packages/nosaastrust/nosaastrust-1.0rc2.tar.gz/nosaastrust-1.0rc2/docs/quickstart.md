# Quickstart

## Services

Each service to be backed-up needs to be described in a YaML file.

As this description aims to be shared and might contain service you don't have access to, add the following line to list which services to backup:

```yaml
backuplist: ["service1","service2"]
```

An example of service description can be found in resources folder.

### List of services to backup

List services in `services` section.

Add the service's name and the plugin to use for fetching data.

```yaml
services:
  service1: # Service's name is service1
    type: rsync # Use plugin rsync
```

Then, depending on data type and plugin type, you may need to add more information:

1. **data to backup are on remote host**

Add host description:

```yaml
    host: user@domain
```

2. **data to backup are on my computer**

```yaml
    host: local
```

3. **data to backup are on a specific path**

```yaml
    path: my/path
```

```yaml
    path: /
```

4. **data to backup are on a git repository**

```yaml
  type: git
  path: git@domain:path/to/repository.git
```

5. **backup a whole GitLab group**

```yaml
  type: gitlab_api
  auth:
    user: gitlab_username
    PAT: PersonalAccessToken # This token can be stored and fetch from a vault
  host: https://gitlab.com
  group_id: groupID
```

6. **Use a specific key with rsync plugin**

```yaml
  service1:
    type: rsync
    auth:
      keyname: my_key
```

7. **Add rotation**

```yaml
  service1:
    type:
    rotation:
      year: number
      month: number
      week: number
      day: number
```

## Backend Configuration

Configuration file must be named `nost.toml` and should be stored in either:

- $HOME/.config
- /etc
- or /usr/share/nost

This configuration file stores information on backend tool used (borgbackup by default) and vault options.

An example is provided at the root of this project.

To use the default configuration, copy nost.toml of this project into one of the locations described above.

### Borg backend

The borg backend requires a passphrase. To avoid multiple password ask, one can
use the variable `BORG_PASSPHRASE_FD` which will be read and forwarded to every
borg calls.

eg using pass:

``` shell
pass borg | BORG_PASSPHRASE_FD=0 nost sync backups.yml
```
