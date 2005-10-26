#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     A. Nagappan <anagappan@novell.com>
# 
#  Copyright 2004 - 2005, Novell, Inc.
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

from ldtp import *
from ldtputils import *
import time

class EvoPassword:
    def EnterPassword (self, password, rememberpassword = None, dialogname = None):
        try:
            try:
                if dialogname != None:
                    setcontext ('Enter password', dialogname)
                waittillguiexist ('dlgEnterpassword')
                if rememberpassword == True:
                    check ('dlgEnterpassword', 'chkRememberthispassword')
                elif rememberpassword == False:
                    uncheck ('dlgEnterpassword', 'chkRememberthispassword')

                # Set password in the text field
                settextvalue ('dlgEnterpassword', 'txt0', password)
                if stateenabled ('dlgEnterpassword', 'btnOK') == 1:
                    # Click OK button
                    click ('dlgEnterpassword', 'btnOK')
                else:
                    log ('Apply button not enabled', 'error')
                    raise LdtpExecutionError (0)
            except error, msg:
                log ('' + str (msg), 'error')
                try:
                    time.sleep (1)
                    click ('dlgEnterpassword', 'btnCancel')
                    releasecontext ()
                    raise LdtpExecutionError (0)
                except error, msg:
                    log ('' + str (msg), 'error')
                    raise LdtpExecutionError (0)
        except LdtpExecutionError:
            log ('enter password failed', 'error')
            LdtpExecutionError (0)
        log ('enter password success', 'info')
