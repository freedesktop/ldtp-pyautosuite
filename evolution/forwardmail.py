
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


#Forwarding an existing Mail

# To Compse a New Mail Message using args supplied by a text file
def compose_mail (search_contact, select_contact, subjecttxt, mailbodytxt):
	selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuMailMessage')
	if guiexist ('frmComposeamessage') == 1:
		settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
        	settextvalue ('frmComposeamessage', 'txtTo', select_contact)
		settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
		setcontext ('Compose a message', subjecttxt)
		click ('frmComposeamessage', 'btnSend')
		click('Evolution-Mail','btnSend/Receive')
		log('compose mail','pass')
	else:
		log('compose mail window does not appear','error')
		log('compose mail','fail')	

# Section to forward mail as attachment
def forward_mail_attachment (search_contact, select_contact, mailbodytxt, fwdsubjecttxt, subjecttxt):
	selectrowpartialmatch ('Evolution-Mail', 'trtblMailFolderTree', 'Mailbox')
	rowcount = getrowcount('Evolution-Mail', 'treetblMails') 
	if rowcount > 0:
	        selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuActions;mnuForwardAs...;mnuAttached')
		#Wait for 3 seconds
    		time.sleep (3)
		if guiexist ('frmComposeamessage') == 1:
			setcontext ('Compose a message', fwdsubjecttxt)
			settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
	        	settextvalue ('frmComposeamessage', 'txtTo', select_contact)
			click ('frmComposeamessage', 'btnSend')
			click('Evolution-Mail','btnSend/Receive')
			log('forwarding mail with attachment','pass')

		else:
			log('compose mail window does not appear','error')
			log('forwarding mail with attachment','fail')

def forward_mail_inline (search_contact, select_contact, mailbodytxt, fwdsubjecttxt, subjecttxt):
	selectrowpartialmatch ('Evolution-Mail', 'trtblMailFolderTree', 'Mailbox')
	rowcount = getrowcount('Evolution-Mail', 'treetblMails') 
	if rowcount > 0:
	        selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuActions;mnuForwardAs...;mnuInline')
		# Wait for 3 seconds
    		time.sleep (3)
		if guiexist ('frmComposeamessage') == 1:
			setcontext ('Compose a message', fwdsubjecttxt)
			settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
	        	settextvalue ('frmComposeamessage', 'txtTo', select_contact)
			click ('frmComposeamessage', 'btnSend')
			click('Evolution-Mail','btnSend/Receive')
			log('forwarding mail inline','pass')

		else:
			log('compose mail window does not appear','error')
			log('forwarding mail inline','fail')


# Section to verify if the mail is sent,
#TODO Verification for attachement is pending (will complete once bhargavi has implemented a component
def verify_forward_attachment (select_contact, fwdsubjecttxt):
	log ('Verifying forwarding mail as attachment','info')
	selectrow ('Evolution-Mail', 'trtblMailFolderTree', 'Sent')        
	# Wait for 3 seconds
    		time.sleep (3)

        selectlastrow ('Evolution-Mail', 'treetblMails')
	selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
	if guiexist ('frmComposeamessage') == 1:
		setcontext ('Compose a message', fwdsubjecttxt)
		if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 2, 1, fwdsubjecttxt) == 1:
			if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 1, 1, toid) == 1:
				if verifypartialtablecell ('frmReadOnlyMail', 'tblattach', 0, 3, subjecttxt):
					log ('Verification successful', 'info')
				else:
					log ('Verification Failed', 'info')
		selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
	else:
		log('compose mail window does not appear','fail')
		log ('Verification of compose mail', 'fail')

def verify_forward_inline (select_contact, fwdsubjecttxt):
	log ('Verifying forwarding mail Inline','info')
	selectrow ('Evolution-Mail', 'trtblMailFolderTree', 'Sent')
       # Wait for 3 seconds
    	time.sleep (3)
	 selectlastrow ('Evolution-Mail', 'treetblMails')
	selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
	if guiexist ('frmComposeamessage') == 1:
		setcontext ('Compose a message', fwdsubjecttxt)
		if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 2, 1, fwdsubjecttxt) == 1:
			if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 1, 1, toid) == 1:
				log ('Verification successful', 'info')
			else:
				log ('Verification Failed', 'info')
		#selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
	else:
		log('compose mail window does not appear','fail')
		log ('Verification of forwarding mail', 'fail')


#trying to read from the file
file = open('send_mail.dat', 'r')
argmts = file.readlines()
search_contact = argmts[0].strip( )
select_contact = argmts[1].strip( )
subjecttxt = argmts[2].strip( )
mailbodytxt = argmts[3].strip( )
fwdsubjecttxt = '[Fwd: ' + subjecttxt + ']'
toid = select_contact



# Call the function
try:

	log ('forward_mail_attachment', 'teststart')	
	compose_mail (search_contact, select_contact, subjecttxt, mailbodytxt)
	forward_mail_attachment (search_contact, select_contact, mailbodytxt, fwdsubjecttxt, subjecttxt)
	verify_forward_attachment (select_contact, fwdsubjecttxt)
	log ('Forwarding mail as attachment was successful', 'pass')
	log ('forward_mail_attachment', 'testend')
	log ('forward_mail_inline', 'teststart')	
	compose_mail (search_contact, select_contact, subjecttxt, mailbodytxt)
	forward_mail_inline (search_contact, select_contact, mailbodytxt, fwdsubjecttxt, subjecttxt)
	verify_forward_inline (select_contact, fwdsubjecttxt)
	selectmenuitem ('Evolution-Mail', 'mnuFile;mnuExit')
	log ('Forwarding mail inline was successful', 'pass')
	log ('forward_mail_inline', 'testend')
except error, msg:
    log (str (msg), 'error')
	log ('mail composing and forwarding', 'fail') 
                                                                           
