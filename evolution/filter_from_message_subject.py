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

#Create and Verify Filter from Message on Subject
import string, time

#Create Filter
def create_filter (index, filter_name, folder_name, account_name):
	try:
		click ('Evolution-Mail', 'tbtnMail')
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Mailbox')
		selectrowindex ('Evolution-Mail', 'treetblMails', index)
		selectmenuitem ('Evolution-Mail', 'mnuTools;mnuCreateFilterFromMessage;mnuFilteronSubject')
		settextvalue('dlgAddFilterRule', 'txtRuleName', filter_name)
		click ('dlgAddFilterRule', 'btn<clickheretoselectafolder>')
		click ('dlgSelectFolder', 'btnNew')
		settextvalue('dlgCreateNewFolder', 'txtFoldername', folder_name)
		selectrow ('dlgCreateNewFolder', 'treetblMailFolderTree', account_name)
		click ('dlgCreateNewFolder', 'btnCreate')
		selectrow ('dlgSelectFolder', 'treetblMailFolderTree', folder_name)
		click ('dlgSelectFolder', 'btnOK')
		click ('dlgAddFilterRule', 'btnOK')
		log ('Create Filter from Message on Subject', 'pass')
	except:
		log ('Create Filter from Message on Subject', 'fail')

#Verify Filter
def verify_filter (index, folder_name):
	try:
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Mailbox')
		filter_mail_count = 0
		subject = getcellvalue ('Evolution-Mail', 'treetblMails', index, 4)
		total_mail_count = getrowcount ('Evolution-Mail', 'treetblMails')
		for i in range (0, total_mail_count):
			temp_subject = getcellvalue ('Evolution-Mail', 'treetblMails', i, 4)
			if (string.find (temp_subject, subject) >= 0):
				filter_mail_count = filter_mail_count + 1
		selectmenuitem ('Evolution-Mail', 'mnuEdit;mnuSelectAll')
		selectmenuitem ('Evolution-Mail', 'mnuActions;mnuApplyFilters')
		time.sleep (2)
		selectrow ('Evolution-Mail', 'treeTabFolder', folder_name)
		time.sleep (2)
		folder_mail_count = getrowcount ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuTools;mnuFilters')
		selectrowindex ('dlgFilters', 'tblFilterRules', 0)
		click ('dlgFilters', 'btnRemove')
		click ('dlgFilters', 'btnOK')
		if (filter_mail_count == folder_mail_count):
			log ('Verify Filter from Message Subject', 'pass')
		else:
			log ('Verify Filter from Message Subject', 'fail')
	except:
		log ('Verify Filter from Message Subject', 'fail')

#Getting the data from a file				
file = open('filter_message_on_subject.dat', 'r')
argmts = file.readlines()
index = int (argmts[1].strip( ))
account_name = argmts[2].strip( )
filter_name = argmts[3].strip( )
folder_name = argmts[4].strip( )

#Calling the functions
log ('Create and Verify Filter from Message on Subject', 'teststart')
log ('Create Filter from Message on Subject', 'teststart')
create_filter(index, filter_name, folder_name, account_name)
log ('Create Filter from Message on Subject', 'testend')
log ('Verify Filter from Message on Subject', 'teststart')
verify_filter (index, folder_name)
log ('Verify Filter from Message on Subject', 'testend')
log ('Create and Verify Filter from Message on Subject', 'testend')

