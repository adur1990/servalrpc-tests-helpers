#!/usr/bin/env python

import socket, random, time
from Helpers import *

basename = socket.gethostname()
random.seed(basename)

if __name__ == "__main__":
    count = 0
    while True:
    	rhizomeRandomFile(basename+"-"+str(count)+".bin", random.randint(1024, 4096))
        print "inserting file"
        count += 1
        insertion_delay = 20 + random.randint(0, 10)
        print "sleeping {}".format(insertion_delay)
        time.sleep(insertion_delay)
