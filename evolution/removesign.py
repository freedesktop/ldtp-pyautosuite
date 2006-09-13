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

from composerprefs import *

try:
    try:
        data_object = LdtpDataFileParser (datafilename)
        name=data_object.gettagvalue ('name')
    except:
        log ('Error while reading values for remove signature test','cause')
        raise LdtpExecutionError (0)
    try:
        removesignature (name[0])
    except:
        log ('remove signature test failed','error')
        raise LdtpExecutionError (0)
except:
    raise LdtpExecutionError (0)
