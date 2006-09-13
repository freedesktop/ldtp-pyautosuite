#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Description:
#  This set of test scripts will test the LDTP framework for correct
#  functioning of its APIs. This is a Regression Suite.
#
#  Author:
#     Prashanth Mohan  <prashmohan@gmail.com>
#
#
#  This test script is free software; you can redistribute it and/or
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

from regression import *
import random, os
data_object     = LdtpDataFileParser (datafilename)
tab_width       = data_object.gettagvalue ('tabwidth')

if tab_width == []:
    tab_width = 10
else:
    tab_width = int(tab_width[0])
    
try:
    check_open('gedit')
except:
    raise

pref = '*Pref*'
log ('getvalue','teststart')
try:
    open_pref()
    if guiexist (pref) != 1:
        log ('Gedit Preferences Window not open','cause')
        raise LdtpExecutionError (0)
    tab = getvalue (pref,'sbtnTabwidth')
    flag = True
    try:
        getvalue (pref,'sbtnSOMETHINGNOTPRESENT')
    except:
        flag = False
    if flag:
        log ('get value works for non present objects','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('getvalue')
    raise LdtpExecutionError (0)
testpass ('getvalue')


log ('setvalue','teststart')
try:
    setvalue (pref,'sbtnTabwidth',tab_width)
    time.sleep (2)
    if int(getvalue (pref,'sbtnTabwidth')) != tab_width: #and \
#           verifysetvalue (pref,'sbtnTabwidth',tab_width) == 1:
        log ('Spin Button value not set','cause')
        raise LdtpExecutionError (0)
    setvalue (pref,'sbtnTabwidth',tab)
    if getvalue (pref,'sbtnTabwidth') != tab:# and \:
#           verifysetvalue (pref,'sbtnTabwidth',tab) == 1:
        log ('Spin Button value not set to initial value','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('setvalue')
    raise LdtpExecutionError (0)
testpass ('setvalue')

click (pref, 'btnClose')
