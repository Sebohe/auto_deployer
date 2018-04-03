import os
import json
from sh import solc
import json
import ast
import toml

def linker (library_addr, library_name):

    #solc --optimize --bin MetaCoin.sol | solc --link --libraries TestLib:<address>
    #
    solc("--libraries", library_name, library_addr)
    pass


def readByteCode(contract_path):
   
    with open(contract_path, 'r') as c:
        return c.readline()

def readABI(contract_path):

    s = ''
    with open(contract_path) as c:
        for line in c:
            s = s + line
   
    return(json.loads(s))


def getTruffleBytecode(json_path):
    """
    Reads truffle compiled json contracts
    and returns the bytecode
    """

def readContractsSource(source_path):
    """
    Generates personalized contract object
    """
    path = os.path.abspath(source_path)
    file_list = os.listdir(source_path)
    only_names_list = []

    for f in file_list:
        only_names_list.append(f.split('.')[0])

    names_list = list(set(only_names_list))
    contract_list = {}

    for n in names_list:
        n = path + '/' + n
        abi = read_abi(n + '.abi')
        byte = read_byte_code(n + '.bin')
        name = n.split('/')[-1]
        c = w3.eth.contract(abi=abi, bytecode=byte, contract_name=name)
        contract_list[name] = {'class': c}

    return contract_list

def readConstructors(contracts):
    """
    read deployment file for constructor parameters 
    """
    ####### This needs to go in a toml file. And a generator function
    contracts['Presale']['args']=[
                    "",
                    200,
                    1000,
                    0,
                    1,
                    contracts['Token']['addr'],
                    ]

    contracts['Crowdsale']['args' ]= ["",
                        10,
                        1000,
                        0,
                        3,
                        contracts['Token']['addr'],
                        100,
                        10000,
                        [20,10,0],
                        [1,1,1],
                        10
                        ]



    contracts['Token']['args'] = [
                        contracts['Presale']['addr'], 
                        contracts['Presale']['addr']
                        ]


    contracts['SafeMath']['args'] = ''
    return contracts
