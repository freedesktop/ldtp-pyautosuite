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

def modcontactlist(datafilename):
    log ('Modify Contact List','teststart')
    try:
        ListName,AddEmailAddresses,DelEmailAddresses=getmodlistvals(datafilename)
        name = '*'+ListName[0]+'*'
        opencontactlist(ListName)
        addtocontactlist (AddEmailAddresses, name)
        delfromcontactlist (DelEmailAddresses, name)
        click (name,'btnOK')
        time.sleep (2)
        verifymodifylist(ListName,AddEmailAddresses,DelEmailAddresses)
    except:
        log ('Unable to modify Contact List','error')
        log ('Modify Contact List','testend')
        raise LdtpExecutionError(0)
    log ('Modify Contact List','testend')

    
def addtocontactlist(addList, name):
    try:
        for val in range(len (addList)):
            settextvalue (name,'txtTypeanemailaddressordragacontactintothelistbelow',addList[val])
            print 'set the list value'
            click (name,'btnAdd')
            time.sleep (1)
            if guiexist ('dlgEvolutionQuery')==1:
                click ('dlgEvolutionQuery','btnCancel')
                time.sleep (1)
    except:
        log ('error while adding contacts to contact list','error')
        raise LdtpExecutionError(0)

def delfromcontactlist (remList, name):
    try:
        for val in range(len(remList)):
            try:
                selectrow (name,'tbl0',remList[val])
            except:
                log (remList[val]+' not in List','error')
            time.sleep (1)
            click (name,'btnRemove')
            time.sleep (1)
    except:
        log ('Contact could not be deleted from contact list','error')
        raise LdtpExecutionError(0)

def verifymodifylist(ListName,InEmail,OutEmail):
    try:
        opencontactlist(ListName)
        name = '*'+ListName[0]+'*'
        setcontext ('Contact List Editor',ListName[0])
        waittillguiexist (name)
        for value in InEmail:
            if (gettablerowindex (name,'tbl0',value)) == -1:
                raise LdtpExecutionError(0)

#        print "values in inemail perfect"
#        raw_input ("input")
#         for value in OutEmail:
#             if (gettablerowindex ('dlgContactListEditor','tbl0',EmailAddresses[val])) != -1:
#                 raise LdtpExecutionError(0)
        click (name,'btnCancel')
    except:
        log ('Contact List Modification has failed verification','error')
        raise LdtpExecutionError(0)
    
modcontactlist (datafilename)
