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

#AutoCompletion
def autocompletion_compose_mail (subjecttxt, bodymailtxt, full_name):
	try:
		selectmenuitem('Evolution-Mail','mnuView;mnuWindow;mnuMail')
		wait(3)
		selectmenuitem('Evolution-Mail','mnuFile;mnuNew;mnuMailMessage')
		wait(3)
		log('OpenedComposemessageDialog','pass')	
		for i in range(0,5):
			try:
				grabfocus('frmComposeamessage','txtTo')	
				typekey ('pnayak')
				wait(3)
				for j in range(0,i+1):
			 		typekey ('<down>')
				typekey ('<return>')
				if verifysettext('frmComposeamessage', 'txtTo', full_name) == 1:
					log('AutoCompletion-Sucess','pass')
					break
	
			except error, msg:
				if string.find(str(msg), 'Verify SetTextValue action failed') == -1:
					print 'error'

		settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
		setcontext ('Compose a message',subjecttxt)
		settextvalue ('frmComposeamessage', 'txtMailBody', bodymailtxt)
		click ('frmComposeamessage', 'btnSend')
		click('Evolution-Mail','btnSend/Receive')		
		log('ComposemessageSuccess','pass')
	
	except error:
		print 'AutoCompletion failed'
		log('AutoCompletion-Compose-message','fail')


def verify_autocompletion_compose_mail (mailid, subjecttxt):
	try:
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Sent')        
	        selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
		log('ComposedmessageOpened','pass')
		setcontext('Compose a message',subjecttxt)
		verifytablecell ('frmReadOnlyMail', 'tblcheck', 1, 1, mailid)
       		verifytablecell ('frmReadOnlyMail', 'tblcheck', 2, 1, subjecttxt)		
		selectmenuitem ('frmReadOnlyMail','mnuFile;mnuClose')
	except error:
		print 'Verification of composition of mail in autocompletion '
		selectmenuitem ('frmReadOnlyMail','mnuFile;mnuClose')
		log('Verification-of-composition-of-mail-in-autocompletion ','fail')


#Trying to read from the file
file = open('autocompletion.dat', 'r')
argmts = file.readlines()
subject_text = argmts[0].strip( )
Bodytxt_Mail = argmts[1].strip( )
full_name = argmts[2].strip( )
to_mailid  = argmts[3].strip( )
		
			
log('AutoCompletion-Compose-and-Verification-message','teststart')
autocompletion_compose_mail (subject_text, Bodytxt_Mail, full_name)
verify_autocompletion_compose_mail (to_mailid, subject_text)
log('AutoCompletion-Compose-and-Verification-message','testend')

