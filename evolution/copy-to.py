#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
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

# Copy a folder from one location to another.

from menu_reorganization import *

try:
	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	from_fldr = data_object.gettagvalue ('from_fldr')[0]
	to_fldr = data_object.gettagvalue ('to_fldr')[0]
	copy_to (from_fldr,to_fldr)
        	
except :

	log('Cannot copy the folder','error')
	raise LdtpExecutionError (0)
		
