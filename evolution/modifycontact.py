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
from contact import *


AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd = getcontactvals(datafilename)
try:
    log ('Modify Contact','teststart')
    #opennewcontact (AddrBook)
    if AddrBook:
        selectaddrbook (AddrBook[0])

    name = titleappend(FullName[0])[1:]
    selectcontact (name)
    selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
    waittillguiexist ('*ContactEditor*')
    addcontact (AddrBook,FullName,Nick,WorkEmail,HomeMail,\
                BusPhone,Yahoo,HomePage,Profession,Notes,\
                HomeAdd,WorkAdd,OtherAdd)
    log ('Modify Contact','pass')
except:
    log ('Modify Contact','fail')
    log ('Modify Contact','testend')
    raise LdtpExecutionError (0)
log ('Modify Contact','testend')

