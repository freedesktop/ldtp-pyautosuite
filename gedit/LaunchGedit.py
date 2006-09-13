#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     N Srinivasan  <raiden.202@gmail.com>
#
#  Copyright 2004-2006 Novell, Inc.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#

#
from ldtp import *
try:
    log('Gedit-Launch','teststart')
    selectmenuitem('frmTop*Panel','mnuApplications;mnuAccessories;mnuTextEditor')
    time.sleep(5)
    if guiexist('*gedit') == 1:
        log('Gedit started successfully','info')
    else:
        log('Gedit cannot be launched','error')
        raise LdtpExecutionError(0)
    time.sleep(3)
    log('Closing gedit..','info')
    selectmenuitem('*gedit','mnuFile;mnuQuit')
    time.sleep(3)
    if guiexist('*gedit') == 0:   
        log('Successfully exited gedit','info')
    else:
        log('Cannot exit gedit','error')
        raise LdtpExecutionError(0)
except:
    log('Cannot','error')
    log('Gedit-Launch','testend')
    raise LdtpExecutionError(0)
