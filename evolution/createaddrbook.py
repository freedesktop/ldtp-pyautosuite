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

def newaddrbook(datafilename):

    log ('Create New Address Book','teststart')
    try:
        data_object = LdtpDataFileParser (datafilename)
        Name=data_object.gettagvalue ('Name')
        #print Name
        #time.sleep (10)
        #selectContactPane()
        window_id=getcurwindow()
        selectmenuitem (window_id,'mnuFile;mnuNew;mnuAddressBook')
        waittillguiexist ('dlgNewAddressBook')
        time.sleep (3)
        comboselect ('dlgNewAddressBook','cboType','On This Computer')
        settextvalue ('dlgNewAddressBook','txtName',Name[0])
        if stateenabled ('dlgNewAddressBook','btnOK')==0:
            log ('Address Book Already Exists','info')
            click ('dlgNewAddressBook','btnCancel')
        else:
            click ('dlgNewAddressBook','btnOK')
    except:
        log ('Error while creating New Address Book','error')
        log ('Create New Address Book','testend')
        raise LdtpExecutionError (0)
    log ('Create New Address Book','testend')

newaddrbook (datafilename)

    
