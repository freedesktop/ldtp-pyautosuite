#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Authors:
#     Bhargavi       <kbhargavi_83@yahoo.co.in>
#     Premkumarr     <jpremkumar@novell.com>
#     Khasim Shaheed <sshaik@novell.com>
#
#  Copyright 2004 Novell, Inc.
#
#  This library is free software; you can redistribute it and/or
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

# Compose a new mail through File menu
from evoutils.mail import *

# Section to compose a new mail through File menu
def compose (to, subject, body, cc=[], attachment=[]):
    try:
        selectmenuitem ('frmEvolution-Mail', 'mnuFile;mnuNew;mnuMailMessage')
	time.sleep (2)
        if waittillguiexist ('frmComposeamessage') == 0:
            log('Compose message window does not appear', 'error')
            raise LdtpExecutionError (0)
        else:
            populate_mail_header (to, subject, body, cc)
	    if attachment:
		    attach_files (attachment)
            click ('frmComposeamessage', 'btnSend')
            if waittillguinotexist ('frmComposeamessage') == 0:
                log ('Failed during clicking the send button', 'error')
                raise LdtpExecutionError (0)
	    if guiexist ('dlgEvolutionError'):
		    log ('Error while sending mail', 'error')
		    click ('dlgEvolutionError', 'btnOK')
		    raise LdtpExecutionError (0)
            else:
                releasecontext();
                click ('frmEvolution-Mail', 'btnSend/Receive')
		time.sleep (2)
    except ldtp.error, msg:
        log ('Compose message failed ' + str (msg), 'cause')
        log ('Compose message failed', 'Fail' );
        raise LdtpExecutionError (0)

# Attach files
def attach_files (attachment):
	try:
		n_attachments = len (attachment)
		for i in range(n_attachments):
			selectmenuitem ('frmComposeamessage', 'mnuInsert;mnuAttachment')
		        if waittillguiexist ('dlgAttachfile(s)') == 0:
                		log ('Select file dialog does not appear','error')
		                raise LdtpExecutionError (0)

			activatewin ('dlgAttachfile(s)')
			time.sleep (1)
		        selectrow ('dlgAttachfile(s)','tblFiles', attachment[i])
                	click ('dlgAttachfile(s)','btnAttach')
			time.sleep (1)
		        if waittillguinotexist ('dlgAttachfile(s)') == 0:
                		log ('Select file dialog not closed','error')
		                raise LdtpExecutionError (0)
	except ldtp.error, msg:
		log ('Attaching file ' + attachment[i] + ' failed' + str (msg), 'error')
		if guiexist ('dlgAttachfile(s)'):
			click ('dlgAttachfile(s)', 'btnCancel')
	
# Reading Input from xml file
def read_maildata (datafile):
	data_object = LdtpDataFileParser (datafile)
	to = data_object.gettagvalue ('to')
	cc = data_object.gettagvalue ('cc')
	subject = data_object.gettagvalue ('subject')
	body = data_object.gettagvalue ('body')
	attachment = data_object.gettagvalue ('attachment')
	sentitemsfolder = data_object.gettagvalue ('sentitemsfolder')
	refimg = data_object.gettagvalue ('refimg')
	return [to, subject, body, cc, attachment, sentitemsfolder, refimg]
   
