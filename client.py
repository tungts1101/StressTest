import os
import time
import gevent
from connector import Connector
from packet.cmd_factory import CmdFactory

class Client():
    def __init__(self, ip='127.0.0.1', port=1102, username='', ping_counter=10):
        self.__connector = Connector(ip, port)
        self.__username = username
        self.__ping_counter = ping_counter
    
    def run(self):
        try:
            self.__connector.connect()
            self.__connector.login(self.__username)
            # gevent.sleep(10)
            for packet in CmdFactory.construct(os.path.join("script", "construct_building.json")):
                # time.sleep(1)
                gevent.sleep(1)
                self.__connector.send(packet)

            gevent.sleep(100)
            ping_counter = 0
            while True:
                # time.sleep(1)
                self.__connector.ping()
                if ping_counter > self.__ping_counter: return
                ping_counter += 1
                gevent.sleep(100)
        except Exception as ex:
            print("{} fails to connect".format(self.__username))