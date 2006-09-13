#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
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
	from_date = data_object.gettagvalue ('from_date')[0]
	to_date = data_object.gettagvalue ('to_date')[0]
	from_time = data_object.gettagvalue ('from_time')[0]
	to_time = data_object.gettagvalue ('to_time')[0]
	calendar = data_object.gettagvalue ('calendar')[0]
	filename = data_object.gettagvalue ('filename')[0]
	repeat_every = data_object.gettagvalue ('repeat_every')[0]
	duration = data_object.gettagvalue ('duration')[0]
	dur_value = data_object.gettagvalue ('dur_value')[0]
	dur_day = data_object.gettagvalue ('dur_day')[0]
	repeat_method = data_object.gettagvalue ('repeat_method')[0]
	no_of_times = data_object.gettagvalue ('no_of_times')[0]
	exceptions = data_object.gettagvalue ('exceptions')[0]
#	print  '1', repeat_every, duration, no_of_times, repeat_method, exceptions, dur_value, dur_day, filename
#	print  '2', summary, location, description, from_date, to_date, from_time, to_time, calendar	
	return repeat_every, duration, no_of_times, repeat_method, exceptions, dur_value, dur_day, filename, summary, location, description, from_date, to_date, from_time, to_time, calendar

def appointment_withattachment():

	try:
		log('Create recursive appoinment with attachment','teststart')
		windowname = 'frmAppointment-Nosummary'
		repeat_every, duration, no_of_times, repeat_method, exceptions, dur_value, dur_day, filename, summary, location, description, from_date, to_date, from_time, to_time, calendar = read_data()

		more_items_todo = 'yes'
	    	selectmenuitem ('frmEvolution-Calendars', 'mnuFile;mnuFile;mnuAppointment')
	    	time.sleep (2)
	
	    	if guiexist (windowname) == 0:
	        	log ('Failed to open new appointment window', 'cause')
			log('Create recursive appoinment with attachment','testend')
	        	raise LdtpExecutionError (0)
	    	else:
			i = insert_appointment (windowname, summary, location, description, from_date, from_time, to_date, to_time, calendar, more_items_todo)

		if i == 1:
            		flag = 1
	        else:
			try:
				click(windowname,'btnRecurrence')
				waittillguiexist('dlgRecurrence')
				insert_recurrence ('dlgRecurrence',duration, dur_value, dur_day, repeat_every, repeat_method, no_of_times, exceptions)
				time.sleep(3)
			except:
				log('Failure in adding recurance data','error')
				print 'Failure in adding recurance data'
				log('Create recursive appoinment with attachment','testend')
				raise LdtpExecutionError (0)

			try:
				click(windowname,'btnAttachments')
				waittillguiexist('dlgAttachfile(s)')
				time.sleep(3)
				selectrow ('dlgAttachfile(s)', 'tblFiles', filename)
				time.sleep(1)
				click('dlgAttachfile(s)','btnOpen')
			except:
				print 'unable to attach the file'
				log('Unable to attach the file','error')
				log('Create recursive appoinment with attachment','testend')
				raise LdtpExecutionError (0)

		click(windowname, 'btnSave')
		
	except:
		log('unable to create the recursive appoinment with attachment','error')
		log('Create recursive appoinment with attachment','testend')
		raise LdtpExecutionError (0)
        log('Recursive appointment with attachment created','info')	
	log('Create recursive appoinment with attachment','testend')
appointment_withattachment()
