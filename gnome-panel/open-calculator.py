selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuCalculator')
wait(5)
if processrunning('gnome-calculator')==1:
	closeappwindow('Calculator - Basic Mode')
else:
    log('process not running')




