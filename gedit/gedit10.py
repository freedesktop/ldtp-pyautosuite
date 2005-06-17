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

# Open a document from URL
log ('Open Document From URL', 'teststart')

try:
    selectmenuitem ('gedit', 'mnuFile;mnuOpenLocation')
    # Wait for 2 seconds, let the Open Location dialog window appear
    time.sleep (2)
    if guiexist ('dlgOpenLocation') == 1:
        settextvalue ('dlgOpenLocation', 'txtEnterLocation', 'http://gnomebangalore.org/ldtp')
        click ('dlgOpenLocation', 'btnOpen')
        time.sleep (2)
        # Check if Alert message poped up
        if guiexist ('alrtErrorOpenFile') == 1:
            click ('alrtErrorOpenFile', 'btnOK')
        time.sleep (2)
        if guiexist ('dlgOpenLocation') == 0:
            # TODO
            # - Verify contents from remote site loaded
            # - Verify contents of loaded file
            log ('Open Document From URL', 'pass')
        else:
            click ('dlgOpenLocation', 'btnCancel')
            log ('Open Location dialog still appears', 'error')
            log ('Open Document From URL', 'fail')
    else:
        log ('Open Location dialog does not appear', 'error')
        log ('Open Document From URL', 'fail')
except error, msg:
    log (str (msg), 'error')
    log ('Open Document From URL', 'fail')

log ('Open Document From URL', 'testend')
