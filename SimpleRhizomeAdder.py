#!/usr/bin/env python

import socket, random, time
from Helpers import *

basename = socket.gethostname()
random.seed(basename)

if __name__ == "__main__":
    count = 0
    while True:
    	rhizomeRandomFile(basename+"-"+str(count)+".bin", random.randint(1024, 4096))
        count += 1
        insertion_delay_ms = 10000 + random.randint(0, 10000)
        time.sleep(float(insertion_delay_ms)/1000)
