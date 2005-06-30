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

# To Reply a Mail using args supplied by a text file

#To reply mail
def reply_mail (mailid, subjecttxt, mailbodytxt, cc_id):
	try: 
		selectmenuitem('Evolution-Mail','mnuView;mnuWindow;mnuMail')
		wait(3)	        
		selectrowpartialmatch ('Evolution-Mail', 'treeTabFolder', 'Mailbox')
		selectlastrow ('Evolution-Mail', 'treetblMails')
		click('Evolution-Mail','btnReply')
		wait(3)
       		setcontext ('Compose a message','Re: '+subjecttxt)
		#selectmenuitem('frmComposeamessage', 'mnuView;mnuCcField')
		settextvalue ('frmComposeamessage', 'txtCc', cc_id)
       		click ('frmComposeamessage', 'btnSend')
		click('Evolution-Mail','btnSend/Receive')		
		log('Reply-message-Success','pass')
	except error:
		print ' Reply messsage Failed'
		log('Reply-Mail-Failed','fail')

def reply_all_mail (mailid, subjecttxt, mailbodytxt):
	try: 
		selectmenuitem('Evolution-Mail','mnuView;mnuWindow;mnuMail')
		wait(3)	        
		selectrowpartialmatch ('Evolution-Mail', 'treeTabFolder', 'Mailbox')
		selectlastrow ('Evolution-Mail', 'treetblMails')
		click('Evolution-Mail','btnReplyAll')
		wait(3)
       		setcontext ('Compose a message','Re: '+subjecttxt)
		#selectmenuitem('frmComposeamessage', 'mnuView;mnuCcField')
       		click ('frmComposeamessage', 'btnSend')
		click('Evolution-Mail','btnSend/Receive')		
		log('Reply-message-Success','pass')
	except error:
		print ' Reply messsage Failed'
		log('Reply-Mail-Failed','fail')


# Section to verify if mail is sent
def verify_reply_mail (mailid, subjecttxt,cc_id):
	try:
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Sent')        
	        selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
		log('Replied-message-Opened','pass')
		setcontext('Compose a message','Re: '+subjecttxt)
        	verifytablecell ('frmReadOnlyMail', 'tblcheck', 1, 1, mailid)
		verifytablecell ('frmReadOnlyMail', 'tblcheck', 2, 1, cc_id)        	
		log('VerificationSuccess','pass')
        	selectmenuitem ('frmReadOnlyMail','mnuFile;mnuClose')
		log('Closemail','pass')
	except error:	
		print ' Verification of Replied mail Failed'
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

log('ReplyandVerificationofMail','teststart')
log('ReplyMail' ,'teststart')
reply_mail (To_emailid, Subject_Mail, Bodytxt_Mail, Cc_mailid)
log('ReplyMail' ,'testend')
log('VerificationofMail' ,'teststart')
verify_reply_mail (To_emailid, Subject_Mail, Cc_verify_mailid)
log('VerificationofMail' ,'testend')
log('ReplyandVerificationofMail','testend')
