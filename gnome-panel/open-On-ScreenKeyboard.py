selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuOn-ScreenKeyboard')
wait(5)
if processrunning('gok')==1:
	closeappwindow('gok')
else:
    log('process not running')
