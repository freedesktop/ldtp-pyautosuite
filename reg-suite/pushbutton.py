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


log ('click on push button','teststart')
try:
    selectmenuitem ('*gedit','mnuTools;mnuDocumentStatistics')
    waittillguiexist ('*DocumentStatistics')
    click ('*DocumentStatistics','btnUpdate')
    flag = True
    try:
        click ('*DocumentStatistics','btn123')
    except:
        flag = False
    if flag:
        log ('Also clicking unavailable buttons','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))    
except:
    testfail ('click on push button')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('click on push button')


log ('enterstring on push button','teststart')
try:
    enterstring ('*DocumentStatistics','btnClose','<return>')
    waittillguinotexist ('*DocumentStatistics')
    if guiexist ('*DocumentStatistics') == 1:
        log ('Dialog did not close','cause')
        raise LdtpExecutionErro (str (traceback.format_exc ()))
except:
    testfail ('enterstring on push button')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('enterstring on push button')
