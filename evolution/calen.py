#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Prashanth Mohan  <prashmohan@gmail.com>
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

from evoutils.calendar import *
from ldtputils import *
from evoutils import *


def create_appointment (summary, location, description, from_date, from_time,
                        to_date, to_time, calendar):
    log ('Appointment Creation', 'teststart')
    try:
        selectCalendarPane()
        windowname = 'frmAppointment-*'
        flag = 0
        selectmenuitem ('frmEvolution-*', 'mnuFile;mnuNew;mnuAppointment')
        waittillguiexist (windowname) 
        if guiexist (windowname) == 0:
            log ('Failed to open new appointment window', 'cause')
            raise LdtpExecutionError (0)

        log ('Insertion of Appointment values', 'teststart')
        menuuncheck (windowname, 'mnuOptions;mnuAllDayEvent')
        insert_appointment (windowname, summary, location, description,
                            from_date, from_time, to_date, to_time,
                            calendar, 'No')
        try:
            print 'starting verify... make sure evolution has focus'
            verify_appointment (windowname, summary, location, description,
                                from_date, from_time, to_date, to_time)
            print 'verify succeeded'
        except:
            log ('Verification of Appointment failed','cause')
            raise LdtpExecutionError (0)
        log ('Appointment creation succeeded', 'pass')
    except LdtpExecutionError,msg:
        print 'Creation of appointment failed' + str(msg)
        log ('Appointment creation succeeded', 'fail')
        log ('Appointment Creation', 'testend')
        raise LdtpExecutionError (0)
    
    log ('Appointment Creation', 'testend')


def create_all_day_event (summary, location, description, from_date,
                          to_date, calendar):
    log ('Create Appointment', 'teststart')
    try:
        windowname = 'frmAppointment-*'
        flag = 0
        more_items_todo = 'yes'
        #summary, location, description, from_date, to_date, calendar = read_data()
        
        time.sleep (2)
        selectmenuitem ('frmEvolution-Calendars', 'mnuFile;mnuNew;mnuAppointment')
        waittillguiexist (windowname)
        time.sleep (2)
        
        if guiexist (windowname) == 0:
            log ('Failed to open new appointment window', 'cause')
            raise LdtpExecutionError (0)
        try:
            menucheck (windowname, 'mnuOptions;mnuAllDayEvent')
            from_time = '0'
            to_time = '0'
        except:
            log ('unable to click the button (All Day event)','cause')
            raise LdtpExecutionError (0)

        insert_appointment (windowname, summary, location, description,
                            from_date, from_time, to_date, to_time,
                            calendar, more_items_todo)
        time.sleep (2)
        click(windowname,'btnSave')

        print 'All Day Event has been completed'
        try:
            print 'starting verify... make sure evolution has focus'
            verify_appointment (windowname, summary, location, description,
                                from_date, from_time, to_date, to_time)
            print 'verify succeeded'
        except:
            log ('Verification of Event failed','cause')
            raise LdtpExecutionError (0)
            
    except:
        log('unable to Create a new appoinment','error')
        log ('Create Appointment', 'fail')
        log ('Create Appointment', 'testend')
        raise LdtpExecutionError (0)
    log ('All day Appointment created','info')
    log ('Create Appointment', 'pass')
    log ('Create Appointment', 'testend')
