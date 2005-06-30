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

def edit_contact (panel, new_mail, mobile):
	try:
		click ('Evolution-Mail', 'tbtnContacts')
		wait (3)
                selectrow ('Evolution-Contacts', 'treetblContacts', 'Personal')
		selectpanelname ('Evolution-Contacts', 'pnlAddbook', panel)
		selectmenuitem ('Evolution-Contacts', 'mnuFile;mnuOpen')
		settextvalue ('dlgContactEditor', 'txtWorkEmail', new_mail)
		settextvalue ('dlgContactEditor', 'txtMobile', mobile)
		click ('dlgContactEditor', 'btnOK')
		wait (1)
		log ('Edit-contact', 'pass')
	except:
		log ('Edit-contact', 'fail')

def verify_edit_contact (panel, new_mail, mobile):
	try:
		selectpanelname ('Evolution-Contacts', 'pnlAddbook', panel)
                selectmenuitem ('Evolution-Contacts', 'mnuFile;mnuOpen')
                wait (1)
	        verifysettext ('dlgContactEditor', 'txtWorkEmail', new_mail)
	        verifysettext ('dlgContactEditor', 'txtMobile', mobile)
	        click ('dlgContactEditor', 'btnCancel')
	        log ('Verify-Edit-contact', 'pass')
	except:
		log ('Verify-Edit-contact', 'fail')
		
file = open('edit_contact.dat', 'r')
argmts = file.readlines()
panel = argmts[1].strip( )
new_mail = argmts[2].strip( )	                	                	
mobile = argmts[3].strip( )

log('EditandVerificationofEditContact','teststart')
log('EditContact' ,'teststart')
edit_contact (panel, new_mail, mobile)
log('EditContact' ,'testend')
log('VerificationofEditContact' ,'teststart')
verify_edit_contact (panel, new_mail, mobile)
log('VerificationofEditContact' ,'testend')
log('EditandVerificationofEditContact','testend')
