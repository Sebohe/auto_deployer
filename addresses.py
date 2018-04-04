# Functions that generates addresses
from ethereum.utils import (
        mk_contract_address,
        encode_hex,
        decode_hex,
        checksum_encode
    )

def determineContractAddr(deployerAddr, tx_count, qty=1):

    addresses = []
    for i in range(tx_count, tx_count + qty):
        _addr = mk_contract_address(deployerAddr, i)
        _addr = checksum_encode(_addr)

    return _addr
