#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Premkumar <jpremkumar@novell.com>
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

#To insert values into an Recurrence tab
def insert_recurrence (windowname, ptlistname, moncount = '3', on = 'First', day = 'Monday', occurences = '5',
                       exception = '2'):
     try: 
         selecttab (windowname, ptlistname, '1')
         time.sleep (2)
         check (windowname, 'chkThisappointmentrecurs')
         time.sleep(1)
         #verifycheck (windowname, 'chkThisappointmentrecurs')
         if stateenabled (windowname, 'btnAdd') == 0:
              log ('Add button is not enabled', 'cause')
              raise LdtpExecutionError (0)
         else:
              setvalue (windowname, 'sbtn0', moncount)
              selectitem (windowname, 'cboday', 'month(s)')
              time.sleep (2)
              selectitem (windowname, 'cbo1st', on)
              time.sleep (2)
              selectitem (windowname, 'cboforever', 'for')
              time.sleep (2)
              setvalue (windowname, 'sbtn1', occurences)
              time.sleep (2)
              #TODO: After the bug regarding ADD buttons not working is fixed uncomment the following segment of code

              #click (windowname, 'btnAdd')
              #time.sleep (2)
              #if guiexist ('dlgAddexception') == 0:
              #     log ('Failed to open exception add dialog', 'cause')
              #     raise LdtpExecutionError (0)
              #else:
                   #TODO: Logic for calculating the exception date from the given exception number
                   #and creating an exception for the same
                   #no_of_months = moncount * exception
                   #time.sleep (1)
              
     except error,msg:
          print "Problem in inserting recurrence details " + str (msg)
          log('errorinrecurrencetab','error')


#To insert values into an Appointment tab
def insert_appointment (windowname, ptlistname, summary, location, description, date0, time0,
                        date1, time1, classification = 'Public', categories = 'Business'):
     try:
         print 'windowname is: ' + windowname
         print 'tablist name is: ' + ptlistname
         selecttab (windowname, ptlistname, '0')
         time.sleep (2)
         settextvalue (windowname,'txt3', summary)
         if windowname == 'dlgMeeting-Nosummary':
              setcontext ('Meeting - No summary', 'Meeting - ' + summary)
         else:
              setcontext ('Appointment - No summary', 'Appointment - ' + summary)
         time.sleep (2)
         if setandverify (windowname, 'txt2',  location) == 0:
              log ('Failed to set value in location field', 'cause')
              raise LdtpExecutionError (0)
         else:
              comboselect (windowname, 'cboPublic', classification)
              #TODO: Use verifyselect to verify the previous operation. Currently could not do
              #due to ambiguos 

              click (windowname, 'btnCategories')
              time.sleep (3)
              if guiexist ('dlgCategories') == 0:
                   log ('Failed to open categories dialog', 'cause')
                   raise LdtpExecutionError (0)
              else:              
                   #NOTE: Here is a small work around for selecting the category because of unclear
                   #behaviour of the table in the category dialog.
                   index = gettablerowindex ('dlgCategories', 'tbl0', categories )
                   selectrowindex ('dlgCategories', 'tbl0', index + 1)
                   time.sleep (2)
                   checkrow ('dlgCategories', 'tbl0', index)
                   time.sleep (2)
                   if verifysettext ('dlgCategories', 'txt0', categories) == 0:
                        log ('Failed to select given category', 'cause')
                        raise LdtpExecutionError (0)
                   else:
                        click ('dlgCategories', 'btnOK')
                        time.sleep (1)
                        if guiexist ('dlgCategories') == 1:
                             log ('Failed to close Category dialog', 'cause')
                             raise LdtpExecutionError (0)
                        else:
                             if  setandverify (windowname, 'txtEventDescription', description) == 0:
                                  log ('Failed to set value in Event description field', 'cause')
                                  raise LdtpExecutionError (0)
                             else:
                                  check (windowname,'chkAlldayevent')

                                  #FIXME: Because of appmap generating same label for both the date fields
                                  #could not set date into first field
                                  #settextvalue (windowname, 'txtTextDateEntry2', date0)
                                  #settextvalue (windowname, 'txtTextDateEntry1', date1)

                                  check ('dlgMeeting-Nosummary','chkAlarm')
     except error,msg:
          print "Problem in inserting appointment details " + str (msg)
          log('errorinappointmenttab','error')

