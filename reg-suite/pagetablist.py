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
tab_count       = data_object.gettagvalue ('tabcount')


if tab_count == []:
    tab_count = 5
else:
    tab_count = int(tab_count[0])

pref = '*Pref*'
log ('tab list count','teststart')
try:
    open_pref()
    count = gettabcount (pref,'ptl0')
    if count != tab_count:
        log ('number of tabs do not tally','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('tab list count')
    raise LdtpExecutionError (0)
testpass ('tab list count')


log ('selecttab','teststart')
try:
    open_pref()
    obj = [ x for x in getobjectlist(pref) if x.startswith ('ptab')]
    if selecttab (pref,'ptl0','View') == 0:
        log ('Unable to select tab','cause')
        raise LdtpExecutionError (0)
    if selecttab (pref,'ptl0','Editor') == 0:
        log ('Unable to select tab','cause')
        raise LdtpExecutionError (0)
    if selecttab (pref,'ptl0','Font & Colors') == 0:
        log ('Unable to select tab','cause')
        raise LdtpExecutionError (0)
    if selecttab (pref,'ptl0','Syntax Highlighting') == 0:
        log ('Unable to select tab','cause')
        raise LdtpExecutionError (0)
    if selecttab (pref,'ptl0','Plugins') == 0:
        log ('Unable to select tab','cause')
        raise LdtpExecutionError (0)

#     for tab in obj:
#         if selecttab (pref,'ptl0',tab[4:]) == 0:
#             log ('Unable to select tab','cause')
#             raise LdtpExecutionError (0)
except:
    testfail ('selecttab')
    raise LdtpExecutionError (0)
testpass ('selecttab')


log ('selecttabindex','teststart')
try:
    for ind in range (tab_count):
        if selecttabindex (pref,'ptl0',ind) == 0:
            log ('Unable to select tab','cause')
            raise LdtpExecutionError (0)
    click (pref,'btnClose')
    waittillguinotexist (pref)
except:
    testfail ('selecttabindex')
    raise LdtpExecutionError (0)
testpass ('selecttabindex')
