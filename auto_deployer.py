#!/usr/bin/env python3
import toml 
from web3 import (
        Web3,
        HTTPProvider
        )

from args import (
        arg_parser
        )

from addresses import determineContractAddr
import contracts
import interwebs

def deployContracts(w3, contractObject, deployer, gasPrice=0):

    w3Contract = w3.eth.contract(
                            abi = contractObject['abi'],
                            bytecode = contractObject['bytecode']
                            )

    txn = {'from': deployer, 'gasPrice': gasPrice} 
    args = contractObject['args']
    tx_hash = w3Contract.deploy(transaction=txn, args=args)

    return tx_hash

def generateConstructorsArgs(contractObject, config):

    contractNames = contractObject.keys()
   
    # The following loops add contract addresses to the contructor arguments
    for cKey in contractObject:
        args = list(config[cKey].values())
        collisions = list(set(args).intersection(contractNames))
        for cKey in collisions: 
            for index in range(len(args)):
                if args[index] == cKey:
                    args[index] = cKey + " " + contractObject[cKey]['address']

        
        contractObject[cKey]['args'] = args
       
    return contractObject

if __name__=='__main__':

    args = arg_parser()
    w3 = Web3(HTTPProvider(args.nodeURL))

    deployer = args.deployer
    try:
        deployer = int(deployer)
        deployer = w3.eth.accounts[deployer]
    except:
        pass

    config = toml.load(args.config)
    Contracts = contracts.generateContracts(args.buildDir, config.keys())
    tx_count = w3.eth.getTransactionCount(deployer)


    for index, cKey in enumerate(Contracts):
        Contracts[cKey]['address'] = determineContractAddr(deployer, tx_count + index + 1)
    
    Contracts = generateConstructorsArgs(Contracts, config)

    for cKey in Contracts:
        Contracts[cKey]['args']

