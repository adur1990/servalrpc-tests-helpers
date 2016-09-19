#!/usr/bin/env python
import hashlib, subprocess, os, binascii, sys, random

SERVALD_BIN = "servald"
RANDOM_FILES_FOLDER = "/tmp/"

def rhizomeRandomFile(name, size_k):
	filepath = RANDOM_FILES_FOLDER + name

	with open(filepath, 'wb') as f:
		# write 1k random data
		f.write(os.urandom(1024))
		#write missing bytes
		f.write('\0' * 1024 * (int(size_k)-1))

	commmand = ["/serval-tests/rhizome-insert-curl", filepath]
	subprocess.check_output(commmand)
	os.remove(filepath)
	return size_k
