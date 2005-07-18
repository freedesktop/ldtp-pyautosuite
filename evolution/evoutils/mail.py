#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Premkumar <jpremkumar@novell.com>
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
from ldtp import *
from ldtputils import *

#To set and verify a textbox
def setandverify (win_name, box_name, value):
    try:
        settextvalue (win_name, box_name, value)
        if verifysettext (win_name, box_name, value) == 0:
            return 0
        return 1
    except:
        return 0

                                        
#To populate mail header
def populate_mail_header (to, subject,body,
                          cc = '', bcc = ''):
    try:
        if to!='' and setandverify ('Composeamessage', 'txtTo', to) == 0:
            log ('Failed to insert text into To field','error')
            raise LdtpExecutionError (0)
        if cc != '' and setandverify ('Composeamessage',
                                      'txtCc', cc) == 0:
            log ('Failed to insert text into Cc field','error')
            raise LdtpExecutionError (0)
        #Note: I have edited the evolution.map to change 'txt0'
        #to 'txtSubject'
        
        #switching is involved
        if subject!='':
            settextvalue ('Composeamessage', 'txtSubject', subject)
            setcontext ('Compose a message', subject)
            time.sleep(3)
            if verifysettext ('Composeamessage', 'txtSubject',
                              subject) == 0:
                log ('Failed to insert text into subject Field','error')
                raise LdtpExecutionError (0)
        #TODO: Change 'txt6' to some meaningful name in
        #evolution.map also in the following code
        if body!='' and setandverify ('Composeamessage', 'txt6',
                                      body) == 0:
            log ('Failed to insert text into Body field','error')
            raise LdtpExecutionError (0)
        #TODO: Check bcc field
        return 1
    except:
        print 'Compose new message failed '
        log ('Compose new message failed', 'Fail' )

#To capture image of the ith mail in the given folder
def capturemailimage (folder_name,i,filename):
    try:
        selectmenuitem ('evolution','mnuTools;mnuMail')
        selectrowpartialmatch ('evolution','ttblMailFolder',folder_name)
        if i==-9:
            i = getrowcount ('evolution','ttblMessageList') - 3
        selectrowindex ('evolution','ttblMessageList',i)
        time.sleep(3)    
        subject = getcellvalue ('evolution','ttblMessageList',i+1,4)
        time.sleep (1)
        selectmenuitem ('evolution','mnuMessage;mnuOpeninNewWindow')
        setcontext ('Readonlyframe',subject)
        time.sleep (5)
        imagecapture (subject,filename)
        selectmenuitem ('Readonlyframe','mnuFile;mnuClose')
        time.sleep(1)
        if guiexist ('Readonlyframe') == 1:
            log ('Message Window is not close after capturing','warning')
            raise LdtpExecutionError (0)
        releasecontext ()
        return 1
    except:
        log ('Capturing of mail failed','warning')
        LdtpExecutionError(0)
        
    
#To verify the ith mail in the given folder with the given image
def verifymailwithimage (folder_name,mail_index,refimg_filename):
    try:
        capturemailimage (folfer_name,mail_index,'cur_mail.png')
        if imagecompare ('cur_mail.png',refimg_filename) == 0.0:
            return 1
        else:
            return 0
    except:
        log ('Comparision of mail images failed - ref image: ' + refimg_filename ,'error')
        LdtpExecutionError (0)
            

