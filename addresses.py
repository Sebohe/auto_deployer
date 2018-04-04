# Functions that generates addresses
from ethereum.utils import (
        mk_contract_address,
        sha3,
        normalize_address,
        encode_hex
    )

def determineContractAddr(deployerAddr, tx_count, qty=1):

    addresses = []
    for i in range(tx_count, tx_count + qty):
        _addr = str(encode_hex(mk_contract_address(deployerAddr, i)))
        _addr = _addr.replace("\'", "")
        _addr = "0x" + _addr[1:]

    return _addr
