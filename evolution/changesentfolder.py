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

from evoutils.mailpreferences import *
from ldtputils import *

# Read data from a file
data_object = LdtpDataFileParser (datafilename)
accountname = data_object.gettagvalue ('accountname')
sent_folder = data_object.gettagvalue ('sent_folder')

if sent_folder:
	sent_folder = sent_folder[0]
else:
	sent_folder = 'Sent Items'

# Call the function
if accountname:
	change_sentfolder (accountname[0], sent_folder)
else:
	log ('accountname not provided in data xml file', 'error')
	raise LdtpExecutionError (0)

