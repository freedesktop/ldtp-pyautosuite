#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Khasim Shaheed <sshaik@novell.com>
#     Bharani <pbk_1983@rediff.com>
#
#  Copyright 2004 Novell, Inc.
#
#  This library is free software; you can redistribute it and/or
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

import time

#Search for files in some specific folder
def search_in_folder (file_name, folder_name):
	try:
		settextvalue ('SearchforFiles', 'txtNameContainsEntry', file_name)
		comboselect ('SearchforFiles', 'cmbLookinfolder', 'Other...')
		time.sleep (3)
		selectrow ('dlgBrowse', 'tblFiles', folder_name)
		click('dlgBrowse','btnOpen')
		click('SearchforFiles','btnFind')
		log ('Search in folder', 'pass')
	except:
		log ('Search in folder', 'fail')

#Getting the data from a file
file = open('browse_files.dat', 'r')
argmts = file.readlines()
file_name = argmts[1].strip( )
folder_name = argmts[2].strip( )

#Calling the function
log ('Search in folder', 'teststart')
search_in_folder (file_name, folder_name)
log ('Search in folder', 'testend')

