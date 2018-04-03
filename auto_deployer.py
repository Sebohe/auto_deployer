#!/usr/bin/env python3
import toml
from web3 import (
        Web3,
        HTTPProvider
        )

from args import (
        arg_parser
        )

import addresses
import contracts
import interwebs

def readConfigFile(config):
    config = toml.load(config)
    pass

if __name__=='__main__':

    args = arg_parser()
    w3 = web3.Web3(HTTPProvider(args.nodeURL))

    deployer = args.deployer
    try:
        deployer = int(deployer)
        deployer = w3.eth.accounts[deployer]
    except:
        pass

    tx_count = w3.eth.getTransactionCount(deployer)
    contracts = read_all_contracts('build')
    contrs_addrs = determine_addresses(deployer, tx_count, len(contracts))

    # Assign address to tokens
    for i, c_key in enumerate(contracts):
        contracts[c_key]['addr'] = contrs_addrs[i]

   
    contracts = read_deploy_args(contracts)

    """
    for c_key in contracts:
        print (contracts[c_key])
        print()
    """

    for c_key in contracts:

        contracts[c_key]['class'].deploy(
                {'from': deployer}, args = contracts[c_key]['args']
                )



