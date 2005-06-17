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

# Cancel the operation after selecting Open Location
log ('Cancel Open Location Operation', 'teststart')
try:
    selectmenuitem ('gedit', 'mnuFile;mnuOpenLocation')
    # Wait for 2 seconds, let the Open Location dialog window appear
    time.sleep (2)
    if guiexist ('dlgOpenLocation') == 1:
        settextvalue ('dlgOpenLocation', 'txtEnterthelocation', 'http://gnomebangalore.org/ldtp')
        # TODO
        # - Verify text in location is set or not ?
        click ('dlgOpenLocation', 'btnCancel')
        if guiexist ('dlgOpenLocation') == 0:
            log ('Cancel Open Location Operation', 'pass')
        else:
            log ('Open Location dialog box still appears', 'error')
            log ('Cancel Open Location Operation', 'fail')
    else:
        log ('Open Location dialog box does not appear', 'error')
        log ('Cancel Open Location Operation', 'fail')
except error, msg:
    log (str (msg), 'error')
    log ('Cancel Open Location Operation', 'fail')
log ('Cancel Open Location Operation', 'testend')
