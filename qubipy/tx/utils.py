from qubipy.tx.builder import Tx_Builder

def create_tx(seed: str, source_public_key: bytes, destination_public_key: bytes, amount: int, target_tick: int, input_type: int, input_size: int) -> tuple[bytes, bytes, bytes, bytes]:
    tx = Tx_Builder()
    tx.set_source_public_key(source_public_key)
    tx.set_destination_public_key(destination_public_key)
    tx.set_amount(amount)
    tx.set_target_tick(target_tick)
    tx.set_input_type(input_type)
    tx.set_input_size(input_size)
    
    return tx.build(seed)
