selectmenuitem('TopPanel', 'mnuPrograms;mnuGames;mnuIagno')
wait(5)
if processrunning('iagno')==1:
	closeappwindow('Iagno')
else:
    log('process not running')
