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

# 'Undo' or 'Redo' changes made to a document in gedit
log ('Undo Redo Operation', 'teststart')
try:
    selectmenuitem ('gedit', 'mnuFile;mnuOpen')
    # Wait 3 seconds, let the Open Dialog appear
    time.sleep (3)
    if guiexist ('dlgOpenFile') == 1:
        # TODO
        # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
        selectrow ('dlgOpenFile', 'tblFiles','sample.txt')
        click ('dlgOpenFile', 'btnOpen')
        time.sleep (2)
        # TODO
        # - Check file opened or not
        if guiexist ('dlgOpenFile') == 0:
            log ('Undo Redo Operation', 'pass')
            settextvalue ('gedit', 'txtGedit', 'Modifying text content')
            # TODO
            # - Try to set this text at end
            # - Try to set this text in starting
            # - Verify text is set or not

            # Do undo operation
            selectmenuitem ('gedit', 'mnuEdit;mnuUndo')
            # TODO
            # - Verify text content is undone

            # Do redo operation
            selectmenuitem ('gedit', 'mnuEdit;mnuRedo')
            # TODO
            # - Verify text content is redone

            selectmenuitem ('gedit', 'mnuFile;mnuClose')
            # Wait for 3 seconds, let alert window for changes appear
            if guiexist ('alrtSaveWindow') == 1:
                click ('alrtSaveWindow', 'btnClosewithoutSaving')
                log ('Undo Redo Operation', 'pass')
            else:
                log ('Alert save window does not appear', 'error')
                log ('Undo Redo Operation', 'fail')
        else:
            log ('Open File dialog window does not appear', 'error')
            log ('Undo Redo Operation', 'fail')
except error, msg:
    log (str (msg), 'error')
    log ('Undo Redo Operation', 'fail')
log ('Undo Redo Operation', 'testend')
