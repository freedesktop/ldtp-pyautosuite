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


from ldtp import *
from ldtputils import *
from contact import getcurwindow

def deletemailaccount (account_name):
    log ('Delete E-Mail Account','teststart')
    try:
        try:
            selectmenuitem ('frmEvolution-Mail','mnuEdit;mnuPreferences')
            waittillguiexist ('dlgEvolutionSettings')
            if verifyaccountexist (account_name)== -1:
                raise LdtpExecutionError (0)
            selectrowpartialmatch ('dlgEvolutionSettings','tblMailAccountsTable',account_name)
        except:
            log ('Account not present','cause')
            raise LdtpExecutionError (0)

        try:
            click ('dlgEvolutionSettings','btnRemove')
            waittillguiexist ('dlgDeleteaccount?')
            click ('dlgDeleteaccount?','btnDelete')
        except:
            log ('Unable to delete the account','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        if verifyaccountexist (account_name) == -1:
            log ('Delete Account','pass')
        else:
            log ('Delete Account','fail')
            raise LdtpExecutionError (0)
        click ('dlgEvolutionSettings','btnClose')
    except:
        log ('Unable to delete account','error')
        log ('Delete E-Mail Account','testend')
        raise LdtpExecutionError (0)
    log ('Delete E-Mail Account','testend')


def verifyaccountexist (account_name):
    try:
        print account_name
        numofchild=getrowcount ('dlgEvolutionSettings','tblMailAccountsTable')
        for num in range (numofchild):
            if getcellvalue ('dlgEvolutionSettings','tblMailAccountsTable',num,1).startswith (account_name):
                print num
                return num

        return -1
    except:
        log ('Unable to verify if account exists','error')
        raise LdtpExecutionError (0)


def enablemailaccount (account_name):
    log ('Enable Mail Account','teststart')
    try:
        try:
            selectmenuitem ('frmEvolution-Mail','mnuEdit;mnuPreferences')
            waittillguiexist ('dlgEvolutionSettings')
            index=verifyaccountexist (account_name)
            if index==-1:                                 
                raise LdtpExecutionError (0)
            selectrowpartialmatch ('dlgEvolutionSettings','tblMailAccountsTable',account_name)
        except:
            log ('Account not present','cause')
            raise LdtpExecutionError (0)

        try:
            selectrow ('dlgEvolutionSettings','tblMailAccountsTable',name)
            time.sleep (2)
            checkrow ('dlgEvolutionSettings','tblMailAccountsTable',index,0)
            checkrow ('dlgEvolutionSettings','tblMailAccountsTable',index,0)
        except:
            log ('Unable to enable Mail Account','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        #verification

        try:
            selectrowpartialmatch ('frmEvolution-Mail','ttblMailFolderTree',account_name)
        except:
            log ('Enable Account','fail')
            raise LdtpExecutionError (0)
        log ('Enable Account','pass')
        click ('dlgEvolutionSettings','btnClose')
    except:
        log ('Mail Account not enabled','error')
        log ('Enable Mail Account','testend')
        raise LdtpExecutionError (0)
    log ('Enable Mail Account','testend')

            
def disablemailaccount (account_name):
    log ('Disable Mail Account','teststart')
    try:
        try:
            selectmenuitem ('frmEvolution-Mail','mnuEdit;mnuPreferences')
            waittillguiexist ('dlgEvolutionSettings')
            index=verifyaccountexist (account_name)
            if index==-1:                                 
                raise LdtpExecutionError (0)
            selectrowpartialmatch ('dlgEvolutionSettings','tblMailAccountsTable',account_name)
            time.sleep (2)
        except:
            log ('Account not present','cause')
            raise LdtpExecutionError (0)

        try:
            uncheckrow ('dlgEvolutionSettings','tblMailAccountsTable',index,0)
            uncheckrow ('dlgEvolutionSettings','tblMailAccountsTable',index,0)
        except:
            log ('Unable to disable Mail Account','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        #verification

        try:
            print account_name
            selectrowpartialmatch ('frmEvolution-Mail','ttblMailFolderTree',account_name)
        except:
            log ('Disable Account','pass')
            log ('Disable Mail Account','testend')
            click ('dlgEvolutionSettings','btnClose')
            return
        log ('Disable Account','fail')
        raise LdtpExecutionError (0)
    except:
        log ('Mail Account not Disabled','error')
        log ('Disable Mail Account','testend')
        raise LdtpExecutionError (0)


def makedefault (account_name):
    log ('Make Mail account default','teststart')
    try:
        time.sleep (3)
        try:
            selectmenuitem ('frmEvolution-Mail','mnuEdit;mnuPreferences')
            waittillguiexist ('dlgEvolutionSettings')
            index=verifyaccountexist (account_name)
            if index==-1:                                 
                raise LdtpExecutionError (0)
            selectrowpartialmatch ('dlgEvolutionSettings','tblMailAccountsTable',account_name)
            time.sleep (2)
        except:
            log ('Account not present','cause')
            raise LdtpExecutionError (0)

        try:
            click ('dlgEvolutionSettings','btnDefault')
            time.sleep (2)
            name=getcellvalue ('dlgEvolutionSettings','tblMailAccountsTable',index,1)
            desired_name=account_name+' '+'[Default]'
            if name == desired_name:
                log ('Set Default','pass')
            else:
                log ('Set Default','fail')
        except:
            log ('Unable to make account as default','error')
            raise LdtpExecutionError (0)
    except:
        log ('Make Account default failed','error')
        log ('Make Mail account default','testend')
        raise LdtpExecutionError (0)
    click ('dlgEvolutionSettings','btnClose')
    log ('Make Mail account default','testend')




def restartevolution():
    log ('Restart Evolution','teststart')
    try:
        time.sleep (3)
        window_id = 'frmEvolution-Mail'
        remap ('evolution',window_id)
        selectmenuitem (window_id,'mnuFile;mnuQuit')
        waittillguinotexist (window_id)
        undoremap ('evolution',window_id)
        time.sleep (2)
        launchapp ('evolution',1)
        time.sleep (2)
        if guiexist (window_id) == 1:
            log ('Evolution Restarted successfully','info')
        else:
            log ('Evolution window not open','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Restart evolution failed','error')
        log ('Restart Evolution','testend')
        raise LdtpExecutionError (0)
    log ('Restart Evolution','testend')
