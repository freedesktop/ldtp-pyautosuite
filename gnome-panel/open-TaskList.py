selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuTaskList')
wait(5)
if processrunning('evolution default:tasks')==1:
	closeappwindow('Evolution - Mail')
else:
    log('process not running')
