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

from ldtp import *
from ldtputils import *
from contact import *
from evoutils.calendar import *

def addmeeting(datafilename,recur):
    log ('Add New Meeting','teststart')
    try:
        addrbook, summary, location, description, from_date, to_date, from_time, to_time, calendar, classification, categories, exception, attendee, email, duration, dur_value, dur_day, count, for_type, no_of_times = getmeetingdata (datafilename)
        print addrbook, summary, location, description, from_date, to_date, from_time, to_time, calendar, classification, categories, exception, attendee, email, duration, dur_value, dur_day, count, for_type, no_of_times
        selectCalendarPane()
        time.sleep (3)
        selectmenuitem ('frmEvolution-Calendars','mnuFile;mnuNew;mnuMeeting')
        windowname = 'frmMeeting-*'
        waittillguiexist (windowname)
        time.sleep (1)
        menuuncheck (windowname, 'mnuOptions;mnuAllDayEvent')
        remap ('evolution',windowname)
        try:
            definemeeting (summary, location, description, from_date, to_date, from_time, to_time, calendar, classification, categories)
        except:
            log ('Could not add main values for meeting','error')
            raise LdtpExecutionError(0)

        addattendees (attendee,email,addrbook)
        time.sleep (2)
        try:
            if recur==1 or len(exception)>0:
                selectmenuitem (windowname, 'mnuOptions;mnuRecurrence')
                waittillguiexist ('dlgRecurrence')
                time.sleep (4)
                insert_recurrence ('dlgRecurrence',duration[0],dur_value[0],
                                   dur_day[0],count[0],for_type[0],
                                   no_of_times[0],exception)
        except:
            raise LdtpExecutionError(0)
        click (windowname,'btnSave')
        if waittillguiexist ('dlgEvolutionQuery') != 0:
            click ('dlgEvolutionQuery','btnDonotSend')
        time.sleep (3)
    except:
        log ('Could not add New meeting','error')
        log ('Add New Meeting','testend')
        raise LdtpExecutionError (0)
    try:
        verifymeeting(summary,location,description,from_date,to_date,from_time,
                      to_time,calendar,classification,categories,exception,
                      attendee,email,duration,dur_value,dur_day,count,for_type,
                      no_of_times)
    except:
        log ('Verification Failed', 'cause')
        log ('Add New Meeting','testend')
        raise LdtpExecutionError (0)
    log ('Add New Meeting','testend')

    
def getmeetingdata(datafilename):
    log ('Getting Values for New Meeting','teststart')
    try:
        data_object = LdtpDataFileParser (datafilename)
        addrbook = data_object.gettagvalue ('addrbook')
        summary = data_object.gettagvalue ('summary')
        location = data_object.gettagvalue ('location')
        description = data_object.gettagvalue ('description')
        from_date = data_object.gettagvalue ('from_date')
        to_date = data_object.gettagvalue ('to_date')
        from_time = data_object.gettagvalue ('from_time')
        to_time = data_object.gettagvalue ('to_time')
        calendar = data_object.gettagvalue ('calendar')
        classification = data_object.gettagvalue ('classification')
        categories = data_object.gettagvalue ('categories')
        exception = data_object.gettagvalue ('exception')
        index = 1
        attendee = []
        email = []
        while True:
            att = data_object.gettagvalue ('attendee'+str(index))
            em = data_object.gettagvalue ('email'+str(index))

            if att == []  or em == []:
                break
            attendee.append (att[0])
            email.append (em[0])
            index += 1

        duration = data_object.gettagvalue ('duration')
        dur_value = data_object.gettagvalue ('durvalue')
        dur_day = data_object.gettagvalue ('durday')
        count = data_object.gettagvalue ('count')
        for_type = data_object.gettagvalue ('fortype')
        no_of_times = data_object.gettagvalue ('nooftimes')
    except:
        log ('Error While getting Values','error')
        log ('Getting Values for New Meeting','testend')
        raise LdtpExecutionError(0)
    log ('Getting Values for New Meeting','testend')
    print addrbook,summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times
    return addrbook,summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times


