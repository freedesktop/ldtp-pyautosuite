#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
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
from evoutils.calendar import *
from ldtputils import *
from evoutils import *

datafilename = 'create-appointment.xml'
#Initialising XML parser with data file
data_object = LdtpDataFileParser (datafilename)

#Extracting imput data from xml file
summary = data_object.gettagvalue ('summary')[0]
location = data_object.gettagvalue ('location')[0]
description = data_object.gettagvalue ('description')[0]
from_date = data_object.gettagvalue ('from_date')[0]
to_date = data_object.gettagvalue ('to_date')[0]
from_time = data_object.gettagvalue ('from_time')[0]
to_time = data_object.gettagvalue ('to_time')[0]
calendar = data_object.gettagvalue ('calendar')[0]
classification = data_object.gettagvalue ('classification')[0]
categories = data_object.gettagvalue ('categories')[0]
#count = data_object.gettagvalue ('count')[0]
#forever = data_object.gettagvalue ('for')[0]
#occurences = data_object.gettagvalue ('occurences')[0]
#exception = data_object.gettagvalue ('exception')

#creation of appointment
log ('Appointment Creation', 'teststart')

try:
    selectCalendarPane()
    windowname = 'frmAppointment-*'
    ptlistname = 'ptl0'
    flag = 0
    selectmenuitem ('frmEvolution-*', 'mnuFile;mnuNew;mnuAppointment')
    waittillguiexist (windowname) 
    if guiexist (windowname) == 0:
        log ('Failed to open new appointment window', 'cause')
        raise LdtpExecutionError (0)
    else:
        log ('Insertion of Appointment values', 'teststart')
        #i = insert_appointment (windowname, ptlistname, summary, location, description, from_date,from_time, to_date, to_time, calendar, classification, categories) 
        i = insert_appointment (windowname, summary, location, description, from_date, from_time, to_date, to_time, calendar, 'No') 
        if i == 1:
            flag = 1
        log ('Insertion of Appointment values', 'testend')
        time.sleep (2)
        if i == 0:
            log ('Insertion of recurrence values', 'teststart')
            if i == 1:
                flag = 1
                log ('Insertion of recurrence values', 'testend')
                time.sleep (2)
        if stateenabled (windowname, 'btnOK') == 1:
            click (windowname , 'btnOK')
        else:
            log ('OK Button is in disabled state!!', 'warning')
            click (windowname , 'btnCancel')
        time.sleep (3)
        if waittillguinotexist ('dlgAppointment-Nosummary') == 0:
            log ('Failed to close appointment dialog' ,'cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        if flag == 1:
            log ('Appointment creation succeeded', 'fail')
        else:
            log ('Appointment creation succeeded', 'pass')
except LdtpExecutionError,msg:
    #releasecontext ()
    print 'Creation of appointment failed' + str(msg)
    log ('Creation of appointment failed', 'error')
    log ('Appointment Creation', 'testend')
except error, msg:
    #releasecontext ()
    print 'Creation of appointment failed' + str(msg)
    log ('Creation of appointment failed', 'error')
    log ('Appointment Creation', 'testend')
    raise LdtpExecutionError (0)
    
log ('Appointment Creation', 'testend')
