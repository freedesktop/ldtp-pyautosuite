selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuScreenReaderandMagnifier')
wait(5)
if processrunning('gnopernicus')==1:
        closeappwindow('Gnopernicus')
else:
    log('process not running')

















