#!/usr/bin/python

from ldtp import *
import string, sys, os
from ldtputils import *
appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./gcalctool.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/gcalctool.map')

launchapp ('gcalctool')
check ('Calculator-Basic', 'mnuBasic') #Perform operations in basic mode

# View About & Credits
execfile ('view-gcalc-about.py')

#Add operations
execfile ('gcalc-add.py')

#Subtract operations
execfile ('gcalc-sub.py')

#Multiply operations
execfile ('gcalc-mul.py')

#Divide operations
execfile ('gcalc-div.py')

#Change mode
execfile ('gcalc-change-mode.py')

# Close gcalctool
selectmenuitem ('Calculator-Basic', 'mnuCalculator;mnuQuit')

