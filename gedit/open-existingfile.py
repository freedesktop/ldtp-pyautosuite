#Open existing file
log ('Open-Existing-File', 'teststart')
#selectmenuitem ('gedit', 'mnuFile;mnuClose')
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
    log ('Passed opening specified file', 'pass')
except error:
    print 'Failed to select specified filename'
    click ('dlgOpenFile', 'btnCancel')
    log ('Failed to select specified filename', 'fail')
selectmenuitem ('gedit', 'mnuDocument;mnuCloseAll')
log ('Open-Existing-File','testend')
