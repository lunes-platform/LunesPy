from lunespy.tx.transfer import TransferToken
from requests import Response

from lunespy.wallet.crypto import bytes_to_b58


def serialize_transfer(tx: TransferToken) -> bytes:
    from lunespy.wallet.crypto import b58_to_bytes
    from struct import pack

    return (
        chr(tx.type).encode() + \
        b58_to_bytes(tx.senderPublicKey) + \
        (b'\1' + b58_to_bytes(tx.assetId) if tx.assetId != "" else b'\0') + \
        (b'\1' + b58_to_bytes(tx.feeAsset) if tx.feeAsset != "" else b'\0') + \
        pack(">Q", tx.timestamp) + \
        pack(">Q", tx.amount) + \
        pack(">Q", tx.fee) + \
        b58_to_bytes(tx.recipient)
    )


def sign_transfer(private_key: str, tx: TransferToken) -> dict:
    from lunespy.utils.crypto.converters import sign
    from lunespy.wallet.crypto import b58_to_bytes, bytes_to_b58

    tx.message = bytes_to_b58(serialize_transfer(tx))

    return bytes_to_b58(sign(
        b58_to_bytes(private_key),
        b58_to_bytes(tx.message)
    ))



# todo async
def broadcast_transfer(mount_tx: dict, node_url: str) -> Response:
    from httpx import post

    return post(
        f'{node_url}/transactions/broadcast',
        json=mount_tx,
        headers={
            'content-type':
            'application/json'
    })
