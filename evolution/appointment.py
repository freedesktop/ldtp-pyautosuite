#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
#     Prashanth Mohan <prashmohan@gmail.com>
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

from ldtputils import *
from evoutils import *
from evoutils.calendar import *

def create_appointment (datafilename, more_items='no'):
    try:
        summary, location, description, from_date, to_date, from_time, to_time, calendar, classification, categories, count, duration, no_of_times, for_type, exception, dur_value, dur_day = get_appointment_data (datafilename)

        windowname = 'frmAppointment-*'
        insert_appointment (windowname, summary, location, description,
                            from_date, from_time, to_date, to_time,
                            calendar, more_items)
        if more_items == 'yes':
            selectmenuitem (windowname, 'mnuOptions;mnuRecurrence')
            waittillguiexist ('dlgRecurrence')
            time.sleep (4)
            insert_recurrence ('*Recurrence', duration, dur_value, dur_day, count, for_type, no_of_times, exception)

        click (windowname,'btnSave')
        try:
            print 'starting verify... make sure evolution has focus'
            verify_appointment (windowname, summary, location, description,
                                from_date, from_time, to_date, to_time, more_items)

            if more_items == 'yes':
                selectmenuitem (windowname, 'mnuOptions;mnuRecurrence')
                waittillguiexist ('dlgRecurrence')
                time.sleep (4)
                verify_recurrence ('dlgRecurrence', duration, dur_value, dur_day, count,
                                   for_type, no_of_times, exception)
            print 'verify succeeded'
            selectmenuitem (windowname,'mnuFile;mnuClose')
        except:
            log ('Verification of Appointment failed','cause')
            selectmenuitem (windowname,'mnuFile;mnuClose')
            raise LdtpExecutionError (0)
    except LdtpExecutionError,msg:
        print 'Creation of appointment failed' + str(msg)
        raise LdtpExecutionError (0)
    

