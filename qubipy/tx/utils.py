"""
utils.py
Qubic Transaction Utilities
"""

from qubipy.crypto.utils import get_private_key_from_subseed, get_subseed_from_seed, get_public_key_from_private_key, get_public_key_from_identity
from qubipy.tx.builder import Tx_Builder

def create_tx(seed: str, dest_id: str, amount: int, target_tick: int) -> tuple[bytes, bytes, bytes, bytes]:
    """
    Creates a transaction using the provided parameters.

    Args:
        seed (str): The seed used to derive keys for signing.
        dest_id (bytes): The destination identity for the transaction.
        amount (int): The amount to be transferred.
        target_tick (int): The target tick for the transaction.

    Returns:
        tuple: A tuple containing the first 80 bytes of the built data, the full built data, the signature, and the transaction hash.
    """

    source_private_key = get_private_key_from_subseed(get_subseed_from_seed(bytes(seed, 'utf-8')))
    source_public_key = get_public_key_from_private_key(source_private_key)
    destination_public_key = get_public_key_from_identity(dest_id)

    tx = Tx_Builder()
    tx.set_source_public_key(source_public_key)
    tx.set_destination_public_key(destination_public_key)
    tx.set_amount(amount)
    tx.set_target_tick(target_tick)
    tx.set_input_type(0)
    tx.set_input_size(0)
    
    return tx.build(seed)