# to do a search for any specified word/phrase in the currently opened document in gedit.
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit', 'mnuSearch;mnuFind')
 settextvalue('dlgFind','txtSearchfor', 'how')

 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 #search from cursor position
 selectmenuitem('gedit', 'mnuSearch;mnuFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how')
 
 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
#case sensitive
 selectmenuitem('gedit', 'mnuSearch;mnuFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how')
 #x=int(raw_input("enter choice:1)Search from the beginning of the document 2) Search from the cursor position")) #no such option available
  #if x==0:
  #if x==1:
 if uncheck('dlgFind', 'chkMatchcase') == 0:
  check('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 #using find icon
 click('gedit','btnFind')
 settextvalue('dlgFind','txtSearchfor', 'how')
 #no search from beginning option available
 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 click('gedit','btnFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how')
 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
# 8th testcase not done
 click('gedit','btnFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how')
 if uncheck('dlgFind', 'chkMatchcase') == 0:
  check('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnFind')
 selectmenuitem('gedit', 'mnuSearch;mnuFindNext')#no keyboard function defined
#searching for phrase
 selectmenuitem('gedit', 'mnuSearch;mnuFind')
 settextvalue('dlgFind','txtSearchfor', 'how are u')
 #no search from beginning option available
 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 #search from cursor position
 selectmenuitem('gedit', 'mnuSearch;mnuFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how are u')
 
 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
#case sensitive
 selectmenuitem('gedit', 'mnuSearch;mnuFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how are u')
 #x=int(raw_input("enter choice:1)Search from the beginning of the document 2) Search from the cursor position"))
  #if x==0:
  #if x==1:
 if uncheck('dlgFind', 'chkMatchcase') == 0:
  check('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 #using find icon
 click('gedit','btnFind')
 settextvalue('dlgFind','txtSearchfor', 'how are u')
 #no search from beginning option available
 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 click('gedit','btnFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how are u')
 if check('dlgFind', 'chkMatchcase') == 0:
  uncheck('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 click('gedit','btnFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how are u')
 if uncheck('dlgFind', 'chkMatchcase') == 0:
  check('dlgFind', 'chkMatchcase')
 click('dlgFind','btnFind')
 click('dlgFind','btnFind')
 selectmenuitem('gedit', 'mnuSearch;mnuFindNext')#no keyboard function defined
#finding using any options
 selectmenuitem('gedit', 'mnuSearch;mnuFind')
 settextvalue('dlgFind', 'txtSearchfor', 'how are u')
 x=int(raw_input("enter choice:1)match case 2) don't match case: "))
 if x == 1:
  if uncheck('dlgFind', 'chkMatchcase') == 0:
    check('dlgFind', 'chkMatchcase')
  else:
    pass
 elif x == 2:
  if check('dlgFind', 'chkMatchcase') == 0:
    uncheck('dlgFind', 'chkMatchcase')
  else:
    pass
 click('dlgFind','btnFind')
 click('dlgFind','btnClose')
 selectmenuitem('gedit','mnuFile;mnuClose')
 click('gedit','btnDon\'tsave') #ldtp error
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
except:
 print "17 error occured is:", sys.exc_info()[0]
 
