import socket
from packet.cmd_send_handshake import CmdSendHandshake
from packet.cmd_send_login import CmdSendLogin
from packet.cmd_send_ping import CmdSendPing

class Connector():
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.__sock.connect((self.__ip, self.__port))
        self.send(CmdSendHandshake().pack())
    
    def login(self, username):
        self.send(CmdSendLogin(username).pack())

    def ping(self):
        self.send(CmdSendPing().pack())

    def send(self, packet):
        self.__sock.sendall(packet.get_data())