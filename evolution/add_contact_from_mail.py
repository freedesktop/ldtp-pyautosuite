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

def add_contact (row_index):
	try:
		click ('Evolution-Mail', 'tbtnMail')
		wait (2)
		selectrowpartialmatch ('Evolution-Mail', 'treeTabFolder', 'Mailbox')
		selectrowindex ('Evolution-Mail', 'treetblMails', row_index)
		selectmenuitem ('Evolution-Mail', 'mnuActions;mnuAddSendertoAddressBook')
		wait(3)
		click ('dlgContactQuick-Add', 'btnOK')
		log ('Add-contact-from-mail', 'pass')
	except:
		log ('Add-contact-from-mail', 'fail')

def verify_add_contact (mail_id, contact):
	try:
		click ('Evolution-Mail', 'tbtnContacts')
		wait (3)
                selectrow ('Evolution-Contacts', 'treetblContacts', 'Personal')
                selectpanelname ('Evolution-Contacts', 'pnlAddbook', contact)
                selectmenuitem ('Evolution-Contacts', 'mnuFile;mnuOpen')
                wait (1)
	        verifysettext ('dlgContactEditor', 'txtWorkEmail', mail_id)
	        click ('dlgContactEditor', 'btnCancel')
	        log ('Verify-Add-contact-from-mail', 'pass')
        except:
		log ('Verify-Add-contact-from-mail', 'fail')
		
file = open('add_from_mail.dat', 'r')
argmts = file.readlines()
index = int (argmts[1].strip( ))
mail = argmts[2].strip( )
cont = argmts[3].strip()

log('AddandVerificationofAddContactFromMail','teststart')
log('AddContactfromMail' ,'teststart')
add_contact (index)
log('AddContactfromMail' ,'testend')
log('VerificationofAddContactfromMail' ,'teststart')
verify_add_contact (mail, cont)
log('VerificationofAddContactfromMail' ,'testend')
log('AddandVerificationofAddContactFromMail','testend')
