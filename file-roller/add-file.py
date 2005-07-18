# 
#  Author:
#     Nagashree M <mnagashree@novell.com>
#     S Vishnu Kumar <vishnukumar.sarvade@gmail.com>
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

try:
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuOpen')
    time.sleep (5)
    selectrow ('dlgOpen', 'tblFiles', 'file-roller.tar.gz')	
    click ('dlgOpen', 'btnOpen')
    setcontext ('Archive Manager', 'file-roller.tar.gz')	
    i = getrowcount ('ArchiveManager', 'tbl0')
    click ('ArchiveManager', 'btnAdd')
    selectrow ('dlgAdd', 'tblFiles', 'test1.tar.gz')
    #click ('dlgAdd', 'btnAdd') #this does not work.
    doubleclickrow ('dlgAdd', 'tblFiles', 'test1.tar.gz') 
    j = getrowcount ('ArchiveManager', 'tbl0')
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuClose')
    if i == j:
	log ('Adding a file to an archive failed', 'fail') 
    else:
	log ('Successfully added a file from an archive', 'pass')
except error:
    log ('Adding a file to an archive failed', 'fail')
