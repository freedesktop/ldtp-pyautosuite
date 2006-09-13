#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Prashanth Mohan  <prashmohan@gmail.com>
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

from contact import *
from evoutils import *
from evoutils.mail import *
from evoutils.mailpreferences import *
from evoutils.composemail import *
from ldtp import *
from ldtputils import *
import os, time

def htmlformatting():
    log ('Check if formatting elements get disabled when HTML setting is off','teststart')
    try:
        selectMailPane()
        window_id = get_window()
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuMailMessage')
        waittillguiexist ('*ComposeMessage')
        time.sleep (1)
        menuuncheck ('*ComposeMessage','mnuHTML')
        if stateenabled ('*ComposeMessage','tbtnTypewriter')==1 or stateenabled ('*ComposeMessage','tbtnBold')==1 or stateenabled ('*ComposeMessage','tbtnItalic')==1 or stateenabled ('*ComposeMessage','tbtnStrikeout')==1:
            log ('text formatting is enabled','cause')
            raise LdtpExecutionError(0)
#         elif stateenabled ('*ComposeMessage','btnImage') == 1 or stateenabled ('*ComposeMessage','btnRule') == 1 or stateenabled ('*ComposeMessage','btnLink') == 1 or stateenabled ('*ComposeMessage','btnTable') == 1:
#             log ('Inserting Objects is enabled','cause')
#             raise LdtpExecutionError(0)
        selectmenuitem ('*ComposeMessage','mnuFile;mnuClose')
    except:
        log ('Menus are enabled when HTML is not selected','error')
        log ('Check if formatting elements get disabled when HTML setting is off','fail')
        log ('Check if formatting elements get disabled when HTML setting is off','testend')
        raise LdtpExecutionError (0)
    log ('Check if formatting elements get disabled when HTML setting is off','pass')
    log ('Check if formatting elements get disabled when HTML setting is off','testend')

                       
def savemail(savemethod,to, subject=[''], body=[], cc=[], bcc=[], attachment=[], draftfolder='Drafts'):
    log ('Test for saving a mail into Drafts folder','teststart')
    try:
        selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', draftfolder)
        waittillguiexist ('frmEvolution-'+draftfolder+'*')
        time.sleep (2)
        draft_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
        print "Draft count:",draft_mail_count
        compose (to, subject, body, cc,bcc, attachment)
        savethismail (savemethod, get_mail_name (subject[0]))
        testsavemail (draft_mail_count,savemethod)
    except:
        log ('Saving Mail failed','error')
        log ('Test for saving a mail into Drafts folder','testend')
        raise LdtpExecutionError (0)
    log ('Test for saving a mail into Drafts folder','testend')


def testsavemail(draft_count,savemethod):
    log ('Verification for save mail','teststart')
    try:
        if savemethod == 0:
            new_draft_count=getrowcount ('frmEvolution-*','ttblMessages')
            print "new count:",new_draft_count
            if new_draft_count>=draft_count+1:
                log ('Save Mail','pass')
            else:
                log ('Save Mail','fail')
                raise LdtpExecutionError (0)
        elif savemethod == 1:
            home=os.environ.get('HOME')
            if os.path.isfile(home+os.sep+'testfile')==True:
                log ('Save Mail','pass')
            else:
                log ('Save Mail','fail')
                raise LdtpExecutionError (0)
    except:
        log ('Save mail could not be verified','error')
        log ('Verification for save mail','fail')
        log ('Verification for save mail','testend')
        raise LdtpExecutionError (0)
    log ('Verification for save mail','pass')
    log ('Verification for save mail','testend')