def insert_appointment (windowname, summary, location, description,
                        from_date, from_time, to_date, to_time,
                        calendar, more_items_todo):
     try:
          time.sleep (2)
          setandverify (windowname, 'txtSummary', summary)
          time.sleep (2)
	  if setandverify (windowname, 'txtLocation', location) == 0:
               log ('Failed to set value in location field', 'cause')
               raise LdtpExecutionError (0)
	  else:
                value = gettextvalue (windowname, 'cboCalendar')
		print value
		if calendar != value:
                    comboselect (windowname, 'cboCalendar', calendar)
          if from_date != '0':
               if setandverify (windowname, 'txtDate', from_date) == 0:
               	    log ('Failed to set value in From date entry', 'cause')
                    raise LdtpExecutionError (0)

          time.sleep (3)
          if guiexist ('*Warning') == 1:
               log ('Error in input date format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)
          
          if to_date != '0':
               try:
                    comboselect (windowname, 'cbofor','until')
               except:
                    pass
               if setandverify (windowname, 'txtDate1', to_date) == 0:
                    log ('Failed to set value in To date entry', 'cause')
                    raise LdtpExecutionError (0)
          time.sleep (1)
          if guiexist ('*Warning') == 1:
               log ('Error in input date format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)
          if str(from_time) != '0':
               if setandverify (windowname, 'txt5', from_time) == 0:
                    log ('Failed to set value in From time entry', 'cause')
                    raise LdtpExecutionError (0)
          time.sleep (1)
          if guiexist ('*Warning') == 1:
               log ('Error in input time format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)
          
          if str(to_time) != '0':
               if setandverify (windowname, 'txt7', to_time) == 0:
                    log ('Failed to set value in to time entry', 'cause')
                    raise LdtpExecutionError (0)
          if guiexist ('*Warning') == 1:
               log ('Error in input time format','cause')
               click ('*Warning','btnOK')
               raise LdtpExecutionError (0)
               
	  if setandverify (windowname, 'txtDescription', description) == 0:
               log ('Failed to set value in description field', 'cause')
               raise LdtpExecutionError (0)
          
	  time.sleep(3)
          if more_items_todo != 'yes':
		click(windowname, 'btnSave')
     except error,msg:
          print "Problem in inserting appointment tab details " + str (msg)
          log('errorinappointmenttab','error')
          raise LdtpExecutionError (0)


def verify_appointment (windowname, summary, location, description,
                        from_date, from_time, to_date, to_time, more_item_to_do='no'):
     selectcalevent (from_date, summary)
     remap ('evolution','frmEvolution-Calendars')
     selectmenuitem ('frmEvolution-Calendars','mnuFile;mnuOpenAppointment')
     win_name = 'frmAppointment-*'
     waittillguiexist (win_name)
     if gettextvalue (win_name, 'txtSummary') != summary:
          log ('Summary not identical','cause')
          raise LdtpExecutionError (0)

     if gettextvalue (win_name, 'txtLocation') != location:
          log ('Location not identical','cause')
          raise LdtpExecutionError (0)
     
     if gettextvalue (win_name, 'txtDescription') != description:
          log ('Description not identical','cause')
          raise LdtpExecutionError (0)

#      if from_date != '0':
#           from_date = from_date.split ('/')
#           year = int ('20'+from_date[2])
#           month = int (from_date[0])
#           day = int (from_date[1])
#           date = datetime.date (year, month, day)
#           weekday = days [date.weekday()]
#           format = weekday + ' ' + from_date[1] + ' ' + months[month-1] + ' ' + str(year)
#           if gettextvalue (win_name,'txtDate').lower() != format.lower():
#                log ('From Date not identical','cause')
#                raise LdtpExecutionError (0)

#      if to_date != '0':
#           to_date = to_date.split ('/')
#           year = int ('20'+to_date[2])
#           month = int (to_date[0])
#           day = int (to_date[1])
#           date = datetime.date (year, month, day)
#           weekday = days [date.weekday()]
#           format = weekday + ' ' + to_date[1] + ' ' + months[month-1] + ' ' + str(year)
#           if gettextvalue (win_name,'txtDate1').lower() != format.lower():
#                log ('To Date not identical','cause')
#                raise LdtpExecutionError (0)

     if from_time != '0':
          if not gettextvalue (win_name,'txt5').startswith (from_time):
               log ('From time not identical','cause')
               raise LdtpExecutionError (0)

     if to_time != '0':
          if not gettextvalue (win_name,'txt7').startswith (to_time):
               log ('From time not identical','cause')
               raise LdtpExecutionError (0)
     if more_item_to_do != 'yes':
          click (win_name, 'btnClose')


def get_appointment_data (datafilename):
    data_object = LdtpDataFileParser (datafilename)
    summary = data_object.gettagvalue ('summary')
    if summary:
        summary = summary [0]
        
    location = data_object.gettagvalue ('location')
    if location:
        location = location [0]
            
    description = data_object.gettagvalue ('description')
    if description:
        description = description [0]
        
    from_date = data_object.gettagvalue ('from_date')
    if from_date:
        from_date = from_date [0]
    
    to_date = data_object.gettagvalue ('to_date')
    if to_date:
        to_date = to_date [0]
    
    from_time = data_object.gettagvalue ('from_time')
    if from_time:
        from_time = '0'
    
    to_time = data_object.gettagvalue ('to_time')
    if to_time:
        to_time = '0'
    
    calendar = data_object.gettagvalue ('calendar')
    if calendar:
        calendar = calendar [0]
    
    classification = data_object.gettagvalue ('classification')
    if classification:
        classification = classification [0]
    
    categories = data_object.gettagvalue ('categories')
    if categories:
        categories = categories [0]

    count = data_object.gettagvalue ('count')
    if count:
        count = count [0]
        
    duration = data_object.gettagvalue ('duration')
    if duration:
        duration = duration[0]
        
    no_of_times = data_object.gettagvalue ('nooftimes')
    if no_of_times:
        no_of_times = no_of_times [0]
    
    fortype = data_object.gettagvalue ('fortype')
    if fortype:
        fortype = fortype [0]

    exception = data_object.gettagvalue ('exception')
        
    durvalue = data_object.gettagvalue ('durvalue')
    if durvalue:
        durvalue = durvalue [0]

    dur_day = data_object.gettagvalue ('durday')
    if dur_day:
        dur_day = dur_day [0]

    return summary, location, description, from_date, to_date, from_time, to_time, \
           calendar, classification, categories, count, duration, no_of_times, \
           fortype, exception, durvalue, dur_day

def modifyappointment (datafilename, occurance=0):
   try:
       try:
           summary, location, description, from_date, to_date, from_time, to_time, calendar, classification, categories, count, duration, no_of_times, for_type, exception, dur_value, dur_day = get_appointment_data (datafilename)
	   windowname = 'frmAppointment-*'
	   selectcalevent (new_date,old_summary)
	   time.sleep(2)
           if selectmenuitem('frmEvolution-Calendars','mnuFile;mnuOpenAppointment') == 1:
		log('Appointment opened','info')
	   else:
		log('Unable to select the menu File;OpenAppointment','cause')
		raise LdtpExecutionError (0)
       except:
           log ('Event not available','cause')
           raise LdtpExecutionError(0)
       try:
           waittillguiexist (windowname)
           if duration or no_of_times or for_type or exception or dur_value or dur_day:
                more_items = 'yes'
           else:
                more_items = 'no'
           insert_appointment (windowname, summary, location, description,
                               from_date, from_time, to_date, to_time,
                               calendar, more_items)
           if more_items == 'yes':
                selectmenuitem (windowname, 'mnuOptions;mnuRecurrence')
                waittillguiexist ('dlgRecurrence')
                time.sleep (4)
                insert_recurrence ('*Recurrence', duration, dur_value, dur_day, count, for_type, no_of_times, exception)

	   click(windowname,'btnSave')
	   time.sleep(3)
       except:
           log ('Error While modifying values','error')
           raise LdtpExecutionError (0)
       if occurance != 0 and guiexist ('dlgQuestion') == 1:
           remap ('evolution','dlgQuestion')
           if occurance == 1:
               click ('dlgQuestion','rbtnThisInstanceOnly')
           elif occurance == 2:
               click ('dlgQuestion','rbtnAllInstances')
           click ('dlgQuestion','btnOK')
       time.sleep(3)
       ## verification
       try:
           print 'starting verify... make sure evolution has focus'
           verify_appointment (windowname, summary, location, description,
                               from_date, from_time, to_date, to_time, more_items)

           if more_items == 'yes':
                selectmenuitem (windowname, 'mnuOptions;mnuRecurrence')
                waittillguiexist ('dlgRecurrence')
                time.sleep (4)
                verify_recurrence ('dlgRecurrence', duration, dur_value, dur_day, count,
                                   for_type, no_of_times, exception)
           print 'verify succeeded'
           selectmenuitem (windowname,'mnuFile;mnuClose')
       except:
            log ('Verification Failed','cause')
            raise LdtpExecutionError (0)
   except:
       log ('Could not Modify the appointment','error')
       raise LdtpExecutionError (0)
   log('Appointment modified','info')   
    
