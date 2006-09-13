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
from evoutils.mail import go_offline

log ('Modify contact when server is offline','teststart')
data_object = LdtpDataFileParser (datafilename)
AddrBook=data_object.gettagvalue ('AddrBook')
name=data_object.gettagvalue ('name')

try:
    #go_offline ()
    selectContactPane()
    selectaddrbook (AddrBook[0])
    selectcontact (titleappen(name[0])[1:])
    selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
    setcontext ('Contact Editor','Contact Editor -'+titleappend (name[0]))
    waittillguiexist ('dlgContactEditor')
except:
    log ('Unable to open contact','cause')
    log ('Modify contact when server is offline','testend')
    raise LdtpExecutionError (0)

try:
    if gettextstate ('dlgContactEditor','txtFullName')==0:
        log ('Text box is disabled','info')
    else:
        log ('Text box is editable','cause')
        raise LdtpExecutionError (0)
except:
    log ('Modify contact when server is offline','testend')
    raise LdtpExecutionError (0)
log ('Modify contact when server is offline','testend')
        
               
