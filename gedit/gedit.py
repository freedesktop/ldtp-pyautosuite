#!/usr/bin/python

from ldtp import *
import string,sys

if len (sys.argv) == 1:
  print 'Appmap path missing'
  sys.exit (0);
else:
  initappmap (sys.argv[1] + '/gedit.map')
  
launchapp ('gedit')

selectmenuitem ('gedit', 'mnuFile;mnuClose')

# Open existing file
execfile ('open-existing-file.py')

# Open page setup
execfile ('page-setup.py')

# close gedit
selectmenuitem ('gedit', 'mnuFile;mnuQuit')
