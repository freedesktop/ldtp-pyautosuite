selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuCalendar')
wait(5)
if processrunning('evolution default:calendar')==1:
	closeappwindow('Evolution - Mail')
else:
    log('process not running')
