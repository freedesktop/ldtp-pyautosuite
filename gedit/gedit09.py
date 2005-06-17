#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Aishoo Team, Fasila
#     A. Nagappan <anagappan@novell.com>
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

# Close all the documents that are opened currently in gedit
log ('Close All Opened Documents', 'teststart')
try:
    selectmenuitem ('gedit', 'mnuFile;mnuOpen')
    # Wait 3 seconds, let the Open Dialog appear
    time.sleep (3)
    if guiexist ('dlgOpenFile') == 1:
        # TODO
        # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
        selectrow ('dlgOpenFile', 'tblFiles', 'sample.txt')
        click ('dlgOpenFile', 'btnOpen')
        time.sleep (2)
        # TODO
        # - Check file opened or not
        if guiexist ('dlgOpenFile') == 0:
            log ('Still dialog window appears', 'error')
            # Open 2nd file
            selectmenuitem ('gedit', 'mnuFile;mnuOpen')
            # Wait 3 seconds, let the Open Dialog appear
            time.sleep (3)
            if guiexist ('dlgOpenFile') == 1:
                # TODO
                # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
                selectrow ('dlgOpenFile', 'tblFiles', 'edit.txt')
                click ('dlgOpenFile', 'btnOpen')
                time.sleep (2)
                # TODO
                # - Check file opened or not
                if guiexist ('dlgOpenFile') == 0:
                    selectmenuitem ('gedit', 'mnuDocuments;mnuCloseAll')
                    log ('Close All Opened Documents', 'pass')
                else:
                    log ('Open dialog window still appears', 'error')
                    log ('Close All Opened Documents', 'fail')
            else:
                log ('Open dialog window does not appear', 'error')
                log ('Close All Opened Documents', 'fail')
        else:
            log ('Open dialog window still appears', 'error')
            log ('Close All Opened Documents', 'fail')
    else:
        log ('Open dialog window does not appear', 'error')
        log ('Close All Opened Documents', 'fail')
except error, msg:
    log (str (msg), 'error')
    log ('Close All Opened Documents', 'fail')
log ('Close All Opened Documents', 'testend')
