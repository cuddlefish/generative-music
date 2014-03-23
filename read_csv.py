# TODO
# this method is the same as for RaspberryPi/webserver_pi/tornado/tornado_app.py
# could be a shared module

import sys
import os
import glob

# called without arguments, get_humidity() will look in the dir indicated by 
# the HUMID_LOG environment variable
try:
	humidity_folder = os.environ.get(HUMID_LOG)
except:
	humidity_folder = "/"

# returns a line of csv like ['1395513142', ' T 19.2', ' H 31.1\n']
def get_newest_line(folder=humidity_folder):
	os.chdir(folder)
	newest = max(glob.iglob('*.*'), key=os.path.getctime)
	file = open(newest, 'r')
	lines = file.readlines()
	file.close()
	return lines[-1].split(',')



if __name__ == "__main__":
	try:
		print 'this module is not configured for command-line use.'
		print 'Looking for line in HUMID_LOG or current directory' 
		get_newest_line()
	except KeyboardInterrupt:
		pass
