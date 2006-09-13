#!/usr/bin/python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Premkumar <jpremkumar@novell.com>
#     Venkateswaran S <wenkat.s@gmail.com>
#     Prashanth Mohan <prashmohan@gmail.com>
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
import datetime

days   = ['Monday','Tuesday','Wednesday','Thursday',
          'Friday','Saturday','Sunday']
months = ['January','February','March','April',
          'May','June','July','August','September',
          'October','Novemeber','December']


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
#           if int (year) < 11 or int (year) > 99:
#                log ('Given year is invalid', 'cause')
#                raise LdtpExecutionError (0)
          setvalue ('dlgSelectDate', 'sbtn0', '20'+year)
          time.sleep (3)
          selectcalendardate ('dlgSelectDate', 'calviewCalendar', day, mnt,
                              int ('20'+year))

     except LdtpExecutionError, msg:
          log ('Unable to select given date', 'cause')
	  raise LdtpExecutionError (0)


def insert_recurrence (windowname, duration, dur_value, dur_day, count, for_type, no_of_times, exception):
     print windowname, duration, dur_value, dur_day, count, for_type, no_of_times, exception
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
	       comboselect (windowname,'cboday(s)',duration)	
               time.sleep (2)
               remap ('evolution',windowname)
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
               remap ('evolution',windowname)
	       comboselect (windowname,'cbofor',for_type)
	       time.sleep(2)
               remap ('evolution',windowname)
	       print no_of_times
	       if for_type == 'for':
	       	    setvalue(windowname,'sbtn1',str(no_of_times))
                    time.sleep(2)
	       elif for_type == 'until':
		    settextvalue(windowname,'txtDate',str(no_of_times))    
	            time.sleep(2)
	       elif for_type == 'forever':
	            pass  	
	       time.sleep(3)
               print exception
               if exception:
                    exception = exception[0]
	       exception=exception.split(' ')	
               if len(exception) > 0:
                    for i in range (len (exception)):
                         click (windowname, 'btnAdd')
                         time.sleep (2)
                         if waittillguiexist ('dlgAddexception') == 0:
                              log ('Failed to open exception add dialog', 'cause')
                              raise LdtpExecutionError (0)
                         else:
                              settextvalue ('dlgAddexception', 'txtDate',
                                            exception[i])
                              click ('dlgAddexception', 'btnOK')
                              if waittillguinotexist ('dlgAddexception') == 0:
                                   log ('Failed to close exception add dialog',
                                        'cause')
                                   raise LdtpExecutionError (0)

	       time.sleep(3)
               click(windowname, 'btnClose')
	       log ('Recurrence details set successfully','info')
          return flag
     except ldtp.error,msg:
          print "Problem in inserting recurrence tab details " + str (msg)
          log ('Error in insertng recurrence tab details', 'error')
          return 0

def verify_recurrence (windowname, duration, dur_value, dur_day, count,
                       for_type, no_of_times, exception):
     try:
          remap ('evolution', windowname)
          objlist = getobjectlist (windowname)
          if waittillguiexist (windowname) == 0:
               log ('Window: ' + windowname + ' Is not open', 'cause')
               raise LdtpExecutionError (0)
	  activatewin (windowname)
          if verifycheck (windowname, 'chkThisappointmentrecurs') == 0:
               log ('Verification of checkbox failed!!', 'cause')
               raise LdtpExecutionError (0)
	  if stateenabled (windowname, 'btnAdd') == 0:
               log ('Add button is not enabled', 'cause')
               raise LdtpExecutionError (0)
          else:
               if count and int(getvalue (windowname, 'sbtn0')) !=  int(count[0]):
                    log ('No of recurrence not set','cause')
                    raise LdtpExecutionError (0)
	       time.sleep(2)

               if duration and not 'cbo'+duration[0] in objlist:
                    log ('Duration not selected','cause')
                    raise LdtpExecutionError (0)

	       if duration and duration[0] == 'day(s)':
		    pass
	       elif duration and duration[0] == 'month(s)':
                    if not ('cbo'+dur_value[0] in objlist and 'cbo'+dur_day[0] in objlist):
                         log ('duration value not selected','cause')
                         raise LdtpExecutionError (0)

	       elif duration and duration[0] == 'week(s)':
		    # those toggle buttons are not recognized in the appmap. so leaving as it is.
		    pass
               elif duration and duration[0] == 'year(s)':
                    pass

               if for_type and not 'cbo'+for_type[0] in objlist:
                    log ('For Type not in object list','cause')
                    raise LdtpExecutionError (0)

               if for_type and for_type[0] == 'for' and str(int(getvalue(windowname,'sbtn1'))) != str (no_of_times[0]):
                    log ('For value not properly set','cause')
                    raise LdtpExecutionError (0)

# 	       elif for_type and for_type[0] == 'until' and gettextvalue(windowname,'txtDate') != get_date_format(no_of_times[0]):
#                     log ('Until Value not properly set','cause')
#                     raise LdtpExecutionError (0)
	       elif for_type and for_type[0] == 'forever':
	            pass  	
	       time.sleep(3)
               if exception:
                    exception = exception[0].split(' ')	
               if len(exception) > 0:
                    for ex in exception:
                         try:
                              select = ex.split ('/')
                              selectrowpartialmatch (windowname,'tbl0',select[0]+'/'+select[1]+'/20'+select[2])
                         except:
                              log ('Execption not added','cause')
                              raise LdtpExecutionError (0)
	       time.sleep(3)
               click(windowname, 'btnClose')
	       log ('Recurrence details set successfully','info')
     except:
          log ('Error in insertng recurrence tab details', 'error')
          click(windowname, 'btnClose')

     
def selectcalevent(fromdate,summary):
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
       activatewin ('frmEvolution-Calendars')
       try:
            selectevent ('frmEvolution-Calendars','calDayView',summary)
       except:
            print 'Unable to select event'
       time.sleep (3)
   except:
       log ('Unable to select event','error')
       raise LdtpExecutionError (0)


def get_date_format (date):

     date = date.split ('/')
     year = int ('20'+date[2])
     month = int (date[0])
     day = int (date[1])
     format = date[1] + ' ' + months[month-1] + ' ' + str(year)
     date = datetime.date (year, month, day)
     weekday = days [date.weekday()]
     format = weekday + ' ' + format
     return format

def parsename (attendee,email):
    name=attendee
    name=name+' <'+email+'>'
    return name