def sendmailwhenoffline (to=[], subject=[], body=[], cc=[], bcc=[], attachment=[]):
    log ('Sending mail when evolution is offline','teststart')
    try:
        go_offline()
    except:
        log ('Unable to go offline','cause')
        log ('Sending mail when evolution is offline','testend')
        raise LdtpExecutionError (0)
    try:
        selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', 'Outbox')
        time.sleep (2)
        waittillguiexist ('frmEvolution-Outbox*')
        outbox_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
        selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', 'Sent')
        time.sleep (2)
        waittillguiexist ('frmEvolution-Sent*')
        sent_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
        compose (to, subject, body, cc,bcc, attachment)
        sendmail (subject)
        selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', 'Outbox')
        waittillguiexist ('frmEvolution-Outbox*')
        time.sleep (10)
        new_outbox_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
        print 'Old:',outbox_mail_count, 'New: ',new_outbox_mail_count
        if new_outbox_mail_count >= outbox_mail_count+1:
            log ('Message has been put in OutBox Folder','info')
        else:
            log ('Message has not been put in OutBox Folder','cause')
            raise LdtpExecutionError (0)
        
        go_online ()
        time.sleep (1)

        try:
            click ('frmEvolution-*', 'btnSend/Receive')
            waittillguiexist ('dlgSend&ReceiveMail')
            waittillguinotexist ('dlgSend&ReceiveMail')
            time.sleep (3)
        except:
            log ('could not send mail','cause')
            raise LdtpExecutionError (0)
        selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', 'Sent')
        waittillguiexist ('frmEvolution-Sent*')
        time.sleep (2)
        new_sent_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
        if new_sent_mail_count==sent_mail_count+new_outbox_mail_count:
            log ('Message sent','info')
            log ('Send Mail while offline Succeeded','info')
        else:
            log ('Message send Failed','error')
            raise LdtpExecutionError (0)
        
    except:
        log ('Send Mail while offline failed','error')
        log ('Sending mail when evolution is offline','fail')
        log ('Sending mail when evolution is offline','testend')
        raise LdtpExecutionError (0)
    log ('Sending mail when evolution is offline','pass')
    log ('Sending mail when evolution is offline','testend')

            
def closecomposewindow(state, window_id='frmComposeMessage'):
    """ state == 0 --> Discard Message
        state == 1 --> Cancel Dialog
        state == 2 --> Save Message"""
    log ('Close compose window','teststart')
    try:
        if guiexist (window_id) == 0:
            log ('Compose window not open','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Close compose window','testend')
        raise LdtpExecutionError (0)
    
    try:
        selectmenuitem (window_id,'mnuFile;mnuClose')
        time.sleep (2)
        if guiexist ('dlgWarning*')==1:
            if state==0:
                click ('dlgWarning*','btnDiscardChanges')
            elif state==1:
                click ('dlgWarning*','btnCancel')
            elif state==2:
                click ('dlgWarning*','btnSaveMessage')
            else:
                log ('Invalid option to choose','cause')
                raise LdtpExecutionError (0)
            log ('Warning Window closed successfully','info')
        else:
            log ('Warning window did not arise','warning')
    except:
        log ('Warning Window did not close successfully','error')
        log ('Close compose window','fail')
        log ('Close compose window','testend')
        raise LdtpExecutionError (0)
    waittillguinotexist (window_id)
    time.sleep (2)
    log ('Close compose window','pass')
    log ('Close compose window','testend')


