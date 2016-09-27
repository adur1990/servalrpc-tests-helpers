#!/usr/bin/env python

import socket, random, time
from Helpers import *

basename = socket.gethostname()
random.seed(basename)

data_set = [53, 512, 2048]

if __name__ == "__main__":
    count = 0
    while True:
        rhizomeRandomFile(basename+"-"+str(count)+".bin", random.choice(data_set))
        count += 1
        insertion_delay = 60 + random.randint(0, 60)
        time.sleep(insertion_delay)
