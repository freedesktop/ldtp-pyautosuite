selectmenuitem('TopPanel', 'mnuAccessories;mnuUnicodeCharacterMap')
wait(5)
if processrunning('gucharmap')==1:
	closeappwindow('gucharmap')
else:
    log('process not running')
