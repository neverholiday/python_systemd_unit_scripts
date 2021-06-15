#!/usr/bin/env python3

import os
import time

import subprocess

def callSubprocess():
	process = subprocess.Popen( [ '/usr/local/bin/internal_script.py', 'test' ] )
	process.communicate()

print( 'Start simple python services' )

while True:
	
	print( 'Run!!!' )
	time.sleep( 20 )
	callSubprocess()