#To perform edit operations
selectmenuitem ('gedit', 'mnuFile;mnuOpen')
selectrowindex ('dlgOpenFile', 'tblFiles' , 1)
click ('dlgOpenFile', 'btnOpen')
selectmenuitem ('gedit', 'mnuEdit;mnuSelectAll')
selectmenuitem ('gedit', 'mnuEdit;mnuCut')
selectmenuitem ('gedit', 'mnuEdit;mnuPaste')
