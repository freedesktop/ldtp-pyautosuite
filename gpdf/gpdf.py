#!/usr/bin/python

from ldtp import *
import string, sys, os
from ldtputils import *
appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./gpdf.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/gpdf.map')

launchapp ('gpdf')

# View About & Credits
execfile ('view-pdf-about.py')

# Open Existing File
execfile ('open-pdf-file.py')

# Zoom in the contents of the file
selectmenuitem ('PDFViewer', 'mnuView;mnuZoomIn')

# Zoom out the contents of the file
selectmenuitem ('PDFViewer', 'mnuView;mnuZoomOut')

# Best fit the contents of the file
selectmenuitem ('PDFViewer', 'mnuView;mnuBestFit')

# View the side bar
check ('PDFViewer', 'mnuSidebar')

# View the properties
execfile ('view-pdf-properties.py')

# Close gpdf
selectmenuitem ('PDFViewer', 'mnuFile;mnuClose')
