#!/usr/bin/python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Khasim Shaheed <khasim.shaheed@gmail.com>
#
#  Copyright 2004 Novell, Inc.
#
#  This test script is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Library General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Library General Public License for more details.
#
#  You should have received a copy of the GNU Library General Public
#  License along with this library; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#

from ldtp import *
from ldtputils import *

def change_style (type, style):
	try:
		if type == 'Forward':
			component = 'cboForwardstyle'
		else:
			style = style + ' original message'
			component = 'cboQuoteoriginalmessage'
	
		selectmenuitem ('frmEvolution-*', 'mnuEdit;mnuPreferences')
		time.sleep (3)
		if waittillguiexist ('dlgEvolutionPreferences') == 0:
			log ('Evolution Settings dialog not opened', 'error')
			raise LdtpExecutionError (0)
	
		selecttab ('dlgEvolutionPreferences', 'ptl0', 'Composer Preferences')	
		selecttab ('dlgEvolutionPreferences', 'ptl2', 'General')
		comboselect ('dlgEvolutionPreferences', component, style)
		click ('dlgEvolutionPreferences', 'btnClose')
		if waittillguinotexist ('dlgEvolutionPreferences') == 0:
			log ('Evolution Settings dialog not closed', 'error')
			raise LdtpExecutionError (0)
	except ldtp.error, msg:
		log ('Changing ' + type + ' failed', 'cause')
		raise LdtpExecutionError (0)

# To Change default Sent Items folder
def change_sentfolder (accountname, folder):
	try:
		selectmenuitem ('frmEvolution-*', 'mnuEdit;mnuPreferences')
		if waittillguiexist ('dlgEvolutionPreferences') == 0:
			log ('Evolution Settings dialog not opened', 'error')
			raise LdtpExecutionError (0)
		time.sleep (3)
		selecttab ('dlgEvolutionPreferences', 'ptl0', 'Mail Accounts')
		time.sleep (2)
		selectrowpartialmatch ('dlgEvolutionPreferences', 'tblMailAccounts', accountname)
		click ('dlgEvolutionPreferences', 'btnEdit')
                time.sleep (2)
		if waittillguiexist ('dlgAccountEditor') == 0:
			log ('Account Editor dialog not opened', 'error')
			raise LdtpExecutionError (0)
		time.sleep (3)
		selecttab ('dlgAccountEditor', 'ptl0', 'Defaults')
		click ('dlgAccountEditor', 'btnSentMessagesFolder')
		if waittillguiexist ('dlgSelectFolder') == 0:
			log ('Select folder dialog not opened', 'error')
			raise LdtpExecutionError (0)
		selectrowpartialmatch ('dlgSelectFolder', 'ttblMailFolderTree', folder)
		time.sleep (1)
		click ('dlgSelectFolder', 'btnOK')
		if waittillguinotexist ('dlgSelectFolder') == 0:
			log ('Select folder dialog not closed', 'error')
			raise LdtpExecutionError (0)
		click ('dlgAccountEditor', 'btnOK')
		if waittillguinotexist ('dlgAccountEditor') == 0:
			log ('Account Editor dialog not closed', 'error')
			raise LdtpExecutionError (0)
		click ('dlgEvolutionPreferences', 'btnClose')
		if waittillguinotexist ('dlgEvolutionPreferences') == 0:
			log ('Evolution Settings dialog not closed', 'error')
			raise LdtpExecutionError (0)
	except ldtp.error, msg:
		log ('Could not able to change sent items folder ' + str (msg), 'error')
		if guiexist ('dlgSelectFolder'):
			click ('dlgSelectFolder', 'btnCancel')
		if guiexist ('dlgAccountEditor'):
			click ('dlgAccountEditor', 'btnCancel')
		if guiexist ('dlgEvolutionPreferences'):
			click ('dlgEvolutionPreferences', 'btnClose')
		time.sleep (3)
		raise LdtpExecutionError (0)

