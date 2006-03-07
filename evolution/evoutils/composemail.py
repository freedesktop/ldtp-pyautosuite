#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Authors:
#     Bhargavi       <kbhargavi_83@yahoo.co.in>
#     Premkumarr     <jpremkumar@novell.com>
#     Khasim Shaheed <khasim.shaheed@gmail.com>
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
def compose (to, subject=[], body=[], cc=[], bcc=[],attachment=[], format=[]):
    try:
        selectmenuitem ('frmEvolution-*', 'mnuFile;mnuNew;mnuMailMessage')
	time.sleep (2)
        if waittillguiexist ('frmComposeMessage') == 0:
            log('Compose message window does not appear', 'error')
            raise LdtpExecutionError (0)
        else:
            populate_mail_header (to, subject, body, cc,bcc)
            if len(format)>0:
                try:
                    if format[0]=='HTML':
                        check ('frmComposeMessage','mnuHTML')
                    elif format[0]=='Plain Text':
                        uncheck ('frmComposeMessage','mnuHTML')
                    else:
                        log ('Format not proper','warning')
                except:
                    log ('Error while setting Format of mail','error')
                    raise LdtpExecutionError (0)                        
	    if attachment:
		    attach_files (attachment)
    except ldtp.error, msg:
        log ('Compose message failed ' + str (msg), 'cause')
        log ('Compose message failed', 'Fail' );
        raise LdtpExecutionError (0)


def sendmail(subject):
    try:
        click ('frmComposeMessage', 'btnSend')
        time.sleep (3)
        if len(subject)==0 and  guiexist ('dlgEvolutionQuery')==1:
            remap ('evolution','dlgEvolutionQuery')
            click ('dlgEvolutionQuery','btnSend')
            undoremap ('evolution','dlgEvolutionQuery')
        if waittillguinotexist ('frmComposeMessage') == 0:
            log ('Failed during clicking the send button', 'error')
            raise LdtpExecutionError (0)
        if guiexist ('dlgEvolutionError'):
            log ('Error while sending mail', 'error')
            click ('dlgEvolutionError', 'btnOK')
            raise LdtpExecutionError (0)
        else:
            releasecontext()
            time.sleep (2)
    except:
        log ('Could not send message','error')
        raise LdtpExecutionError (0)


def savethismail (savemethod):
    """savemethod == 0 --> Save Draft
       savemethod == 1 --> save in FS"""
    try:
        if savemethod==0:
            selectmenuitem ('frmComposeMessage','mnuFile;mnuSaveDraft')
            time.sleep (1)
            selectmenuitem ('frmComposeMessage','mnuFile;mnuClose')
        elif savemethod==1:
            selectmenuitem ('frmComposeMessage','mnuFile;mnuSaveAs')
            waittillguiexist ('dlgSaveas')
            settextvalue ('dlgSaveas','txtName','testfile')
            click ('dlgSaveas','btnSave')
            time.sleep (2)
            if guiexist ('dlgOverwritefile?')==1:
                click ('dlgOverwritefile?','btnOverwrite')
                log ('testfile already exists','warning')
            selectmenuitem ('frmComposeMessage','mnuFile;mnuClose')
            waittillguiexist ('dlgWarning')
            click ('dlgWarning','btnDiscardChanges')
        else:
            log ('invalid save method','cause')
            raise LdtpExecutionError (0)

    except:
        log ('Saving Mail Failed!','error')
        raise LdtpExecutionError (0)

            
        
                    
# Attach files
def attach_files (attachment):
	try:
		n_attachments = len (attachment)
		for i in range(n_attachments):
			selectmenuitem ('frmComposeMessage', 'mnuInsert;mnuAttachment')
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
        bcc = data_object.gettagvalue ('bcc')
	subject = data_object.gettagvalue ('subject')
	body = data_object.gettagvalue ('body')
	attachment = data_object.gettagvalue ('attachment')
	sentitemsfolder = data_object.gettagvalue ('sentitemsfolder')
	refimg = data_object.gettagvalue ('refimg')
	#return [to, subject, body, cc, bcc, attachment, sentitemsfolder, refimg]
        return to, cc, bcc, subject, body, attachment, sentitemsfolder, refimg 
   
