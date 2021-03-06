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

from ldtp import *
from ldtputils import *
from mailtests import closecomposewindow
from contact import *
from evoutils.mail import *
from evoutils import *

def addnewsignature(name,text):
    log ('Add New Signature','teststart')
    try:
        selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab ('dlgEvolutionPreferences', 'ptl0', 'Composer Preferences')
            time.sleep (1)
            selecttab ('dlgEvolutionPreferences', 'ptl2','Signatures')
            time.sleep (1)
            click (window_id,'btnAdd2')
            waittillguiexist ('frmEditsignature')
            time.sleep (1)
        except:
            log ('Unable to open Edit Signature window','cause')
            raise LdtpExecutionError (0)
        fillinsignaturevalues(name,text)
        time.sleep (2)
        #verification code
        # verifysignature (name,text) http://bugzilla.gnome.org/show_bug.cgi?id=324241
        num=getrowcount (window_id,'tblSignatures')
        flag=False
        for x in range (num):
            if getcellvalue (window_id,'tblSignatures',x,0) == name:
                flag=True
                break
        click (window_id,'btnClose')
        if flag==True:
            log ('Signature added successfully','info')
            return 1
        else:
            log ('Signature not added succcessfully','cause')
            return 0
            raise LdtpExecutionError (0)
    except:
        log ('Add New Signature failed','error')
        log ('Add New Signature','testend')
        raise LdtpExecutionError (0)
    log ('Add New Signature','testend')


def fillinsignaturevalues (name,text):
    try:
        window_id='frmEditsignature'
        settextvalue (window_id,'txt0',name)
        settextvalue (window_id,'txt1',text)
        time.sleep (1)
        click (window_id,'btnSaveandClose')
        time.sleep (5)
        if guiexist ('*EvolutionError'):
            click ('*EvolutionError','btnOK')
        waittillguinotexist (window_id)
    except:
        log ('Unable to fill in values for signature','cause')
        raise LdtpExecutionError (0)

def verifysignature (name,text):
    window_id='dlgEvolutionPreferences'
    try:
        selectrow (window_id,'tblSignatures',name)
    except:
        log ('Signature not added','cause')
        raise LdtpExecutionError (0)
    try:
        time.sleep (1)
        click (window_id,'btnEdit1')
        waittillguiexist ('frmEditsignature')
        if verifysettext ('frmEditSignature','txt0',name) ==0:
            log ('Name not set properly','cause')
            raise LdtpExecutionError (0)
        if verifysettext ('frmEditSignature','txt1',text) == 0:
            log ('text not set properly','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Signature not set properly','error')
        raise LdtpExecutionError (0)
            

def edit_signature (name,text,newname=''): #http://bugzilla.gnome.org/show_bug.cgi?id=324241
    log ('Edit Signature','teststart')
    try:
        selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab ('dlgEvolutionPreferences', 'ptl0', 'Composer Preferences')
            time.sleep (1)
            selecttab ('dlgEvolutionPreferences', 'ptl2','Signatures')
            time.sleep (1)
            try:
                selectrow ('dlgEvolutionPreferences','tblSignatures',name)
            except:
                log ('signature not present','cause')
                raise LdtpExecutionError (0)
            time.sleep (1)
            click (window_id,'btnEdit1')
            waittillguiexist ('frmEditsignature')
            time.sleep (1)
        except:
            log ('Unable to open Edit Signature window','cause')
            raise LdtpExecutionError (0)
        if newname !='':
            name=newname
        fillinsignaturevalues(name,text)
        
        #verifysignature (name,text)
    except:
        log ('Edit Signature failed','error')
        log ('Edit Signature','testend')
        raise LdtpExecutionError (0)
    #undoremap ('evolution',window_id)
    log ('Edit Signature','testend')


