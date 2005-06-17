#to view information about any currently available(installed or uninstalled ) plugins in gedit .
launchapp ('gedit')
import sys
try:
 selectmenuitem('gedit', 'mnuEdit;mnuPreferences')
 selecttab('dlgPreferences','ptlPreferences','4')
 click('dlgPreferences','btnAboutPlugin')
 click('dlgAboutDocumentStatistics','btnCredits')
 click('dlgCredits','btnClose')
 click('dlgAboutDocumentStatistics','btnClose')# btnclose is not clicked or not working
 selectrowindex('dlgPreferences','tblplugins',3)#cell is not choosed
 click('dlgPreferences','btnAboutPlugin')
 click('dlgAboutDocumentStatistics','btnCredits')
 click('dlgCredits','btnClose') #this is not closed i.e 2nd time
 click('dlgAboutDocumentStatistics','btnClose')# btnclose is not clicked or not working
 click('dlgPreferences','btnClose')
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
except:
 print "21 error occured is:", sys.exc_info()[0]
