#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Anjana <anjana_091@rediffmail.com>
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

#trying to read from the file
file = open('appointment.dat', 'r')
argmts = file.readlines()
summary = argmts[0].strip( )
location = argmts[1].strip( )
description = argmts[2].strip( )
status = argmts[3].strip( )
s1 = 'Unable to get gui handle'

def Create_meeting(summary,location,description,status):
	try:
		#code to implement creation of meeting
		selectmenuitem('Evolution-Mail','mnuView;mnuWindow;mnuCalendars')
		selectmenuitem('Evolution-Calendars','mnuFile;mnuNew;mnuAppointment')
		wait(3)
		selecttab('dlgAppointment-Nosummary','ptlAppointment - No summary','0')
		settextvalue('dlgAppointment-Nosummary','txtSummary',summary)
		setcontext('Appointment - No summary','Appointment - '+summary)
		settextvalue('dlgAppointment-Nosummary','txtLocation',location)
		comboselect('dlgAppointment-Nosummary','Classification','Private')
		click('dlgAppointment-Nosummary','btnCategories')
		settextvalue('dlgCategories','txtItem',status)
		click('dlgCategories','btnOK')
		settextvalue('dlgAppointment-Nosummary','txtEventDescription',description)
		check ('dlgAppointment-Nosummary','chkAlarm')
		comboselect('dlgAppointment-Nosummary','Alarm','1 hour before appointment')
		click('dlgAppointment-Nosummary','btnCustomize')
		click('dlgAlarms','btnAdd')
		comboselect('dlgAddAlarm','cmbpop','Play a sound')
		comboselect('dlgAddAlarm','cmbmin','minute(s)')
		comboselect('dlgAddAlarm','cmbbefore','before')
		comboselect('dlgAddAlarm','cmbstart','end of appointment')
		check('dlgAddAlarm','chkRepeatthealarm')
		setvalue('dlgAddAlarm','sbtnnum1','13')
		setvalue('dlgAddAlarm','sbtnnum2','3')
		comboselect('dlgAddAlarm','cmbminutes','hours')
		check('dlgAddAlarm','chkCustomalarmsound')
		uncheck('dlgAddAlarm','chkCustomalarmsound')
		click('dlgAddAlarm','btnOK')
		click('dlgAlarms','btnOK')
		click('dlgAppointment-Nosummary','btnOK')
		log('Creation-of-Appointment','pass')
	except error:
		print "Cudnt create appointment"
		log('Creation-of-Appointment','fail')
#END

def verify_meeting(summary,location,description):
	#for i in range (1,2):
	#print i
	try:
		selecteventindex('Evolution-Calendars','calview',1)
		selectmenuitem('Evolution-Calendars','mnuFile;mnuOpenAppointment')
		wait(5)
		setcontext ('Appointment - No summary', 'Appointment - '+summary)
		if verifysettext('dlgAppointment-Nosummary','txtSummary',summary)==1:
			if verifysettext('dlgAppointment-Nosummary','txtLocation',location)==1:
				if verifysettext('dlgAppointment-Nosummary','txtEventDescription',description)==1:
					print "File found"
					click('dlgAppointment-Nosummary','btnCancel')		
					log('Verification-of-Appointment','pass')
			
	except error,msg:
		if string.find(str(msg),s1)== -1:
			print "----Error---"
			log('Verification-of-Appointment','fail')
#END


log ('CreatinAppointment','teststart')

#call the function
Create_meeting(summary,location,description,status)
wait(2)		
#call the function
verify_meeting(summary,location,description)		



log('CreatinAppointment','testend')

