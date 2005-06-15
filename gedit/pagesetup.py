#To open pagesetup dialog
log ('Launch-PageSetup', 'teststart')
selectmenuitem ('gedit', 'mnuFile;mnuPageSetup');
click ('dlgPageSetup', 'btnClose')
selectmenuitem ('gedit', 'mnuFile;mnuCloseAll')
selectmenuitem ('gedit', 'mnuFile;mnuQuit')
log ('Launched Page Setup dialog successfully','pass')
log ('Launch-PageSetup','testend')
