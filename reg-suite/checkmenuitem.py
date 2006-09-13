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


log ('menucheck','teststart')
try:
    if menucheck ('*gedit','mnuView;mnuStatusbar') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (0)
    time.sleep (2)
    if verifymenucheck ('*gedit','mnuView;mnuStatusbar') != 1:
        log ('verifymenucheck - Check Menu item not checked','cause')
        raise LdtpExecutionError (0)
    if verifymenuuncheck ('*gedit','mnuView;mnuStatusbar') != 0:
        log ('verifymenuuncheck - Check Menu item not checked','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('menucheck')
    raise LdtpExecutionError (0)
testpass ('menucheck')



log ('menuuncheck','teststart')
try:
    if menuuncheck ('*gedit','mnuView;mnuStatusbar') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (0)
    time.sleep (2)
    if verifymenuuncheck ('*gedit','mnuView;mnuStatusbar') != 1:
        log ('verifymenuuncheck - Check Menu item not checked','cause')
        raise LdtpExecutionError (0)
    if verifymenucheck ('*gedit','mnuView;mnuStatusbar') != 0:
        log ('verifymenucheck - Check Menu item not checked','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('menuuncheck')
    raise LdtpExecutionError (0)
testpass ('menuuncheck')


log ('selectmenuitem on checkmenu','teststart')
try:
    curstate = verifymenucheck ('*gedit','mnuView;mnuStatusbar')
    if selectmenuitem ('*gedit','mnuView;mnuStatusbar') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (0)
    time.sleep (2)
    if verifymenucheck ('*gedit','mnuView;mnuStatusbar') == curstart:
        log ('verifymenucheck - Check Menu item not inverted','cause')
        raise LdtpExecutionError (0)
    curstate = verifymenucheck ('*gedit','mnuView;mnuStatusbar')
    if selectmenuitem ('*gedit','mnuView;mnuStatusbar') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (0)
    time.sleep (2)
    if verifymenucheck ('*gedit','mnuView;mnuStatusbar') == curstart:
        log ('verifymenucheck - Check Menu item not inverted 2nd time','cause')
        raise LdtpExecutionError (0)
except:
    testfail ('selectmenuitem on checkmenu')
    raise LdtpExecutionError (0)
testpass ('selectmenuitem on checkmenu')


