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

def deployContracts(w3, contractObject, deployer, gasPrice=0):

    for key in contractObject:

        abi = contractObject[key]['abi']
        bytecode = contractObject[key]['bytecode']
        w3Contract = w3.eth.contract(
                                abi = abi,
                                bytecode = bytecode 
                                )

        tempList = []
        for a in contractObject[key]['args']:
            value = a.split(" ")[1]
            try:
                value = int(value)
            except:
                pass

            tempList.append(value)

        args = tempList
        txn = {'from': deployer, 'gasPrice': gasPrice} 
        txn_receipt = w3Contract.constructor(*args).transact(txn)
        contractObject[key]['txn_receipt'] = txn_receipt

    return contractObject 

def generateConstructorsArgs(contractObject, config):

    # The following loops add contract addresses to the contructor arguments
    for cKey in contractObject:
        args = list(config[cKey].values()) 
        for index in range(len(args)):
            containsAddr = args[index].split(" ")
            if "address" == containsAddr[1]:
                args[index] = cKey + " " + contractObject[containsAddr[0]]['address']

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
        Contracts[cKey]['address'] = determineContractAddr(deployer, tx_count + index)
    
    Contracts = generateConstructorsArgs(Contracts, config)
    Contracts = deployContracts(w3, Contracts, deployer)

    print ("Network = {}".format(args.nodeURL), end = '\n\n')
    for cKey in Contracts:
        print ("{} = {}".format(cKey, Contracts[cKey]['address']), end ='\n\n')
