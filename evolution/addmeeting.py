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

from ldtp import *
from ldtputils import *
from contact import *
#from calendar import *

def addmeeting(datafilename,recur):
    log ('Add New Meeting','teststart')
    try:
        addrbook,summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times=getmeetingdata (datafilename)
        #selectCalendarPane()
        time.sleep (3)
        selectmenuitem ('frmEvolution-Calendars','mnuFile;mnuNew;mnuMeeting')
        waittillguiexist ('frmMeeting-Nosummary')
        time.sleep (1)
        try:
            definemeeting (summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories)
        except:
            log ('Could not add main values for meeting','error')
            raise LdtpExecutionError(0)
        addattendees (attendee,email,addrbook)
        time.sleep (2)
        try:
            if recur==1 or len(exception)>0:
                click ('frmMeeting-Nosummary','btnRecurrence')
                waittillguiexist ('dlgRecurrence')
                print 'dlgRecurrence',duration[0],dur_value[0],dur_day[0],count[0],for_type[0],no_of_times[0],exception[0]
                time.sleep (4)
                insert_recurrence ('dlgRecurrence',duration[0],dur_value[0],dur_day[0],count[0],for_type[0],no_of_times[0],exception[0])
        except:
            raise LdtpExecutionError(0)
        click ('frmMeeting-Nosummary','btnSave')
        releasecontext()
        waittillguiexist ('dlgEvolutionQuery')
        remap ('evolution','dlgEvolutionQuery')
        click ('dlgEvolutionQuery','btnDon\'tSend')
        undoremap ('evolution','dlgEvolutionQuery')
        time.sleep (3)
    except:
        log ('Could not add New meeting','error')
        log ('Add New Meeting','testend')
        raise LdtpExecutionError (0)
    try:
        verifymeeting(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times)
    except:
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
        attendee = data_object.gettagvalue ('attendee')
        email = data_object.gettagvalue ('email')
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
        click ('frmMeeting-Nosummary','btnAttendees')
        waittillguiexist ('dlgRequiredParticipants')
        time.sleep (1)
        comboselect ('dlgRequiredParticipants','cboAddressBook',addrbook[0])
        remap ('evolution','dlgRequiredParticipants')
        attendee=attendee[0].split (':')
        email=email[0].split (':')
        if len(attendee)!=len(email):
            log ('Mismatch in Attendee name and email','error')
            raise LdtpExecutionError (0)
        for ind in range(len(attendee)):
            try:
                att=parsename(attendee[ind],email[ind])
                print att,"Inside for loop"
                if gettablerowindex ('dlgRequiredParticipants','tblRequiredParticipants',att)==-1:
                    print "inside if"
                    selectrow ('dlgRequiredParticipants','tblContacts',att)
                    print "row selected"
                    click ('dlgRequiredParticipants', 'btnAdd1')
                    time.sleep (1)
            except:
                log ('User not found','cause')
                raise LdtpExceptionError(0)
        click ('dlgRequiredParticipants', 'btnClose')
        undoremap ('evolution','dlgRequiredParticipants')
    except:
        log ('Attendee Addition failed','error')
        log ('Add Attendees','testend')
        raise LdtpExecutionError (0)
    log ('Add Attendees','testend')

        
def verimeetattendees(attendee,email):
    try:
        click ('frmMeeting-Nosummary','btnAttendees')
        waittillguiexist ('dlgRequiredParticipants')
        remap ('evolution','dlgRequiredParticipants')
        attendee=attendee.split (' ')
        email=email.split (' ')
        for ind in len(attendee):
            att=parsename(attendee[ind],email[ind])
            if gettablerowindex ('dlgRequiredParticipants','tblRequiredParticipants',att)==-1:
                log ('User Not found','cause')
                raise LdtpExceptionError(0)
        click ('dlgRequiredParticipants', 'btnClose')
        undoremap ('evolution','dlgRequiredParticipants')
    except:
        raise LdtpExecutionError (0)


def parsename (attendee,email):
    name=attendee
    name=name+' <'+email+'>'
    return name


def selectmeeting(fromdate,summary):
    log ('Selecting a Meeting','teststart')
    try:
        date=fromdate.split('/')
        fromdate=date[1]+'/'+date[0]+'/'+date[2]
        print fromdate
        selectdate (fromdate)
        time.sleep (2)
    except:
        log ('Unable to select date','error')
        log ('Selecting a Meeting','testend')
        raise LdtpExecutionError(0)
    try:
        remap ('evolution','frmEvolution-Calendars')
        #objects=getobjectlist('frmEvolution-Calendars')
        activatewin ('frmEvolution-Calendars')
        selectevent ('frmEvolution-Calendars','calDayView',summary)
        selectevent ('frmEvolution-Calendars','calDayView',summary)
        undoremap ('evolution','frmEvolution-Calendars')
        time.sleep (3)
    except:
        log ('Unable to select event','error')
        log ('Selecting a Meeting','testend')
    log ('Selecting a Meeting','testend')

    