def checkheaders(ref_image):
    log ('Check Compose window header boxes','teststart')
    try:
        window_id=getcurwindow()
        selectmenuitem ('window_id','mnuFile;mnuNew;mnuMailMessage')
        waittillguiexist ('frmComposeMessage')
    except:
        log ('could not open Mail Editor','cause')
        log ('Check Compose window header boxes','testend')
        raise LdtpExecutionError (0)

    try:
        menucheck ('frmComposeMessage','mnuFromField')
        menucheck ('frmComposeMessage','mnuPost-ToField')
        menucheck ('frmComposeMessage','mnuReply-ToField')
        menucheck ('frmComposeMessage','mnuCcField')
        menucheck ('frmComposeMessage','mnuBccField')
    except:
        log ('error while selecting fields','cause')
        log ('Check Compose window header boxes','testend')
        raise LdtpExecutionError (0)

    try:
        imagecapture('Compose Message','IMAGES/cur_mail.png')
    except:
        log ('Error while capturing image of window','cause')
        log ('Check Compose window header boxes','testend')
        raise LdtpExecutionError (0)

    try:
        if imagecompare (ref_image,'IMAGES/cur_mail.png') < 1.0:
            log ('Header fields ','pass')
            menuuncheck ('frmComposeMessage','mnuFromField')
            menuuncheck ('frmComposeMessage','mnuPost-ToField')
            menuuncheck ('frmComposeMessage','mnuReply-ToField')
            menuuncheck ('frmComposeMessage','mnuCcField')
            menuuncheck ('frmComposeMessage','mnuBccField')
            selectmenuitem ('frmComposeMessage','mnuFile;mnuClose')
        else:
            log ('Header fields ','fail')
            selectmenuitem ('frmComposeMessage','mnuFile;mnuClose')
            raise LdtpExecutionError(0)
    except:
        log ('Header fields do not match','warning')
        log ('Check Compose window header boxes','testend')
        raise LdtpExecutionError (0)
    log ('Check Compose window header boxes','testend')


def add_to_replytofield(replyto,to):
    log ('Add to reply-to field','teststart')
    try:
        selectMailPane()
        window_id='frmEvolution-*'
        subject =['test for reply to']
        body=subject
        selectrowpartialmatch (window_id,'ttblMailFolderTree','Sent')
        waittillguiexist ('frmEvolution-Sent*')
        sent_mail_count = getrowcount (window_id,'ttblMessages')
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuMailMessage')
        time.sleep (5)
        waittillguiexist ('frmComposeMessage')
        sub = populate_mail_header (to,subject,body)
        menucheck (sub,'mnuReply-ToField')
        settextvalue (sub,'txtReply-To',replyto)
        sendmail (subject)
        click (window_id, 'btnSend/Receive')
        waittillguiexist ('dlgSend&ReceiveMail')
        waittillguinotexist ('dlgSend&ReceiveMail')
        time.sleep (5)
        new_sent_mail_count = getrowcount (window_id,'ttblMessages')
        print 'NEW :: ',new_sent_mail_count, 'OLD :: ',sent_mail_count
        if new_sent_mail_count < sent_mail_count + 1:
            log ('Message not sent','cause')
            raise LdtpExecutionError (0)
        selectrowindex(window_id,'ttblMessages',sent_mail_count)
        selectmenuitem (window_id,'mnuMessage;mnuPostaReply')
        waittillguiexist ('frmRe:*')
        if gettextvalue ('frmRe:*','txtTo') != replyto:
            log ('To field does not have replyto address','cause')
            raise LdtpExecutionError (0)
        menuuncheck (sub,'mnuReply-ToField')
        selectmenuitem ('frmRe:*','mnuFile;mnuClose')
        log ('Reply to Field','pass')
    except:
        log ('Reply to Field','fail')
        log ('Add to reply-to field','testend')
        raise LdtpExecutionError (0)
    log ('Add to reply-to field','testend')


def background_image_test (to,bgimage,ref_image):
    log ('background image','teststart')
    try:
        subject=['background image test']
        body=['background image test']
        selectMailPane()
        window_id='frmEvolution-*'
        time.sleep (2)
        selectrowpartialmatch (window_id,'ttblMailFolderTree','Sent')
        waittillguiexist ('frmEvolution-Sent*')
        sent_mail_count = getrowcount (window_id,'ttblMessages')
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuMailMessage')
        waittillguiexist ('frmComposeMessage')
        populate_mail_header ([to],subject,body)
        insert_bgimage (bgimage[0])
        sendmail (subject)
        click (window_id, 'btnSend/Receive')
        waittillguiexist ('dlgSend&ReceiveMail')
        waittillguinotexist ('dlgSend&ReceiveMail')
        new_sent_mail_count=getrowcount (window_id,'ttblMessages')
        if new_sent_mail_count < sent_mail_count+1:
            log ('Could not send mail','cause')
            raise LdtpExecutiontionError (0)
    except:
        log ('Mail was not sent','error')
        log ('background image','testend')
        raise LdtpExecutionError (0)
    try:
        if verifymailwithimage ('Sent',sent_mail_count,ref_image) ==1:
            log ('Backgroung Image ','pass')
        else:
            log ('Background Image ','fail')
            raise LdtpExecutionError(0)
        print "outside"
    except:
        log ('Background image test did not pass','error')
        log ('background image','testend')
        raise LdtpExecutionError (0)
    log ('background image','testend')
    

