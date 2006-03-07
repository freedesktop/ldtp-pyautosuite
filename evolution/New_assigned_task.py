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
# This script will create a new assigned task.

#!/usr/bin/env python

from ldtp import *
from ldtputils import *

def addattendees(attendee,email,addrbook):
   log ('Add Attendees','teststart')
   try:
       click ('frmAssignedTask-Nosummary','btnAttendees')
       waittillguiexist ('dlgRequiredParticipants')
       time.sleep (1)
       comboselect ('dlgRequiredParticipants','cboAddressBook',addrbook)
       #remap ('evolution','dlgRequiredParticipants')
       attendee=attendee[0].split (':')
       email=email[0].split (':')
       if len(attendee)!=len(email):
           log ('Mismatch in Attendee name and email','error')
           raise LdtpExecutionError (0)
       for ind in range(len(attendee)):
           try:
	       att=attendee[ind] + ' <'+ email[ind] + '>'
               print att,"Inside for loop"
               if gettablerowindex('dlgRequiredParticipants','tblRequiredParticipants',att)==-1:
                   print "inside if"
                   selectrow ('dlgRequiredParticipants','tblContacts',att)
                   print "row selected"
                   click ('dlgRequiredParticipants', 'btnAdd1')
                   time.sleep (1)
           except:
               log ('User not found','cause')
               raise LdtpExceptionError(0)
       click ('dlgRequiredParticipants', 'btnClose')
       #undoremap ('evolution','dlgRequiredParticipants')
   except:
       log ('Attendee Addition failed','error')
       log ('Add Attendees','testend')
       raise LdtpExecutionError (0)
   log ('Add Attendees','testend')

def read_new_taskdata():

	try:
		log('read user data','teststart')
		data_object = LdtpDataFileParser (datafilename)
		Email = data_object.gettagvalue ('email')
		Organizer = data_object.gettagvalue ('organizer')
		Attendees = data_object.gettagvalue ('Attendees')
		Att_emails = data_object.gettagvalue ('Att_emails')
		addr_book = data_object.gettagvalue ('addr_book')
		Group = data_object.gettagvalue ('group')
		Summary = data_object.gettagvalue ('summary')
		Desc = data_object.gettagvalue ('Desc')
		Start_date = data_object.gettagvalue ('start_date')
		Start_time = data_object.gettagvalue ('start_time')
		End_date = data_object.gettagvalue ('due_date')
		End_time = data_object.gettagvalue ('due_time')
		Time_zone = data_object.gettagvalue ('time_zone')
		log('User data read successfull','info')
		log('read user data','testend')
		return [Email, Organizer, Attendees, Att_emails, addr_book, Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone]

	except:
		log('Unable to read the user data or data file missing','error')
 		log('read user data','testend')
		raise LDTPexecutionerror(0)

	log('read user data','testend')

def new_task():

	""" Routine to add a new task """ 	
	#Verify: This script fails to set the group combo box.

	try:
		log('Create new assigned task','teststart')
		Email, Organizer, Attendees, Att_emails, addr_book, Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone = read_new_taskdata()

		selectmenuitem('frmEvolution-Tasks','mnuFile;mnuNew;mnuAssignedTask')
		waittillguiexist('frmAssignedTask-Nosummary')
		log('Dlgbox new assigned task appeared','info')
		settextvalue ('frmAssignedTask-Nosummary', 'txtSummary', Summary[0])
		setcontext('Assigned Task - No summary','Assigned Task - ' + Summary[0])
		time.sleep(3)
		settextvalue ('frmAssignedTask-Nosummary', 'txtDescription', Desc[0])
		settextvalue ('frmAssignedTask-Nosummary', 'txtDate1',Start_date[0])
		settextvalue ('frmAssignedTask-Nosummary', 'txtDate',End_date[0])
		settextvalue ('frmAssignedTask-Nosummary', 'txt8',Start_time[0])
		settextvalue ('frmAssignedTask-Nosummary', 'txt6',End_time[0])
		#settextvalue ('frmAssignedTask-Nosummary', 'txt7',Organizer[0]+ ' <'+Email[0]+'>')
                # Organizer is not text. It's a noname combo. Need file bug 
		comboselect ('frmAssignedTask-Nosummary', 'cboPersonal', Group[0])
		time.sleep(2)
		addattendees(Attendees,Att_emails,addr_book[0])	
		time.sleep(2)
		log('User data Loaded','info')

	except:
		log('Unable to enter the values','error')
		log('Create a new assigned task','testend')
		raise LdtpExecutionError(0)

# Click Save and then exit.
	try:
		click('frmAssignedTask-Nosummary','btnSave')
		time.sleep(3)
		if guiexist('dlgEvolutionQuery') == 1:
			#remap('evolution','dlgEvolutionQuery')
			click('dlgEvolutionQuery','btnDon\'tSend')
			#undoremap('evolution','dlgEvolutionQuery')
		log('Assigned Task Creation Completed','info')
		print 'Task has been created'
	except:
		log('Unable to save the task')
		log('Create a new assigned task','testend')
		raise LdtpExecutionError(0)

	log('Create a new assigned task','testend')
new_task()
