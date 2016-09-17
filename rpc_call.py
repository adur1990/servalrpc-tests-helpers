#!/usr/bin/env python
import subprocess, os, sys, random, socket, time, argparse, tempfile

parser = argparse.ArgumentParser(description='Call RPCs in different modes.')
parser.add_argument('-m', dest='mode', required=True, help='call mode (t, r, s, d)')
parser.add_argument('-n', dest='count', required=True, type=int, help='number of RPCs to be called')
parser.add_argument('-d', dest='dest', required=True, help='destination (any, all, sid)')
parser.add_argument('-s', dest='size', required=True, type=int, help='size of the file for complex cases')
args = parser.parse_args()

globals().update(vars(args))

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
    devnull = open(os.devnull, 'w')

    if size == 0:
        # simple call
        if dest == 'sid':
            # simple call to sid
            if mode == 't':
                # simple call to sid transparent
                while count > 0:
                    receiver = random.choice(other_sids)
                    subprocess.call(["rpc", "-c", "--", receiver, "simple", my_sid, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)
            else:
                # simple call to sid special mode
                while count > 0:
                    receiver = random.choice(other_sids)
                    subprocess.call(["rpc", "-c", '-'+mode, "--", receiver, "simple", my_sid, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)
        else:
            # simple call to any/all
            if mode == 't':
                # simple call to any/all transparent
                while count > 0:
                    subprocess.call(["rpc", "-c", "--", dest, "simple", my_sid, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)
            else:
                # simple call to any/all special mode
                while count > 0:
                    subprocess.call(["rpc", "-c", '-'+mode, "--", dest, "simple", my_sid, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)
    else:
        # complex call
        if dest == 'sid':
            # complex call to sid
            if mode == 't':
                # complex call to sid transparent
                while count > 0:
                    temp = tempfile.NamedTemporaryFile(dir='/tmp')
                    temp.write(os.urandom(1024))
                    temp.write('\0' * 1024 * (int(size)-1))

                    receiver = random.choice(other_sids)
                    subprocess.call(["rpc", "-c", "--", receiver, "complex", temp.name, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    temp.close()
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)
            else:
                # complex call to sid special mode
                while count > 0:
                    temp = tempfile.NamedTemporaryFile(dir='/tmp')
                    temp.write(os.urandom(1024))
                    temp.write('\0' * 1024 * (int(size)-1))

                    receiver = random.choice(other_sids)
                    subprocess.call(["rpc", "-c", '-'+mode, "--", receiver, "complex", temp.name, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    temp.close()
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)
        else:
            # complex call to any/all
            if mode == 't':
                # complex call to any/all transparent
                while count > 0:
                    temp = tempfile.NamedTemporaryFile(dir='/tmp')
                    temp.write(os.urandom(1024))
                    temp.write('\0' * 1024 * (int(size)-1))

                    subprocess.call(["rpc", "-c", "--", dest, "complex", temp.name, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    temp.close()
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)
            else:
                # complex call to any/all special mode
                while count > 0:
                    temp = tempfile.NamedTemporaryFile(dir='/tmp')
                    temp.write(os.urandom(1024))
                    temp.write('\0' * 1024 * (int(size)-1))

                    subprocess.call(["rpc", "-c", '-'+mode, "--", dest, "complex", temp.name, "0,0,0,0,0,0,0,0"], stdout=devnull, stderr=devnull)
                    count = count - 1
                    temp.close()
                    sleeptime = random.randint(10, 20)
                    time.sleep(sleeptime)

    devnull.close()
