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
from evoutils.mail import *
from evoutils import *

def mailtoaddbook(datafilename):
    log ('Add Mail Sender to Address Book','teststart')
    try:
        data_object = LdtpDataFileParser (datafilename)
        subject = data_object.gettagvalue ('subject')
        selectMailPane()
        time.sleep (2)
        try:
            selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree','Inbox')
            waittillguiexist ('frmEvolution-Inbox*')
            time.sleep (2)
            selectrow ('frmEvolution-*','ttblMessages',subject[0])
            time.sleep (1)
            row=getrowindex (subject[0])
            name=getcellvalue ('frmEvolution-*','ttblMessages',row,3)
            name=name[:name.find('<')]
            name=name[:-1]
        except:
            log ('Row not found in list','error')
            raise LdtpExecutionError(0)
        selectmenuitem ('frmEvolution-*','mnuMessage;mnuAddSendertoAddressBook')
        print name
        time.sleep (5)
        if guiexist ('dlgContactQuick-Add')==1:
            click ('dlgContactQuick-Add','btnOK')
        elif guiexist ('dlgContactEditor')==1:
            click ('dlgContactEditor','btnCancel')

        time.sleep (3)
        if guiexist ('*DuplicateContactDetected*') == 1:
            click ('*DuplicateContactDetected*', 'btnAdd');
            waittillguinotexist ('*DuplicateContactDetected*')
        else:
            waittillguinotexist ('dlgContactQuick-Add')
    except:
        log ('Adding mail sender to Address Book failed','error')
        log ('Add Mail Sender to Address Book','testend')
        raise LdtpExecutionError(0)
    log ('Add Mail Sender to Address Book','testend')

mailtoaddbook (datafilename)