def verifymeeting(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories,exception,attendee,email,duration,dur_value,dur_day,count,for_type,no_of_times):
    log ('Verify Added Meeting','teststart')
    try:
        selectmeeting (from_date[0],summary[0])
        time.sleep (2)
        selectmenuitem ('frmEvolution-Calendars','mnuFile;mnuOpenAppointment')
        setcontext ('Meeting - No summary','Meeting - '+summary[0])
        time.sleep (3)
        waittillguiexist ('frmMeeting-Nosummary')
        verimeetmainwindow(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories)
        # added attendees are not in the right side text boxes. Un comment when bug removed
        #verimeetattendees (attendee,email)
        selectmenuitem ('frmMeeting-Nosummary','mnuFile;mnuClose')
    except:
        log ('Meeting not Verified','error')
        log ('Verify Added Meeting','testend')
        raise LdtpExecutionError (0)
    log ('Verify Added Meeting','testend')


def verimeetmainwindow(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories):
    try:
#         if verifysettext ('frmMeeting-Nosummary','cboCalendar',calendar[0])==0:
#             log ('Calendar not set properly','cause')
#             raise LdtpExecutionError(0)
        print summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories
        if verifysettext ('frmMeeting-Nosummary','txtSummary',summary[0])==0:
            log ('Summary not set properly','cause')
            raise LdtpExecutionError(0)
        print location[0]
        if len(location)>0 and  verifysettext ('frmMeeting-Nosummary','txtLocation',location[0])==0:
            log ('Location not set properly','cause')
            raise LdtpExecutionError(0)
        #if verifysettext ('frmMeeting-Nosummary','txtDescription',description[0])==0:
            #log ('Description not set properly','cause')
            #raise LdtpExecutionError(0)
        if len(from_date)>0 and verifysettext ('frmMeeting-Nosummary','txtTextDateEntry',from_date[0])==0:
            log ('From Date not set properly','cause')
            raise LdtpExecutionError(0)
        if len(to_date)>0 and verifysettext ('frmMeeting-Nosummary','txtTextDateEntry1',to_date[0])==0:
            log ('To-Date not set properly','cause')
            raise LdtpExecutionError(0)
        if len(from_time)>0 and verifysettext ('frmMeeting-Nosummary','txt3',from_time[0])==0:
            log ('From-Time not set properly','cause')
            raise LdtpExectionError(0)
        if len(to_time)>0 and verifysettext ('frmMeeting-Nosummary','txt5',to_time[0])==0:
            log ('To-Time not set properly','cause')
            raise LdtpExecutionError(0)
        remap ('evolution','frmMeeting-Nosummary')
        if len(categories)>0 and  verifysettext ('frmMeeting-Nosummary','txt0',categories[0])==0:
            log ('Categories not set properly','cause')
            raise LdtpExecutionError(0)
        undoremap ('evolution','frmMeeting-Nosummary')
    except:
        raise LdtpExecutionError(0)


def definemeeting(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories):
    log ('Define meeting values','teststart')
    try:
        time.sleep (2)
        try:
            uncheck ('frmMeeting-Nosummary','mnuAlldayEvent')
            comboselect ('frmMeeting-Nosummary','cboCalendar',calendar[0])
        except:
            log ('Calendar not present','cause')
            raise LdtpExecutionError(0)
        settextvalue ('frmMeeting-Nosummary','txtSummary',summary[0])
        setcontext ('Meeting - No summary','Meeting - '+summary[0])
        print "Setting Sumary Over"
        if len(location)>0:
            settextvalue ('frmMeeting-Nosummary','txtLocation',location[0])
        print "Setting Location Over"
        if len (description)>0:
            settextvalue ('frmMeeting-Nosummary','txtDescription',description[0])
        print "Setting Desc Over"
        if len(from_date)>0:
            settextvalue ('frmMeeting-Nosummary','txtTextDateEntry',from_date[0])
        print "Setting from date Over"
        if len (to_date)>0:
            settextvalue ('frmMeeting-Nosummary','txtTextDateEntry1',to_date[0])
        print "Setting TO DATE Over"
        if len(from_time)>0:
            settextvalue ('frmMeeting-Nosummary','txt3',from_time[0])
        print "Setting from time Over"
        if len(to_time)>0:
            settextvalue ('frmMeeting-Nosummary','txt5',to_time[0])
        print "Setting to time  Over"
        try:
            selectmenuitem ('frmMeeting-Nosummary','mnuOptions;mnuClassification;mnu'+classification[0])
        except:
            log ('Classification incorrectly specified','cause')
            raise LdtpExecutionError(0)
        if len (categories)>0:
            check ('frmMeeting-Nosummary','mnuCategories')
            remap ('evolution','frmMeeting-Nosummary')
            settextvalue ('frmMeeting-Nosummary','txt0',categories[0])
            undoremap ('evolution','frmMeeting-Nosummary')
        print "Setting Categories Over"
    except:
        log ('Define Meeting values failed','error')
        log ('Define meeting values','testend')
        raise LdtpExecutionError(0)
    log ('Define meeting values','testend')


