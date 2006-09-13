#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
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

import time, types, os
from ldtp import *
from ldtputils import *
#from contact import *
from evoutils import *

# To set and verify a textbox
def setandverify (win_name, box_name, value):
	try:
		text = ''
		if type (value) == types.StringType or type (value) == types.UnicodeType:
			text = value
		elif type (value) == types.ListType:
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
    win_id = '*ComposeMessage*'
    try:
        if to != [] and setandverify ('*ComposeMessage*', 'txtTo', to) == 0:
            log ('Failed to insert text into To field','error')
            raise LdtpExecutionError (0)
        if cc != []:
	    selectmenuitem ('*ComposeMessage*','mnuView;mnuCcField')
	    if setandverify ('*ComposeMessage*', 'txtCc', cc) == 0:
		    log ('Failed to insert text into Cc field','error')
		    raise LdtpExecutionError (0)
        if bcc != []:
	    selectmenuitem ('*ComposeMessage*','mnuView;mnuBccField')
	    if setandverify ('*ComposeMessage*', 'txtBcc', bcc) == 0:
		    log ('Failed to insert text into Bcc field','error')
		    raise LdtpExecutionError (0)
        #cant use set and verify since context switching is involved
        if subject:
            settextvalue ('*ComposeMessage*', 'txtSubject', subject[0])
	    win_id = get_mail_name (subject[0])
            if verifysettext (win_id, 'txtSubject',
			      subject[0]) == 0:
                log ('Failed to insert text into subject Field','error')
                raise LdtpExecutionError (0)
        if body and setandverify (win_id, 'txt6', str(body[0])) == 0:
            log ('Failed to insert text into Body field','error')
            raise LdtpExecutionError (0)
        return win_id
    except:
	log ('Compose mail failed', 'error')
	if guiexist (win_id):
		selectmenuitem ('*ComposeMessage*', 'mnuFile;mnuClose')
		time.sleep (2)
        raise LdtpExecutionError (0)

#To capture image of the ith mail in the given folder
def capturemailimage (sent_folder, sent_mail_count, filename):
    try:
        selectrowpartialmatch ('frmEvolution*', 'ttblMailFolderTree', sent_folder)
	waittillguiexist ('frmEvolution-'+sent_folder+'*')
	time.sleep (2)
	print "SENT MAIL COUNT:",sent_mail_count
	new_count = getrowcount ('frmEvolution*', 'ttblMessages')
	print "NEW COUNT:", new_count

	if (sent_mail_count+1) > new_count:
	    log ('Sent mail missing from Sent folder', 'error')
	    raise LdtpExecutionError (0)
        selectrowindex ('frmEvolution*', 'ttblMessages', sent_mail_count)
	time.sleep (2)
        subject = getcellvalue ('frmEvolution*', 'ttblMessages', sent_mail_count, 4)
        selectmenuitem ('frmEvolution*', 'mnuMessage;mnuOpeninNewWindow')
	time.sleep (1)

	window_id = get_mail_name (subject)
	if waittillguiexist (window_id) == 0:
            log ('Message failed to open', 'cause')
            raise LdtpExecutionError (0)

	activatewin (subject)
	time.sleep (1)
	print 'Capturing image of the sent mail for comparision...'
        imagecapture (subject, 'IMAGES/'+filename)
	print '...done'
	time.sleep (2)
        selectmenuitem (window_id, 'mnuFile;mnuClose')
        if waittillguinotexist (window_id) == 0:
            log ('Message Window is not close after capturing', 'warning')
            raise LdtpExecutionError (0)
        return 1
    except ldtp.error, msg:
        log ('Capturing of mail failed ' + str (msg), 'warning')
        raise LdtpExecutionError(0)
        
