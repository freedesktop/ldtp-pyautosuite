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


try:
    check_open('gedit')
except:
    raise

data_object     = LdtpDataFileParser (datafilename)
chkbox          = data_object.gettagvalue ('checkbox')
if chkbox == []:
    chkbox = 'chkDisplaylinenumbers'
else:
    chkbox = chkbox[0]

pref = '*Pref*'
log ('check','teststart')
try:
    open_pref()
    if guiexist (pref) != 1:
        log ('Gedit Preferences Window not open','cause')
        raise LdtpExecutionError (0)
    if check (pref,chkbox) != 1:
        log ('Check failed','cause')
        raise LdtpExecutionError (0)
    time.sleep (2)
    if verifycheck (pref,chkbox) != 1:
        log ('Checkbox not checked','cause')
        raise LdtpExecutionError (0)
    if verifyuncheck (pref,chkbox) != 0:
        log ('Checkbox not checked','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('check')
    raise LdtpExecutionError (0)
testpass ('check')


log ('uncheck','teststart')
try:
    if uncheck (pref,chkbox) != 1:
        log ('UnCheck failed','cause')
        raise LdtpExecutionError (0)
    time.sleep (2)
    if verifyuncheck (pref,chkbox) != 1:
        log ('Checkbox not unchecked','cause')
        raise LdtpExecutionError (0)
    if verifycheck (pref,chkbox) != 0:
        log ('Checkbox not unchecked','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('uncheck')
    raise LdtpExecutionError (0)
testpass ('uncheck')


log ('click on checkbox','teststart')
try:
    pres = verifycheck (pref,chkbox)
    click (pref,chkbox)
    time.sleep (2)
    if verifycheck (pref,chkbox) == pres:
        log ('Click did not function properly','cause')
        raise LdtpExecutionError (0)
    click (pref,chkbox)
    time.sleep (2)
    if verifycheck (pref,chkbox) != pres:
        log ('Click did not function properly','cause')
        raise LdtpExecutionError (0)
    click (pref,'btnClose')
    waittillguinotexist (pref)
except:
    testfail ('click on checkbox')
    raise LdtpExecutionError (0)
testpass ('click on checkbox')
