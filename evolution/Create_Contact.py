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

def create_contact (name, mail_id):
	try:
		click ('Evolution-Mail', 'tbtnMail')
		wait (3)
                selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuContact')
		wait (1)
		settextvalue ('dlgContactEditor', 'txtFullName', name)
		setcontext ('Contact Editor', name)
		settextvalue ('dlgContactEditor', 'txtWorkEmail', mail_id)
		click ('dlgContactEditor','btnOK')
		wait (1)
		log ('Create-Contact', 'pass')
	except:
		log ('Create-Contact', 'fail')

def verify_create_contact (panel, name, mail_id):
	try:
		click ('Evolution-Mail', 'tbtnContacts')
		wait (3)
                selectrow ('Evolution-Contacts', 'treetblContacts', 'Personal')
		selectpanelname ('Evolution-Contacts', 'pnlAddbook', panel)
                selectmenuitem ('Evolution-Contacts', 'mnuFile;mnuOpen')
                wait (1)
	        verifysettext ('dlgContactEditor', 'txtFullName', name)
	        verifysettext ('dlgContactEditor', 'txtWorkEmail', mail_id)
	        click ('dlgContactEditor', 'btnCancel')
		wait (1)
	        log ('Verify-Create-contact', 'pass')
	except:
		log ('Verify-Create-contact', 'fail')
		
file = open('create_contact.dat', 'r')
argmts = file.readlines()
name = argmts[1].strip( )
mail_id = argmts[2].strip( )	                	                	
panel = argmts[3].strip( )

log('CreateandVerificationofCreateContact','teststart')
log('CreateContact' ,'teststart')
create_contact (name, mail_id)
log('CreateContact' ,'testend')
log('VerificationofCreateContact' ,'teststart')
verify_create_contact (panel, name, mail_id)
log('VerificationofCreateContact' ,'testend')
log('CreateandVerificationofCreateContact','testend')
