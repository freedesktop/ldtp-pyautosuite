#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bharani <pbk_1983@rediff.com>
#     Khasim Shaheed <sshaik@novell.com>
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

#Searching for files names that contains a given string
def search (search_string):
	try:
		settextvalue ('SearchforFiles', 'txtNameContainsEntry', search_string)
		click('SearchforFiles', 'btnFind')
		log ('Simple Search', 'pass')
	except:
		log ('Simple Search', 'fail')

#Getting the data from a file
file = open('simple_search.dat', 'r')
argmts = file.readlines()
search_string = argmts[1].strip( )

#Calling the function
log ('Simple Search', 'teststart')
search (search_string)
log ('Simple Search', 'testend')