def template_test(to,template,ref_image):
    log ('applying templates','teststart')
    try:
        subject=['template test']
        body=['template test\ntemplate test\ntemplate test\ntemplate test\n']
        selectMailPane()
        window_id='frmEvolution-*'
        selectrowpartialmatch (window_id,'ttblMailFolderTree','Sent')
        waittillguiexist ('frmEvolution-Sent*')
        sent_mail_count = getrowcount (window_id,'ttblMessages')
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuMailMessage')
        waittillguiexist ('frmComposeMessage')
        populate_mail_header ([to],subject,body)
        apply_template (template)
        sendmail (subject)
        click ('frmEvolution-*', 'btnSend/Receive')
        waittillguiexist ('dlgSend&ReceiveMail')
        waittillguinotexist ('dlgSend&ReceiveMail')
        new_sent_mail_count = getrowcount (window_id,'ttblMessages')
        if new_sent_mail_count < sent_mail_count+1:
            log ('Could not send mail','cause')
            raise LdtpExecutiontionError (0)
    except:
        log ('Mail was not sent','error')
        log ('applying templates','testend')
        raise LdtpExecutionError (0)
    try:
        if verifymailwithimage ('Sent',sent_mail_count,ref_image) ==1:
            log ('Template Test','pass')
        else:
            log ('Template Test','fail')
            raise LdtpExecutionError(0)
    except:
        log ('Template test did not pass','error')
        log ('applying templates','testend')
        raise LdtpExecutionError (0)
    log ('applying templates','testend')
    

def find_and_replace_test(replace,with):
    log ('Find and replace','teststart')
    try:
        text = getmailtext()
        grabfocus ('frmComposeMessage','txt6')
        #selectmenuitem ('frmComposeMessage','mnuEdit;mnuSelectAll')
        selectmenuitem ('frmComposeMessage','mnuEdit;mnuReplace')
        waittillguiexist ('dlgReplace')
        settextvalue ('dlgReplace','txtReplace',replace)
        settextvalue ('dlgReplace','txtWith',with)
        click ( 'dlgReplace','btnFindandReplace')
        waittillguinotexist ('dlgReplace')
        time.sleep (2)
        if guiexist('dlgReplaceconfirmation')==1:
            click ('dlgReplaceconfirmation','btnReplaceAll')
            waittillguinotexist ('dlgReplaceconfirmation')

        print 'TEXT:',text
        print 'NEWTEXT:',getmailtext()
        if getmailtext() == text.replace (replace,with):
            log ('Find and Replace','pass')
        else:
            log ('Find and Replace','fail')
            raise LdtpExecutionError (0)
    except:
        log ('Error in Find and Replace','error')
        log ('Find and replace','testend')
        raise LdtpExecutionError (0)
    log ('Find and replace','testend')
    

