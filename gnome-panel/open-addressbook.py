selectmenuitem('TopPanel', 'mnuPrograms;mnuAccessories;mnuAddressBook')
wait(5)
if processrunning('evolution default:contacts')==1:
	closeappwindow('Evolution - Mail')
else:
    log('process not running')

