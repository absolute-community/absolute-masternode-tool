# Connection to "public" nodes

This solution is designed for non-technical users who may have difficulty configuring their own JSON-RPC node, or for those who do not want to waste their time repeating what others have done before and have made publicly available :-)

From the user's point of view, the solution is based on several JSON-RPC nodes made available by the Absolute community to the users of the *Absolute Masternode Tool* and *absolutemnb* apps. At the time of writing, one of the nodes (actually three, accessed under one shared IP address) was managed by @chaeplin, a very well-known Absolute Core developer, and the other three by myself (@Bertrand256).

## Technical information

These nodes are based on the following components:
 * Absolute daemon (*absoluted*) processing JSON-RPC requests
 * *Nginx* web server, as a frontend serving SSL requests sent by the applications
 * A Lua script, as a broker between *nginx* and *absoluted*

Configuration is based on ethereum-nginx-proxy, adapted to Absolute requirements by @chaeplin: https://github.com/chaeplin/absolute-ticker/tree/master/web/nginx

## Configuration

When version 0.9.5 or higher of the DMT application is run the first time, "public" connections will automatically be added to the configuration. Open DMT and click the `Configure` button. In the `Configuration` dialog you should see the following three connections:
 * https://amt.absify.me:18889


![Public connection configuration window](img/dmt-config-dlg-public.png)

If you see connections and all three are checked (enabled) you don't need to do anything. If you see connections but they are not enabled, you just need to enable them. I also suggest deactivating all other connections, since these may be connections from an old configuration.

If any of the listed "predefined" nodes are missing or are incomplete, follow these steps:
 * Select all the text from the block below and copy to the clipboard (do not miss the square brackets at the beginning and the end of the text), for Absolute MAINNET:
```﻿
[
    {
        "use_ssh_tunnel": false,
        "host": "test.absify.me",
        "port": "18889",
        "username": "abs_mn_user",
        "password": "abs_mn_user",
        "use_ssl": true
    }
]
```
and for Absolute TESTNET:
```
[
    {
        "use_ssh_tunnel": false,
        "host": "tamt.absify.me",
        "port": "17778",
        "username": "abs_mn_user",
        "password": "abs_mn_user",
        "use_ssl": true
    }
]
```
 * Right-click on the `Connections` box.
 * From the popup menu choose the `Paste connection(s) from cliboard` action:
    ![Paste connections from clipboard](img/dmt-config-dlg-public-recover.png)
 * Click `Yes` to the question whether you want to import connections.

All three connections should then be added to the configuration.

## Security

To perform its job, the application must send some data to the JSON-RPC node that may be perceived as sensitive. Specifically, these are the client's IP address and the JSON-RPC commands themselves, with their respective arguments.

For example, the action initiated by the `Get status` button sends the following data to the node:
```python
{"version": "1.1", "id": 2, "params": ["full", "19e7eba493a026f205078469566e4df6a5a4b1428965574b55bec2412ddc9c48-0"], "method": "masternodelist"}
```

To maximize user anonymity, all three published nodes have disabled logging of any information related to JSON-RPC commands. The logging configuration is exactly the same as the example scripts provided by @chaeplin here: [https://github.com/chaeplin/absolute-ticker/tree/master/web/nginx](https://github.com/chaeplin/absolute-ticker/tree/master/web/nginx).

Despite this, if you would prefer not to risk sharing this information, it is suggested to disable the configuration options for the "public" nodes and choose a different type of connection:

- [Connection to a local Absolute daemon](config-connection-direct.md)
- [Connection to a remote Absolute daemon through an SSH tunnel](config-connection-ssh.md)
