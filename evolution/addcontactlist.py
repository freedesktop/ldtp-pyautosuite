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
from contact import *

def addnewlist(datafilename):
    """Function to add a new Contact List"""
    log ('Add New List','teststart')
    try:
        ListName,EmailAddresses=getcontactlistvals(datafilename)
        selectContactPane()
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuNew;mnuContactList')
        waittillguiexist ('dlgContactListEditor')
        time.sleep (2)
        settextvalue ('dlgContactListEditor','txtListname',ListName[0])
        setcontext ('Contact List Editor',ListName[0])
        for val in range(len (EmailAddresses)):
            settextvalue ('dlgContactListEditor','txtTypeanemailaddressordragacontactintothelistbelow',EmailAddresses[val])
            click ('dlgContactListEditor','btnAdd')
            time.sleep (1)
            if guiexist ('dlgEvolutionQuery')==1:
                click ('dlgEvolutionQuery','btnCancel')
                time.sleep (1)
        click ('dlgContactListEditor','btnOK')
        time.sleep (5)
        if guiexist ('dlgDuplicateContactDetected')==1:
            log ('contact already exists','info')
            click ('dlgDuplicateContactDetected','btnAdd')
            time.sleep(2)
        verifyaddnewlist (ListName,EmailAddresses)
    except:
        log ('Failed during add new list','error')
        log ('Add New List','testend')
        raise LdtpExecutionError(0)
    log ('Add New List','testend')


def verifyaddnewlist(ListName,EmailAddresses):
    log ('checking if List added successfully','teststart')
    try:
        selectcontact (ListName[0])
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        waittillguiexist ('dlgContactListEditor')
        for val in range (len(EmailAddresses)):
            if (gettablerowindex ('dlgContactListEditor','tbl0',EmailAddresses[val])) == -1:
                raise LdtpExecutionError(0)
        click ('dlgContactListEditor','btnCancel')
    except:
        log ('Contact List Addition failed during Verification','error')
        log ('checking if List added successfully','testend')
        raise LdtpExecutionError(0)
    log ('checking if List added successfully','testend')

        
addnewlist (datafilename)
