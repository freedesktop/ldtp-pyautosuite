

i = doesmenuitemexist('mozilla','mnuFile;mnuCloseTab')

while (i == 1):
	selectmenuitem('mozilla', 'mnuFile;mnuCloseTab')
	i= doesmenuitemexist('mozilla','mnuFile;mnuCloseTab')
        print i
selectmenuitem('mozilla','mnuFile;mnuQuit')
