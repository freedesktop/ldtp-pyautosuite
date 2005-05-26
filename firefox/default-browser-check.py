#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
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

log ('Check Default Browser', 'teststart')
try:
    # Due to a bug in Firefox accessibility, we have to reinitialize SPI_init
    reinitldtp ()
    if guiexist ('DefaultBrowser') == 1:
        log ('Default browser dialog appeared')
        log ('Check Default Browser', 'pass')
        click ('DefaultBrowser', 'btnNo')
        # Due to a bug in Firefox accessibility, we have to reinitialize SPI_init
        reinitldtp ()
    else:
        log ('Default browser dialog does not appear')
        log ('Check Default Browser', 'fail')
except error:
    log ('Check Default Browser', 'fail')
    log ('Check Default Browser', 'testend')
    raise LdtpException (0)
log ('Check Default Browser', 'testend')