def undo_redo_test():
    log ('Undo and Redo','teststart')
    try:
        window_id = 'frmComposeMessage'
        numchild = getpanelchildcount(window_id,'pnlPanelcontainingHTML')
        present_text = getmailtext()
        
        appendtext (window_id,'txt'+str(6+numchild-1),'addedtext')
        added_text = getmailtext()
        
        try:
            selectmenuitem (window_id,'mnuEdit;mnuUndo')
        except:
            log ('Undo Button is not active','cause')
            raise LdtpExecutionError (0)

        undoed_text = getmailtext()

        if undoed_text == present_text:
            log ('Undo','pass')
        else:
            log ('Undo','fail')
            raise LdtpExecutionError (0)

        try:
            selectmenuitem (window_id,'mnuEdit;mnuRedo')
        except:
            log ('Redo Button is not active','cause')
            raise LdtpExecutionError (0)

        redoed_text = getmailtext()

        if redoed_text == added_text :
            log ('Redo','pass')
        else:
            log ('Redo','fail')
            raise LdtpExecutionError (0)
        selectmenuitem (window_id,'mnuEdit;mnuUndo')
    except:
        log ('Undo - Redo test failed','error')
        log ('Undo and Redo','testend')
        raise LdtpExecutionError (0)
    log ('Undo and Redo','testend')
    

def spell_check_test(method):
    """
    method == 0  --> Replace
    method == 1  --> Ignore
    method == 2  --> Skip
    method == 3  --> Add to Dict
    method == 4  --> Close Spell Checker
    method == 5  --> Back Button"""
    log ('Spell Check','teststart')
    try:
        window_id='dlgSpellchecker'
        selectmenuitem ('frmComposeMessage','mnuEdit;mnuCheckSpelling')
        time.sleep (2)
        addwords=[]
        if guiexist ('dlgInformation')==1:
            click ('dlgInformation','btnOK')
            log ('No Spelling mistakes','info')
        elif guiexist (window_id)==1 and method != 4 and method != 5:

            # do the actual replacement/skipping/ignoring here
            while guiexist (window_id)==1:
                remap ('evolution',window_id)
                obj=getobjectlist(window_id)
                for objects in obj:
                    if objects.startswith ('tbl'):
                        obj=objects
                        break
                repl = getrowcount (window_id,obj)

                if method==0:
                    if repl>0:
                        click (window_id,'btnReplace')
                    else:
                        log ('No Sugesstion for this word','info')
                elif method==1:
                    click (window_id,'btnIgnore')
                elif method==2:
                    click (window_id,'btnSkip')
                elif method==3:
                    obj=obj[obj.find('\'')+1:]
                    obj=obj[:obj.find('\'')]
                    addwords.append (obj)
                    click (window_id,'btnAddword')
                else:
                    log ('Unknown Method given','cause')
                    raise LdtpExecutionError (0)

                time.sleep (1)

            #verification of the above code
            if method == 3:
                present_text=gettextvalue ('frmComposeMessage','txt6')
                text=''

                for value in addwords:
                    text+=value
                    text+=' '

                text=text[:-1]
                settextvalue ('frmComposeMessage','txt6',text)

            #verification for all 3 methods
            
            selectmenuitem ('frmComposeMessage','mnuEdit;mnuCheckSpelling')
            time.sleep (2)

            if guiexist ('dlgInformation')==1 and method in [0,1,3]:
                click ('dlgInformation','btnOK')
                log ('Spell Check','pass')
            elif guiexist (window_id) == 1 and method == 2:
                click (window_id,'btnClose')
                waittillguinotexist (window_id)
                log ('Spell Check','pass')
            else:
                log ('Verification of Spell check failed','cause')
                log ('Spell Check','fail')
                raise LdtpExecutionError (0)

            if method==3:
                settextvalue ('frmComposeMessage','txt6',present_text)
                

        elif guiexist (window_id) == 1 and method == 4:
            click (window_id,'btnClose')
            waittillguinotexist (window_id)
            time.sleep (1)

            if guiexist (window_id) == 0:
                log ('Close button Works','info')
            else:
                log ('Close button Failed','cause')
                raise LdtpExecutionError (0)
            
        elif guiexist (window_id) == 1 and method == 5:
            #enter code for back button here
             obj=getobjectlist(window_id)

             for objects in obj:
                 if objects.startswith ('tbl'):
                     obj=objects
                     break

             obj=obj[obj.find('\'')+1:]
             obj=obj[:obj.find('\'')]
             last_word = obj
             click (window_id,'btnSkip')
             time.sleep (1)
             if guiexist (window_id) == 0:
                 log ('Only 1 mistyped occurance','cause')
                 raise LdtpExecutionError (0)

             try:
                 click (window_id,'btnBack')
             except:
                 log ('Could not click Back Button','cause')
                 raise LdtpExecutionError (0)

             time.sleep (1)
             obj=getobjectlist(window_id)

             for objects in obj:
                 if objects.startswith ('tbl'):
                     obj=objects
                     break

             obj=obj[obj.find('\'')+1:]
             obj=obj[:obj.find('\'')]
             new_word = obj
             click (window_id,'btnClose')
             waittillguinotexist (window_id)
             if new_word != last_word:
                 log ('Back does not lead to last misspelt word','cause')

    except:
        log ('Spell Check','fail')
        log ('Spell Check','testend')
        raise LdtpExecutionError (0)
    log ('Spell Check','pass')
    log ('Spell Check','testend')


