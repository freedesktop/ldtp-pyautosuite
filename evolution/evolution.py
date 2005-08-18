#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtP
#
#  Author:     
#     Premkumar <jpremkumar@novell.com>
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
from evoutils.mail import *
from evoutils.calendar import *
import string, sys, os, time

startlog('evolution.log',1)

appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./evolution.map', os.F_OK | os.R_OK) == 0:
    log ('Appmap path missing','error')
    stoplog ()
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/evolution.map')

launchapp ('evolution')

log ('Evolution Mailer Suite', 'begin')

## MAIL ##
#Compose mail
execfile ('compose-mail.py')
time.sleep (60)

#Reply to a mail
execfile ('reply-mail.py')
time.sleep (60)

#Forward a mail
execfile ('forward-mail.py')
time.sleep (60)

#Compose mail with attachment
execfile('compose-mail-w-attachment.py')
time.sleep (60)

#TODO: Test script for sending html has to be  written
#To send an HTML file and verify the same.
#execfile ('sendhtmlmail.py')

#To view a plain text mail
execfile ('view-mail.py')
time.sleep (60)

#To move a mail from one directory to another
execfile ('movemail.py')
time.sleep (60)

#To copy a mail from one directory to another
execfile ('copymail.py')
time.sleep (60)

#To delete a mail from a given directory
execfile ('deletemail.py')
time.sleep (60)

log ('Evolution Mailer Suite', 'end')

log ('Evolution Calendar Suite', 'begin')

## MEETING ## 
time.sleep (3)
execfile ('create-meeting.py')
time.sleep (3)
execfile ('verify-meeting.py')

## APPOINTMENT ##
time.sleep (3)
execfile ('create-appointment.py')
time.sleep (3)
execfile ('verify-appointment.py')

## CALENDAR ##
time.sleep (3)
execfile ('create-calendar.py')
time.sleep (3)

log ('Evolution Calendar Suite', 'end')

stoplog ()
