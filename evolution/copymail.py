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

#Copying an existing Mail

# Section to select and copy mail
def copy_verify_mail ():
	selectrowpartialmatch ('Evolution-mail', 'treeTabFolder', 'Inbox')
	row_before = getrowcount('Evolution-mail', 'treetblMails') 
	selectrowpartialmatch ('Evolution-mail', 'treeTabFolder', 'Mailbox')
	rowcount = getrowcount('Evolution-mail', 'treetblMails') 
	if rowcount > 0:
	        selectlastrow ('Evolution-mail', 'treetblMails')
		#selectmenuitem ('Evolution-mail', 'mnuFile;mnuOpenMessage')
		selectmenuitem ('Evolution-mail', 'mnuActions;mnuCopyToFolder')
		selectrowpartialmatch ('dlgSelectfolder', 'foldertable', 'Inbox')
		click ('dlgSelectfolder','btnCopy')
		selectrowpartialmatch ('Evolution-mail', 'treeTabFolder', 'Inbox')
		wait (5)
		row_after = getrowcount('Evolution-mail', 'treetblMails')
		selectmenuitem ('Evolution-mail', 'mnuFile;mnuClose')
		if row_after > row_before:
			log ('Copying a mail passed successfully', 'pass') 
		else :
			log ('Copying a mail failed', 'fail')
	else:
		log ('No Mails in the MailBox directory to be Copied', 'Warning')
		log ('Did not move any mails to other folder', 'Pass')

#Unable to proceed with verification of moved mails with comparing with subject, data, to and from fields as workaround using row count to verify.  
#	subject = getactivewin ()
#	print subject
	#setcontext ('Compose a message', subjecttxt)
       	#i = verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 1, 1, fromid)
#	print i



# Call the function
try:
	log ('copyingmail', 'teststart')	
	copy_verify_mail ()
	log ('copyingmail', 'testend')
except error:
	log ('Cppying mail failed', 'fail') 
                                                                           
