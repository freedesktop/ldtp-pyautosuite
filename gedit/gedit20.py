#to view installed & uninstalled plugins in gedit.
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit', 'mnuEdit;mnuPreferences')
 #if selecttab('dlgPreferences','ptlPreferences','4')== 1:
 selecttab('dlgPreferences','ptlPreferences','4')
 click('dlgPreferences','btnClose')
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
except:
 print "20 error occured is:", sys.exc_info()[0]
