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
from mailtests import *


try:
    data_object = LdtpDataFileParser (datafilename)
    to=data_object.gettagvalue ('to')
    ref_img2=data_object.gettagvalue ('list_ref_image')
except:
    log ('Unable to read values for textformatting','cause')
    raise LdtpExecutionError (0)


try:
    lists_test(to[0],ref_img2)
except:
    log ('Error in Text formatting','cause')
    raise LdtpExecutionError (0)
