# to copy and paste text in gedit.
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 selectmenuitem('gedit', 'mnuEdit;mnuCopy')
 selectmenuitem('gedit', 'mnuFile;mnuNew')
 selectmenuitem('gedit', 'mnuEdit;mnuPaste')
#using icons
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 click('gedit', 'btnCopy')
 selectmenuitem('gedit', 'mnuFile;mnuNew')
 click('gedit', 'btnPaste')

 #copying at the end of the document
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 selectmenuitem('gedit', 'mnuEdit;mnuCopy')
  #no particular cursor positioning function ..go to line option
 selectmenuitem( 'gedit', 'mnuSearch;mnuGotoLine')
 settextvalue('dlgGotoLine','txtLinenumber','5')
 click('dlgGotoLine','btnGotoLine')
 click('dlgGotoLine','btnClose')
 selectmenuitem('gedit', 'mnuEdit;mnuPaste')
  
#using icons
 selectmenuitem('gedit', 'mnuEdit;mnuSelectAll')
 click('gedit', 'btnCopy')
 selectmenuitem( 'gedit', 'mnuSearch;mnuGotoLine')
 settextvalue('dlgGotoLine','txtLinenumber','10')
 click('dlgGotoLine','btnGotoLine')
 click('dlgGotoLine','btnClose')
 click('gedit', 'btnPaste')
  
 selectmenuitem('gedit','mnuFile;mnuClose')
 click('gedit','btnDon\'tsave') #not clicked
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
 click('gedit','btnDon\'tsave')
except:
 print "15 error occured is:", sys.exc_info()[0]


 
