"""
utils.py
Utility functions for the Qubic Transaction
"""
from qubipy.crypto.utils import sign, kangaroo_twelve, get_private_key_from_subseed, get_subseed_from_seed, get_public_key_from_private_key, get_identity_from_public_key

class Tx_Builder:
    def __init__(self):
        self.built_data = bytearray()

        self.source_public_key = None
        self.destination_public_key = None
        self.amount = 0
        self.target_tick = 0
        self.input_type = 0
        self.input_size = 0

        self.payload = None

    def set_source_public_key(self, public_key: bytes) -> 'Tx_Builder':
        self.source_public_key = public_key
        return self
    
    def set_destination_public_key(self, public_key: bytes) -> 'Tx_Builder':
        self.destination_public_key = public_key
        return self
    
    def set_amount(self, amount: int) -> 'Tx_Builder':
        self.amount = amount
        return self
    
    def set_target_tick(self, tick: int) -> 'Tx_Builder':
        self.target_tick = tick
        return self
    
    def set_input_type(self, input_type: int) -> 'Tx_Builder':
        self.input_type = input_type
        return self
    
    def set_input_size(self, input_size: int) -> 'Tx_Builder':
        self.input_size = input_size
        return self
    
    def build(self, seed: str) -> bytes:
        offset = 0

        if self.source_public_key:
            self.built_data[offset:offset+len(self.source_public_key)] = self.source_public_key
            offset += len(self.source_public_key)
        
        if self.destination_public_key:
            self.built_data[offset:offset+len(self.destination_public_key)] = self.destination_public_key
            offset += len(self.destination_public_key)
        
        self.built_data[offset:offset+8] = self.amount.to_bytes(8, byteorder='little')
        offset += 8
        
        self.built_data[offset:offset+4] = self.target_tick.to_bytes(4, byteorder='little')
        offset += 4
        
        self.built_data[offset:offset+2] = self.input_type.to_bytes(2, byteorder='little')
        offset += 2
        
        self.built_data[offset:offset+2] = self.input_size.to_bytes(2, byteorder='little')
        offset += 2
        
        # Sign the transaction
        seed_bytes = bytes(seed, 'utf-8')

        subseed = get_subseed_from_seed(seed_bytes)
        private_key = get_private_key_from_subseed(subseed)
        public_key = get_public_key_from_private_key(private_key)

        tx_digest = kangaroo_twelve(self.built_data, offset, 32)

        signature = sign(subseed, public_key, tx_digest)

        self.built_data[offset:offset+len(signature)] = signature
        offset += len(signature)

        digest = kangaroo_twelve(self.built_data, offset, 32)
        tx_hash = get_identity_from_public_key(digest).lower()

        return self.built_data[:80], self.built_data, signature, tx_hash
