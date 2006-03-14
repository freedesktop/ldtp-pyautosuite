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
	from_date = data_object.gettagvalue ('from_date')[0]
	to_date = data_object.gettagvalue ('to_date')[0]
	from_time = data_object.gettagvalue ('from_time')[0]
	to_time = data_object.gettagvalue ('to_time')[0]
	calendar = data_object.gettagvalue ('calendar')[0]
	filename = data_object.gettagvalue ('filename')[0]
	return filename, summary, location, description, from_date, to_date, from_time, to_time, calendar

def appointment_withattachment():

	try:
		log('Create appoinment with attachment','teststart')
		windowname = 'frmAppointment-*'
		filename, summary, location, description, from_date, to_date, from_time, to_time, calendar = read_data()
		more_items_todo = 'yes'
		
	    	selectmenuitem ('frmEvolution-Calendars', 'mnuFile;mnuFile;mnuAppointment')
	    	time.sleep (2)
	
	    	if guiexist (windowname) == 0:
	        	log ('Failed to open new appointment window', 'cause')
			log('Create appoinment with attachment','testend')
	        	raise LdtpExecutionError (0)
	    	else:
			i = insert_appointment (windowname, summary, location, description, from_date, from_time, to_date, to_time, calendar, more_items_todo)

		if i == 1:
            		flag = 1
	        else:
			try:
				click(windowname,'btnAttach')
				waittillguiexist('dlgAttachfile(s)')
				time.sleep(3)
				selectrow ('dlgAttachfile(s)', 'tblFiles', filename)
				time.sleep(2)
				click('dlgAttachfile(s)','btnOpen')
			except:
				print 'unable to select the file'
				log('Create appoinment with attachment','testend')
				raise LdtpExecutionError (0)

		if click(windowname, 'btnSave') == 0:
			log('Unable to click the Save button','cause')
			log('Create appoinment with attachment','testend')
		else:
			log('Appoinment with attachment created','testend')
	except:
		log('unable to create the appoinment with attachment','error')
		log('Create appoinment with attachment','testend')
		raise LdtpExecutionError (0)

appointment_withattachment()
