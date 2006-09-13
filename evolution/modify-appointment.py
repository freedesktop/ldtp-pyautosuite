#!/usr/bin/python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
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
# To modify a current appointment.
from ldtp import *
from ldtputils import *
from evoutils.calendar import *

def read_data():
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
	new_date = data_object.gettagvalue ('date')[0]
	old_summary = data_object.gettagvalue ('old_summary')[0]
#	print new_date, old_summary, summary, location, description, from_date, to_date, from_time, to_time, calendar
	return new_date, old_summary, summary, location, description, from_date, to_date, from_time, to_time, calendar

def modifyappointment(occurance,new_date, old_summary, summary, location, description, from_date, to_date, from_time, to_time, calendar):

   log ('Modify Appointment','teststart')
   try:
       try:
 
	   windowname = 'frmAppointment-Nosummary'
	   more_items_todo = 'yes'
	   selectcalevent (new_date,old_summary)
	   time.sleep(2)
           if selectmenuitem('frmEvolution-Calendars','mnuFile;mnuOpenAppointment') == 1:
		log('Appointment opened','info')
	   else:
		log('Unable to select the menu File;OpenAppointment','cause')
           	log ('Modify Appointment','testend')
		raise LdtpExecutionError (0)
       except:
           log ('Event not available','cause')
           log ('Modify Appointment','testend')
           raise LdtpExecutionError(0)
       try:
           setcontext ('Appointment - No summary','Appointment - '+old_summary)
           waittillguiexist ('frmAppointment-Nosummary')
           #definemeeting(summary,location,description,from_date,to_date,from_time,to_time,calendar,classification,categories)
	   insert_appointment (windowname, summary, location, description, from_date, from_time, to_date, to_time, calendar, more_items_todo)
	   click(windowname,'btnSave')
	   time.sleep(3)
       except:
           log ('Error While modifying values','error')
           raise LdtpExecutionError (0)
       if guiexist ('dlgQuestion')==1:
           remap ('evolution','dlgQuestion')
           if occurance==0:
               click ('dlgQuestion','rbtnThisInstanceOnly')
           elif occurance==1:
               click ('dlgQuestion','rbtnAllInstances')
           click ('dlgQuestion','btnOK')
           undoremap ('evolution','dlgQuestion')
       releasecontext()
       time.sleep(3)
       if guiexist ('dlgEvolutionQuery'):
	       remap ('evolution','dlgEvolutionQuery')
       	       click ('dlgEvolutionQuery','btnDon\'tSend')
       	       undoremap ('evolution','dlgEvolutionQuery')
   except:
       log ('Could not Modify the appointment','error')
       log ('Modify Appointment','testend')
       raise LdtpExecutionError (0)

   log('Appointment modified','info')   
   log ('Modify Appointment','testend')

new_date, old_summary, summary, location, description, from_date, to_date, from_time, to_time, calendar = read_data()
log('Modify all instance of an appointment','teststart')
modifyappointment(1,new_date, old_summary, summary, location, description, from_date, to_date, from_time, to_time, calendar)
log('Modify all instance of an appointment','testend')
log('Modify This instance only','teststart')
modifyappointment(0,new_date, old_summary, summary, location, description, from_date, to_date, from_time, to_time, calendar)
log('Modify This instance only','testend')