def removesignature(name):
    log ('Remove Signature','teststart')
    try:
        selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionSettings'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
            selecttab (window_id, 'ptl2','Signatures')
            time.sleep (1)
            try:
                selectrow (window_id,'tblSignatures',name)
            except:
                log ('signature not present','cause')
                raise LdtpExecutionError (0)
            time.sleep (1)
            click (window_id,'btnRemove2')
        except:
            log ('Unable to remove signature','cause')
            raise LdtpExecutionError (0)

        try:
            #verification
            num = getrowcount (window_id,'tblSignatures')
            flag = 0
            for x in range (num):
                if getcellvalue (window_id,'tblSignatures',x,0) == name:
                    flag=1
                    break
            if flag == 1:
                log ('Signature not removed','cause')
                raise LdtpExecutionError (0)
            else:
                log ('Signature removed succcessfully','cause')
        except:
            log ('Remove signature verification failed','error')
            raise LdtpExecutionError (0)
    except:
        log ('Remove signature failed','error')
        log ('Remove Signature','testend')
        raise LdtpExecutionError (0)
    log ('Remove Signature','testend')
    

def format_in_HTML (to, text):
    log ('format messages in HTML','teststart')
    try:
        if to == [] or text == []:
            log ('Not enough input available','cause')
            raise LdtpExecutionError (0)
        to = to[0]
        text = text[0]
        subject = 'Test for HTML formatting'
        selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
            selecttab (window_id, 'ptl2','General')
            check (window_id,'chkFormatmessagesinHTML')
            time.sleep (1)
            if verifycheck (window_id,'chkFormatmessagesinHTML')==0:
                log ('Checkbox not checked','cause')
                raise LdtpExecutionError (0)
        except:
            log ('Unable to select HTML formatting','error')
            raise LdtpExecutionError (0)

        click (window_id,'btnClose')
        
        try:
            selectmenuitem ('frmEvolution-*','mnuFile;mnuNew;mnuMailMessage')
            waittillguiexist ('frmComposeMessage')
            settextvalue ('frmComposeMessage','txtTo',to)
            settextvalue ('frmComposeMessage','txt6',text)
            settextvalue ('frmComposeMessage','txtSubject',subject)
            compose_window = get_mail_name (subject)
            click (compose_window,'btnSend')
            time.sleep (2)
            if guiexist ('dlgEvolutionQuery') != 1:
                log ('Warning for HTML formatting did not come up','cause')
                raise LdtpExecutionError (0)
            click ('dlgEvolutionQuery','btnCancel')
            closecomposewindow (0, compose_window)
        except:
            log ('Verification Failed','error')
            raise LdtpExecutionError (0)

        #undo setting HTML formatting
        try:
            
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
            uncheck (window_id,'chkFormatmessagesinHTML')
        except:
            log ('Unable to unselect HTML formatting','error')
            raise LdtpExecutionError (0)

        click (window_id,'btnClose')
    except:
        log ('setting default HTML formatting failed','error')
        log ('format messages in HTML','testend')
        raise LdtpExecutionError (0)
    log ('format messages in HTML','testend')

    
def changelanginspellcheck():
    log ('Enable languages in Composer preferences for spell check','teststart')
    try:
        time.sleep (3)
        #selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
            #remap ('evolution',window_id)
            selecttab (window_id, 'ptl2','Spell Checking')
            noofrows=getrowcount ('dlgEvolutionPreferences','tblLanguages')
            langs = []
            for x in range (noofrows):
                checkrow ('dlgEvolutionPreferences','tblLanguages',x,0)
                langs.append (getcellvalue ('dlgEvolutionPreferences','tblLanguages',x,1))
            click ('dlgEvolutionPreferences','btnClose')
        except:
            log ('Unable to select languages','cause')
            raise LdtpExecutionError (0)

        #verification
        try:
            selectmenuitem ('frmEvolution-*','mnuFile;mnuNew;mnuMailMessage')
            waittillguiexist ('frmComposeMessage')
            settextvalue ('frmComposeMessage','txt6','\nHelo ande wlcme')
            selectmenuitem ('frmComposeMessage','mnuEdit;mnuSpellCheckDocument')
            waittillguiexist ('dlgSpellchecker')
            for lang in langs:
                try:
                    comboselect ('dlgSpellchecker','cboAddtodictionary',lang)
                    time.sleep (1)
                except:
                    log ('Unable to select Language which was enabled','cause')
                    raise LdtpExecutionError (0)
            time.sleep (2)
            click ('dlgSpellchecker','btnClose')
            time.sleep (2)
            closecomposewindow (0)
        except:
            log ('verification for select languages failed','error')
            raise LdtpExecutionError (0)
    except:
        log ('Unable to select languages for spell checking','error')
        log ('Enable languages in Composer preferences for spell check','testend')
        raise LdtpExecutionError (0)
    log ('Enable languages in Composer preferences for spell check','testend')


