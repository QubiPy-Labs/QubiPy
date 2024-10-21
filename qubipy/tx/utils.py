"""
utils.py
Utility functions for the Qubic Transaction
"""
from qubipy.crypto.utils import sign, verify, getTxHashFromDigest, getPrivateKeyFromSubSeed

class QubiPy_Tx:
    def __init__(self):
        self.built_data = bytearray()

        self.source_public_key = None
        self.destination_public_key = None
        self.amount = 0
        self.target_tick = 0
        self.input_type = 0
        self.input_size = 0

        self.payload = None

    def set_source_public_key(self, public_key: bytes) -> 'QubiPy_Tx':
        self.source_public_key = public_key
        return self
    
    def set_destination_public_key(self, public_key: bytes) -> 'QubiPy_Tx':
        self.destination_public_key = public_key
        return self
    
    def set_amount(self, amount: int) -> 'QubiPy_Tx':
        self.amount = amount
        return self
    
    def set_target_tick(self, tick: int) -> 'QubiPy_Tx':
        self.target_tick = tick
        return self
    
    def set_input_type(self, input_type: int) -> 'QubiPy_Tx':
        self.input_type = input_type
        return self
    
    def set_input_size(self, input_size: int) -> 'QubiPy_Tx':
        self.input_size = input_size
        return self
    
    def build(self, seed: str) -> bytes:
        self.built_data = bytearray([0])
        offset = 0

        # Serialize source_public_key
        if self.source_public_key:
            self.built_data[offset:offset+len(self.source_public_key)] = self.source_public_key
            offset += len(self.source_public_key)
        
        # Serialize destination_public_key
        if self.destination_public_key:
            self.built_data[offset:offset+len(self.destination_public_key)] = self.destination_public_key
            offset += len(self.destination_public_key)
        
        # Serialize amount as 8 bytes big endian
        self.built_data[offset:offset+8] = self.amount.to_bytes(8, byteorder='big')
        offset += 8
        
        # Serialize target_tick as 4 bytes big endian
        self.built_data[offset:offset+4] = self.target_tick.to_bytes(4, byteorder='big')
        offset += 4
        
        # Serialize input_type as 2 bytes big endian
        self.built_data[offset:offset+2] = self.input_type.to_bytes(2, byteorder='big')
        offset += 2
        
        # Serialize input_size as 2 bytes big endian
        self.built_data[offset:offset+2] = self.input_size.to_bytes(2, byteorder='big')
        offset += 2
        
        # Serialize seed
        seed_bytes = seed.encode('utf-8')
        
        private_key = get_private_key_from_seed(seed)
        signature = sign(private_key, self.built_data)
        
        return self.built_data