#To verify the ith mail in the given folder with the given image
def verifymailwithimage (folder_name, sent_mail_count, refimg_filename, subject=[]):

    try:
	# TODO: Have to black out the date display region for best results
	# 85, 94 && 340,200
	if subject:
	    subject = get_mail_name (subject[0])
	else:
	    subject = 'frmReadonly'
	if not (refimg_filename):
		log ('Reference Image not provided', 'error')
		raise LdtpExecutionError (0)
	print folder_name,sent_mail_count, refimg_filename
	time.sleep (1)
        if not (capturemailimage (folder_name, sent_mail_count, 'cur_mail.png')):
	    print "error while capturing image"
	    raise LdtpExecutionError (0)
	time.sleep (3)
	blackoutregion ('IMAGES/cur_mail.png','IMAGES/cur_mail.png',85,94,340,200)

	if imagecompare ('IMAGES/cur_mail.png',refimg_filename[0]) < 3.0:
		#selectmenuitem (subject, 'mnuFile;mnuClose')
            return 1
        else:
	    #selectmenuitem (subject, 'mnuFile;mnuClose')
            return 0
	
    except ldtp.error, msg:
        log ('Comparision of mail images failed - ' + str (msg), 'error')
		
	if guiexist (subject):
		selectmenuitem (subject, 'mnuFile;mnuClose')
	raise LdtpExecutionError (0)
            
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
	menucheck ('frmComposeMessage','mnuHTML')
	time.sleep (1)
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuPage')
	time.sleep (2)
        waittillguiexist ('dlgFormatPage')
	settextvalue ('dlgFormatPage','cboBackgroundImageFilePath',os.getcwd() + os.sep + bgimage)
#        click ('dlgFormatPage','btnBrowse')
# 	time.sleep (2)	
#         waittillguiexist('uknBackgroundImage')
# 	time.sleep (2)
#         click ('uknBackgroundImage','btnHome')
# 	time.sleep (2)
#         selectrow ('uknBackgroundImage','tblFiles',bgimage)
#         click ('uknBackgroundImage','btnOK')
        click ('dlgFormatPage','btnClose')
    except:
        log ('could not apply BackGround Image','cause')
        raise LdtpExecutionError (0)
    

def apply_template(template):
    try:
	menucheck ('frmComposeMessage','mnuHTML')
	time.sleep (2)
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuPage')
        waittillguiexist ('dlgFormatPage')
        try:
            comboselect ('dlgFormatPage','cboTemplate',template)
        except:
            log ('unable to select template','cause')
            raise LdtpExecutionError (0)
        click ('dlgFormatPage','btnClose')
    except:
        log ('Could not apply template','error')
        raise LdtpExecutionError (0)


def getmailtext(window_id = '*Compose*'):
    try:
        if guiexist (window_id) != 1:
	    log ('Compose window not open','cause')
	    raise LdtpExecutionError (0)
        numchild=getpanelchildcount(window_id,'pnlPanelcontainingHTML')
	print numchild
	text=''
	for val in range (6,6+numchild):
	    print text, 'txt'+str(val)
	    temp = gettextvalue(window_id,'txt'+str(val))
	    if temp != None:
	        text += temp
	    text+='\n'
    except:
        log ('could not get text from Compose Window','error')
	raise LdtpExecutionError (0)
    if len(text)==0:
	return text
    else:
        return text[:-1]


def getrowindex(subject):
    try:
        noofchild=getrowcount ('frmEvolution-*','ttblMessages')
	for ind in range (noofchild):
	    if getcellvalue ('frmEvolution-*','ttblMessages',ind,4) == subject:
	        return ind
	if ind == noofchild-1:
	    log ('Message not present','cause')
	    raise LdtpExecutionError (0)
    except:
        log ('Unable to get index of message','error')
	raise LdtpExecutionError (0)

	

def getsentmailtext(window_id='frmReadonly'):
    try:
	noofchild = getpanelchildcount (window_id,'pnlPanelcontainingHTML1')
	text=''
	for textboxno in range (noofchild):
	    temp = gettextvalue (window_id,'txt'+str(textboxno))
	    if temp != None:
	        text += temp
	    text+='\n'
	if len (text) > 0:
	    text=text[:-1]

	return text
    except:
        log ('Unable to get text from sent mail','cause')
	raise LdtpExecutionError (0)

		

