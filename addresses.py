# Functions that generates addresses
from ethereum.utils import (
        mk_contract_address,
        sha3,
        normalize_address,
        encode_hex
    )

def determineContractAddr(deployerAddr, tx_count, qty):

    addresses = []
    for i in range(tx_count, tx_count + qty):
        _addr = str(encode_hex(mk_contract_address(deployerAddr, i)))
        addresses.append(_addr)

    return addresses
