#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
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
from evoutils.mail import *
from evoutils.mailpreferences import *
from evoutils.composemail import *
from evoutils.change_status import *
from evoutils.change_properties import *
from evoutils.menu_reorganization import *


def apply_filter(folder,subject):
    log ('Apply Filter','teststart')
    try:
        #selectMailPane()
        window_id='frmEvolution-Mail'
        remap ('evolution',window_id)
        try:
            selectrowpartialmatch (window_id,'ttblMailFolderTree',folder)
        except:
            log ('Folder not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        try:
            selectrow (window_id,'ttblMessageList',subject)
        except:
            log ('Message not available','cause')
            raise LdtpExecutionError (0)

        selectmenuitem (window_id,'mnuMessage;mnuApplyFilters')
        time.sleep (2)
        undoremap ('evolution',window_id)
    except:
        log ('Apply Filter failed','error')
        log ('Apply Filter','testend')
        raise LdtpExecutionError (0)
    log ('Apply Filter','testend')


def movemessage (from_folder,to_folder,subject):
    log ('Move Message','teststart')
    try:
        #selectMailPane()
        window_id='frmEvolution-Mail'
        time.sleep (3)
        #remap ('evolution','frmEvolution-Mail')
        try:
            selectrowpartialmatch (window_id,'ttblMailFolderTree',to_folder)
        except:
            log ('To Folder not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        print "To folder reached"
        initial_dest_count=getrowcount (window_id,'ttblMessageList')
        print initial_dest_count
        try:
            selectrowpartialmatch (window_id,'ttblMailFolderTree',from_folder)
        except:
            log ('From Folder not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        print "from folder reached"
        initial_src_count=getrowcount (window_id,'ttblMessageList')
        print initial_src_count
        time.sleep (2)
        try:
            selectrow (window_id,'ttblMessageList',subject)
        except:
            log ('Message not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (1)
        try:
            selectmenuitem (window_id,'mnuMessage;mnuMovetoFolder')
            waittillguiexist ('dlgSelectfolder')
            selectrowpartialmatch ('dlgSelectfolder','ttblMailFolderTree',to_folder)
        except:
            log ('To Folder not available','cause')
        time.sleep (1)
        if stateenabled ('dlgSelectfolder','btnMove')!=1:
            log ('Move button not enabled','cause')
            raise LdtpExecutionError (0)

        click ('dlgSelectfolder','btnMove')
        time.sleep (3)
        #verification starts here
        new_src_count=getrowcount (window_id,'ttblMessageList')
        print new_src_count
        
        if new_src_count != initial_src_count-1:
            log ('Message still in source folder','cause')
            raise LdtpExecutionError (0)
        
        selectrowpartialmatch (window_id,'ttblMailFolderTree',to_folder)
        time.sleep (1)
        new_dest_count=getrowcount (window_id,'ttblMessageList')
        print new_dest_count
        
        if new_dest_count!=initial_dest_count+1:
            log ('Message not added to Destination folder','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Moving a Message failed','error')
        log ('Move Message','testend')
        raise LdtpExecutionError (0)
    #undoremap ('evolution','frmEvolution-Mail')
    log ('Moving a Message succeeded','info')
    log ('Move Message','testend')
        
            

def copymessage (from_folder,to_folder,subject):
    log ('Copy Message','teststart')
    try:
        #selectMailPane()
        #remap ('evolution','frmEvolution-Mail')
        window_id='frmEvolution-Mail'
        try:
            selectrowpartialmatch (window_id,'ttblMailFolderTree',to_folder)
        except:
            log ('To Folder not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (1)        
        initial_dest_count=getrowcount (window_id,'ttblMessageList')
        
        try:
            selectrowpartialmatch (window_id,'ttblMailFolderTree',from_folder)
        except:
            log ('From Folder not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (1)
        initial_src_count=getrowcount (window_id,'ttblMessageList')
        
        try:
            selectrow (window_id,'ttblMessageList',subject)
        except:
            log ('Message not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (1)        
        try:
            selectmenuitem (window_id,'mnuMessage;mnuCopytoFolder')
            time.sleep (1)
            waittillguiexist ('dlgSelectfolder')
            remap ('evolution','dlgSelectfolder')
            selectrowpartialmatch ('dlgSelectfolder','ttblMailFolderTree',to_folder)
        except:
            log ('To Folder not available','cause')
        time.sleep (1)
        if stateenabled ('dlgSelectfolder','btnCopy')!=1:
            log ('Move button not enabled','cause')
            raise LdtpExecutionError (0)

        click ('dlgSelectfolder','btnCopy')
        time.sleep (3)
        undoremap ('evolution','dlgSelectfolder')
        #verification
        new_src_count=getrowcount (window_id,'ttblMessageList')
        if new_src_count != initial_src_count:
            log ('Message not in source folder','cause')
            raise LdtpExecutionError (0)
        
        selectrowpartialmatch (window_id,'ttblMailFolderTree',to_folder)
        time.sleep (3)
        new_dest_count=getrowcount (window_id,'ttblMessageList')
        print initial_dest_count, new_dest_count
#        raw_input ("abc")
        if new_dest_count!=initial_dest_count+1:
            log ('Message not added to Destination folder','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Copying a message failed','error')
        log ('Copy Message','testend')
        raise LdtpExecutionError (0)
    #undoremap ('evolution','frmEvolution-Mail')
    log ('Copying a message succeeded','info')
    log ('Copy Message','testend')


def deletemessage(folder,subject):
    log ('Delete Message','teststart')
    try:
        #selectMailPane()
        #remap ('evolution','frmEvolution-Mail')
        window_id='frmEvolution-Mail'
        time.sleep (2)
        try:
            selectrowpartialmatch (window_id,'ttblMailFolderTree',folder)
        except:
            log ('Folder not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        initial_count=getrowcount (window_id,'ttblMessageList')
        time.sleep (2)
        try:
            selectrow (window_id,'ttblMessageList',subject)
        except:
            log ('Message not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)

        try:
            selectmenuitem (window_id,'mnuEdit;mnuDeleteMessage')
            time.sleep (1)
        except:
            log ('Unable to select Delete message','cause')
            raise LdtpExecutionError (0)

        #verification
        new_count=getrowcount (window_id,'ttblMessageList')
        
        if new_count != initial_count-1:
            log ('Folder still has mail','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Unable to delete message','error')
        log ('Delete Message','testend')
        raise LdtpExecutionError (0)
    #undoremap ('evolution','frmEvolution-Mail')
    log ('Delete Message successful','info')
    log ('Delete Message','testend')


def saveattachments(folder,subject,save_location):
    log ('Save Attachments','teststart')
    try:
        #selectMailPane()
        #remap ('evolution','frmEvolution-Mail')
        window_id='frmEvolution-Mail'
        try:
            selectrowpartialmatch (window_id,'ttblMailFolderTree',folder)
        except:
            log ('Folder not available','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        try:
            selectrow (window_id,'ttblMessageList',subject)
            time.sleep (2)
            selectmenuitem (window_id,'mnuMessage;mnuOpeninNewWindow')
            setcontext ('Readonlyframe',subject)
            waittillguiexist ('frmReadonly')
            remap ('evolution','frmReadonly')
            time.sleep (3)
        except:
            log ('Message not available','cause')
            raise LdtpExecutionError (0)

        try:
            click ('frmReadonly','btnSaveAll')
            waittillguiexist ('dlgSelectfoldertosaveallattachments')
        except:
            log ('Message does not have attachments','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        try:
            save_location=save_location.split ('/')
            for fldr in save_location:
                doubleclickrow ('dlgSelectfoldertosaveallattachments','tblFiles',fldr)
                time.sleep (1)
            if stateenabled ('dlgSelectfoldertosaveallattachments','btnSave')==0:
                log ('Unable to Save in this folder','cause')
                raise LdtpExecutionError (0)

            click ('dlgSelectfoldertosaveallattachments','btnSave')
        except:
            log ('Unable to find destination folder','cause')
            raise LdtpExecutionError (0)
        selectmenuitem ('frmReadonly','mnuFile;mnuClose')
        undoremap ('evolution','frmReadonly')
        releasecontext()
    except:
        log ('Unable to Save attachments','error')
        log ('Save Attachments','testend')
        raise LdtpExecutionError (0)
    #undoremap ('evolution','frmEvolution-Mail')
    log ('All attachments saved','info')
    log ('Save Attachments','testend')


def delete_folder_when_offline(folder):
    log ('Delete folder while offline','teststart')
    try:
        go_offline ()
        #selectMailPane ()
        if delete_nonsys_folder(folder) == 0:
            log ('Delete folder not permitted while offline','info')
            #log ('Delete folder while offline','testend')
            #return
        else:
            log ('Delete folder allowed while offline','cause')
            log ('Delete folder while offline','testend')
            raise LdtpExecutionError (0)
    
    except:
        log ('Delete folder while offline','testend')
        raise LdtpExecutionError (0)
    log ('Delete folder while offline','testend')
        
def move_folder_when_offline (from_fldr,to_fldr):
    log ('Move folder while offline','teststart')
    try:
        go_offline ()
        #selectMailPane()
    except:
        log ('unable to select Mailpane','error')
        raise LdtpExecutionError (0)
    try:
        move_to (from_fldr,to_fldr)
    except:
        log ('Move folder not permitted while offline','info')
        log ('Move folder while offline','testend')
        return

    log ('Move folder permitted while offline','cause')
    log ('Move folder while offline','testend')
    raise LdtpExecutionError (0)
            

def copy_folder_when_offline (from_fldr,to_fldr):
    log ('Copy folder while offline','teststart')
    try:
        go_offline ()
        #selectMailPane()
    except:
        log ('unable to select Mailpane','error')
        log ('Copy folder while offline','testend')
        raise LdtpExecutionError (0)
    try:

        copy_to (from_fldr, to_fldr)
    except:
        log ('Copy folder not permitted while offline','info')
        log ('Copy folder while offline','testend')
        return

    log ('Copy folder permitted while offline','cause')
    log ('Copy folder while offline','testend')
    raise LdtpExecutionError (0)


def create_folder_when_offline (fldr,location=''):
    log ('create folder while offline','teststart')
    try:
        go_offline ()
        selectmenuitem ('frmEvolution-*','mnuFile;mnuNew;mnuMailFolder')
        #selectMailPane()
    except:
        log ('unable to select Mailpane','error')
        log ('create folder while offline','testend')
        raise LdtpExecutionError (0)
    if create_folder (fldr,location) != 0:
        log ('Create folder permitted while offline','cause')
        log ('create folder while offline','testend')
        raise LdtpExecutionError (0)

    log ('Create folder not permitted while offline','info')
    log ('create folder while offline','testend')


def rename_folder_when_offline (old_name,new_name):
    log ('Rename folder while offline','teststart')
    try:
        go_offline ()
        #selectMailPane()
    except:
        log ('unable to select Mailpane','error')
        log ('Rename folder while offline','testend')
        raise LdtpExecutionError (0)
    try:
        rename (old_name,new_name)
    except:
        log ('Rename not permitted while offline','info')
        log ('Rename folder while offline','testend')
        return

    log ('Rename permitted while offline','cause')
    log ('Rename folder while offline','testend')
    raise LdtpExecutionError (0)


# def expunging_when_offline ():
#     log ('Expunging while offline','teststart')
#     try:
#         go_offline ()
#         #selectMailPane()
#     except:
#         log ('unable to select Mailpane','error')
#         log ('Expunging while offline','testend')
#         raise LdtpExecutionError (0)
#     try:
#         expunge()
#     except:
#         log ('Expunge not permitted while offline','info')
#         log ('Expunging while offline','testend')
#         return

#     log ('Expunge allowed while offline','cause')
#     log ('Expunging while offline','testend')
#     raise LdtpExecutionError (0)


def marking_messages_when_offline(fldr, subject, status='', importance='', junk_status=0, follow_up_flag='', due_date='', time='', progres=''):
    log ('Marking messages when offline','teststart')
    try:
        go_offline()
        change_status(fldr, subject, status, importance, junk_status, follow_up_flag, due_date, time, progres)
    except:
        log ('Change status failed while offline','error')
        log ('Marking messages when offline','testend')
        raise LdtpExecutionError (0)
    log ('Marking messages when offline','testend')

