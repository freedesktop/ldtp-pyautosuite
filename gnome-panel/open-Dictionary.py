selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuDictionary')
wait(5)
if processrunning('gnome-dictionary -a')==1:
	closeappwindow('Dictionary')
else:
    log('process not running')


