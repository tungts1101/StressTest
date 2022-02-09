from .cmd_define import CMD
from outpacket import OutPacket

class CmdSendLogin(OutPacket):
    def __init__(self, username):
        super().__init__()
        self.set_cmd_id(CMD["LOGIN"])
        self.__username = username

    def put_data(self):
        self.put_str(self.__username)