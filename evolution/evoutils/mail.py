#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Authors:
#     Premkumar      <jpremkumar@novell.com>
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

import time, types
from ldtp import *
from ldtputils import *
from contact import *

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
        window_id = 'frmEvolution-*'
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
                print type (value)
		if type (value) is types.StringType:
                #if isinstance(value,types.StringType):
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
def populate_mail_header (to=[], subject=[], body=[], cc = [], bcc = []):
    try:
        if to and setandverify ('frmComposeMessage', 'txtTo', to) == 0:
            log ('Failed to insert text into To field','error')
            raise LdtpExecutionError (0)
	print "HERE"    
        if cc:
	    check ('frmComposeMessage','mnuCcField')
	    if setandverify ('frmComposeMessage', 'txtCc', cc) == 0:
		    log ('Failed to insert text into Cc field','error')
		    raise LdtpExecutionError (0)
        if bcc:
	    check ('frmComposeMessage','mnuBccField')
	    if setandverify ('frmComposeMessage', 'txtBcc', bcc) == 0:
		    log ('Failed to insert text into Bcc field','error')
		    raise LdtpExecutionError (0)

        #cant use set and verify since context switching is involved
        if subject:
            settextvalue ('frmComposeMessage', 'txtSubject', subject[0])
            setcontext ('Compose Message', subject[0])
            if verifysettext ('frmComposeMessage', 'txtSubject',
                              subject[0]) == 0:
                log ('Failed to insert text into subject Field','error')
                raise LdtpExecutionError (0)

	        
        #TODO: Change 'txt6' to some meaningful name in
        #evolution.map also in the following code
        if body and setandverify ('frmComposeMessage', 'txt6', str(body[0])) == 0:
            log ('Failed to insert text into Body field','error')
            raise LdtpExecutionError (0)
        #TODO: Check bcc field
        return 1
    except:
	log ('Compose mail failed', 'error')
	if guiexist ('frmComposeMessage'):
		selectmenuitem ('frmComposeMessage', 'mnuFile;mnuClose')
		time.sleep (2)
        raise LdtpExecutionError (0)

#To capture image of the ith mail in the given folder
def capturemailimage (sent_folder, sent_mail_count, filename):
    try:
        selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', sent_folder)
	time.sleep (2)
	print "SENT MAIL COUNT:",sent_mail_count
	print "NEW COUNT:",getrowcount ('frmEvolution-Mail', 'ttblMessageList')
	
	if (sent_mail_count+1) > getrowcount ('frmEvolution-Mail', 'ttblMessageList'):
		log ('Sent mail missing from Sent folder', 'error')
		raise LdtpExecutionError (0)
	remap ('evolution','frmEvolution-Mail')
        selectrowindex ('frmEvolution-Mail', 'ttblMessageList', sent_mail_count)
	time.sleep (2)
        subject = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', sent_mail_count, 4)
	undoremap ('evolution','frmEvolution-Mail')
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
	print folder_name,sent_mail_count, refimg_filename
	time.sleep (1)
        if not (capturemailimage (folder_name, sent_mail_count, 'cur_mail.png')):
	    print "error while capturing image"
	    raise LdtpExecutionError (0)
	time.sleep (3)
	if imagecompare ('IMAGES/cur_mail.png',refimg_filename[0]) < 3.0:
            return 1
        else:
            return 0
	
    except ldtp.error, msg:
        log ('Comparision of mail images failed - ' + str (msg), 'error')
	if guiexist ('frmReadonly'):
		selectmenuitem ('frmReadonly', 'mnuFile;mnuClose')
        LdtpExecutionError (0)
            
def get_HTML_pref(cont_name,addrbook='Personal'):
    try:
        selectContactPane()
	time.sleep (1)
	selectaddrbook(addrbook)
	time.sleep (1)
	selectcontact (cont_name)
	time.sleep (1)
	selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        setcontext ('Contact Editor','Contact Editor -'+titleappend(cont_name))
	print 'Contact Editor -'+titleappend(cont_name)
	time.sleep (10)
	waittillguiexist ('dlgContactEditor')
	if verifycheck ('dlgContactEditor','chkWantstoreceiveHTMLmail')==1:
	    ret=1
        else:
	    ret=0
        click ('dlgContactEditor','btnCancel')
	selectMailPane ()
    except:
        log ('Could not get HTML preference','cause')
	raise LdtpExecutionError (0)
    return ret


