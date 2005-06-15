#!/usr/bin/python

from ldtp import *
import string, sys, os
from ldtputils import *

appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./gedit.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/gedit.map')

launchapp ('gedit')

#To add the initial XML info to the log script
log ('GEditSuite',"begin")

#To open an new file
execfile ('open-newfile.py')

#To open an existing file
execfile ('open-existingfile.py')

#To perform edit operations
execfile ('edit.py')

#To open pagesetup dialog
execfile ('pagesetup.py')

log ('GEditSuite','end')
