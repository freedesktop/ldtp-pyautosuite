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

#Viewing an existing Mail
from ldtp import *
import ldtputils

# To Compse a New Mail Message using args supplied by a text file
def compose_html_mail (search_contact, select_contact, subjecttxt, mailbodytxt):
        selectmenuitem ('Evolution-mail', 'mnuFile;mnuNew;mnuMailMessage')
	check ('frmComposeamessage', 'mnuHTML')
	click ('frmComposeamessage', 'btnTable')
	wait (3)
	click ('dlgInsert:Table', 'btnClose')
	settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
        settextvalue ('frmComposeamessage', 'txtTo', select_contact)
	settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
	setcontext ('Compose a message', subjecttxt)
	click ('frmComposeamessage', 'btnSend')
	click('Evolution-mail','btnSend/Receive')


# Section to capture the sent mails images 
def capture_composed_mail (select_contact, subjecttxt):
	selectrow ('Evolution-mail', 'treeTabFolder', 'Sent')        
        selectlastrow ('Evolution-mail', 'treetblMails')
	selectmenuitem ('Evolution-mail', 'mnuFile;mnuOpenMessage')
	setcontext ('Compose a message', subjecttxt)
	ldtputils.imagecapture ('Compose test mail', 'to_compare_html.png')
	selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')

# Section to capture the received mails images 
def compare_received_mail (select_contact, subjecttxt):
	selectrowpartialmatch ('Evolution-mail', 'treeTabFolder', 'Mailbox')
        selectlastrow ('Evolution-mail', 'treetblMails')
	selectmenuitem ('Evolution-mail', 'mnuFile;mnuOpenMessage')
	setcontext ('frmComposeamessage', subjecttxt)
        ldtputils.imagecapture ('Compose test mail', 'image_html.png')
	ldtputils.imagecompare ('to_compare_html.png', 'image_html.png')
	setcontext ('Compose a message', subjecttxt)
	selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
	#selectmenuitem ('Evolution-mail', 'mnuFile;mnuClose')

#trying to read from the file
file = open('send_mail.dat', 'r')
argmts = file.readlines()
search_contact = argmts[0].strip( )
select_contact = argmts[1].strip( )
subjecttxt = argmts[2].strip( )
mailbodytxt = argmts[3].strip( )

# Call the function
#try:
log ('viewmail', 'teststart')	
compose_html_mail (search_contact, select_contact, subjecttxt, mailbodytxt)
capture_composed_mail (select_contact, subjecttxt)
compare_received_mail (select_contact, subjecttxt)
log ('Viewing a mail passed', 'pass') 
log ('viewmail', 'testend')
#except error:
log ('Viewing mail failed', 'fail') 
                                                                           