def addattendees(attendee,email,addrbook):
    log ('Add Attendees','teststart')
    try:
        window_id = 'frmMeeting-*'
        click (window_id,'btnAttendees')
        waittillguiexist ('dlgRequiredParticipants')
        time.sleep (1)
        comboselect ('dlgRequiredParticipants','cboAddressBook',addrbook[0])
        remap ('evolution','dlgRequiredParticipants')
        #attendee=attendee[0].split (':')
        #email=email[0].split (':')
        print attendee, email
        if len(attendee)!=len(email):
            log ('Mismatch in Attendee name and email','error')
            raise LdtpExecutionError (0)
        for ind in range(len(attendee)):
            try:
                att = parsename(attendee[ind],email[ind])
                print att,"Inside for loop"
                if gettablerowindex ('dlgRequiredParticipants','tblRequiredParticipants',att)==-1:
                    print "inside if"
                    selectrowpartialmatch ('dlgRequiredParticipants','tblContacts',att)
                    print "row selected"
                    click ('dlgRequiredParticipants', 'btnAdd1')
                    time.sleep (1)
            except:
                log ('User not found','cause')
                raise LdtpExceptionError(0)
        click ('dlgRequiredParticipants', 'btnClose')
        #undoremap ('evolution','dlgRequiredParticipants')
    except:
        log ('Attendee Addition failed','error')
        log ('Add Attendees','testend')
        raise LdtpExecutionError (0)
    log ('Add Attendees','testend')

        
def verimeetattendees(attendee,email):
    try:
        click ('frmMeeting-Nosummary','btnAttendees')
        waittillguiexist ('dlgRequiredParticipants')
        attendee=attendee.split (' ')
        email=email.split (' ')
        for ind in len(attendee):
            att=parsename(attendee[ind],email[ind])
            if gettablerowindex ('dlgRequiredParticipants','tblRequiredParticipants',att)==-1:
                log ('User Not found','cause')
                raise LdtpExceptionError(0)
        click ('dlgRequiredParticipants', 'btnClose')
    except:
        raise LdtpExecutionError (0)


def parsename (attendee,email):
    name=attendee
    name=name+' <'+email+'>'
    return name


def verifymeeting(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times):
    log ('Verify Added Meeting','teststart')
    try:
        try:
            print from_date
            print summary
        except:
            print 'from_date, summary not available'
        selectcalevent (from_date[0],summary[0])
        time.sleep (2)
        selectmenuitem ('frmEvolution-Calendars','mnuFile;mnuOpenAppointment')
        window_id = 'frmMeeting-*'
        time.sleep (3)
        waittillguiexist (window_id)
        verimeetmainwindow(summary,location,description,from_date,to_date,from_time,
                           to_time,calendar,classification,categories)
        #verimeetattendees (attendee,email)
        if duration or dur_value or dur_day or count or for_type or no_of_times:
            selectmenuitem (window_id,'mnuOptions;mnuRecurrence')
            waittillguiexist ('dlgRecurrence')
            verify_recurrence ('dlgRecurrence', duration, dur_value, dur_day, count,
                               for_type, no_of_times, exception)
            waittillguinotexist ('dlgRecurrence')
        selectmenuitem (window_id,'mnuFile;mnuClose')
    except:
        log ('Meeting not Verified','error')
        log ('Verify Added Meeting','testend')
        selectmenuitem (window_id,'mnuFile;mnuClose')
        raise LdtpExecutionError (0)
    log ('Verify Added Meeting','testend')


def verimeetmainwindow(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories):
    try:
