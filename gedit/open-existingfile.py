#Open existing file
selectmenuitem ('gedit', 'mnuFile;mnuClose')
selectmenuitem ('gedit', 'mnuFile;mnuOpen')

# Open existing file using file index
selectrowindex ('dlgOpenFile', 'tblFiles' , 1)
click ('dlgOpenFile', 'btnOpen')
selectmenuitem ('gedit', 'mnuDocuments;mnuCloseAll')

# Open existing file
selectmenuitem ('gedit', 'mnuFile;mnuNew')
selectmenuitem ('gedit', 'mnuFile;mnuOpen')
try:
    # Open existing file using file name
    selectrow ('dlgOpenFile', 'tblFiles','readme')
    click ('dlgOpenFile', 'btnOpen')
except error:
    print 'Failed to select specified filename'
    click ('dlgOpenFile', 'btnCancel')
selectmenuitem ('gedit', 'mnuDocument;mnuCloseAll')