def insert_bgimage (bgimage):
    try:
        check ('frmComposeamessage','mnuHTML')
	time.sleep (1)
        selectmenuitem ('frmComposeamessage','mnuFormat;mnuPage')
        waittillguiexist ('dlgFormatPage')
	remap ('evolution','dlgFormatPage')
        click ('dlgFormatPage','btnBrowse')
        waittillguiexist('uknBackgroundImage')
	time.sleep (2)
        click ('uknBackgroundImage','btnHome')
        remap ('evolution','uknBackgroundImage')
	time.sleep (2)
        selectrow ('uknBackgroundImage','tblFiles',bgimage)
        click ('uknBackgroundImage','btnOK')
        undoremap ('evolution','uknBackgroundImage')
        click ('dlgFormatPage','btnClose')
	undoremap ('evolution','dlgFormatPage')
    except:
        log ('could not apply BackGround Image','cause')
        raise LdtpExecutionError (0)
    

def apply_template(template):
    try:
        check ('frmComposeamessage','mnuHTML')
	time.sleep (10)
        selectmenuitem ('frmComposeamessage','mnuFormat;mnuPage')
        waittillguiexist ('dlgFormatPage')
	remap ('evolution','dlgFormatPage')
	print "after wait"
        try:
	    print template
            comboselect ('dlgFormatPage','cboTemplate',template)
        except:
            log ('unable to select template','cause')
            raise LdtpExecutionError (0)
        click ('dlgFormatPage','btnClose')
	remap ('evolution','dlgFormatPage')
    except:
        log ('Could not apply template','error')
        raise LdtpExecutionError (0)


def getmailtext():
    try:
        window_id='frmComposeamessage'
        if guiexist (window_id) != 1:
	    log ('Compose window not open','cause')
	    raise LdtpExecutionError (0)
        numchild=getpanelchildcount(window_id,'pnlPanelcontainingHTML')
	remap ('evolution',window_id)
	text=''
	for val in range (6,6+numchild):
	    text+=gettextvalue(window_id,'txt'+str(val))
	    text+='\n'
	undoremap ('evolution',window_id)
    except:
        log ('could not get text from Compose Window','error')
	raise LdtpExecutionError (0)
    if len(text)==0:
	return text
    else:
        return text[:-1]


def getrowindex(subject):
    try:
        noofchild=getrowcount ('frmEvolution-Mail','ttblMessageList')
	for ind in range (noofchild):
	    if getcellvalue ('frmEvolution-Mail','ttblMessageList',ind,4) == subject:
	        return ind
	if ind == noofchild-1:
	    log ('Message not present','cause')
	    raise LdtpExecutionError (0)
    except:
        log ('Unable to get index of message','error')
	raise LdtpExecutionError (0)

	
def go_offline():
    log ('Go Offline','teststart')
    try:
        window_id=getcurwindow()
        remap ('evolultion',window_id)
        flag=False
        for x in getobjectlist(window_id):
            if x == 'mnuWorkOffline':
                flag=True
                break

        if flag==True:
            selectmenuitem (window_id,'mnuFile;mnuWorkOffline')
            log ('going offline','info')
        else:
            log ('already offline','info')
            log ('Go Offline','testend')
            return
        undoremap ('evolution',window_id)
	time.sleep (1)
        flag=False
        remap ('evolution',window_id)
        for x in getobjectlist (window_id):
            if x == 'mnuWorkOnline':
                flag=True
                break
        if flag == False:
            log ('Work Online not available','cause')
            raise LdtpExecutionError (0)
        undoremap ('evolution',window_id)
    except:
        log ('Could not go offline','error')
        log ('Go Offline','testend')
        raise LdtpExecutionError (0)
    log ('Go Offline','testend')


def go_online ():
    log ('Go Online','teststart')
    try:
        window_id=getcurwindow()
        remap ('evolultion',window_id)
        flag=False
        for x in getobjectlist(window_id):
            if x == 'mnuWorkOnline':
                flag=True
                break

        if flag==True:
            selectmenuitem (window_id,'mnuFile;mnuWorkOnline')
            log ('going online','info')
        else:
            log ('already online','info')
            log ('Go Online','testend')
            return
        undoremap ('evolution',window_id)
	time.sleep (1)
        flag=False
        remap ('evolution',window_id)
        for x in getobjectlist (window_id):
            if x == 'mnuWorkOffline':
                flag=True
                break
        if flag == False:
            log ('Work Offline not available','cause')
            raise LdtpExecutionError (0)
        undoremap ('evolution',window_id)
    except:
        log ('Could not go Online','error')
        log ('Go Online','testend')
        raise LdtpExecutionError (0)
    log ('Go Online','testend')

def getsentmailtext():
    try:
        remap ('evolution','frmReadonly')
	noofchild = getpanelchildcount ('frmReadonly','pnlPanelcontainingHTML')

	text=''
	for textboxno in range (noofchild):
	    text+=gettextvalue ('frmReadonly','txt'+str(textboxno))
	    text+='\n'
	if len (text) > 0:
	    text=text[:-1]

	return text
    except:
        log ('Unable to get text from sent mail','cause')
	raise LdtpExecutionError (0)

		