#         if verifysettext ('frmMeeting-Nosummary','cboCalendar',calendar[0])==0:
#             log ('Calendar not set properly','cause')
#             raise LdtpExecutionError(0)
        window_id = 'frmMeeting-*'
        if verifysettext (window_id,'txtSummary',summary[0])==0:
            log ('Summary not set properly','cause')
            raise LdtpExecutionError(0)
        print location[0]
        if len(location)>0 and  verifysettext (window_id,'txtLocation',location[0])==0:
            log ('Location not set properly','cause')
            raise LdtpExecutionError(0)
        if verifysettext (window_id,'txtDescription',description[0])==0:
            log ('Description not set properly','cause')
            raise LdtpExecutionError(0)
#         if len(from_date)>0 and verifysettext ('frmMeeting-Nosummary','txtTextDateEntry',from_date[0])==0:
#             log ('From Date not set properly','cause')
#             raise LdtpExecutionError(0)
#         if len(to_date)>0 and verifysettext ('frmMeeting-Nosummary','txtTextDateEntry1',to_date[0])==0:
#             log ('To-Date not set properly','cause')
#             raise LdtpExecutionError(0)
#         if len(from_time)>0 and verifysettext ('frmMeeting-Nosummary','txt3',from_time[0])==0:
#             log ('From-Time not set properly','cause')
#             raise LdtpExectionError(0)
#         if len(to_time)>0 and verifysettext ('frmMeeting-Nosummary','txt5',to_time[0])==0:
#             log ('To-Time not set properly','cause')
#             raise LdtpExecutionError(0)
        if len(categories)>0 and  verifysettext (window_id,'txtCategories',categories[0])==0:
            log ('Categories not set properly','cause')
            raise LdtpExecutionError(0)
    except:
        raise LdtpExecutionError(0)


def definemeeting(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories):
    log ('Define meeting values','teststart')
    try:
        time.sleep (2)
        window_id = 'frmMeeting-*'
        try:
            menuuncheck (window_id,'mnuOptions;mnuAllDayEvent')
            comboselect (window_id,'cboCalendar',calendar[0])
        except:
            log ('Calendar not present','cause')
            raise LdtpExecutionError(0)
        settextvalue (window_id,'txtSummary',summary[0])

        print "Setting Sumary Over"
        if len(location)>0:
            settextvalue (window_id,'txtLocation',location[0])
        print "Setting Location Over"
        if len (description)>0:
            settextvalue (window_id,'txtDescription',description[0])
        print "Setting Desc Over"
        if len(from_date)>0:
            settextvalue (window_id,'txtDate',from_date[0])
            time.sleep (2)
            if guiexist ('*Warning') == 1:
               log ('Error in input date format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)

        print "Setting from date Over"
        if len (to_date)>0:
            comboselect (window_id, 'cbofor','until')
            settextvalue (window_id,'txtDate1',to_date[0])
            time.sleep (2)
            if guiexist ('*Warning') == 1:
               log ('Error in input date format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)
            
        print "Setting TO DATE Over"
        if len(from_time)>0:
            settextvalue (window_id,'txt3',from_time[0])
            time.sleep (2)
            if guiexist ('*Warning') == 1:
               log ('Error in input date format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)

        print "Setting from time Over"
        if len(to_time)>0:
            settextvalue (window_id,'txt5',to_time[0])
            time.sleep (2)
            if guiexist ('*Warning') == 1:
               log ('Error in input date format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)
            
        print "Setting to time  Over"
        try:
            selectmenuitem (window_id,'mnuOptions;mnuClassification;mnu'+classification[0])
            print "Classification menu is special"
        except:
            log ('Classification incorrectly specified','cause')
            raise LdtpExecutionError(0)
        if len (categories)>0:
            menucheck (window_id,'mnuEdit;mnuCategories')
            remap ('evolution',window_id)
            settextvalue (window_id,'txtCategories',categories[0])
        print "Setting Categories Over"
    except:
        log ('Define Meeting values failed','error')
        log ('Define meeting values','testend')
        raise LdtpExecutionError(0)
    log ('Define meeting values','testend')
