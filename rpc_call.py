#!/usr/bin/env python
import subprocess, os, sys, random, socket, time

SERVALD_BIN = "servald"

def getSid():
    sid = subprocess.check_output(SERVALD_BIN + " id self", shell=True)
    return sid.split('\n')[2]

def getNeightbourSids():
	with open("/tmp/serval-all-sids", 'r') as sid_file:
		return filter(lambda x: x != getSid(), map(lambda x: x.replace('\n', ''), sid_file.readlines()))

if __name__ == '__main__':
    random.seed(socket.gethostname())

    my_sid = getSid()
    other_sids = getNeightbourSids()

    if len(sys.argv) == 4:
        mode = sys.argv[1]
        num = int(sys.argv[2])

        while num > 0:
            if sys.argv[3] == "any" or sys.argv[3] == "all":
                receiver = sys.argv[3]
            else:
                receiver = random.choice(other_sids)
            devnull = open(os.devnull, 'w')
            ret_code = subprocess.call(["rpc", "-c", mode, "--", receiver, "simple", my_sid, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
            devnull.close()
            num = num - 1
            sleeptime = random.randint(10, 20)
            time.sleep(sleeptime)
    elif len(sys.argv) == 3:
        num = int(sys.argv[1])

        while num > 0:
            if sys.argv[2] == "any" or sys.argv[2] == "all":
                receiver = sys.argv[1]
            else:
                receiver = random.choice(other_sids)
            devnull = open(os.devnull, 'w')
            ret_code = subprocess.call(["rpc", "-c", "--", receiver, "simple", my_sid, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
            devnull.close()
            num = num - 1
            sleeptime = random.randint(10, 20)
            time.sleep(sleeptime)
