selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuTerminalServerClient')
wait(5)
if processrunning('tsclient')==1:
	closeappwindow('tsclient')
else:
    log('process not running')
