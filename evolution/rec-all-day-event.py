#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
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

# To create an appoinment with attachment.

#from create-appointment import *
from evoutils.calendar import *
from ldtp import *
from ldtputils import *

def read_data():
	#Initialising XML parser with data file
	data_object = LdtpDataFileParser (datafilename)

	#Extracting imput data from xml file
	summary = data_object.gettagvalue ('summary')[0]
	location = data_object.gettagvalue ('location')[0]
	description = data_object.gettagvalue ('description')[0]
	from_date = data_object.gettagvalue ('start_date')[0]
	to_date = data_object.gettagvalue ('due_date')[0]
	from_time = data_object.gettagvalue ('start_time')[0]
	to_time = data_object.gettagvalue ('due_time')[0]
	calendar = data_object.gettagvalue ('calendar')[0]
	
	repeat_every = data_object.gettagvalue ('repeat_every')[0]
	duration = data_object.gettagvalue ('duration')[0]
	no_of_times = data_object.gettagvalue ('no_of_times')[0]
	repeat_method = data_object.gettagvalue ('repeat_method')[0]
	exceptions = data_object.gettagvalue ('exceptions')[0]
	dur_value = data_object.gettagvalue ('dur_value')[0]
	dur_day = data_object.gettagvalue ('dur_day')[0]
	return dur_value, dur_day, repeat_every, duration, no_of_times, repeat_method, exceptions, summary, location, description, from_date, to_date, from_time, to_time, calendar

def appointment_withrecurrence():

	try:
		log('Recursive All day event','teststart')
		windowname = 'frmAppointment-Nosummary'
		dur_value, dur_day, repeat_every, duration, no_of_times, repeat_method, exceptions, summary, location, description, from_date, to_date, from_time, to_time, calendar = read_data()

		time.sleep(5)
		more_items_todo = 'yes'
	    	selectmenuitem ('frmEvolution-Calendars', 'mnuFile;mnuFile;mnuAppointment')
	    	time.sleep (2)
	
	    	if guiexist (windowname) == 0:
	        	log ('Failed to open new appointment window', 'cause')
	        	raise LdtpExecutionError (0)
	    	else:
			try:
				click(windowname,'tbtnAlldayEvent')
				from_time=0
				to_time=0
			except:
				print 'unable to click the button (All Day event)'
				log('Recursive All day event','testend')
				raise LdtpExecutionError (0)

			i = insert_appointment (windowname, summary, location, description, from_date, from_time, to_date, to_time, calendar, more_items_todo)

		if i == 1:
            		flag = 1
	        else:
			try:
				click(windowname,'btnRecurrence')
				waittillguiexist('dlgRecurrence')
				insert_recurrence ('dlgRecurrence',duration, dur_value, dur_day, repeat_every, repeat_method, no_of_times, exceptions)
				time.sleep(3)
				click(windowname, 'btnSave')
			except:
				print 'unable to create the recursive appoinment'
				log('Recursive All day event','testend')
				raise LdtpExecutionError (0)
		
	except:
		log('unable to create the recursive appoinment','error')
		log('Recursive All day event','testend')
		raise LdtpExecutionError (0)
	log('Recursive all day event Created','info')
	log('Create appoinment with attachment','testend')
appointment_withrecurrence()
