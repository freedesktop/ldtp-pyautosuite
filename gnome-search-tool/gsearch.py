#!/usr/bin/python
                                                           
from ldtp import *
import string, sys, os
                                                           
appmap_path = ''
                                                           
if len (sys.argv) == 1:
  if os.access ('./gnome-search-tool.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]
                                                           
initappmap (appmap_path + '/gnome-search-tool.map')
                                                           
launchapp ('gnome-search-tool')

execfile('simplesearch.py')

launchapp ('gnome-search-tool')
execfile('pathsetting.py')

launchapp ('gnome-search-tool')

execfile('browsefiles.py')

launchapp('gnome-search-tool')
execfile('showmoreoptions.py')
