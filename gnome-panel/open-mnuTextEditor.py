selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuTextEditor')
wait(5)
if processrunning('gedit')==1:
	closeappwindow('gedit')
else:
    log('process not running')
