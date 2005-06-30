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
s1='Unable to get gui handle'

#Deletion of appointment
def delete_appointment(summary,location,description):
	#for i in range(1,4):
		#print i
	try:
		selecteventindex('Evolution-Calendars','calview',1)
		selectmenuitem('Evolution-Calendars','mnuFile;mnuOpenAppointment')
		wait(5)
                setcontext ('Appointment - No summary', 'Appointment - '+summary)
		wait(5)
		if verifysettext('dlgAppointment-Nosummary','txtSummary',summary) == 1:
			if verifysettext('dlgAppointment-Nosummary','txtLocation',location) == 1:
				if verifysettext('dlgAppointment-Nosummary','txtEventDescription',description) == 1:
					print 'File found'
					click('dlgAppointment-Nosummary','btnCancel')
					#selecteventindex('Evoution-Calendars','calview',1)
					selectmenuitem('Evolution-Calendars','mnuEdit;mnuDelete')
					wait(5)
					click('dlgEvolutionQuery','btnDelete')
					print "file Deleted"
					
		log('Deletion-of-Appointment','pass')
	except error,msg:
		if string.find(str(msg),s1)== -1:
			print "Error nt due to gui handle."	
		print "File not found...."
		releasecontext('Appointment - '+summary,'Appointment - No summary')
		log('Deletion-of-Appointment','fail')
#END

#verification of Delete
def verify_delete():
	try:
		selecteventindex('Evolution-Calendars','calview',1)
		log('Verification-of-Delete','fail')
	except error:
		print "No calendar event present"
 		log('Verification-of-Delete','pass')

#END		

log('Delete-an-Existing-Appointment','teststart')
	
#call the function
delete_appointment(summary,location,description)
verify_delete()

log('Delete-an-Existing-Appointment','testend')
