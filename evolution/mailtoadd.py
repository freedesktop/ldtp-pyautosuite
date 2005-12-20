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
from contact import titleappend
from evoutils.mail import *

def mailtoaddbook(datafilename):
    log ('Add Mail Sender to Address Book','teststart')
    try:
        data_object = LdtpDataFileParser (datafilename)
        subject=data_object.gettagvalue ('subject')
        selectMailPane()
        time.sleep (2)
        try:
            remap ('evolution','frmEvolution-Mail')
            selectrowpartialmatch ('frmEvolution-Mail','ttblMailFolderTree','Inbox')
            time.sleep (2)
            selectrow ('frmEvolution-Mail','ttblMessageList',subject[0])
            time.sleep (1)
            row=getrowindex (subject[0])
            name=getcellvalue ('frmEvolution-Mail','ttblMessageList',row,3)
            name=name[:name.find('<')]
            name=name[:-1]
        except:
            log ('Row not found in list','error')
            raise LdtpExecutionError(0)
        selectmenuitem ('frmEvolution-Mail','mnuMessage;mnuAddSendertoAddressBook')
        print name
        time.sleep (5)
        print name.find(' ')
        if name.find (' ') >-1:
            setcontext ('Contact Editor','Contact Editor -'+titleappend(name))
        else:
            setcontext ('Contact Editor','Contact Editor - '+name)
        print 'Contact Editor -'+titleappend(name)
        if guiexist ('dlgContactQuick-Add')==1:
            click ('dlgContactQuick-Add','btnOK')
        elif guiexist ('dlgContactEditor')==1:
            click ('dlgContactEditor','btnCancel')
        undoremap ('evolution','frmEvolution-Mail')
    except:
        log ('Adding mail sender to Address Book failed','error')
        log ('Add Mail Sender to Address Book','testend')
        raise LdtpExecutionError(0)
    log ('Add Mail Sender to Address Book','testend')

mailtoaddbook (datafilename)
