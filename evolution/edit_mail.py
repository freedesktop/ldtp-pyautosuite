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

def compose_mail (mailid, subjecttxt, mailbodytxt):
	try:
		selectmenuitem('Evolution-Mail','mnuFile;mnuNew;mnuMailMessage')
		settextvalue ('frmComposeamessage', 'txtTo', mailid)
		settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
		setcontext ('Compose a message',subjecttxt)
		settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
		selectmenuitem('frmComposeamessage', 'mnuEdit;mnuSelectAll')
		click('frmComposeamessage','btnCut')
		click('frmComposeamessage','btnPaste')
		log('Cut-Paste-Operation','pass')
		selectmenuitem('frmComposeamessage', 'mnuEdit;mnuSelectAll')
		click('frmComposeamessage','btnCopy')	
		click('frmComposeamessage','btnPaste')
		click('frmComposeamessage','btnPaste')
		log('Copy-Paste-Operation','pass')
		selectmenuitem ('frmComposeamessage','mnuFile;mnuClose')
		click('dlgWarning:ModifiedMessage','btnDiscardChanges')
	except error:
		print "Edit Operation Failed"
		log('Edit-operation-failed','fail')


#To get arguments from file
file = open('send_mail.dat', 'r')
argmts = file.readlines()
To_emailid = argmts[1].strip( )
Subject_Mail = argmts[2].strip( )
Bodytxt_Mail = argmts[3].strip( )

#call to function
log('edit-operation','teststart')
wait(3)
compose_mail (To_emailid, Subject_Mail, Bodytxt_Mail)
log('edit-operation','testend')
