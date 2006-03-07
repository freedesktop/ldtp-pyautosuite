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

#To create an Appointment
from evoutils.calendar import *
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
	calendar = data_object.gettagvalue ('calendar')[0]
	return summary, location, description, from_date, to_date, calendar

def create_appoinment():
	log ('Create Appointment', 'teststart')
	try:
		windowname = 'frmAppointment-Nosummary'
	    	flag = 0
		more_items_todo = 'yes'
		summary, location, description, from_date, to_date, calendar = read_data()

	    	#selectmenuitem ('frmEvolution-Calendars', 'mnuView;mnuWindow;mnuCalendars')
	    	time.sleep (2)
	    	selectmenuitem ('frmEvolution-Calendars', 'mnuFile;mnuNew;mnuAppointment')
	    	time.sleep (2)

	    	if guiexist (windowname) == 0:
	        	log ('Failed to open new appointment window', 'cause')
	        	raise LdtpExecutionError (0)
	    	else:

			try:
				click(windowname,'tbtnAllDayEvent')
				from_time=0
				to_time=0
			except:
				print 'unable to click the button (All Day event)'
				log ('Create Appointment', 'testend')
				raise LdtpExecutionError (0)
#                        print windowname, summary, location, description, from_date, from_time, to_date, to_time, calendar, more_items_todo
			i = insert_appointment (windowname, summary, location, description, from_date, from_time, to_date, to_time, calendar, more_items_todo)

			if i == 1:
        	    		flag = 1
        		time.sleep (2)
			click(windowname,'btnSave')

	except:
		log('unable to Create a new appoinment','error')
		log ('Create Appointment', 'testend')
		raise LdtpExecutionError (0)
	log ('All day Appointment created','info')
	log ('Create Appointment', 'testend')

create_appoinment()
