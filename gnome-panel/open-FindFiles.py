selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuFindFiles')
wait(5)
if processrunning('gnome-search-tool')==1:
	closeappwindow('Search for Files')
else:
    log('process not running')
