# Architecture

There are two main parts in the project:

1. retrieve the data (the fetcher)
2. manage the data: rotation, encryption, storage (the backend)

The implementation of the fetcher will follow a plugin architecture as it allows
to add multiple support with no modification to the core.

The backend must be replacable. Borg will be the default supported backend. The
final data can be stored localy or on a distant server.

## Sequence Diagram (draft)

```
nost    pluginA    pluginB    backend            server1    server2    storage
 |        |          |          |                  |          |          |
=============================================================================
# Backup server1 using pluginA
 |        |          |          |                  |          |          |
 |------->|          |          |                  |          |          |
 |        |--------------------------------------->|          |          |
 |        |<- - - - - - - - - - - - - - - - - - - -|          |          |
 |        |-------------------->|                  |          |          |
 |        |          |          |--------------------------------------->|
 |        |          |          |<- - - - - - - - - - - - - - - - - - - -|
 |        |<- - - - - - - - - - |                  |          |          |
 |<- - - -|          |          |                  |          |          |
 |        |          |          |                  |          |          |
 |        |          |          |                  |          |          |
=============================================================================
# Backup server2 using pluginB
 |        |          |          |                  |          |          |
 |------------------>|          |                  |          |          |
 |        |          |--------------------------------------->|          |
 |        |          |<- - - - - - - - - - - - - - - - - - - -|          |
 |<- - - - - - - - - |          |                  |          |          |
 |----------------------------->|                  |          |          |
 |        |          |          |--------------------------------------->|
 |        |          |          |<- - - - - - - - - - - - - - - - - - - -|
 |        |          |<- - - - -|                  |          |          |
 |<- - - - - - - - - |          |                  |          |          |
 |        |          |          |                  |          |          |
nost    pluginA    pluginB    backend            server1    server2    storage
```

## Class diagram (draft)

```

    ,--------------------------------.
    |Plugin                          |
    |--------------------------------|
    |+ do_configure()                |
    |+ do_authenticate()             |
    |+ do_presync()                  |
    |+ do_sync(Credentials,          |
    |          Backend, backendopts) |
    |+ do_postsync()                 |
    |+ do_clean()                    |
    `--------------------------------'
                Δ
                |
     ,----------|-----------.
     |          |           |
     |          |           |
 ,-------.  ,-------.   ,-------.
 |PluginA|  |PluginB|   |PluginC|
 |-------|  |-------|   |-------|
 `-------'  `-------'   `-------'


       ,-----------.
       |Credentials|
       ,-----------.
       |+ auth()   |
       `-----------'
            |
            |
            |*
    ,----------------------.
    |Vault                 |
    |----------------------|
    |+ retrieve()          |
    `----------------------'
                Δ
                |
     ,----------|-----------.
     |                      |
     |                      |
 ,----------.       ,--------------.
 |LocalVault|       |BitwardenVault|
 |----------|       |--------------|
 `----------'       `--------------'


         ,-------------------.
         |Backend            |
         |-------------------|
         |+ init(storageType)|
         |+ process()        |
         |+ rotate()         |
         |+ alert()          |-------------+
         |+ encrypt()        |             |
         |+ list()           |             |
         |+ retrieve(id)     |             |
         `-------------------'             |
              Δ                            |
              |                            |
              |                            |1
         ,-----------.           ,-------------------.
         |BorgBackend|           |StorageManagerDraft|
         |-----------|           |-------------------|
         `-----------'           |+ send()           |
                                 `-------------------'
                                           Δ
                                           |
                                           |
                                  +--------+--------+
                                  |                 |
                           ,------------.   ,--------------.
                           |LocalStorage|   |DistantStorage|
                           |------------|   |--------------|
                           `------------'   `--------------'


```

- `Plugin` is the abstract class from which all plugins are inherited. The
  number of subclasses and instances of each is unlimited.
- `Credentials` is an abstract class to manage credentials. There should be one
  per service. A subclass shall be defined in every plugin.
- `Vault` is an abstract class to define vaults. Their usage is up to the
  `Credentials` object
- `Backend` is the backup manager in charge of encryption, rotation,
  storage. There can be only one and it owns a `StorageManager`. It shall be
  able to list all stored backup and to retrieve them.
- `StorageManager` is an abstract class to manage the storage.
