#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Nagashree <mnagashree@novell.com>
#     Premkumar <jpremkumar@novell.com>
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

# To Forward a Mail using args supplied by a text file
from evoutils.mail import *

#To Forward mail
def forward_mail (to,body,subject_new='',cc=''):
	try:
		selectmenuitem('evolution','mnuTools;mnuMail')
		time.sleep(3)

		#TODO: Write additional code to select the particular
		#folder from Folder tree before moving to the next statement
		
		#TODO: Uncomment the following when getrowcount bug
		#is fixed in evolution/accessibility
		#selectlastrow ('evolution', 'ttblMessageList')

		cur_index=getrowcount ('evolution','ttblMessageList')-3;

		#TOOD: When Uncommenting the previous statement remove
		#the following statement
		selectrowindex ('evolution','ttblMessageList',cur_index)

		subject = getcellvalue('evolution','ttblMessageList',cur_index+1,4)
		click('evolution','btnForward')
		time.sleep(3)
		setcontext ('Compose a message','[Fwd: '+subject+']')
		if guiexist('Composeamessage') == 0:
			log ('Failed to open forward frame','error')
			raise LdtpExecutionError(0)
		else:
			if populate_mail_header (to,subject_new,
						 body,cc) == 0:
				log ('Failed to populate mail header',
				     'error')
				raise LdtpExecutionError (0)
			else:
				click ('Composeamessage', 'btnSend')
				if guiexist ('Composeamessage') == 0:
					log ('Failed to close Compose dialog after sending','error')
					raise LdtpExecutionError(0)
				else:
					click('evolution','btnSend/Receive')
					log('Forward-message-Success','pass')
					releasecontext()
	except error:
		print 'Forward messsage Failed'
		log('Forward-Mail-Failed','fail')

#Trying to read from the file
inpfile = open('forward-mail.dat', 'r')
argmts = inpfile.readlines()
to_mailid = argmts[0].strip( )
Bodytxt_Mail = argmts[1].strip( )
if Bodytxt_Mail == '~':
	Bodytxt_Mail = ''
Subjecttxt = argmts[2].strip( )
if Subjecttxt == '~':
	Subjecttxt = ''
Cc_mailid = argmts[3].strip( )
if Cc_mailid == '~':
	Cc_mailid = ''

# Call the function

log('Forward Mail and verify','teststart')
log('Forward Mail' ,'teststart')
forward_mail (to_mailid,Bodytxt_Mail,Subjecttxt,Cc_mailid)
log('Forward Mail' ,'testend')
log('Forward Mail - Verification','teststart')
verifymailwithimage ('Sent Items',-9,'forwardmail_refimage.png')
log('Forward Mail - Verification' ,'testend')
log('Forward Mail and verify','testend')
