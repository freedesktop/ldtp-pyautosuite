#to replace any word/phrase in the currently opened document with another word/phrase in gedit.
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit', 'mnuSearch;mnuReplace')
 settextvalue('dlgReplace','txtReplacewith','why')
 settextvalue('dlgReplace','txtSearchfor','how')
#no search from beginning option available
 if check('dlgReplace', 'chkMatchcase') == 0:
  uncheck('dlgReplace', 'chkMatchcase')
 click('dlgReplace', 'btnFind')
 if False:
  click('gedit','btnOK')
 else:
  click('dlgReplace', 'btnReplace')
#case sensitive
 settextvalue('dlgReplace','txtReplacewith','why')
 #if verifysettext('dlgReplace', 'txtReplacewith','how') == 1:
  # print "it is already 'how'"
 settextvalue('dlgReplace','txtSearchfor','how')
#no search from beginning option available
 if uncheck('dlgReplace', 'chkMatchcase') == 0:
  check('dlgReplace', 'chkMatchcase')
 click('dlgReplace', 'btnFind')
 
 if False:
  click('gedit','btnOK')
 else:
  click('dlgReplace', 'btnReplace')
#no 7th testcase since same
 settextvalue('dlgReplace','txtReplacewith','why')
 if (settextvalue('dlgReplace','txtSearchfor','how')==1 and settextvalue('dlgReplace','txtSearchfor','how')==1):
#no search from beginning option available
  if check('dlgReplace', 'chkMatchcase') == 0:
   uncheck('dlgReplace', 'chkMatchcase')
  click('dlgReplace', 'btnFind')
  
  if False:
   click('gedit','btnOK')
  else:
   click('dlgReplace', 'btnReplace')
 else:
  print "text occurs more than twice"
#case sensitive
  settextvalue('dlgReplace','txtReplacewith','why')
 if (verifysettext('gedit','txtgedit','how')==1 and verifysettext('gedit','txtgedit','how')==1):
#no search from beginning option available
  if uncheck('dlgReplace', 'chkMatchcase') == 0:
   check('dlgReplace', 'chkMatchcase')
  click('dlgReplace', 'btnFind')
  
  if False:
   click('gedit','btnOK')
  else:
   click('dlgReplace', 'btnReplace')
 else:
  print "text occurs more than twice"
# using replace icon
 click('gedit','btnReplace')
 settextvalue('dlgReplace','txtReplacewith','why')
 settextvalue('dlgReplace','txtSearchfor','how')
#no search from beginning option available
 if check('dlgReplace', 'chkMatchcase') == 0:
  uncheck('dlgReplace', 'chkMatchcase')
 click('dlgReplace', 'btnFind')
 
 if False:
  click('gedit','btnOK')
 else:
  click('dlgReplace', 'btnReplace')
#case sensitive
 settextvalue('dlgReplace','txtReplacewith','why')
 #if verifysettext('dlgReplace', 'txtReplacewith','how') == 1:
  # print "it is already 'how'"
 settextvalue('dlgReplace','txtSearchfor','how')
#no search from beginning option available
 if uncheck('dlgReplace', 'chkMatchcase') == 0:
  check('dlgReplace', 'chkMatchcase')
 click('dlgReplace', 'btnFind')
 
 if False:
  click('gedit','btnOK')
 else:
  click('dlgReplace', 'btnReplace')

#no 7th testcase since same
 settextvalue('dlgReplace','txtReplacewith','why')
 if (verifysettext('gedit','txtgedit','how')==1 and verifysettext('gedit','txtgedit','how')==1):
#no search from beginning option available
  if check('dlgReplace', 'chkMatchcase') == 0:
   uncheck('dlgReplace', 'chkMatchcase')
  click('dlgReplace', 'btnFind')
  
  if False:
   click('gedit','btnOK')
  else:
   click('dlgReplace', 'btnReplace')
 else:
  print "text occurs more than twice"
#case sensitive
  settextvalue('dlgReplace','txtReplacewith','why')
 if (verifysettext('gedit','txtgedit','how')==1 and verifysettext('gedit','txtgedit','how')==1):
#no search from beginning option available
  if uncheck('dlgReplace', 'chkMatchcase') == 0:
   check('dlgReplace', 'chkMatchcase')
  click('dlgReplace', 'btnFind')
  
  if False:
   click('gedit','btnOK')
  else:
   click('dlgReplace', 'btnReplace')
 else:
  print "text occurs more than twice"
# no 10th testcase
 click('dlgReplace', 'btnClose')
 selectmenuitem('gedit','mnuFile;mnuClose')
 click('gedit','btnDon\'tsave')
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
except:
 print "18 error occured is:", sys.exc_info()[0]
 
