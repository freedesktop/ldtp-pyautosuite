#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     SR Aginesh <sraginesh@novell.com>
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

log ('Help Window', 'teststart')
try:
    selectmenuitem ('Mozilla', 'mnuHelp;mnuHelpContents')
    # Let us wait for some time, so that help window will be invoked
    time.sleep (5)
    if guiexist ('FirefoxHelp') == 1:
        log ('Help window appeared', 'info')
        activatewin ('Mozilla Firefox Help')
        typekey ('<alt>f4')
    time.sleep (2)
    if guiexist ('FirefoxHelp') == 0:
        log ('Help window closed successfully', 'info')
        log ('Help Window', 'pass')
    else:
        log ('Help window still not closed', 'error')
        log ('Help Window', 'fail')
except error:
    log ('Help Window', 'fail')
log ('Help Window', 'testend')

#cannot execute this also because of an accessibility bug
#selectmenuitem('mozilla','mnuHelp;mnuAboutMozillaFirefox')
#click('dlgHelp','btnCredits')
