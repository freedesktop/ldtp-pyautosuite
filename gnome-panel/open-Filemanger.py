selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuFileManager')
wait(5)
if processrunning('nautilus')==1:
	closeappwindow('abdul')
else:
     log('process-not running')

