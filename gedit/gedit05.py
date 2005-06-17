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

# Click cancel in save as dialog box, after selecting a file
log ('Click Cancel In Save As Dialog Box', 'teststart')
try:
    selectmenuitem ('gedit', 'mnuFile;mnuOpen')

    # Wait for 3 seconds, let the open dialog box window appear
    time.sleep (3)

    if guiexist ('dlgOpenFile') == 1:
        # TODO
        # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
        selectrow ('dlgOpenFile', 'tblFiles', 'sample.txt')
        # TODO
        # - Check if file does not exist
        click ('dlgOpenFile', 'btnOpen')

        # Wait for 3 seconds, let the open dialog box window appear
        time.sleep (3)
        if guiexist ('dlgOpenFile') == 1:
            log ('Open dialog box appears after opening file', 'error')
            log ('Click Cancel In Save As Dialog Box', 'fail')
        else:
            # TODO
            # Check if file opened successfully
            # Wait for 2 seconds, Let the file be loaded
            time.sleep (2)
            selectmenuitem ('gedit', 'mnuFile;mnuSaveAs')
            # Wait for 2 seconds, Let the file be loaded
            time.sleep (2)
            if guiexist ('dlgSaveas') == 1:
                # btncancel is not working (hanged) - comment by fasila
                click ('dlgSaveas', 'btnCancel')
                # Wait for 2 seconds, Let the file be loaded
                time.sleep (2)
                if guiexist ('dlgSaveas') == 0:
                    log ('Click Cancel In Save As Dialog Box', 'pass')
                else:
                    log ('Save As dialog box still appears', 'error')
                    log ('Click Cancel In Open Dialog Box', 'fail')
            else:
                log ('Save As dialog box does not appear', 'error')
                log ('Click Cancel In Save As Dialog Box', 'fail')
    else:
        log ('Open dialog box does not appear', 'error')
        log ('Click Cancel In Save As Dialog Box', 'fail')
except error, msg:
    log (str (msg), 'error')
    log ('Click Cancel In Save As Dialog Box', 'fail')
log ('Click Cancel In Save As Dialog Box', 'testend')
