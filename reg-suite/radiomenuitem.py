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
    open_evo()
except:
    raise

try:
    click ('*Evolution*','tbtnMail')
    #time.sleep (3)
    selectrowpartialmatch ('*Evolution*','ttblMailFolderTree','Inbox')
    waittillguiexist ('*Evolution*')
except:
    log ('Could not set up initial Conditions in Evolution','cause')
    raise LdtpExecutionError (str (traceback.format_exc ()))

    
log ('menucheck on radiomenuitem','teststart')
try:
    #time.sleep (3)
    if menucheck ('*Evolution*','mnuView;mnuCurrentView;mnuBySubject') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    #time.sleep (2)
    if verifymenucheck ('*Evolution*','mnuView;mnuCurrentView;mnuBySubject') != 1:
        log ('verifymenucheck - Radio Menu item not checked','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if verifymenuuncheck ('*Evolution*','mnuView;mnuCurrentView;mnuBySubject') != 0:
        log ('verifymenuuncheck - Radio Menu item not checked','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('menucheck on radiomenuitem')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('menucheck on radiomenuitem')


log ('selectmenuitem on radiomenuitem','teststart')
try:
    if selectmenuitem  ('*Evolution*',
                        'mnuView;mnuCurrentView;mnuBySender') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    #time.sleep (2)
    if verifymenucheck  ('*Evolution*',
                         'mnuView;mnuCurrentView;mnuBySender') != 1:
        log ('verifymenucheck - Radio Menu item not inverted','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if verifymenuuncheck  ('*Evolution*',
                           'mnuView;mnuCurrentView;mnuBySender') != 0:
        log ('verifymenuuncheck - Radio Menu item not inverted','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    selectmenuitem  ('*Evolution*', 'mnuView;mnuCurrentView;mnuMessages')
except:
    testfail ('selectmenuitem on radiomenuitem')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('selectmenuitem on radiomenuitem')

close_evo()
