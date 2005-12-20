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

#To insert values into an Appointment tab
def insert_appointment (windowname, ptlistname, summary, location, description, from_date, from_time, to_date, to_time, calendar, classification, categories):
	try:
		flag = 0
		selecttab (windowname, ptlistname, 'Appointment')
		time.sleep (2)
		settextvalue (windowname, 'txtSummary', summary)
		if windowname == 'dlgMeeting-Nosummary':
			setcontext ('Meeting - No summary', 'Meeting - ' + summary)
		else:
			setcontext ('Appointment - No summary', 'Appointment - ' + summary)
			time.sleep (2)
		if setandverify (windowname, 'txtLocation', location) == 0:
			log ('Failed to set value in location field', 'cause')
			raise LdtpExecutionError (0)
          
		if classification != gettextvalue (windowname, 'cboClassification'):
			comboselect (windowname, 'cboClassification', classification)
			if verifyselect (windowname, 'cboClassification', classification) == 0:
				log ('Verification of Classification combo box failed!!', 'warning')
				flag = 1

		click (windowname, 'btnCategories')
		time.sleep (3)
		if guiexist ('dlgCategories') == 0:
			log ('Failed to open categories dialog', 'cause')
			raise LdtpExecutionError (0)
		else:
			select_catagory (categories)             
                         
		if setandverify (windowname, 'txtDescription', description) == 0:
			log ('Failed to set value in Event description field', 'cause')
			raise LdtpExecutionError (0)
		if from_date != '0':
			if setandverify (windowname, 'txtStarttime', from_date) == 0:
				log ('Failed to set value in From date entry', 'cause')
				raise LdtpExecutionError (0)
		if from_time != '0':
			if setandverify (windowname, 'txt9', from_time) == 0:
				log ('Failed to set value in From time entry', 'cause')
				raise LdtpExecutionError (0)
		if to_date != '0':
			if setandverify (windowname, 'txtEndtime', to_date) == 0:
				log ('Failed to set value in To date entry', 'cause')
				raise LdtpExecutionError (0)
		if to_time != '0':
			if setandverify (windowname, 'txt7', to_time) == 0:
				log ('Failed to set value in From time entry', 'cause')
				raise LdtpExecutionError (0)
		print '****************' + str (flag) + '**************'
		return flag
	except error,msg:
		print "Problem in inserting appointment tab details " + str (msg)
		log('errorinappointmenttab','error')
		return 0

def getrecentrowindex (windowname, tablename, column, summary):
	totalcount = getrowcount (windowname, tablename)
	if totalcount != 0:
		for i in range (totalcount-1, -1, -1):
			cur_summary = getcellvalue (windowname, tablename, i, column)
			print cur_summary + ' == ' + summary
			if summary == cur_summary:
				return i
	return -1

#Add participants to Meeting from Required Participants popup
def add_participant (windowname, participant):
	try:
		if waittillguiexist (windowname) == 0:
			log ('Window: ' + windowname + ' Is not open', 'cause')
			raise LdtpExecutionError (0)

		settextvalue (windowname, txtSearch, participant)
		selectrow (windowname, tblContacts, 0)
		if stateenabled (windowname, 'btnAdd') == 1:
			click (windowname , 'btnAdd')
		else:
			log ('Add Button is in disabled state no contact found!!', 'warning')

		click (windowname , 'btnClose')
		time.sleep (3)
		if waittillguinotexist (windowname) == 0:
			log ('Failed to close Meeting dialog' ,'cause')
			raise LdtpExecutionError (0)

		time.sleep (2)
		return 1

	except error,msg:
		print "Problem in adding participant " + str (msg)
		log('errorinrequiredparticipant','error')
		return 0


          
#Select categories from categories popup
def select_catagory (catagory):
	try:
		if guiexist ('dlgCategories') == 0:
			log ('Failed to open categories dialog', 'cause')
			raise LdtpExecutionError (0)
		else:
			index = gettablerowindex ('dlgCategories', 'tbl0', catagory)
			checkrow ('dlgCategories', 'tbl0', index)
			time.sleep (2)
			if verifysettext ('dlgCategories', 'txtItem(s)belongtothesecategories', catagory) == 0:
				#TODO: Make sure to close all the open windows before raising exception
				log ('Failed to select given category', 'cause')
				raise LdtpExecutionError (0)
			else:
				click ('dlgCategories', 'btnOK')
				time.sleep (1)
			if waittillguinotexist ('dlgCategories') == 0:
				log ('Failed to close Category dialog', 'cause')
				raise LdtpExecutionError (0)
			else:
				return 1
	except error,msg:
		print "Problem in selecting catagory" + str (msg)
		log('errorinselectcatagory','error')
		return 0

 
#Verifyf the fields in appointment tab  
def verifyappointmenttab (windowname, ptlistname, summary, location, description, from_date, from_time, to_date, to_time, calendar, classification, categories):
	try:
		if windowname == 'dlgMeeting-Nosummary':
			setcontext ('Meeting - No summary', 'Meeting - ' + summary)
			if guiexist ('dlgMeeting-Nosummary') == 0:
				log ('Failed to open meeting dialog', 'cause')
				raise LdtpExecutionError (0)
		else:
			setcontext ('Appointment - No summary', 'Appointment - ' + summary)
			if guiexist ('dlgAppointment-Nosummary') == 0:
				log ('Failed to open appointment dialog', 'cause')
				raise LdtpExecutionError (0)

		time.sleep (2)
		if verifysettext (windowname, 'txtSummary', summary) == 0:
			log ('In appointment tab summary field is not set to ' + summary, cause)
			raise LdtpExecutionError (0)

		if verifysettext (windowname, 'txtLocation', location) == 0:
			log ('In appointment tab location field is not set to ' + location, cause)
			raise LdtpExecutionError (0)

		if verifysettext (windowname, 'txtDescription', description) == 0:
			log ('In appointment tab description field is not set to ' + description, cause)
			raise LdtpExecutionError (0)

		if from_date:
			if verifysettext (windowname, 'txtStarttime', from_date) == 0:
				log ('In appointment tab From date is not set to ' + from_date, 'cause')
				raise LdtpExecutionError (0)

		if from_time:
			if verifysettext (windowname, 'txt9', from_time) == 0:
				log ('In appointment tab From time is not set to ' + from_time, 'cause')
				raise LdtpExecutionError (0)

		if to_date:
			if verifysettext (windowname, 'txtEndtime', to_date) == 0:
				log ('In appointment tab To date is not set to' + to_date, 'cause')
				raise LdtpExecutionError (0)

		if to_time:
			if verifysettext (windowname, 'txt7', to_time) == 0:
				log ('In appointment tab From time is not set to ' + to_time, 'cause')
				raise LdtpExecutionError (0)
	
		print '****************' + str (flag) + '**************'
		return flag
	
	except error,msg:
		log ('Verification of Appointment tab fields failed ' + str (msg), 'error')
		return 0
	

def selectdate (new_date):
	print "inside select date"
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
		print month
		time.sleep (5)
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
		print "inside"
		time.sleep (4)
		
		flag = 0
		if waittillguiexist (windowname) == 0:
			log ('Window: ' + windowname + ' Is not open', 'cause')
			
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
			print count
			time.sleep (5)
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

		
