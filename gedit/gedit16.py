# to cut and paste text in gedit
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 selectmenuitem('gedit', 'mnuEdit;mnuCut')
 selectmenuitem('gedit', 'mnuFile;mnuNew')
 selectmenuitem('gedit', 'mnuEdit;mnuPaste')
#using icons
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 click('gedit', 'btnCut')
 selectmenuitem('gedit', 'mnuFile;mnuNew')
 click('gedit','btnPaste')

 #copying at the end of the document
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 selectmenuitem('gedit', 'mnuEdit;mnuCut')
 while settextvalue('gedit','txtgedit',' '):
  selectmenuitem('gedit', 'mnuEdit;mnuPaste')
  break
#using icons
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 click('gedit', 'btnCut')
 while settextvalue('gedit','txtgedit',' '):
  click('gedit', 'btnPaste')
  break
 selectmenuitem('gedit','mnuFile;mnuClose')
 click('gedit','btnDon\'tsave')#not clicked
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
 click('gedit','btnDon\'tsave')
except:
 print "16 error occured is:", sys.exc_info()[0]

