#!/usr/bin/python

from ldtp import *
import string, sys, os

appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./gnome-dictionary.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/gnome-dictionary.map')

launchapp ('gnome-dictionary')

#To search for a word
settextvalue ('gnomedictionary', 'txtWordEntry', 'python')
click ('gnomedictionary','btnLookUpWord')
wait (5)
selectmenuitem('gnomedictionary','mnuDictionary;mnuPrint')
click ('dlgPrintWordDefinition','btnCancel')
selectmenuitem('gnomedictionary','mnuEdit;mnuPreferences')
selecttab('dlgDictionaryPreferences','ptlDictionary Preferences','1')
click('dlgDictionaryPreferences','btnClose')
selectmenuitem ('gnomeDictionary', 'mnuDictionary;mnuClose')



