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

def modifycontact(datafilename):
    log('Contact Modificaton','teststart')

    try:
        AddrBook,Name,NewWorkEmail,NewHomeEmail,NewHomeAdd,NewWorkAdd,NewOtherAdd=getmodifiedvals(datafilename)
#        print AddrBook,Name,NewWorkEmail,NewHomeEmail,NewHomeAdd,NewWorkAdd,NewOtherAdd
        if AddrBook != []:
            selectaddrbook (AddrBook[0])
            time.sleep (2)
        selectcontact (titleappend(Name[0])[1:])
        time.sleep (2)
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        setcontext ('Contact Editor','Contact Editor -'+titleappend(Name[0]))
        waittillguiexist ('dlgContactEditor')
        if len (NewWorkEmail)>0:
            settextvalue ('dlgContactEditor','txtWork',NewWorkEmail[0])
        time.sleep (1)
        if len (NewHomeEmail)>0:
            settextvalue ('dlgContactEditor','txtHome',NewHomeEmail[0])
        time.sleep (1)
        if len(NewHomeAdd)>0:
            settextvalue ('dlgContactEditor','txtAddress',NewHomeAdd[0])
        time.sleep (1)
        if len(NewWorkAdd)>0:
            settextvalue ('dlgContactEditor','txtAddress1',NewWorkAdd[0])
        time.sleep (1)
        if len(NewOtherAdd)>0:
            settextvalue ('dlgContactEditor','txtAddress2',NewOtherAdd[0])
        time.sleep (1)
        click ('dlgContactEditor','btnOK')
        time.sleep (3)
        if guiexist ('dlgDuplicateContactDetected')==1:
            click ('dlgDuplicateContactDetected','btnAdd')
        verifymodifications(AddrBook,Name,NewWorkEmail,NewHomeEmail,NewHomeAdd,NewWorkAdd,NewOtherAdd)
    except:
        log ('Error While Modifying values','error')
        log('Contact Modificaton','testend')
        raise LdtpExecutionError(0)
    log('Contact Modificaton','testend')

        
def getmodifiedvals(datafilename):
    log ('Getting values for Contact Modification','teststart')
    try:
        data_object = LdtpDataFileParser (datafilename)
        AddrBook=data_object.gettagvalue ('AddrBook')
        Name=data_object.gettagvalue ('Name')
        NewWorkEmail=data_object.gettagvalue ('WorkEmail')
        NewHomeEmail=data_object.gettagvalue ('HomeEmail')
        NewHomeAdd=data_object.gettagvalue ('HomeAddress')
        NewWorkAdd=data_object.gettagvalue ('WorkAddress')
        NewOtherAdd=data_object.gettagvalue ('OtherAddress')
    except:
        log ('data read failed','error')
        log ('Getting values for Contact Modification','testend')
        raise LdtpExecutionError(0)
    log ('Getting values for Contact Modification','testend')
    return AddrBook,Name,NewWorkEmail,NewHomeEmail,NewHomeAdd,NewWorkAdd,NewOtherAdd


def verifymodifications(AddrBook,FullName,WorkEmail,HomeMail,HomeAdd,WorkAdd,OtherAdd):
    log ('Verify Modified Contact','teststart')
    try:
        selectaddrbook(AddrBook[0])
        selectcontact(titleappend(FullName[0])[1:])
        time.sleep (2)
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        title='dlgContactEditor-'+titleappend(FullName[0]).replace(' ','')
        setcontext ('Contact Editor','Contact Editor -'+titleappend(FullName[0]))
        waittillguiexist ('dlgContactEditor')
        time.sleep(2)
#         print gettextvalue ('dlgContactEditor','txtFullName')
#         print FullName[0]
#         print "full name"
        if gettextvalue ('dlgContactEditor','txtFullName')!=FullName[0]:
            log ('Full Name does not match','info')
            raise LdtpExecutionError(0)
#        print "Full Name over"
        if len (WorkEmail)>0 and gettextvalue ('dlgContactEditor','txtWork')!=WorkEmail[0]:
            log ('Work Email matches','info')
            raise LdtpExecutionError(0)
        if len(HomeMail)>0 and  gettextvalue ('dlgContactEditor','txtHome')!=HomeMail[0]:
            log ('Home Email matches','info')
            raise LdtpExecutionError(0)
## BUG IN EVOLUTION ##
## evo 2.5.2 stores an extra new line char at the end of the address fields
## uncommment the following lines when bug fixed 
#         if len(HomeAdd)>0 and   gettextvalue ('dlgContactEditor','txtAddress')!=HomeAdd[0]:
#             log ('Home Address matches','info')
#             raise LdtpExecutionError(0)
#         if len (WorkAdd)>0 and  gettextvalue ('dlgContactEditor','txtAddress1')!=WorkAdd[0]:
#             log ('Work Address matches','info')
#             raise LdtpExecutionError(0)
#         if len(OtherAdd)>0 and  gettextvalue ('dlgContactEditor','txtAddress2')!=OtherAdd[0]:
#             log ('Other Address matches','info')
#             raise LdtpExecutionError(0)
        click ('dlgContactEditor','btnCancel')
    except:
        log ('Contact has not been modified correctly','error')
        log ('Verify Modified Contact','testend')
        raise LdtpExecutionError(0)
    log ('Verify Modified Contact','testend')

modifycontact(datafilename)
