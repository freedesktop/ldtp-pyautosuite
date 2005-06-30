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

def delete_contact (panel):
	try:
		click ('Evolution-Mail', 'tbtnContacts')
		wait (3)
		selectrow ('Evolution-Contacts', 'treetblContacts', 'Personal')
                selectpanelname ('Evolution-Contacts', 'pnlAddbook', panel)
                selectmenuitem ('Evolution-Contacts', 'mnuEdit;mnuDelete')
                click ('altQuestion', 'btnDelete')
		log ('Delete-Contact', 'pass')
	except:
		log ('Delete-Contact', 'fail')

def verify_delete_contact (panel):
	try:
		selectpanelname ('Evolution-Contacts', 'pnlAddbook', panel)
		log ('Verify-Delete-contact', 'fail')
        except:
		log ('Verify-Delete-contact', 'pass')
		
file = open('delete_contact.dat', 'r')
argmts = file.readlines()
panel = argmts[1].strip( )

log('DeleteandVerificationofDeleteContact','teststart')
log('DeleteContact' ,'teststart')
delete_contact (panel)
log('DeleteContact' ,'testend')
log('VerificationofDeleteContact' ,'teststart')
verify_delete_contact (panel)
log('VerificationofDeleteContact' ,'testend')
log('DeleteandVerificationofDeleteContact','testend')
