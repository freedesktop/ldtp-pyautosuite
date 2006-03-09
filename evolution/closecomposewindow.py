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


from mailtests import *

try:
    data_object = LdtpDataFileParser (datafilename)
    state=data_object.gettagvalue ('state')
except:
    log ('Could not read values for close compose window test','cause')
    raise LdtpExecutionError (0)
try:
    time.sleep (3)
    selectmenuitem ('frmEvolution-*','mnuFile;mnuNew;mnuMailMessage')
    waittillguiexist ('frmComposeMessage')
    settextvalue ('frmComposeMessage','txt6','abc')
    closecomposewindow (int(state[0]))
except:
    log ('Close compose window failed','error')
    raise LdtpExecutionError (0)

        
