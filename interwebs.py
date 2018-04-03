from web3 import Web3, HTTPProvider
import json

def url_breaker(var):
    s = var.split(':')
    addr = s[0]+':'+s[1]
    port = s[-1]
    return addr, port

if __name__=='__main__':

    w3 = Web3(HTTPProvider(C['TEST']))
    deployer = w3.eth.accounts[-1]
    print (deployer)
    print ()
    
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



