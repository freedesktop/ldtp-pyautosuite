#to highlight the contents of the currently opened document.
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 #ctrl-A is not implemented
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
except:
 print "14 error occured is:", sys.exc_info()[0]
