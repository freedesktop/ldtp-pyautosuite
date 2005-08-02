#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
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
#To create an Appointment

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

#creation fo appointment
log ('Appointment Creation', 'teststart')

try:
    windowname = 'dlgAppointment-Nosummary'
    ptlistname = 'ptlAppointment-Nosummary0'
    selectmenuitem ('evolution', 'mnuView;mnuWindow;mnuCalendars')
    time.sleep (2)
    selectmenuitem ('evolution', 'mnuFile;mnuFileNew;mnuAppointment')
    time.sleep (2)
    if guiexist (windowname) == 0:
        log ('Failed to open new appointment window', 'cause')
        raise LdtpExecutionError (0)
    else:
        log ('Insertion of Appointment values', 'teststart')
        insert_appointment (windowname, ptlistname, summary, location, description, date0,
                            time0, date1, time1, classification, categories)
        log ('Insertion of Appointment values', 'testend')
        time.sleep (2)
        log ('Insertion of recurrence values', 'teststart')
        insert_recurrence (windowname, ptlistname, moncount, on, day, occurences, exception)
        log ('Insertion of recurrence values', 'testend')
        time.sleep (2)
        click (windowname , 'btnOK')
        time.sleep (3)
        log ('Ignore the following error message, Because of Guiexist usage', 'info')
        if guiexist ('dlgAppointment-Nosummary') == 1:
            log ('Failed to close appointment dialog' ,'cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        releasecontext ()
        log ('Appointment creation succeeded', 'pass')
except error,msg:
    releasecontext ()
    print 'Creation of appointment failed' + str(msg)
    log ('Creation of appointment failed', 'error')
    
log ('Appointment Creation', 'testend')
