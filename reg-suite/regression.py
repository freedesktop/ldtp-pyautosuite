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

from ldtp import *
from ldtputils import *

def check_open (app_name='gedit'):
    print 'in check_open'
    if guiexist ('*gedit') != 1:
        launchapp (app_name,1)
        waittillguiexist ('*gedit')
    if guiexist ('*gedit') !=1:
        raise LdtpExecutionError (0)
    return


def close_gedit ():
    selectmenuitem ('*gedit','mnuFile;mnuQuit')
    if guiexist ('*Question') == 1:
        click ('*Question','btnClosewithoutSaving')
    return


def open_evo():
    if guiexist ('*Evolution-*') != 1:
        launchapp ('evolution',1)
        time.sleep (2)
        if guiexist ('*Evolution') == 1:
            click ('*Evolution','btnNo')
        waittillguiexist ('*Evolution-*')
    if guiexist ('*Evolution-*') !=1:
        raise LdtpExecutionError (0)
    return


def close_evo():
    selectmenuitem ('*Evolution*','mnuFile;mnuQuit')
    waittillguinotexist ('*Evolution*')
    return
    

def open_pref ():
    selectmenuitem ('*-gedit','mnuEdit;mnuPreferences')
    waittillguiexist ('*Pref*')
    if guiexist ('*Pref*') == 0:
        log ('Preferences Window could not be opened','cause')
        raise LdtpExecutionError (0)
    return


def testfail (testname):
    log (testname, 'fail')
    log (testname, 'testend')


def testpass (testname):
    log (testname, 'pass')
    log (testname, 'testend')
