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
    selectrow ('dlgOpen', 'tblShortcuts', 'Home')
    doubleclickrow ('dlgOpen', 'tblShortcuts', 'Home') 
    selectrow ('dlgOpen', 'tblFiles', 'file-roller.tar.gz')	
    click ('dlgOpen', 'btnOpen')
    time.sleep (5)	
    setcontext ('Archive Manager', 'file-roller.tar.gz')
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuRename')
    settextvalue ('dlgRename', 'txtNewName', 'test')
    click ('dlgRename', 'btnRename')
    setcontext ('Archive Manager', 'test.tar.gz')
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuClose')

    #verification
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuOpen')
    time.sleep (5)
    selectrow ('dlgOpen', 'tblFiles', 'test.tar.gz')	
    click ('dlgOpen', 'btnOpen')
    setcontext ('Archive Manager', 'test.tar.gz')
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuRename')
    settextvalue ('dlgRename', 'txtNewName', 'file-roller')
    click ('dlgRename', 'btnRename')
    setcontext ('Archive Manager', 'file-roller.tar.gz')
    selectmenuitem ('ArchiveManager', 'mnuArchive;mnuClose')
    log ('Successfully renamed an existing archive', 'pass')
except error:
    log ('Copying an archive to different location failed', 'fail')
