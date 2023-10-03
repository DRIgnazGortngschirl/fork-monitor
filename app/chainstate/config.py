
nodes_debug = {
    'Hyperledger Besu,Phoenix,v1.4.3-stable-3f4f14c1': {
        'url': 'http://localhost:8555',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Core-Geth,Phoenix,v1.11.2-stable-cbe4a649': {
        'url': 'http://localhost:8565',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Open Ethereum,Phoenix,v3.0.0-nightly-56885fe4': {
        'url': 'http://localhost:8545',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Multi-Geth,Phoenix,v1.9.14-stable-3f141bb4': {
        'url': 'http://localhost:8575',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Geth Classic,Agharta,v6.1.2-stable-71d8b42b': {
        'url': 'http://localhost:8585',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
}

nodes_production = {
    'Hyperledger Besu-AT,Mystique,v23.7.3': {
        'url': 'https://besu-at.etc-network.info/',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Core-Geth-AT,Mystique,v1.12.14': {
        'url': 'https://geth-at.etc-network.info/',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Hyperledger Besu-DE,Mystique,v23.7.3': {
       'url': 'https://besu-at.etc-network.info/',
       'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Core-Geth-DE,Mystique,v1.12.14': {
        'url': 'https://geth-at.etc-network.info/',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
}

nodes_fallback = {
    'Hyperledger Besu,Phoenix,v1.4.3-stable-3f4f14c1': {
        'url': 'http://ceibo.htznr.fault.dev:8555',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Core-Geth,Phoenix,v1.11.2-stable-cbe4a649': {
        'url': 'http://ceibo.htznr.fault.dev:8565',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Open Ethereum,Phoenix,v3.0.0-nightly-56885fe4': {
        'url': 'http://ceibo.htznr.fault.dev:8545',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Multi-Geth,Phoenix,v1.9.14-stable-3f141bb4': {
        'url': 'http://ceibo.htznr.fault.dev:8575',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
    'Geth Classic,Agharta,v6.1.2-stable-71d8b42b': {
        'url': 'http://ceibo.htznr.fault.dev:8585',
        'explorer': "https://blockscout.com/etc/mainnet/blocks/%s",
    },
}