def text_formatting_test(to,ref_image):
    log ('text formatting','teststart')
    try:
        subject=['bold,italic,strikethrough test']
        selectMailPane()
        window_id='frmEvolution-*'
        selectrowpartialmatch (window_id,'ttblMailFolderTree','Sent')
        waittillguiexist ('frmEvolution-Sent*')
        sent_mail_count=getrowcount (window_id,'ttblMessages')
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuMailMessage')
        waittillguiexist ('frmComposeMessage')
        menucheck ('frmComposeMessage','mnuHTML')
        time.sleep (1)
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuStyle;mnuBold')
        settextvalue ('frmComposeMessage','txt6','Hello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuStyle;mnuItalic')
        settextvalue ('frmComposeMessage','txt7','Hello\n')
        settextvalue ('frmComposeMessage','txt8','Hello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuStyle;mnuStrikethrough')
        settextvalue ('frmComposeMessage','txt9','Hello\n')
        settextvalue ('frmComposeMessage','txt10','Hello')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuAlignment;mnuCenter')
        settextvalue ('frmComposeMessage','txt10','Hello\n')
        settextvalue ('frmComposeMessage','txt11','Hello')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuAlignment;mnuRight')
        settextvalue ('frmComposeMessage','txt11','Hello\n')
        populate_mail_header ([to],subject)
        sendmail (subject)
        click ('frmEvolution-*', 'btnSend/Receive')
        waittillguiexist ('dlgSend&ReceiveMail')
        waittillguinotexist ('dlgSend&ReceiveMail')
        time.sleep (5)
        new_sent_mail_count = getrowcount (window_id,'ttblMessages')
        if new_sent_mail_count < sent_mail_count+1:
            log ('Could not send mail','cause')
            raise LdtpExecutiontionError (0)
    except:
        log ('Mail was not sent','error')
        log ('text formatting','testend')
        raise LdtpExecutionError (0)
    try:
        if verifymailwithimage ('Sent',sent_mail_count,ref_image, subject) ==1:
            log ('Text Formatting ','pass')
        else:
            log ('Text Formatting ','fail')
            raise LdtpExecutionError(0)
    except:
        log ('Text formatting test did not pass','error')
        log ('text formatting','testend')
        raise LdtpExecutionError (0)
    log ('text formatting','testend')
    

