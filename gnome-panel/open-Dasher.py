selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuDasher')
wait(5)
if processrunning('dasher')==1:
	closeappwindow('dasher')
else:
    log('process not running')

