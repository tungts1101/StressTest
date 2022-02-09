# from gevent.pool import Pool
import gevent
import time
import json
from client import Client
import signal
import sys
from getmac import get_mac_address as gma

def run(counter, cfg):
    username = "dev_stress_{}_{}".format("_".join(gma().split(':')), counter)
    print(username)
    # client = Client(username=username, ping_counter=cfg["NUM_PING"])
    client = Client(ip="49.213.82.124", port=10105, username=username, ping_counter=cfg["NUM_PING"])
    client.run()

def signal_handler(sig, frame):
    end = time.time()
    print("Time: {:.2f} ms".format((end - start) * 1000))
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global start, end

    cfg = json.load(open("config.json"))
    counter = 1000000
    start = time.time()
    jobs = [gevent.spawn(run, counter + i, cfg) for i in range(cfg["NUM_CLIENT"])]
    gevent.joinall(jobs)
    end = time.time()
    print("Time: {:.2f} ms".format((end - start) * 1000))
