#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
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

from addmeeting import *

def modifymeeting(datafilename,occurance=0):
    log ('Modify Meeting','teststart')
    try:
        addrbook,summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times=getmeetingdata (datafilename)
        print addrbook,summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times
#        raw_input ('modfify meeting values')
        #selectCalendarPane()
        try:
            selectmeeting (from_date[0],summary[0])
            selectmenuitem ('frmEvolution-Calendars','mnuFile;mnuOpenAppointment')
        except:
            log ('Event not available','cause')
            raise LdtpExecutionError(0)
        try:
            setcontext ('Meeting - No summary','Meeting - '+summary[0])
            waittillguiexist ('frmMeeting-Nosummary')
            definemeeting (summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories)
        except:
            log ('Error While modifying values','error')
            raise LdtpExecutionError (0)
        try:
            if len(attendee)>0:
                addattendees (attendee,email,addrbook)
                time.sleep (1)
        except:
            log ('error adding attendees','cause')
            raise LdtpExecutionError(0)
# uncomment if recurrence setting should also be changed
#         try:
#             if recur==1 or len(exception)>0:
#                 #click ('frmMeeting-Nosummary','btnRecurrence')
#                 selectmenuitem ('frmMeeting-Nosummary','mnuOptions;mnuRecurrence')
#                 waittillguiexist ('dlgRecurrence')             
#                 insert_recurrence ('dlgRecurrence',duration[0],dur_value[0],dur_day[0],count[0],for_type[0],no_of_times[0],exception[0])
#         except:
#             log ('error during recurrence','cause')
#             raise LdtpExecutionError(0)
        click ('frmMeeting-Nosummary','btnSave')
        time.sleep (3)
        if guiexist ('dlgQuestion')==1:
            remap ('evolution','dlgQuestion')
            if occurance==0:
                click ('dlgQuestion','rbtnThisInstanceOnly')
            elif occurance==1:
                click ('dlgQuestion','rbtnAllInstances')
            click ('dlgQuestion','btnOK')
            undoremap ('evolution','dlgQuestion')
        releasecontext()
        waittillguiexist ('dlgEvolutionQuery')
        remap ('evolution','dlgEvolutionQuery')
        click ('dlgEvolutionQuery','btnDon\'tSend')
        undoremap ('evolution','dlgEvolutionQuery')
        waittillguinotexist ('dlgEvolutionQuery')
    except:
        log ('Could not Modify New meeting','error')
        log ('Modify Meeting','testend')
        raise LdtpExecutionError (0)
    try:
        log ('Verify modified Meeting','teststart')
        verifymeeting (summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times)
        #verifymeeting (addrbook,summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times)
    except:
        log ('Modify meeting verify failed','error')
        log ('Modify Meeting','testend')
        raise LdtpExecutionError (0)
    log ('Modify Meeting','testend')

def deletemeeting(fromdate,summary,occurance=0):
    """ occurance == 0 Non recursive
        occurance == 1 if only this instance
        occurance == 2 for all instances"""
    log ('Delete Meeting/Appointment','teststart')
    try:
        selectmeeting (fromdate,summary)
        time.sleep (2)
        if occurance == 0:
            selectmenuitem ('frmEvolution-Calendars','mnuEdit;mnuDelete')
        elif occurance == 1:
            selectmenuitem ('frmEvolution-Calendars','mnuEdit;mnuDeletethisOccurrence')
        else:
            selectmenuitem ('frmEvolution-Calendars','mnuEdit;mnuDeleteAllOccurrences')
        waittillguiexist ('dlgEvolutionQuery')
        remap ('evolution','dlgEvolutionQuery')
        click ('dlgEvolutionQuery','btnDelete')
        undoremap ('evolution','dlgEvolutionQuery')
        time.sleep (3)
        waittillguiexist ('dlgEvolutionQuery')
        remap ('evolution','dlgEvolutionQuery')
        click ('dlgEvolutionQuery','btnDon\'tSend')
        undoremap ('evolution','dlgEvolutionQuery')
        waittillguinotexist ('dlgEvolutionQuery')
    except:
        log ('Delete Meeting/Appointment Failed','error')
        log ('Delete Meeting/Appointment','testend')
        raise LdtpExecutionError(0)
    log ('Delete Meeting/Appointment','testend')
