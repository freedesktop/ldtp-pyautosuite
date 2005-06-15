#!/usr/bin/python
from ldtp import *
import string, sys, os
from ldtputils import *
appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./gnome-font-properties.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/gnome-font-properties.map')

launchapp ('gnome-font-properties')
click('dlgFontPreferences','btnApplicationfont')
selectrowindex('dlgPickaFont','tblFamily',5)
selectrowindex('dlgPickaFont','tblStyle',3)
selectrowindex('dlgPickaFont','tblSize',5)
click('dlgPickaFont','btnOK')

