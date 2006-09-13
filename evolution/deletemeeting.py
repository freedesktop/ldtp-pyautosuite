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

from meeting import *

try:
    log ('Delete non recursive Meeting','teststart')
    try:
        data_object = LdtpDataFileParser (datafilename)
        fromdate=data_object.gettagvalue ('fromdate')
        summary=data_object.gettagvalue ('summary')
    except:
        log ('Error while reading values for delete meeting','cause')
        log ('Delete non recursive Meeting','fail')
        raise LdtpExecutionError (0)

    try:
        deletemeeting (fromdate[0],summary[0],0)
    except:
        log ('Unable to delete meeting','error')
        log ('Delete non recursive Meeting','fail')
        raise LdtpExecutionError (0)
    log ('Delete non recursive Meeting','pass')

except:
    log ('Delete non recursive Meeting','testend')
    raise LdtpExecutionError (0)
log ('Delete non recursive Meeting','testend')
