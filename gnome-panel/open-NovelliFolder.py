selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuNovelliFolder')
wait(5)
if processrunning('/opt/novell/ifolder/bin/novell-ifolder-client')==1:
	closeappwindow('/opt/novell/ifolder/bin/novell-ifolder-client')
else:
    log('process not running')
