#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     A. Nagappan <anagappan@novell.com>
# 
#  Copyright 2004 Novell, Inc.
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
import string, sys, os, commands, time, filecmp

appmap_path = ''
default_dir = os.getcwd ()
bugbuddy_exe_path = 'bug-buddy'

startlog ('bug-buddy.xml', 1)

log ('Bug Buddy Test Report', 'begin')

if len (sys.argv) == 1:
  if os.access ('./bug-buddy.map', os.F_OK | os.R_OK) == 0:
    log ('Appmap path missing', 'error')
    log ('Bug Buddy Test Report', 'end')
    stoplog ()
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/bug-buddy.map')

try:
    # TO DO
    # We need to check in this script
    # If bug-buddy is already invoked by external application
    # we should not invoke it once again
    execfile ('launch.py')
except LdtpExecutionError:
    log ('Unable to launch Bug Buddy', 'Error')
    log ('Bug Buddy Test Report', 'end')
    stoplog ()
    sys.exit (0)

time.sleep (5)

def set_summary (summary):
    settextvalue ('BugBuddy', 'txtSummary', summary)

def select_application ():
    check ('BugBuddy', 'rdoTheapplicationdoesnotfunctioncorrectly')

def select_translation ():
    check ('BugBuddy', 'rdoTheTranslationiswrong')

def select_documentation ():
    check ('BugBuddy', 'rdoThedocumentationiswrong')

def select_enhancement ():
    check ('BugBuddy', 'rdoRequestamissingfeature')

def select_expert ():
    check ('BugBuddy', 'rdoDebugacrashedorrunningapplication')

def select_products ():
    check ('BugBuddy', 'rdoShowProducts')

def select_applications ():
    check ('BugBuddy', 'rdoShowApplications')

def describe_bug ():
    # TO DO
    # Before setting new description, if some stack trace is available
    # we need to get that text and then start adding new text
    # Because settextvalue just overwrites existing text content :(
    txtDesc = 'Description of Problem:\n' + 'Just testing description' + '\n\n'
    txtSteps = 'Steps to reproduce the problem:\n' + 'Just testing reproducing steps' + '\n\n'
    txtActual = 'Actual results:\n' + 'Just testing actual results' + '\n\n'
    txtExpected = 'Expected results:\n' + 'Just expected results' + '\n\n'
    txtHowOften = 'How often does this happen?\n' + 'Just testing how often does this happen' + '\n\n'
    txtAdditionalInfo = 'Additional Information:\n' + 'Just testing additional information' + '\n\n'
    settextvalue ('BugBuddy', 'txtDescription', txtDesc + txtSteps + txtActual +
                  txtExpected + txtHowOften + txtAdditionalInfo)

try:
    # TO DO
    # For 0.1.7 release hardcoded selecting application, needs to be dynamic ;)
    select_application ()

    # Navigate to next screen
    click ('BugBuddy', 'btnForward')
    time.sleep (5)

    # TO DO
    # Selecting show products - For 0.1.7 release hardcoded selecting show products, needs to be dynamic ;)
    select_products ()
    # On my laptop it takes a long delay to load all the products
    # So, I have given a long delay - Old DELL laptop ;)
    time.sleep (15)

    # TO DO
    # Selecting beagle - For 0.1.7 release hardcoded selecting beagle, needs to be dynamic ;)
    selectrow ('BugBuddy', 'tblProducts', 'beagle')

    # Navigate to next screen
    click ('BugBuddy', 'btnForward')
    time.sleep (2)

    # TO DO
    # Selecting General - For 0.1.7 release hardcoded selecting general, needs to be dynamic ;)
    selectrow ('BugBuddy', 'tblComponent', 'General')

    # Navigate to next screen
    click ('BugBuddy', 'btnForward')
    time.sleep (2)
    # Frequently reported bugs page. Just navigating this page also.
    click ('BugBuddy', 'btnForward')

    # TO DO
    # Argument to this function should be passed from external script to this script
    set_summary ('bug-buddy test-scripts using Linux Desktop Testing Project')

    # TO DO
    # Values in describe_bug functions are hard coded. Needs to be modified and
    # this function should take all the required arguments plus need to fill
    # optional arguments (If required ?)
    describe_bug ()

    # After describing the bug navigate to next page
    click ('BugBuddy', 'btnForward')

    # Select mail option. To send the bug report as mail
    check ('BugBuddy', 'rdoUsesendmaildirectly')
    # Name of the person who files the bug. Should be changed, if necessary ;)
    settextvalue ('BugBuddy', 'txtName', 'Linux Desktop Testing Project')
    # Email id of the person who files the bug. Should be changed, if necessary ;)
    settextvalue ('BugBuddy', 'txtEmail', 'ldtp@gnomebangalore.org')
    # Navigate to next screen
    click ('BugBuddy', 'btnForward')

    # Recipients
    # Hardcoded to anagappan@novell.com for timebeing. This has to be changed.
    # Till the time we are in testing phase, maybe some id like this can be there ;)
    # But I'm annoid with spam mails :D
    settextvalue ('BugBuddy', 'txtTo', 'anagappan@novell.com')
    # Send the report
    click ('BugBuddy', 'btnSendReport')
    # Close bug buddy
    click ('BugBuddy', 'btnClose')

    # If everything goes well
    log ('Bug Buddy Test Report', 'pass')
except error, msg:
    log ('Unable to use Bug Buddy', 'Error')
    log (str (msg), 'Cause')
    log ('Bug Buddy Test Report', 'fail')
log ('Bug Buddy Test Report', 'end')
stoplog ()
