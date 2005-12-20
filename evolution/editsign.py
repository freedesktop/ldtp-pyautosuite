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
from composerprefs import *

try:
    try:
        data_object = LdtpDataFileParser (datafilename)
        text=data_object.gettagvalue ('text')
        name=data_object.gettagvalue ('name')
        newname=data_object.gettagvalue ('newname')
    except:
        log ('Error while reading values for edit signature test','cause')
        raise LdtpExecutionError (0)
    try:
        if len (newname) >0:
            edit_signature (name[0],text[0],newname[0])
        else:
            edit_signature (name[0],text[0])
    except:
        log ('edit signature test failed','error')
        raise LdtpExecutionError (0)
except:
    raise LdtpExecutionError (0)