def forwardstyle(fldr,subject):
    log ('Changing forward styles','teststart')
    try:
        selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
#             for combo in getobjectlist (window_id):
#                 if combo in ['cboQuoted','cboAttachment','cboInline']:
#                     break

            comboselect (window_id,'cboForwardstyle','Attachment')
            click (window_id,'btnClose')
            time.sleep (2)
            selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',fldr)
            waittillguiexist ('frmEvolution-'+fldr+'*')
            time.sleep (2)
            selectrow ('frmEvolution-*','ttblMessages',subject)
            message_id = get_mail_name (subject)
            selectmenuitem ('frmEvolution-*','mnuMessage;mnuOpeninNewWindow')
            waittillguiexist (message_id)
            time.sleep (2)
            text = getsentmailtext (message_id)
            print text
            selectmenuitem (message_id,'mnuFile;mnuClose')
            waittillguinotexist (message_id)
            click ('frmEvolution-*','btnForward')                        
            message_id = get_mail_name('[Fwd: '+subject+']')
            waittillguiexist (message_id)
            time.sleep (2)
            fwdtext = getmailtext (message_id)
            if fwdtext == '':
                log ('Forward style - Attachment works fine','info')
            else:
                log ('Forward style - Attachment not proper','cause')
                raise LdtpExecutionError (0)

            selectmenuitem (message_id,'mnuFile;mnuClose')
            waittillguinotexist (message_id)
        except:
            log ('Forward style Attachment failed','error')
            raise LdtpExecutionError (0)

        try:            
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
#             for combo in getobjectlist (window_id):
#                 if combo in ['cboQuoted','cboAttachment','cboInline']:
#                     break

            comboselect (window_id,'cboForwardstyle','Inline')
            click (window_id,'btnClose')
            click ('frmEvolution-*','btnForward')
            waittillguiexist (message_id)
            time.sleep (2)
            fwdtext = getmailtext (message_id)
            print 'FWD TEXT: ',fwdtext,'TEXT: ',text
            fwdtext.find (text)
            if not fwdtext.startswith ('-------- Forwarded Message --------'):
                    log ('Forward style - Inline not proper','cause')
                    raise LdtpExecutionError (0)
            if fwdtext.find (text) == -1:
                log ('Forward style - Inline not proper','cause')
                raise LdtpExecutionError (0)
            else:
                log ('Forward style - Inline works fine','info')
            selectmenuitem (message_id,'mnuFile;mnuClose')
            waittillguinotexist (message_id)
        except:
            log ('Forward style Inline failed','error')
            raise LdtpExecutionError (0)
    except:
        log ('Attachement style selection failed','error')
        log ('Changing forward styles','testend')
        raise LdtpExecutionError (0)
    log ('Changing forward styles','testend')


def prompt_for_empty_subject(to):
    log ('Prompt for empty subject line','teststart')
    try:
        #selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
            check (window_id,'chkPromptwhensendingmessageswithanemptysubjectline')
            time.sleep (1)
            if verifycheck (window_id,'chkPromptwhensendingmessageswithanemptysubjectline') == 0:
                log ('Unable to check option','cause')
                raise LdtpExecutionError (0)
            click (window_id,'btnClose')
            waittillguinotexist (window_id)
        except:
            log ('Unable to Enable prompt for empty subject line','cause')
            raise LdtpExecutionError (0)

        try:
            selectmenuitem ('frmEvolution-*','mnuFile;mnuNew;mnuMailMessage')
            waittillguiexist ('frmComposeMessage')
            settextvalue ('frmComposeMessage','txtTo',to)
            click ('frmComposeMessage','btnSend')
            if waittillguiexist ('dlgEvolutionQuery') == 0:
                log ('Prompt did not appear','cause')
                raise LdtpExecutionError (0)
            time.sleep (1)
            click ('dlgEvolutionQuery','btnSend')
            waittillguinotexist ('frmComposeMessage')
        except:
            log ('Prompting for empty subject line failed for verification','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Enabling Empty subject line failed','error')
        log ('Prompt for empty subject line','testend')
        raise LdtpExecutionError (0)
    log ('Prompt for empty subject line','testend')