def selectdate (new_date):
    log ('Selecting the Date','teststart')
    try:
        selectmenuitem ('frmEvolution-Calendars','mnuView;mnuSelectDate')
        if waittillguiexist ('dlgSelectDate') == 0:
            log ('Select date dialog is not open', 'cause')
            raise LdtpExecutionError (0)
        time.sleep (2)
        date_components = new_date.split ('/')
        month = int (date_components[1])
        mnt=month
        if month < 0 or month > 12:
            log ('Given month is invalid', 'cause')
            raise LdtpExecutionError (0)
        if month==1:
            month='January'
        elif month==2:
            month='February'
        elif month==3:
            month='March'
        elif month==4:
            month='April'
        elif month==5:
            month='May'
        elif month==6:
            month='June'
        elif month==7:
            month='July'
        elif month==8:
            month='August'
        elif month==9:
            month='September'
        elif month==10:
            month='October'
        elif month==11:
            month='November'
        else:
            month='December'
        comboselect ('dlgSelectDate', 'cboDecember', month)
        day = int (date_components[0])
        if day < 1 or day > 31:
            log ('Given date is invalid', 'cause')
            raise LdtpExecutionError (0)
        year = date_components[2]
        if int (year) < 1111 or int (year) > 9999:
            log ('Given year is invalid', 'cause')
            raise LdtpExecutionError (0)
        setvalue ('dlgSelectDate', 'sbtn0', year)
        time.sleep (3)
        selectcalendardate ('dlgSelectDate', 'calviewCalendar', day, mnt, int (year))
    except LdtpExecutionError, msg:
        log ('Unable to select given date', 'cause')
        log ('Selecting the Date','testend')
        raise LdtpExecutionError (0)
    log ('Selecting the Date','testend')


def insert_recurrence (windowname,duration,dur_value,dur_day,count,for_type,no_of_times,exception):
    try:
        flag = 0
        if waittillguiexist (windowname) == 0:
            log ('Window: ' + windowname + ' Is not open', 'cause')
            raise LdtpExecutionError (0)
        else:
            activatewin ('dlgRecurrence')
            if stateenabled (windowname, 'btnAdd') == 1:
                log ('Add button is enabled by default!!', 'warning')
                flag = 1
            check (windowname, 'chkThisappointmentrecurs')
            time.sleep (2)
            if verifycheck (windowname, 'chkThisappointmentrecurs') == 0:
                log ('Verification of checkbox failed!!', 'cause')
                raise LdtpExecutionError (0)
            if stateenabled (windowname, 'btnAdd') == 0:
                log ('Add button is not enabled', 'cause')
                raise LdtpExecutionError (0)
            else:
                setvalue (windowname, 'sbtn0', count)
                time.sleep(2)
                remap ('evolution',windowname)
                comboselect (windowname,'cboday(s)',duration)
                undoremap ('evolution',windowname)
                remap ('evolution',windowname)
                time.sleep (2)
                
                if duration == 'day(s)':
                    pass
                elif duration == 'month(s)':
                    comboselect(windowname,'cbo1st',dur_value) 
                    comboselect(windowname,'cboday',dur_day)
                elif duration == 'week(s)':
                    # those toggle buttons are not recognized in the appmap. so leaving as it is.
                    pass
                elif duration == 'year(s)':
                    pass	  
			
                time.sleep(2)
                comboselect (windowname,'cbofor',for_type)
                undoremap ('evolution',windowname)
                remap ('evolution',windowname)
                time.sleep(2)
                print no_of_times
                if for_type == 'for':
                    setvalue(windowname,'sbtn1',str(no_of_times))
                    time.sleep(2)
                elif for_type == 'until':
                    settextvalue(windowname,'txtTextDateEntry',str(no_of_times))    
                    time.sleep(2)
                elif for_type == 'forever':
                    pass  	
                undoremap ('evolution',windowname)
                remap ('evolution',windowname)
                time.sleep(3)
                
                exception=exception.split(' ')	
                if len(exception) > 0:
                    for i in range (len (exception)):
                        click (windowname, 'btnAdd')
                        time.sleep (2)
                        if waittillguiexist ('dlgAddexception') == 0:
                            log ('Failed to open exception add dialog', 'cause')
                            raise LdtpExecutionError (0)
                        else:
                            settextvalue ('dlgAddexception', 'txtTextDateEntry', exception[i])
                            click ('dlgAddexception', 'btnOK')
                            if waittillguinotexist ('dlgAddexception') == 0:
                                log ('Failed to close exception add dialog', 'cause')
                                raise LdtpExecutionError (0)
                            
                time.sleep(3)
                undoremap ('evolution',windowname)
                remap('evolution',windowname)
                click(windowname, 'btnClose')
                log ('Recurrence details set successfully','info')
                undoremap ('evolution',windowname)
                return flag
    except ldtp.error,msg:
        print "Problem in inserting recurrence tab details " + str (msg)
        log ('Error in insertng recurrence tab details', 'error')
        return 0
