#To open a new file
log ('Open-New-File', 'teststart')
selectmenuitem ('gedit', 'mnuFile;mnuClose')
selectmenuitem ('gedit', 'mnuFile;mnuNew')
selectmenuitem ('gedit', 'mnuFile;mnuClose')
log ('Pass', 'pass')
log ('Open-New-File', 'testend')