def prompt_for_only_bcc (to):
    log ('Prompt for only bcc recepients','teststart')
    try:
        #selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Composer Preferences')
            time.sleep (1)
            remap ('evolution',window_id)
            check (window_id,'chkPromptwhensendingmessageswithonlyBccrecipientsdefined')
            time.sleep (1)
            if verifycheck (window_id,'chkPromptwhensendingmessageswithonlyBccrecipientsdefined') == 0:
                log ('Unable to check option','cause')
                raise LdtpExecutionError (0)
            click (window_id,'btnClose')
            waittillguinotexist (window_id)
        except:
            log ('Unable to Enable prompt for only bcc recepients','cause')
            raise LdtpExecutionError (0)

        try:
            selectmenuitem ('frmEvolution-*','mnuFile;mnuNew;mnuMailMessage')
            compose_id = 'frmComposeMessage'
            waittillguiexist (compose_id)
            settextvalue (compose_id,'txtBcc',to)
            settextvalue (compose_id,'txtSubject','Test for prompt for only bcc recepients')
            #setcontext ('Compose a message','Test for prompt for only bcc recepients')
            compose_id = get_mail_name ('Test for prompt for only bcc recepients')
            click (compose_id,'btnSend')
            time.sleep (5)
            if waittillguiexist ('dlgEvolutionWarning') == 0:
                log ('Prompt did not appear','cause')
                raise LdtpExecutionError (0)
            remap ('evolution','dlgEvolutionWarning')
            click ('dlgEvolutionWarning','btnSend')
        except:
            log ('Prompting for only bcc recepients failed for verification','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Enabling prompt for only bcc recepients failed','error')
        log ('Prompt for only bcc recepients','testend')
        raise LdtpExecutionError (0)
        
    log ('Prompt for only bcc recepients','testend')


def prompt_when_expunging(fldr):
    log ('Check for Prompting when expunging','teststart')
    try:
        #selectMailPane()
        try:
            selectmenuitem ('frmEvolution-*','mnuEdit;mnuPreferences')
            window_id='dlgEvolutionPreferences'
            waittillguiexist (window_id)
            time.sleep (1)
            selecttab (window_id, 'ptl0', 'Mail Preferences')
            time.sleep (1)
            #remap ('evolution',window_id)
            check (window_id,'chkConfirmwhenexpungingafolder')
            time.sleep (1)
            if verifycheck (window_id,'chkConfirmwhenexpungingafolder') == 0:
                log ('Unable to check checkbox','cause')
                raise LdtpExecutionError (0)
            click (window_id,'btnClose')
        except:
            log ('Unable to enable prompting before expunging','cause')
            raise LdtpExecutionError (0)
        #verification for prompt
        try:
            selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',fldr)
            waittillguiexist ('frmEvolution-'+fldr+'*')
            time.sleep (1)
            selectmenuitem ('frmEvolution-*','mnuFolder;mnuExpunge')
            if waittillguiexist ('dlgEvolutionQuery') == 0:
                log ('Prompt did not show','cause')
                raise LdtpExecutionError (0)
            remap ('evolution','dlgEvolutionQuery')
            click ('dlgEvolutionQuery','btnCancel')
        except:
            raise LdtpExecutionError (0)
        #verification for expunging

#         if getrowcount ('frmEvolution-*','ttblMessageList') != 0:
#             log ('Expunging failed','cause')
#             raise LdtpExecutionError (0)

    except:
        log ('Enabling prompt while expunging failed','error')
        log ('Check for Prompting when expunging','testend')
        raise LdtpExecutionError (0)
    log ('Check for Prompting when expunging','testend')
