#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Authors:
#     Premkumar      <jpremkumar@novell.com>
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

import time, types
from ldtp import *
from ldtputils import *

# To Change component
def get_window (component=None):
	window_id = ''
        if guiexist ('frmEvolution-Mail') == 1:
            	window_id = 'frmEvolution-Mail'
        elif guiexist ('frmEvolution-Calendars') == 1:
            	window_id = 'frmEvolution-Calendars'
        elif guiexist ('frmEvolution-Tasks') == 1:
            	window_id = 'frmEvolution-Tasks'
        elif guiexist ('frmEvolution-Contacts') == 1:
            	window_id = 'frmEvolution-Contacts'
	elif guiexist ('frmEvolution-Memos') == 1:
            	window_id = 'frmEvolution-Memos'
	if component:
		if window_id:
			selectmenuitem (window_id, 'mnuView;mnuWindow;mnu' + component)
			time.sleep (3)
			return 1
		else:	
			return 0
	else:
		return window_id

# To set and verify a textbox
def setandverify (win_name, box_name, value):
	try:
		text = ''
		if type (value) == types.StringType:
			text = value
		else:	
			length = len (value)
			for i in range (length):
				text = text + str (value[i]) + ', '
				
	        settextvalue (win_name, box_name, text)
		tokens = text.split ('\n')
		if tokens[0] != text:
			verify_value = tokens[0]
		else:
			verify_value = text

	        if verifysettext (win_name, box_name, verify_value) == 0:
			return 0
	        return 1
	except:
		return 0
                                        
#To populate mail header
def populate_mail_header (to, subject, body,
                          cc = [], bcc = []):
    try:
        if to and setandverify ('frmComposeamessage', 'txtTo', to) == 0:
            log ('Failed to insert text into To field','error')
            raise LdtpExecutionError (0)
	    
        if cc and setandverify ('frmComposeamessage', 'txtCc', cc) == 0:
            log ('Failed to insert text into Cc field','error')
            raise LdtpExecutionError (0)
                
        #cant use set and verify since context switching is involved
        if subject:
            settextvalue ('frmComposeamessage', 'txtSubject', subject[0])
            setcontext ('Compose a message', subject[0])
            if verifysettext ('frmComposeamessage', 'txtSubject',
                              subject[0]) == 0:
                log ('Failed to insert text into subject Field','error')
                raise LdtpExecutionError (0)

        #TODO: Change 'txt6' to some meaningful name in
        #evolution.map also in the following code
        if body and setandverify ('frmComposeamessage', 'txt6', str(body[0])) == 0:
            log ('Failed to insert text into Body field','error')
            raise LdtpExecutionError (0)
        #TODO: Check bcc field
        return 1
    except:
	log ('Compose mail failed', 'error')
	if guiexist ('frmComposeamessage'):
		selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
		time.sleep (2)
        raise LdtpExecutionError (0)

#To capture image of the ith mail in the given folder
def capturemailimage (sent_folder, sent_mail_count, filename):
    try:
        selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', sent_folder)
	time.sleep (2)
	if (sent_mail_count+1) != getrowcount ('frmEvolution-Mail', 'ttblMessageList'):
		log ('Sent mail missing from Sent folder', 'error')
		raise LdtpExecutionError (0)

        selectrowindex ('frmEvolution-Mail', 'ttblMessageList', sent_mail_count)
	time.sleep (2)
        subject = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', sent_mail_count, 4)
        setcontext ('Readonlyframe', subject)
        selectmenuitem ('frmEvolution-Mail', 'mnuMessage;mnuOpeninNewWindow')
	time.sleep (1)
        if waittillguiexist ('frmReadonly') == 0:
            log ('Readonlyframe failed to open', 'cause')
            raise LdtpExecutionError (0)
	
	activatewin (subject)
	time.sleep (1)
	print 'Capturing image of the sent mail for comparision...'
        imagecapture (subject, 'IMAGES/'+filename)
	print '...done'
        selectmenuitem ('frmReadonly', 'mnuFile;mnuClose')
        if waittillguinotexist ('frmReadonly') == 0:
            log ('Message Window is not close after capturing', 'warning')
            raise LdtpExecutionError (0)

        releasecontext ()
        return 1
    except ldtp.error, msg:
        log ('Capturing of mail failed ' + str (msg), 'warning')
        LdtpExecutionError(0)
        
#To verify the ith mail in the given folder with the given image
def verifymailwithimage (folder_name, sent_mail_count, refimg_filename):
    try:
	# TODO: Have to black out the date display region for best results
	if not (refimg_filename):
		log ('Reference Image not provided', 'error')
		raise LdtpExecutionError (0)
        if not (capturemailimage (folder_name, sent_mail_count, 'cur_mail.png')):
		raise LdtpExecutionError (0)
	time.sleep (3)
        if imagecompare ('IMAGES/cur_mail.png', refimg_filename[0]) < 0.5:
            return 1
        else:
            return 0

    except ldtp.error, msg:
        log ('Comparision of mail images failed - ' + str (msg), 'error')
	if guiexist ('frmReadonly'):
		selectmenuitem ('frmReadonly', 'mnuFile;mnuClose')
        LdtpExecutionError (0)
            
