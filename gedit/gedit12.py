#to revert to a saved version of a currently opened document.
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 cuttext('gedit','txtgedit','1;3')
 pastetext('gedit','txtgedit',10)
 selectmenuitem('gedit','mnuFile;mnuRevert')
 click('gedit','btnRevert')#this is giving an ldtp error
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
except:
 print "12 error occured is:", sys.exc_info()[0]
