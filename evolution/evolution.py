#!/usr/bin/python

from ldtp import *
import string, sys, os

appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./evolution-2.2.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/evolution-2.2.map')

#launchapp ('evolution-2.2')

setcontext ('Compose a message', 'test mail')
settextvalue ('Composeamessage', 'txtTo', 'nagappan@ldg.net')
settextvalue ('Composeamessage', 'txtSubject', '')
releasecontext ()
settextvalue ('Composeamessage', 'txtCc', 'nagappan@ldg.net')
