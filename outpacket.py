class OutPacket():
    def __init__(self):
        self._data = []
        self._controller_id = 1
        self._cmd_id = -1

    def pack(self):
        self.pack_header()
        self.put_data()
        self.update_size()
        return self

    def pack_header(self):
        self._header = 0b10010000
        self.put_byte(self._header)
        self.put_unsigned_short(3)
        self.put_byte(self._controller_id)
        self.put_short(self._cmd_id)
    
    def set_controller_id(self, controller_id):
        self._controller_id = controller_id

    def set_cmd_id(self, cmd_id):
        self._cmd_id = cmd_id
    
    def get_data(self):
        return b''.join(self._data)

    def put_data(self):
        pass
    
    def put_byte(self, val):
        self._data.append(OutPacket.to_byte(val))

    def put_unsigned_short(self, val):
        self.put_byte(val >> 8)
        self.put_byte(val >> 0)

    def put_short(self, val):
        self.put_byte((val >> 8) & 0xff)
        self.put_byte((val >> 0) & 0xff)
    
    def put_int(self, val):
        self.put_byte((val >> 24) & 0xff)
        self.put_byte((val >> 16) & 0xff)
        self.put_byte((val >> 8) & 0xff)
        self.put_byte((val >> 0) & 0xff)
    
    def put_long(self, val):
        self.put_byte((val >> 56) & 0xff)
        self.put_byte((val >> 48) & 0xff)
        self.put_byte((val >> 40) & 0xff)
        self.put_byte((val >> 32) & 0xff)
        self.put_byte((val >> 24) & 0xff)
        self.put_byte((val >> 16) & 0xff)
        self.put_byte((val >> 8) & 0xff)
        self.put_byte((val >> 0) & 0xff)
    
    def put_byte_arr(self, val, len):
        self.put_short(len)
        self.put_bytes(val)
    
    def put_str(self, val):
        length = len(val)
        self.put_byte_arr(bytearray(val.encode()), length)
    
    def put_bytes(self, vals):
        for val in vals:
            self.put_byte(val)
    
    def update_unsigned_short_at_pos(self, val, pos):
        self._data[pos] = OutPacket.to_byte(val >> 8)
        self._data[pos + 1] = OutPacket.to_byte(val >> 0)
    
    def update_size(self):
        self.update_unsigned_short_at_pos(len(self._data) - 3, 1)
    
    def to_byte(val):
        return val.to_bytes(1, 'big')