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

# Save a mail as draft and verify
import time

# Save a message as draft
def save_draft (to_address, cc_address, msg_subject, msg_body):
	try:
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuMailMessage')
		time.sleep (1)
	        check ('frmComposeamessage', 'mnuCcField')
		settextvalue ('frmComposeamessage', 'txtTo', to_address)
		settextvalue ('frmComposeamessage', 'txtCc', cc_address)
		settextvalue ('frmComposeamessage', 'txtSubject', msg_subject)
		setcontext ('Compose a message', msg_subject)
		settextvalue ('frmComposeamessage', 'txtMailBody', msg_body)
		selectmenuitem ('frmComposeamessage', 'mnuFile;mnuSave')
		selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
		log ('Saving a draft', 'pass')
	except:
		log ('Saving a draft', 'fail')			

#Verify saved draft
def verify_draft (draft_folder, to_address, cc_address, msg_subject, msg_body):
	try:
		selectrow ('Evolution-Mail', 'treeTabFolder', draft_folder)
		time.sleep (3)
		selectlastrow ('Evolution-Mail', 'treetblMails')
                selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
                setcontext('Compose a message', msg_subject)
                verifysettext ('frmComposeamessage', 'txtTo', to_address)
                verifysettext ('frmComposeamessage', 'txtCc', cc_address)
                verifysettext ('frmComposeamessage', 'txtSubject', msg_subject)
                selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
                log ('Verify saved draft', 'pass')
        except:
                log ('Verify saved draft', 'fail')

#Getting the data
file = open('save_draft.dat', 'r')
argmts = file.readlines()
draft_folder = argmts[1].strip( )
to_address = argmts[2].strip( )
cc_address = argmts[3].strip( )
msg_subject = argmts[4].strip( )
msg_body = argmts[5].strip( )


#Calling the functions
log ('Save and Verify saved draft', 'teststart')
log ('Save a message as draft', 'teststart')
save_draft (to_address, cc_address, msg_subject, msg_body)
log ('Save a message as draft', 'testend')
log ('Verify saved draft', 'tesstart')
verify_draft (draft_folder, to_address, cc_address, msg_subject, msg_body)
log ('Verify saved draft', 'testend')
log ('Change and Verify saved draft', 'testend')

