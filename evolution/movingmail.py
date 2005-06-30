#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Nagashree <mnagashree@novell.com>
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

#Viewing an existing Mail
from ldtp import *

# To Compse a New Mail Message using args supplied by a text file
def compose_mail (search_contact, select_contact, subjecttxt, mailbodytxt):
        selectmenuitem ('Evolution-mail', 'mnuFile;mnuNew;mnuMailMessage')
	settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
        settextvalue ('frmComposeamessage', 'txtTo', select_contact)
	settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
	setcontext ('Compose a message', subjecttxt)
	click ('frmComposeamessage', 'btnSend')


# Section to select and move received mail
def move_verify_mail (search_contact, select_contact, subjecttxt, mailbodytxt):
	selectrowpartialmatch ('Evolution-mail', 'treeTabFolder', 'Inbox')
	row_before = getrowcount('Evolution-mail', 'treetblMails') 
	selectrowpartialmatch ('Evolution-mail', 'treeTabFolder', 'Mailbox')
	rowcount = getrowcount('Evolution-mail', 'treetblMails') 
	if rowcount > 0:
	        selectlastrow ('Evolution-mail', 'treetblMails')
		selectmenuitem ('Evolution-mail', 'mnuActions;mnuMoveToFolder')
		selectrowpartialmatch ('dlgSelectfolder', 'foldertable', 'Inbox')
		click ('dlgSelectfolder','btnMove')
		selectrowpartialmatch ('Evolution-mail', 'treeTabFolder', 'Inbox')
	        selectlastrow ('Evolution-mail', 'treetblMails')
		selectmenuitem ('Evolution-mail', 'mnuFile;mnuOpenMessage')
		setcontext ('Compose a message', subjecttxt)
		if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 2, 1, subjecttxt) == 1:
			if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 1, 1, toid) == 1:
				log ('Verification successful', 'info')
		else:
			log ('Verification Failed', 'info')
		selectmenuitem ('Evolution-mail', 'mnuFile;mnuExit')
		
# Trying to read from the file
file = open('send_mail.dat', 'r')
argmts = file.readlines()
search_contact = argmts[0].strip( )
select_contact = argmts[1].strip( )
subjecttxt = argmts[2].strip( )
mailbodytxt = argmts[3].strip( )
toid = search_contact + ' <' + select_contact + '>'

# Call the function
try:
	 
	log ('movingmail', 'teststart')	
	compose_mail (search_contact, select_contact, subjecttxt, mailbodytxt)
	move_verify_mail (search_contact, select_contact, subjecttxt, mailbodytxt)
	log ('Moving mail passed', 'pass')
	log ('movingmail', 'testend')
except error:
	log ('Moving mail failed', 'fail') 
                                                                           
