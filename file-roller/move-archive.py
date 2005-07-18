# 
#  Author:
#     Nagashree M <mnagashree@novell.com>
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
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuMove')
    selectrow ('dlgMove', 'tblShortcuts', 'Desktop')
    doubleclickrow ('dlgMove', 'tblShortcuts', 'Desktop')
    click ('dlgMove', 'btnMove')
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuClose')

    #Verification
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuOpen')
    time.sleep (5)
    selectrow ('dlgOpen', 'tblShortcuts', 'Desktop')
    doubleclickrow ('dlgOpen', 'tblShortcuts', 'Desktop')
    selectrow ('dlgOpen', 'tblFiles', 'file-roller.tar.gz')	
    click ('dlgOpen', 'btnOpen')
    setcontext ('Archive Manager', 'file-roller.tar.gz')	
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuClose')
    #selectrow ('dlgMove', 'tblShortcuts', 'Home')
    #doubleclickrow ('dlgMove', 'tblShortcuts', 'Home')
    #click ('dlgMove', 'btnHome')
    #click ('dlgMove', 'btnMove')
    #selectmenuitem ('ArchiveManager', 'mnuArchive;mnuClose')
    log ('Successfully Moved an archive from one location to another', 'pass') 
except error:
    log ('Moving an archive to different location failed', 'fail')
