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


from mailaccounts import restartevolution
from contact import *
from evoutils.change_status import *


def emptytrashonexit():
    log ('Empty Trash on Exit','teststart')
    try:
        selectMailPane()
        time.sleep (2)
        selectmenuitem ('frmEvolution-Mail','mnuEdit;mnuPreferences')
        window_id='dlgEvolutionSettings'
        waittillguiexist (window_id)
        time.sleep (1)
        selecttab (window_id, 'ptl0', 'Mail Preferences')
        time.sleep (1)
        remap ('evolution',window_id)
        check (window_id,'chkEmptytrashfoldersonexit')
        time.sleep (1)
        if verifycheck (window_id,'chkEmptytrashfoldersonexit') == 0:
            log ('Unable to check option','cause')
            raise LdtpExecutionError (0)
        comboselect (window_id,'cboEverytime','Every time')
        click (window_id,'btnClose')
    except:
        log ('Unable to enable empty trash on exit','error')
        log ('Empty Trash on Exit','testend')
        raise LdtpExecutionError (0)
    undoremap ('evolution',window_id)

    #verification
    try:
        restartevolution()
        time.sleep (3)
        selectrowpartialmatch ('frmEvolution-Mail','ttblMailFolderTree','Trash')
        waittillguiexist ('frmEvolution-Trash*)
        msgs_in_trash = getrowcount ('frmEvolution-Mail','ttblMessageList')
        if msgs_in_trash != 0:
            log ('trash stil has some messages','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Automatic trash emptying on exit failed','error')
        log ('Empty Trash on Exit','testend')
        raise LdtpExecutionError (0)
    log ('Empty Trash on Exit','testend')
            


def mark_msg_as_read (fldr,subject,time='3'):
    log ('Automatically mark messages as read','teststart')
    try:
        selectMailPane()
        time.sleep (2)
        selectmenuitem ('frmEvolution-Mail','mnuEdit;mnuPreferences')
        window_id='dlgEvolutionSettings'
        waittillguiexist (window_id)
        time.sleep (1)
        selecttab (window_id, 'ptl0', 'Mail Preferences')
        time.sleep (1)
        remap ('evolution',window_id)
        check (window_id,'chkMarkmessagesasreadafter')
        time.sleep (1)
        if verifycheck (window_id,'chkMarkmessagesasreadafter') == 0:
            log ('Unable to select option for atuomatically marking messages are read','cause')
            raise LdtpExecutionError (0)
        setvalue (window_id,'stbn0',time)
        time.sleep (1)
        if verifysetvalue (window_id,'sbtn0',time) == 0:
            log ('Unable to set value of time before marking unread','cause')
            raise LdtpExecutionError (0)
        click (window_id,'btnClose')
    except:
        log ('could not enable automatic marking of messages as read','error')
        log ('Automatically mark messages as read','testend')
        raise LdtpExecutionError (0)

    try:
        change_status (fldr,subject,'unread')
        time.sleep (int(time))
        Row_index=getrowindex(subject)
        if getcellvalue('frmEvolution-Mail','ttblMessageList',Row_index,0) == 1:
            log ('Message did not change to unread status','cause')
            raise LdtpExecutionError (0)
    except:
        log ('verification of automatically marking messages as read failed','error')
        log ('Automatically mark messages as read','testend')
        raise LdtpExecutionError (0)
            


    
        
