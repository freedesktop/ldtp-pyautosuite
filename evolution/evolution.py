
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:     
#     Bhargavi <kbhargavi_83@yahoo.co.in>
#     Khasim Shaheed <sshaik@novell.com>
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

#!/usr/bin/python

from ldtp import *
import string, sys, os

appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./evolution-2.2.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/evolution-2.2.map')

launchapp ('evolution-2.2')

log('EvolutionSuite','begin')

## MAIL ##
#mail compose
execfile ('Compose_mail.py')

#mail compose with attachment
wait(3)
execfile('compose_attach.py')

#editoperation in compose mail dialog
wait(3)
execfile('edit_mail.py')

#deletion of mail
wait(3)
execfile('delete_mail.py')

#Autocompletion
wait(3)
execfile('auto.py')

# To send an HTML file and verify the same.
execfile ('sendhtmlmail.py')

# To send an HTML file and verify the same.
execfile ('forwardmail.py')

#To view a plain text mail
execfile ('viewmail.py')

#To view an html mail
execfile ('viewhtmlmail.py') 

#To move a mail from one directory to another
execfile ('movingmail.py')

#To copy a mail from one directory to another
execfile ('copymail.py')

## MEETING ## 
#Meeting
wait(3)
execfile('meeting.py')

## TASK ##
# Task
wait(3)
execfile('Create_Task.py')

# Assign Task
wait(3)
execfile('Create_Assign_Task.py')

##  APPOINTMENT ##
#Creation of Appointment
wait(3)
execfile('create_appointment.py')

#Deletion of Appointment
wait(3)
execfile('delete_appointment.py')

### CONTACTS
execfile ('add_contact_from_mail.py')
execfile ('edit_contact.py')
execfile ('delete_contact.py')
execfile ('Create_Contact.py')

execfile('web_cal.py')

log('EvolutionSuite','begin')




