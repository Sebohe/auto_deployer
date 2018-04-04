import os
import json
from sh import solc
import ast
import toml
import web3 as w3

def linker (library_addr, library_name):

    #solc --optimize --bin MetaCoin.sol | solc --link --libraries TestLib:<address>
    #
    solc("--libraries", library_name, library_addr)
    pass

def parseBuildDir():
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

def getTruffleABI(json_path):
    pass

def getTruffleBytecode(json_path):
    """
    Reads truffle compiled json contracts
    and returns the bytecode
    """
    pass

def jsonExtraction(source_path, contractNames):
   
    contractList = {} 
    for cName in contractNames:
        path = os.path.join(source_path, cName + ".json")
        with open(path) as f:
            contractList[cName] = json.load(f)
   
    return contractList

def generateContracts(source_path, contractNames):
    """
    Generates personalized contract object
    """
    path = os.path.abspath(source_path)
    fileList = os.listdir(source_path)
  
    fileExtInDir = []
    for f in fileList:
        #print (f)
        fileExtInDir.append(os.path.splitext(f)[1])

    fileExtInDir = list(set(fileExtInDir)) 

    if any("json" in s for s in fileExtInDir):
        return jsonExtraction(source_path, contractNames) 


    contract_list = []
    return contract_list

def readConstructors(constructor_file):
    
    return contracts
