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
# This script will create a new task.


from task import *

def create_task(Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories):
	log('Create New Task','teststart')
	try:
		selectTaskPane()
		no_rows_b4creat = getrowcount ('frmEvolution-Tasks', 'tblTasks') 
		click('frmEvolution-Tasks','btnNew')
		if waittillguiexist('frmTask-Nosummary') == 1:
			log('New task window opened','info')
		else:
			log('Unable to open the new task window','error')
			raise LdtpExecutionError (0)
		fill_task (Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories)
		click('frmTask-*','btnSave')
	except:
		log ('Unable to create Task','cause')
		log('Create New Task','fail')
		log('Create New Task','teststart')
		raise LdtpExecutionError (0)
	
	try:
		time.sleep(3)
		no_rows_aftercreat = getrowcount ('frmEvolution-Tasks', 'tblTasks') 
		if no_rows_aftercreat == no_rows_b4creat + 1 and \
		       selectrow('frmEvolution-Tasks','tblTasks',Summary[0]) == 1:
			log('Task Creation Completed and verified','info')
			verify_task (Group, Summary, Desc, Start_date,
				     Start_time, End_date, End_time,
				     Time_zone, Categories)
			print 'Task Creation completed and verified.'
		else:
			raise LdtpExecutionError(0)
		click ('frmTask-*','btnClose')		
	except:
		print 'Unable to verify the task :'+Summary[0]
		log('Task not created','cause')
		log('Task Creation Completed and verified','fail')
		log('Create New Task','testend')
		click ('frmTask-*','btnClose')
	        raise LdtpExecutionError(0)	
	log('Task Creation Completed and verified','pass') 
	log('Create New Task','testend')

		
	
# Call the function

Group, Summary, Desc, Start_date, Start_time, \
       End_date, End_time, Time_zone, \
       Categories = gettaskdata (datafilename)

create_task(Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories)

