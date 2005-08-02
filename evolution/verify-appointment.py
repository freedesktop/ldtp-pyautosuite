#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Sheetal <svnayak18@yahoo.com>
#     Prem <jpremkumar@novell.com>
#
#  Copyright 2004 Novell, Inc.
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
#To create a Meeting

#Reading inputs from file
file = open ('create-appointment.dat','r')
data = file.readlines ()
summary = data[0].strip ()
location = data[1].strip ()
description = data[2].strip ()
classification = data[3].strip ()
categories = data[4].strip ()
moncount = data[5].strip ()
on = data[6].strip ()
day = data[7].strip ()
occurences = data[8].strip ()
exception = data[9].strip ()

#TODO: INCLUDE actual date values after fixing the problem in insert_appointment
date0 = 0
time0 = 0
date1 = 0
time1 = 0

#setting up default values
if classification == '$':
    classification = 'Public'
if categories == '$':
    categories = 'Business'
if moncount == '$':
    moncount = '3'
if on == '$':
    on = 'First'
if day == '$':
    day = 'Monday'
if occurences == '$':
    occurences = '5'
if exception =='$' or exception > occurences:
    if exception > occurences:
        log ('Setting exception to default value since given value is inappropriate', 'warning')
    exception = 2

#creation fo meeting
log ('Appointment Verification', 'teststart')

try:
    if guiexist ('evolution') == 0:
	log ('Evolution wondow not found', 'cause')
	raise LdtpExecutionError (0)
    else:
	selectmenuitem ('evolution', 'mnuView;mnuWindow;mnuCalendars')
    	time.sleep (2)
	#selectmenuitem ('evolution', 'mnuView;mnuCurrentView;mnuListView')
	#time.sleep (2)
        if selectrow ('evolution', 'tbl0', summary) == 0:
            log ('Selection of table value failed', 'cause')
            raise LdtpExecutionError (0)
        time.sleep (3)
	typekey ('<ctrl>o')
	time.sleep (2)
	setcontext ('Appointment - No Summary', 'Appointment - '+summary)
        time.sleep (2)
	if guiexist ('dlgAppointment-Nosummary') == 0:
	    log ('Failed to open Corresponding Appointment dialog', 'cause')
	    raise LdtpExecutionError (0)
	else:
	    windowname = 'dlgAppointment-Nosummary'
	    ptlistname = 'ptlAppointment'
            if verifysettext (windowname, 'txtLocation', location) == 0:
                log ('Verification of location field failed', 'cause')
                raise LdtpExecutionError (0)
            else:
                if verifysettext (windowname, 'txt0', categories) == 0:
                    log ('Verification of category field failed', 'cause')
                    raise LdtpExecutionError (0)
                else:
                    if verifysettext (windowname, 'txtEventDescription', description) == 0:
                        log ('Verification of description field failed', 'cause')
                        raise LdtpExecutionError (0)
                    else:
                        #TODO: Include verification of combo boxes and check boxes after the bugs in them
                        #are fixed
                        click (windowname, 'btnCancel')
                        time.sleep (2)
                        log ('Ignore the following error message, Because of Guiexist usage', 'info')
                        if guiexist (windowname) == 1:
                            log ('Failed to close Appointment Dialog', 'cause')
                            releasecontext ()
                            raise LdtpExecutionError (0)
                        else:
                            log ('Verification of Appointment Succeeded','Pass')
                            releasecontext ()
except error,msg:
    releasecontext ()
    print 'Verification of Appointment failed' + str(msg)
    log ('Verification of Appointment failed', 'error')
    
log ('Appointment Verification', 'testend')
