import json
import os
from .cmd_define import CMD
from .cmd_send_move import CmdSendMove

class CmdFactory():
    @classmethod
    def construct(cls, filepath):
        packets = []
        try:
            with open(filepath) as script:
                cfg = json.load(script)
                script.close()
                for cmd_id, i_cfg in cfg.items():
                    cmd_id = int(cmd_id)
                    if cmd_id == CMD["MOVE"]:
                        packets.append(CmdSendMove(i_cfg["obj_id"], i_cfg["pos"]["x"], i_cfg["pos"]["y"]).pack())

            return packets
        except Exception as e:
            print(e)
            return []