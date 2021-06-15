#!/usr/bin/env python3

import sys
import os

import time

import subprocess

#
#	NOTE : Can change gid and uid if you need sub script to run with other user, not root
#
os.setgid( 117 )
os.setuid( 112 )
 
def process():
	'''!	TODO : Implement here
	'''
	print( 'Process...' )
	output = subprocess.check_output( 'whoami' )
	print( 'I am {}'.format( str( output, 'utf-8' ) ) )
	time.sleep( 10 )
	print( 'Done!' )


print( f'Sub-script run with {sys.argv}' )
#	TODO : Implement something here
process()