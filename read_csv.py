# TODO
# this method is the same as for RaspberryPi/webserver_pi/tornado/tornado_app.py
# could be a shared module

import os
import glob

print 'yo'

def get_humidity(folder):
	os.chdir(folder)
	newest = max(glob.iglob('*.*'), key=os.path.getctime)
	file = open(newest, 'r')
	lines = file.readlines()
	file.close()

	# returns a line of csv like ['1395513142', ' T 19.2', ' H 31.1\n']	
	return lines[-1].split(',')

def sjso():
	print 'works'