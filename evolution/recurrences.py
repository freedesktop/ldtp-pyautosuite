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

s1 ='Unable to get gui handle'

def Create_rec_meeting(summary,location):
	try:
		wait(5)
		#code to implement creation of meeting
		selectmenuitem('Evolution-Calendars','mnuFile;mnuNew;mnuAppointment')
		selecttab('dlgAppointment-Nosummary','ptlAppointment - No summary','0')
		settextvalue('dlgAppointment-Nosummary','txtSummary',summary)
		setcontext('Appointment - No summary','Appointment - '+summary)
		settextvalue('dlgAppointment-Nosummary','txtLocation',location)
		settextvalue('dlgAppointment-Nosummary','txtEventDescription',description)
		selecttab('dlgAppointment-Nosummary','ptlAppointment - No summary','1')
		check('dlgAppointment-Nosummary','chkThisappointmentrecurs')
		click('dlgAppointment-Nosummary','btnAdd')
		settextvalue('dlgAddexception','txtTextDateEntry','06/29/05')
		click('dlgAddexception','btnOK')
		click('dlgAppointment-Nosummary','btnOK')
		log('Creation-of-Recurring-Appointment','pass')
		
	except :
		print "Error"
		log('Creation-of-Recurring-Appointment','fail')


def verify_rec_meeting(summary,location,description):
	#for i in range (1,4):
		#print i
	try:
		selecteventindex('Evolution-Calendars','calview',1)
		selectmenuitem('Evolution-Calendars','mnuFile;mnuOpenAppointment')
		wait(5)
		setcontext ('Appointment - No summary', 'Appointment - '+summary)
		if verifysettext('dlgAppointment-Nosummary','txtSummary',summary)==1:
			if verifysettext('dlgAppointment-Nosummary','txtLocation',location)==1:
				if verifysettext('dlgAppointment-Nosummary','txtEventDescription',description)==1:
					#if check('dlgAppointment-Nosummary','chkThisappointmentoccurs')==1:
					print "File Found"
					click('dlgaAppoinment-Nosummary','btnCancel')
		log('Verification-of-Recurring-Appointment','pass')				
	except error,msg:
		if string.find(str(msg),s1)== -1:
			print "File not found(nt cz of gui handle)."	
		print "--File  nt found..bt  stilll continuing"
		log('Verification-of-Recurring-Appointment','fail')




log('CreatinAppointment','teststart')

#call the function
Create_rec_meeting(summary,location)
			
#call the function
verify_rec_meeting(summary,location,description)

log('CreatinAppointment','testend')
		
