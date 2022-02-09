from .cmd_define import CMD
from outpacket import OutPacket

class CmdSendMove(OutPacket):
    def __init__(self, obj_id, x, y):
        super().__init__()
        self.set_cmd_id(CMD["MOVE"])
        self.__obj_id = obj_id
        self.__x = x
        self.__y = y

    def put_data(self):
        self.put_int(1)
        self.put_int(self.__obj_id)
        self.put_int(self.__x)
        self.put_int(self.__y)
        self.put_byte(0)