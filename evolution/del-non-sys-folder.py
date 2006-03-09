#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
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

# Delete a non system folder.
from menu_reorganization import *

data_object = LdtpDataFileParser (datafilename)
#Extracting imput data from xml file

fldr = data_object.gettagvalue ('folder_name')[0]

try:
	log('Delete a non-sys folder','teststart')
	if delete_nonsys_folder(fldr) == 1:
		print fldr + ' has been Deleted'
                log('Delete a non-sys folder','pass')
	else:
		print 'Unable to delete'
                log('Delete a non-sys folder','pass')
        log ('Delete a non-sys folder','testend')

except:
        log('cannot delete a folder','error')
        log('Delete a non-sys folder','testend')
        raise LdtpExecutionError(0)


