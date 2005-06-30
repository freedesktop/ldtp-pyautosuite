#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Khasim Shaheed <sshaik@novell.com>
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

# Change the default draft folder and verify
import time

#Change the default draft folder
def change_draft (new_draft, index, account):
	try:
		selectmenuitem ('Evolution-Mail', 'mnuView;mnuWindow;mnuMail')
		time.sleep (3)
		selectmenuitem ('Evolution-Mail', 'mnuEdit;mnuPreferences')
		time.sleep (3)
		if guiexist ('dlgEvolutionSettings') == 1:
			selectrowindex ('dlgEvolutionSettings', 'tblAccounts', index)	
			click ('dlgEvolutionSettings', 'btnEdit')
			time.sleep (3)
			if guiexist ('dlgAccountEditor') == 1:
				selecttab ('dlgAccountEditor', 'ptlAccountEditor', '3')
				click ('dlgAccountEditor', 'btnDrafts')	
				time.sleep (3)
				if guiexist ('dlgSelectFolder') == 1:
					click ('dlgSelectFolder', 'btnNew')
					time.sleep (3)
					if guiexist ('dlgCreateNewFolder') == 1:
                				settextvalue('dlgCreateNewFolder', 'txtFoldername', new_draft)
                				selectrow ('dlgCreateNewFolder', 'treetblMailFolderTree', account)
                				click ('dlgCreateNewFolder', 'btnCreate')
					else:
						log ('Create New Folder dialog does not appear', 'error')
						log ('Change Draft Folder', 'fail')
                			selectrow ('dlgSelectFolder', 'treetblMailFolderTree', new_draft)
                			click ('dlgSelectFolder', 'btnOK')
				else:
					log ('Select Folder dialog does not appear', 'error')
                                        log ('Change Draft Folder', 'fail')
				click ('dlgAccountEditor', 'btnOK')
			else:
				log ('Account Editor dialog does not appear', 'error')
                                log ('Change Draft Folder', 'fail')
			click ('dlgEvolutionSettings', 'btnClose')
			log ('Change Draft Folder', 'pass')
		else:
			log ('Evolution Settings dialog does not appear', 'error')
                        log ('Change Draft Folder', 'fail')
	except error, msg:
		log (str (msg), 'error')
                log ('Change Draft Folder', 'fail')

#Verify whether draft folder has been changed or not
def verify_draft (new_draft, to_address, cc_address, msg_subject, msg_body):
	try:
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuMailMessage')
		if guiexist ('frmComposeamessage') == 1:
			settextvalue ('frmComposeamessage', 'txtTo', to_address) 
			if verifycheck ('frmComposeamessage', 'mnuView;mnuCcField') == 0:
				check ('frmComposeamessage', 'mnuView;mnuCcField')
			settextvalue ('frmComposeamessage', 'txtCc', cc_address) 
			settextvalue ('frmComposeamessage', 'txtSubject', msg_subject)
			setcontext ('Compose a message', msg_subject)
			settextvalue ('frmComposeamessage', 'txtMailBody', msg_body)
			selectmenuitem ('frmComposeamessage', 'mnuFile;mnuSaveDraft')
			selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
		else:
			log ('Compose a message dialog does not appear', 'error')
			log ('Verify Change draft', 'fail')
		selectrow ('Evolution-Mail', 'treeTabFolder', new_draft)
		selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
                setcontext('Compose a message', msg_subject)
		if guiexist ('frmReadOnlyMail') == 1:
                	verifytablecell ('frmReadOnlyMail', 'tblcheck', 1, 1, to_address)
	                verifytablecell ('frmReadOnlyMail', 'tblcheck', 2, 1, cc_address)
        	        verifytablecell ('frmReadOnlyMail', 'tblcheck', 3, 1, msg_subject)
                	selectmenuitem ('frmReadOnlyMail','mnuFile;mnuClose')
		else:
			log ('Selected message not opened', 'error')
			log ('Verify Change draft', 'fail')
		log ('Verify Change draft', 'pass')
	except msg, error:
		log (str (msg), 'error')
		log ('Verify Change draft', 'fail')

#Getting the data
file = open('change_draft.dat', 'r')
argmts = file.readlines()
index = int (argmts[1].strip( ))
account = argmts[2].strip( )
new_draft = argmts[3].strip( )
to_address = argmts[4].strip( )
cc_address = argmts[5].strip( )
msg_subject = argmts[6].strip( )
msg_body = argmts[7].strip( )


#Calling the functions
log ('Change and Verify Change Draft Folder', 'teststart')
log ('Change Draft Folder', 'teststart')
change_draft (new_draft, index, account)
log ('Change Draft Folder', 'testend')
log ('Verify Change Draft Folder', 'tesstart')
veriry_draft (new_draft, to_address, cc_address, msg_subject, msg_body)
log ('Verify Change Draft Folder', 'testend')
log ('Change and Verify Change Draft Folder', 'testend')
