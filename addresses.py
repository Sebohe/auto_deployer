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
        _addr = str(encode_hex(mk_contract_address(deployerAddr, i)))
        _addr = _addr.replace("\'", "")
        _addr = checksum_encode(decode_hex(_addr))

    return _addr
