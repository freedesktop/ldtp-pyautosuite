#To perform edit operations
log ('Edit-File', 'teststart')
selectmenuitem ('gedit', 'mnuFile;mnuOpen')
selectrowindex ('dlgOpenFile', 'tblFiles' , 1)
click ('dlgOpenFile', 'btnOpen')
selectmenuitem ('gedit', 'mnuEdit;mnuSelectAll')
selectmenuitem ('gedit', 'mnuEdit;mnuCut')
selectmenuitem ('gedit', 'mnuEdit;mnuPaste')
selectmenuitem ('gedit', 'mnuFile;mnuSave')
log ('edit.py', 'pass')
log ('Edit-File', 'testend')
