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
    open_evo ()
except:
    raise

data_object     = LdtpDataFileParser (datafilename)
rows            = data_object.gettagvalue ('rowcount')


evo_win  = 'frmEvolution-*'
pref     = '*EvolutionPreferences'
acnt_tab = 'tblMailAccounts'

log ('getrowcount','teststart')
try:
    selectmenuitem (evo_win,'mnuEdit;mnuPreferences')
    if waittillguiexist (pref) == 0:
        log ('Preferences Window not open yet','cause')
        raise LdtpExecutionError (0)
    row_count = getrowcount (pref, acnt_tab)
    if rows != [] and rows != row_count:
        log ('No of rows does not match with input','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('getrowcount')
    raise LdtpExecutionError (0)
testpass ('getrowcount')


acnts = []
log ('getcellvalue','teststart')
try:
    for index in range (row_count):
        val = getcellvalue (pref, acnt_tab, index, 1)
## http://bugzilla.gnome.org/show_bug.cgi?id=352220
#         if verifytablecell (pref, acnt_tab, index, 1, val) == 0:
#             log ('problem in getcellvalue','cause')
#             raise LdtpExecutionError (0)
        acnts.append (val)
except:
    testfail ('getcellvalue')
    raise LdtpExecutionError (0)
testpass ('getcellvalue')


log ('selectrowindex','teststart')
try:
    for index in range (row_count):
        if selectrowindex (pref, acnt_tab, index) != 1:
            log ('Unable to select index','cause')
            raise LdtpExecutionError (0)
        time.sleep (1)

        if gettablerowindex (pref, acnt_tab, acnts[index]) != index:
            log ('Index not selected','cause')
            raise LdtpExecutionError (0)
except:
    testfail ('selectrowindex')
    raise LdtpExecutionError (0)
testpass ('selectrowindex')


log ('selectrow','teststart')
try:
    index = 0
    for acnt in acnts:
        if doesrowexist (pref, acnt_tab, acnt) == 1 and selectrow (pref, acnt_tab, acnt) != 1:
            log ('Unable to select row','cause')
            raise LdtpExecutionError (0)
        time.sleep (1)
        if gettablerowindex (pref, acnt_tab, acnt) != index:
            log ('Index not selected','cause')
            raise LdtpExecutionError (0)
        index += 1
except:
    testfail ('selectrow')
    raise LdtpExecutionError (0)
testpass ('selectrow')


log ('selectlastrow','teststart')
try:
    if selectlastrow (pref,acnt_tab) != 1:
        log ('selectlastrow failed','cause')
        raise LdtpExecutionError (0)
    time.sleep (1)
    if gettablerowindex (pref, acnt_tab, acnt) != (len (acnts)-1):
        log ('Index not selected','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('selectlastrow')
    raise LdtpExecutionError (0)
testpass ('selectlastrow')


log ('checkrow','teststart')
try:
    for index in range (row_count):
        if uncheckrow (pref, acnt_tab, index) == 0:
            log ('Unable to uncheck row','cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        if checkrow (pref, acnt_tab, index) == 0:
            log ('Unable to check row','cause')
            raise LdtpExecutionError (0)
except:
    testfail ('checkrow')
    raise LdtpExecutionError (0)
testpass ('checkrow')
click (pref,'btnClose')
