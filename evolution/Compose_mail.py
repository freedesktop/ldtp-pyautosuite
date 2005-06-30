#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bhargavi <kbhargavi_83@yahoo.co.in>
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

# To Compse a New Mail Message using args supplied by a text file

#To compose a mail
def compose_mail (mailid, subjecttxt, mailbodytxt, cc_id):
	try: 
		selectmenuitem('Evolution-Mail','mnuView;mnuWindow;mnuMail')
		wait(3)
	        selectmenuitem('Evolution-Mail','mnuFile;mnuNew;mnuMailMessage')
		log('OpenedComposemessageDialog','pass')
		selectmenuitem('frmComposeamessage', 'mnuView;mnuCcField')
        	settextvalue ('frmComposeamessage', 'txtTo', mailid)
		settextvalue ('frmComposeamessage', 'txtCc', cc_id)
        	settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
        	setcontext ('Compose a message',subjecttxt)
        	settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
        	click ('frmComposeamessage', 'btnSend')
		click('Evolution-Mail','btnSend/Receive')		
		log('ComposemessageSuccess','pass')
	except:
		print ' Compose messsage Failed'
		log('Compose-Mail-Failed','fail')

# Section to verify if mail is sent
def verify_compose_mail (mailid, subjecttxt,cc_id_verify):
	try:
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Sent')        
	        selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
		log('ComposedmessageOpened','pass')
		setcontext('Compose a message',subjecttxt)
        	verifytablecell ('frmReadOnlyMail', 'tblcheck', 1, 1, mailid)
		verifytablecell ('frmReadOnlyMail', 'tblcheck', 2, 1, cc_id_verify)
        	verifytablecell ('frmReadOnlyMail', 'tblcheck', 3, 1, subjecttxt)
		log('VerificationSuccess','pass')
        	selectmenuitem ('frmReadOnlyMail','mnuFile;mnuClose')
		log('Closemail','pass')
	except error:	
		print ' Verification of Sent mail Failed'
		log('Verification-of-mail-failed','fail')


#Trying to read from the file
file = open('send_mail.dat', 'r')
argmts = file.readlines()
To_emailid = argmts[1].strip( )
Subject_Mail = argmts[2].strip( )
Bodytxt_Mail = argmts[3].strip( )
Cc_mailid = argmts[5].strip( )
Cc_verify_mailid = argmts[6].strip( )
# Call the function

log('ComposeandVerificationofMail','teststart')
log('ComposeofMail' ,'teststart')
wait(3)
compose_mail (To_emailid, Subject_Mail, Bodytxt_Mail, Cc_mailid)
log('ComposeofMail' ,'testend')
wait(3)
log('VerificationofMail' ,'teststart')
wait(3)
verify_compose_mail (To_emailid, Subject_Mail,Cc_verify_mailid)
log('VerificationofMail' ,'testend')
log('ComposeandVerificationofMail','testend')
