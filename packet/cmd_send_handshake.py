from .cmd_define import CMD
from outpacket import OutPacket

class CmdSendHandshake(OutPacket):
    def __init__(self):
        super().__init__()
        self.set_controller_id(0)
        self.set_cmd_id(CMD["HANDSHAKE"])