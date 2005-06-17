# to save all the currently open and modified documents in gedit even if one of those documents is a new document (i.e. gedit will prompt the user for a file name for all the newly created documents that have been modified).
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 #click('dlgOpenFile','btnOpen')
 #selectrowindex('dlgOpenFile', 'tblFiles',8)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 settextvalue('gedit','txtgedit','how are u')
#opening 2nd existing file
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 #click('dlgOpenFile','btnOpen')
 selectrow('dlgOpenFile', 'tblFiles','sa.py')
 click('dlgOpenFile','btnOpen')
 
 settextvalue('gedit','txtgedit','how do u do')#text values are always stored in existing files no cursor positioning function
#opening new 2 files and modifying it
 selectmenuitem('gedit', 'mnuFile;mnuNew')
 settextvalue('gedit','txtgedit','I am fine')
 selectmenuitem('gedit','mnuFile;mnuNew')
 settextvalue('gedit','txtgedit','thank u')
#opening 2 new files
 selectmenuitem('gedit','mnuFile;mnuNew')
 selectmenuitem('gedit','mnuFile;mnuNew')
#saving all documents and closing it
 selectmenuitem('gedit','mnuDocuments;mnuSaveAll')
 click('dlgSaveas','tbtnBrowseforotherfolders')
 settextvalue('dlgSaveas','txtName','f1')
 click('dlgSaveas', 'btnSave')
 settextvalue('dlgSaveas','txtName','f2')
 click('dlgSaveas','tbtnBrowseforotherfolders')
 click('dlgSaveas','btnSave')
 
 settextvalue('dlgSaveas','txtName','f3')
 click('dlgSaveas','tbtnBrowseforotherfolders')
 click('dlgSaveas','btnSave')
 
 settextvalue('dlgSaveas','txtName','f4')
 click('dlgSaveas','tbtnBrowseforotherfolders')
 click('dlgSaveas','btnSave')
 selectmenuitem('gedit','mnuDocuments;mnuCloseAll')
#reopening all files
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrowindex('dlgOpenFile', 'tblShortcuts',0)
 selectrow('dlgOpenFile', 'tblFiles','sample.py')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrow('dlgOpenFile', 'tblFiles','sa.py')
 click('dlgOpenFile','btnOpen')
 
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrow('dlgOpenFile', 'tblFiles','f1')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrow('dlgOpenFile', 'tblFiles','f2')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrow('dlgOpenFile', 'tblFiles','f3')
 click('dlgOpenFile','btnOpen')
 selectmenuitem('gedit','mnuFile;mnuOpen')
 selectrow('dlgOpenFile', 'tblFiles','f4')
 click('dlgOpenFile','btnOpen')
#quitting
 selectmenuitem ('gedit','mnuFile;mnuQuit')
except:
 print "08 error occured is:", sys.exc_info()[0]
 

 
