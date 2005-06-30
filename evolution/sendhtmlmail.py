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

#Sending an HTML file Mail

# To Compse a New Mail Message using args supplied by a text file
def compose_html_mail (search_contact, select_contact, subjecttxt, mailbodytxt):
        selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuMailMessage')
	check ('frmComposeamessage', 'mnuHTML')
	click ('frmComposeamessage', 'btnTable')
	wait (3)
	click ('dlgInsert:Table', 'btnClose')
	settextvalue ('frmComposeamessage', 'txtMailBody', mailbodytxt)
        settextvalue ('frmComposeamessage', 'txtTo', select_contact)
	settextvalue ('frmComposeamessage', 'txtSubject', subjecttxt)
	setcontext ('Compose a message', subjecttxt)
	click ('frmComposeamessage', 'btnSend')


def verify_sent_mail (select_contact, subjecttxt):
		selectrow ('Evolution-Mail', 'treeTabFolder', 'Sent')        
		selectlastrow ('Evolution-Mail', 'treetblMails')
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
		setcontext ('Compose a message', subjecttxt)
		#print 'Context set'
		if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 2, 1, subjecttxt) == 1:
			if verifytablecell ('frmReadOnlyMail', 'tblMailHdr', 1, 1, toid) == 1:
				log ('Verification of sending mail as HTML was successful', 'info')
		else:
			log ('Verification Failed', 'info')
		#selectmenuitem ('Evolution-Mail', 'mnuFile;mnuClose')
		

# Section to capture the sent mails images 
#def verify_sent_mail (select_contact, subjecttxt):
#	selectrow ('Evolution-Mail', 'treeTabFolder', 'Sent')        
#	wait (3)
 #       selectlastrow ('Evolution-Mail', 'treetblMails')
#	selectmenuitem ('Evolution-Mail', 'mnuFile;mnuOpenMessage')
#	selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
#	selectmenuitem ('Evolution-Mail', 'mnuFile;mnuExit')
#As part of verification just going to sent folder and opening the mail (need to compare subject and other fields that is not currently done

# Trying to read from the file

file = open('send_mail.dat', 'r')
argmts = file.readlines()
search_contact = argmts[0].strip( )
select_contact = argmts[1].strip( )
subjecttxt = argmts[2].strip( )
mailbodytxt = argmts[3].strip( )
#toid = search_contact + ' <' + select_contact + '>'
toid = select_contact

# Call the function
try:
	log ('Compose_HTML_Mail', 'teststart')	
	compose_html_mail (search_contact, select_contact, subjecttxt, mailbodytxt)
	verify_sent_mail (select_contact, subjecttxt)
	log ('Composing HTML mail passed', 'pass') 
	log ('Compose_HTML_Mail', 'testend')
except error:
	log ('Composing HTML mail failed', 'fail') 
                                                                  
