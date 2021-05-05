
# default "public" connections for RPC proxy
absoluted_default_connections = [
    {
        "use_ssh_tunnel": False,
        "host": "amt.absify.me",
        "port": "18889",
        "username": "abs_mn_user",
        "password": "abs_mn_user",
        "use_ssl": True,
        "rpc_encryption_pubkey": "30820122300d06092a864886f70d01010105000382010f003082010a0282010100d8338321c24a6ea567ba3e670c1e93f75b61f05c3dce37641e078ad58e8f44dc3c29fb2b78b9e9d5162fe604eb73622f922e2ed05f9087be773db88d90115c47e27b5d8fee1dc6f9cb18a9f53b9c5cb9ba5a3578ee4a26265ef4e3b13eb661dd1a08f138405a41fcd7e377f1cfc47a481dac6b55390cfd29b81f0accc06430c1ab5258458a1d6a961d0b12770ef4202e87493af2e476da32fac59a53be326a0ad7c45bbc624b997fccf898cb7e1ea9e0dbcac9db2956318ce25bd1f80785df299abea8061ab9eacd5d3de718d221c7683d16b1ee5f5637d1b121b04c13cdf2ac5f7682d902549c2786e527228517c0e360529140acaa6a8e405d4f1be55112890203010001"
    },
    {
        "use_ssh_tunnel": False,
        "host": "tamt.absify.me",
        "port": "17778",
        "username": "abs_mn_user",
        "password": "abs_mn_user",
        "use_ssl": True,
        "testnet": True,
        "rpc_encryption_pubkey": "30820122300d06092a864886f70d01010105000382010f003082010a0282010100cb66bbc41d1788d7e229bffb1393a4f2a5478950fa9f2c398463798eb87c790cbcf6d1e6778382fe9b2295fcb2edd8a512b8fdebe727f807e7564a5d479da07961ca586e21c6ec2f641628b195acddccd2ad06dc9b03e404acf2230d7b3ff518c04c2b345ff7889419c8297e4fae6e0471447b128cb88fe7deb7c75900c965d5f04c9811f02ca9db7982ce709108f3a34beb91b494372f1a7ec45e725c243bc0eee6e4660da8ceebf0ae1fd617d87f4a46239e04c9120097afa677d8dd55052b201b5bda3c5d215553204bc2f178d7f22f97867d7b0952ea7e447eae03fa63081285730bc04928f64077c1a07e47271566e2337aff177a39b02b1d299482d49f0203010001"
    }
]
