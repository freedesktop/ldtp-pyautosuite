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
# This script will create a new task.


from ldtp import *
from ldtputils import *
import string, sys, os, commands, time, filecmp

def selectTasksPane():
   """Selects the Tasks Pane in Evolution"""
   log ('Open Evolution Tasks Pane','teststart')
   setcontext ('Evolution - Mail','Evolution - Mail')
   #code to find the present window and revert back to the Tasks Pane
   if guiexist('frmEvolution-Mail')!=1:
        log ('Present Window now Mail pane','info')
        setcontext ('Evolution - Mail','Evolution - Contacts')
        if guiexist('frmEvolution-Mail')!=1:
             log ('Present Window now Tasks pane','info')
             setcontext ('Evolution - Mail','Evolution - Calendars')
             if guiexist('frmEvolution-Mail')!=1:
                  log ('Present Window now Calendars pane','info')
                  setcontext ('Evolution - Mail','Evolution - Memos')
                  if guiexist('frmEvolution-Mail')!=1:
                       log ('Present Window now Memos pane','info')
                       setcontext ('Evolution - Mail','Evolution - Tasks')
                       log ('Present Window has to be Taskspane','info')
   time.sleep (1)
   try:
       click ('frmEvolution-Mail','tbtnTasks')
       time.sleep(3)
       waittillguiexist ('frmEvolution-Tasks')

   except:
       log ('error selecting Tasks pane','error')
       log ('Open Evolution Tasks Pane','testend')
       raise LdtpExecutionError(0)

   log ('Open Evolution Tasks Pane','testend')

def create_task(Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories):
	log('Create New Task','teststart')
	try:
		remap('evolution','frmEvolution-Tasks')
		no_rows_b4creat = getrowcount ('frmEvolution-Tasks', 'tblTaskTable') 
		click('frmEvolution-Tasks','btnNew')
		if waittillguiexist('frmTask-Nosummary'):
			log('New task window opened','info')
		else:
			log('Unable to open the new task window','error')
		comboselect ('frmTask-Nosummary', 'cboPersonal', Group[0])
		time.sleep(3)
		settextvalue ('frmTask-Nosummary', 'txtSummary', Summary[0])
		setcontext('Task - No summary','Task - '+Summary[0])
		settextvalue ('frmTask-Nosummary', 'txtDescription', Desc[0])
		settextvalue ('frmTask-Nosummary', 'txtTextDateEntry1',Start_date[0])
		settextvalue ('frmTask-Nosummary', 'txtTextDateEntry',End_date[0])
		settextvalue ('frmTask-Nosummary', 'txt5',Start_time[0])
		settextvalue ('frmTask-Nosummary', 'txt3',End_time[0])
		settextvalue ('frmTask-Nosummary', 'txt7',Time_zone[0])
		settextvalue ('frmTask-Nosummary', 'txt1',Categories[0])
		time.sleep(2)
		log('User Details entered','info')
	except:
		print 'Error in entering the values'
		releasecontext()		
		log('Error in entering the values','error')
		log('Create New Task','testend')
	        raise LdtpExecutionError(0)
	
	try:
		click('frmTask-Nosummary','btnSave')
		time.sleep(3)
		no_rows_aftercreat = getrowcount ('frmEvolution-Tasks', 'tblTaskTable') 
		if no_rows_aftercreat == no_rows_b4creat + 1:
			if selectrow('frmEvolution-Tasks','tblTaskTable',Summary[0]) == 1:
				log('Task Creation Completed and verified','info')
				print 'Task Creation completed and verified.'
		else:
			raise LdtpExecutionError(0)	
	except:
		print 'Unable to verify the task :'+Summary[0]
		log('Unable to save the task')
		log('Create New Task','testend')
		releasecontext()
	        raise LdtpExecutionError(0)	

	undoremap('evolution','frmEvolution-Tasks')
	releasecontext()
	log('Create New Task','testend')
	

# Read the data from the xml file.	

data_object = LdtpDataFileParser (datafilename)
Group = data_object.gettagvalue ('group')
Summary = data_object.gettagvalue ('summary')
Desc = data_object.gettagvalue ('desc')
Start_date = data_object.gettagvalue ('start_date')
Start_time = data_object.gettagvalue ('start_time')
End_date = data_object.gettagvalue ('end_date')
End_time = data_object.gettagvalue ('end_time')
Time_zone = data_object.gettagvalue ('time_zone')
Categories = data_object.gettagvalue ('Categories') 

# Call the function

selectTasksPane()
create_task(Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories)

