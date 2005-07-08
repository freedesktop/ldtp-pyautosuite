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

#Searching for files with given text in that
def search (search_string, text):
        try:
                settextvalue ('SearchforFiles', 'txtNameContainsEntry', search_string)
		click ('SearchforFiles', 'tbtnShowmoreoptions')
                click('SearchforFiles', 'btnAdd')
                settextvalue ('SearchforFiles', 'txtContainsthetextentry', text)
                click('SearchforFiles', 'btnFind')
                log ('Search for file with given text', 'pass')
        except:
                log ('Search for file with given text', 'fail')

#Getting the data from a file
file = open('search_with_text.dat', 'r')
argmts = file.readlines()
search_string = argmts[1].strip( )
text = argmts[2].strip( )

#Calling the function
log ('Search for file with given text', 'teststart')
search (search_string, text)
log ('Simple for file with given text', 'testend')
