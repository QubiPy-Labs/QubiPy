"""
utils.py
Qubic Transaction Utilities
"""

from qubipy.tx.builder import Tx_Builder

def create_tx(seed: str, source_public_key: bytes, destination_public_key: bytes, amount: int, target_tick: int, input_type: int, input_size: int) -> tuple[bytes, bytes, bytes, bytes]:
    """
    Creates a transaction using the provided parameters.

    Args:
        seed (str): The seed used to derive keys for signing.
        source_public_key (bytes): The source public key for the transaction.
        destination_public_key (bytes): The destination public key for the transaction.
        amount (int): The amount to be transferred.
        target_tick (int): The target tick for the transaction.
        input_type (int): The input type for the transaction.
        input_size (int): The input size for the transaction.

    Returns:
        tuple: A tuple containing the first 80 bytes of the built data, the full built data, the signature, and the transaction hash.
    """
    tx = Tx_Builder()
    tx.set_source_public_key(source_public_key)
    tx.set_destination_public_key(destination_public_key)
    tx.set_amount(amount)
    tx.set_target_tick(target_tick)
    tx.set_input_type(input_type)
    tx.set_input_size(input_size)
    
    return tx.build(seed)
