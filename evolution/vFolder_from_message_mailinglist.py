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

#Create and Verify vFolder from Message on MailingList
import string, import

#Create vFolder
def create_vFolder (index, vFolder_name):
	try:
		click ('Evolution-Mail', 'tbtnMail')
		time.sleep (2)
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Mailbox')
		selectrowindex ('Evolution-Mail', 'treetblMails', index)
		selectmenuitem ('Evolution-Mail', 'mnuTools;mnuCreatevFolderFromMessage;mnuvFolderonMailingList')
		settextvalue('dlgNewvFolder', 'txtRuleName', vFolder_name)
		click ('dlgNewvFolder', 'btnOK')
		log ('Create vFolder from Message on MailingList', 'pass')
	except:
		log ('Create vFolder from Message on MailingList', 'fail')

#Verify vFolder
def verify_vFolder (index, folder_name):
	try:
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Mailbox')
		vFolder_mail_count = 0
		mailinglist = getcellvalue ('Evolution-Mail', 'treetblMails', index, 3)
		total_mail_count = getrowcount ('Evolution-Mail', 'treetblMails')
		for i in range (0, total_mail_count):
			temp_mailinglist = getcellvalue ('Evolution-Mail', 'treetblMails', i, 3)
			if (string.find (temp_mailinglist, mailinglist) >= 0):
				vFolder_mail_count = vFolder_mail_count + 1
		selectrow ('Evolution-Mail', 'treeTabFolder', folder_name)
		time.sleep (2)
		folder_mail_count = getrowcount ('Evolution-Mail', 'treetblMails')
		if (vFolder_mail_count == folder_mail_count):
			log ('Verify vFolder from Message MailingList', 'pass')
		else:
			log ('Verify vFolder from Message MailingList', 'fail')
	except:
		log ('Verify vFolder from Message MailingList', 'fail')

#Getting the data from a file				
file = open('vFolder_message_on_mailinglist.dat', 'r')
argmts = file.readlines()
index = int (argmts[1].strip( ))
vFolder_name = argmts[2].strip( )

#Calling the functions
log ('Create and Verify vFolder from Message on MailingList', 'teststart')
log ('Create vFolder from Message on MailingList', 'teststart')
create_vFolder(index, vFolder_name)
log ('Create vFolder from Message on MailingList', 'testend')
log ('Verify vFolder from Message on MailingList', 'teststart')
verify_vFolder (index, vFolder_name)
log ('Verify vFolder from Message on MailingList', 'testend')
log ('Create and Verify vFolder from Message on MailingList', 'testend')

