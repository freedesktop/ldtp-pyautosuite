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

#To rename a folder.

from menu_reorganization import *

data_object = LdtpDataFileParser (datafilename)
#Extracting imput data from xml file

old_name = data_object.gettagvalue ('old_name')[0]
new_name = data_object.gettagvalue ('new_name')[0]

try:
	log('Rename a folder','teststart')
	if rename(old_name,new_name) == 1:
		print old_name + ' has been renamed as '+new_name
		log('Fldr has been renamed','info')	
        	log('Fldr has been renamed','pass')
	else:
		log('probs in renaming the fldr','info')		
        	log('Fldr has been renamed','fail')

        log('Rename a folder','testend')

except:
        log('cannot rename a folder','error')
        log('Rename a folder','testend')
        raise LdtpExecutionError(0)