def lists_test(to,ref_image):
    log ('numbered,alphabetic,bulleted lists','teststart')
    try:
        subject=['Compose editor List test']
        selectMailPane()
        window_id='frmEvolution-*'
        selectrowpartialmatch (window_id,'ttblMailFolderTree','Sent')
        waittillguiexist ('frmEvolution-Sent*')
        sent_mail_count=getrowcount (window_id,'ttblMessages')
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuMailMessage')
        waittillguiexist ('frmComposeMessage')
        menucheck ('frmComposeMessage','mnuHTML')
        time.sleep (1)
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuHeading;mnuBulletedList')
        settextvalue ('frmComposeMessage','txt6','Hello\nHello\nHello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuHeading;mnuNumberedList')
        settextvalue ('frmComposeMessage','txt9','Hello\nHello\nHello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuHeading;mnuAlphabeticalList')
        settextvalue ('frmComposeMessage','txt12','Hello\nHello\nHello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuHeading;mnuRomanNumeralList')
        settextvalue ('frmComposeMessage','txt15','Hello\nHello\nHello\n')
        populate_mail_header ([to],subject)
        sendmail (subject)
        click ('frmEvolution-*', 'btnSend/Receive')
        waittillguiexist ('dlgSend&ReceiveMail')        
        waittillguinotexist ('dlgSend&ReceiveMail')
        time.sleep (5)
        new_sent_mail_count=getrowcount (window_id,'ttblMessages')
        if new_sent_mail_count < sent_mail_count+1:
            log ('Could not send mail','cause')
            raise LdtpExecutiontionError (0)
    except:
        log ('Mail was not sent','error')
        log ('numbered,alphabetic,bulleted lists','testend')
        raise LdtpExecutionError (0)
    try:
        if verifymailwithimage ('Sent',sent_mail_count,ref_image, subject) == 1:
            log ('Text Formatting ','pass')
        else:
            log ('Text Formatting ','fail')
            raise LdtpExecutionError(0)
        #undoremap ('evolution',window_id)
    except:
        log ('Text formatting test did not pass','error')
        log ('numbered,alphabetic,bulleted lists','testend')
        raise LdtpExecutionError (0)
    log ('numbered,alphabetic,bulleted lists','testend')
    

def fonts_test(to,ref_image):
    log ('Fonts Test','teststart')
    try:
        subject=['Compose editor Fonts test']
        selectMailPane()
        window_id='frmEvolution-*'
        selectrowpartialmatch (window_id,'ttblMailFolderTree','Sent')
        waittillguiexist ('frmEvolution-Sent*')
        sent_mail_count=getrowcount (window_id,'ttblMessages')
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuMailMessage')
        waittillguiexist ('frmComposeMessage')
        menucheck ('frmComposeMessage','mnuHTML')
        time.sleep (1)
        settextvalue ('frmComposeMessage','txt6','Hello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuFontSize;mnu+1')
        settextvalue ('frmComposeMessage','txt7','Hello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuFontSize;mnu+2')
        settextvalue ('frmComposeMessage','txt8','Hello\n')
        selectmenuitem ('frmComposeMessage','mnuFormat;mnuFontSize;mnu+3')
        settextvalue ('frmComposeMessage','txt9','Hello\n')
        populate_mail_header ([to],subject)
        sendmail (subject)
        click ('frmEvolution-*', 'btnSend/Receive')
        waittillguiexist ('dlgSend&ReceiveMail')
        waittillguinotexist ('dlgSend&ReceiveMail')
        time.sleep (5)
        new_sent_mail_count=getrowcount (window_id,'ttblMessages')
        if new_sent_mail_count < sent_mail_count+1:
            log ('Could not send mail','cause')
            raise LdtpExecutiontionError (0)
    except:
        log ('Mail was not sent','error')
        log ('Fonts Test','testend')
        raise LdtpExecutionError (0)
    try:
        if verifymailwithimage ('Sent',sent_mail_count,ref_image, subject) ==1:
            log ('Fonts in compose editor ','pass')
        else:
            log ('Fonts in compose editor ','fail')
            raise LdtpExecutionError(0)
    except:
        log ('Fonts in compose editor did not pass','error')
        log ('Fonts Test','testend')
        raise LdtpExecutionError (0)
    log ('Fonts Test','testend')
