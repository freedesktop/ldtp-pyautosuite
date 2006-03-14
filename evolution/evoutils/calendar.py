#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Premkumar <jpremkumar@novell.com>
#     Venkateswaran S <wenkat.s@gmail.com>
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

def getrecentrowindex (windowname, tablename, column, summary):
     totalcount = getrowcount (windowname, tablename)
     if totalcount != 0:
          for i in range (totalcount-1, -1, -1):
               cur_summary = getcellvalue (windowname, tablename, i, column)
               print cur_summary + ' == ' + summary
               if summary == cur_summary:
                    return i
     return -1

def selectdate (new_date):
     try:
          selectmenuitem ('frmEvolution-Calendars','mnuView;mnuSelectDate')
          if waittillguiexist ('dlgSelectDate') == 0:
               log ('Select date dialog is not open', 'cause')
               raise LdtpExecutionError (0)
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
	  	  
          click ('dlgSelectDate', 'cbo*')
	  comboselect ('dlgSelectDate', 'cbo*', month)
          time.sleep (3)
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
	  raise LdtpExecutionError (0)

def insert_appointment (windowname, summary, location, description, from_date, from_time,
                        to_date, to_time, calendar, more_items_todo):
     try:
          flag = 0
          time.sleep (2)
          settextvalue (windowname, 'txtSummary', summary)
          #setcontext ('Appointment - No summary', 'Appointment - ' + summary)
          time.sleep (2)
	  if setandverify (windowname, 'txtLocation', location) == 0:
               log ('Failed to set value in location field', 'cause')
               raise LdtpExecutionError (0)
	  else:
                value = gettextvalue (windowname, 'cboCalendar')
		print value
		if calendar != value:
                    comboselect (windowname, 'cboCalendar', calendar)
                    #if verifyselect (windowname, 'cboCalendar', calendar) == 0:
                    #     print calendar
		    #	 time.sleep(3)
		    #	 log ('Verification of calendar combo box failed!!', 'warning')
                    #     flag = 1
          if from_date != '0':
               if setandverify (windowname, 'txtDate1', from_date) == 0:
               	    log ('Failed to set value in From date entry', 'cause')
                    raise LdtpExecutionError (0)
          if str(from_time) != '0':
               if setandverify (windowname, 'txt3', from_time) == 0:
                    log ('Failed to set value in From time entry', 'cause')
                    raise LdtpExecutionError (0)
          if to_date != '0':
               if setandverify (windowname, 'txtDate1', to_date) == 0:
                    log ('Failed to set value in To date entry', 'cause')
                    raise LdtpExecutionError (0)
          if str(to_time) != '0':
               if setandverify (windowname, 'txt5', to_time) == 0:
                    log ('Failed to set value in From time entry', 'cause')
                    raise LdtpExecutionError (0)
	  if setandverify (windowname, 'txtDescription', description) == 0:
               log ('Failed to set value in description field', 'cause')
               raise LdtpExecutionError (0)
          
	  time.sleep(3)
          if more_items_todo != 'yes':
		click(windowname, 'btnSave')
          return flag

     except error,msg:
          print "Problem in inserting appointment tab details " + str (msg)
          log('errorinappointmenttab','error')
          return 0


def insert_recurrence (windowname, duration, dur_value, dur_day, count, for_type, no_of_times, exception):
     try:
          flag = 0
          if waittillguiexist (windowname) == 0:
               log ('Window: ' + windowname + ' Is not open', 'cause')
               raise LdtpExecutionError (0)
	  activatewin (windowname)
	  if stateenabled (windowname, 'btnAdd') == 1:
               log ('Add button is enabled by default!!', 'warning')
               flag = 1
          time.sleep (1)
	  check (windowname, 'chkThisappointmentrecurs')

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
          return flag
     except ldtp.error,msg:
          print "Problem in inserting recurrence tab details " + str (msg)
          log ('Error in insertng recurrence tab details', 'error')
          return 0

def selectcalevent(fromdate,summary):

   log ('Selecting a Cal event','teststart')
   try:
       time.sleep(5)
       date=fromdate.split('/')
       fromdate=date[1]+'/'+date[0]+'/'+date[2]
       print fromdate
       selectdate (fromdate)
       time.sleep (2)
   except:
       log ('Unable to select date','error')
       log ('Selecting a  Cal event','testend')
       raise LdtpExecutionError (0)
   try:
       #remap ('evolution','frmEvolution-Calendars')
       activatewin ('frmEvolution-Calendars')
       selectevent ('frmEvolution-Calendars','calDayView',summary)
       #undoremap ('evolution','frmEvolution-Calendars')
       time.sleep (3)
   except:
       log ('Unable to select event','error')
       log ('Selecting a Cal event','testend')
       raise LdtpExecutionError (0)
   log ('Selecting a Cal event','testend')

def selectCalendarPane():
    """Selects the Calendars Pane in Evolution"""
    log ('Open Evolution Calendars Pane','teststart')
    try:
         window_id=getcurwindow()
         click (window_id,'tbtnCalendars')
         waittillguiexist ('frmEvolution-Calendars')
    except:
        log ('error selecting Calendars pane','error')
        log ('Open Evolution Calendars Pane','testend')
        raise LdtpExecutionError(0)

    log ('Open Evolution Calendars Pane','testend')

def getcurwindow():
     if guiexist ('frmEvolution-Mail')==1:
          return 'frmEvolution-Mail'
     elif guiexist ('frmEvolution-Contacts')==1:
          return 'frmEvolution-Contacts'
     elif guiexist ('frmEvolution-Calendars')==1:
          return 'frmEvolution-Calendars'
     elif guiexist ('frmEvolution-Memos')==1:
          return 'frmEvolution-Memos'
     elif guiexist ('frmEvolution-Tasks')==1:
          return 'frmEvolution-Tasks'
