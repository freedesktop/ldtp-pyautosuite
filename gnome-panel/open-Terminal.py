selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuTerminal')
wait(5)
if processrunning('gnome-terminal')==1:
	closeappwindow('Terminal')
else:
    log('process not running')
