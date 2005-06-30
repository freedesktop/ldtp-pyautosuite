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

def compose_mail_with_attachment (mailid, subjecttxt, mailbodytxt, attachment_file):
	try: 
		selectmenuitem('Evolution-Mail','mnuView;mnuWindow;mnuMail')
	        selectmenuitem('Evolution-Mail','mnuFile;mnuNew;mnuMailMessage')
		log('OpenedComposemessageDialog','pass')
	      	settextvalue ('frmComposeamessage', 'txtTo', mailid)
	     	settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
	       	setcontext ('Compose a message',subjecttxt)
	       	settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
		selectmenuitem('frmComposeamessage','mnuInsert;mnuAttachment')
		selectrow('dlgAttachfile(s)','tblFiles',attachment_file)
		click ('dlgAttachfile(s)','btnOpen')
	       	click ('frmComposeamessage', 'btnSend')
		wait (5)
		click('Evolution-Mail','btnSend/Receive')
		log('ComposemessageSuccess','pass')
	except:
		print ' Compose messsage Failed'
		log('Compose-Mail-with-attachment-Failed','fail')


def verify_compose_mail_with_attachment (mailid, subjecttxt, attachment_file):
	try:
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Sent')        
	        selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
		log('ComposedmessageOpened','pass')
		setcontext('Compose a message',subjecttxt)
		verifytablecell ('frmReadOnlyMail', 'tblcheck', 1, 1, mailid)
       		verifytablecell ('frmReadOnlyMail', 'tblcheck', 2, 1, subjecttxt)
		verifypartialtablecell ('frmReadOnlyMail', 'tblattach', 0, 3, attachment_file)
		selectmenuitem ('frmReadOnlyMail','mnuFile;mnuClose')
	except error:
		print 'Verification of composition of mail with attachment failed '
		log('Verification-of-composition-of-mail-with-attachment-failed ','fail')

#Trying to read from the file
file = open('send_mail.dat', 'r')
argmts = file.readlines()
To_emailid = argmts[1].strip( )
Subject_Mail = argmts[2].strip( )
Bodytxt_Mail = argmts[3].strip( )
attach_file  = argmts[4].strip( )

# Call the function

log('ComposeandVerificationofMail-with-attachment','teststart')
log('ComposeofMail' ,'teststart')
wait(3)
compose_mail_with_attachment (To_emailid, Subject_Mail, Bodytxt_Mail, attach_file)
log('ComposeofMail' ,'testend')
wait(3)
log('VerificationofMail' ,'teststart')
verify_compose_mail_with_attachment (To_emailid, Subject_Mail,attach_file)
log('VerificationofMail' ,'testend')
log('ComposeandVerificationofMail-with-attachment','testend')
