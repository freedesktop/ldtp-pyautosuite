#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
#     Prashanth Mohan  <prashmohan@gmail.com>
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
# This script will delete a particular task.


from ldtp import *
from ldtputils import *

def read_data ():
	try:
		data_object = LdtpDataFileParser (datafilename)
		summary = data_object.gettagvalue ('summary')
		log('User data read successfull','info')
		return summary
		
	except:
		log('Unable to read the user data or data file missing','error')
		raise LdtpExecutionError(0)


# The takes the tsak summary as input and deletes that task. 
# Note: This doesnt chk whether the selected task is assigned or not.

try:
	log('Delete a task','teststart')
	Wrong_index = 'The index you entered exceeded the no of available tasks'
	waittillguiexist('frmEvolution-Tasks')
	summary = read_data()

	no_rows_b4deleting = getrowcount ('frmEvolution-Tasks', 'tblTasks') 

	#if selectrowpartialmatch ('frmEvolution-Tasks', 'tblTasks', summary[0]) == 1:
        # selectrowpartialmatch doesn't work: 333090

        if selectrow ('frmEvolution-Tasks', 'tblTasks', summary[0]) == 1:
		click('frmEvolution-Tasks', 'btnDelete')
		waittillguiexist('dlgEvolutionQuery')
		time.sleep(3)
		click('dlgEvolutionQuery','btnDelete')
		log('The specified task has been deleted','info')
                time.sleep(2)
		no_rows_afterdeleting = getrowcount ('frmEvolution-Tasks', 'tblTasks')
		if no_rows_afterdeleting == no_rows_b4deleting -1:
			time.sleep(3)
			log('the task has been deleted','info')	
		else:
			print 'Deletion of task verify failed'
			log('Deletion of task verify failed','error')
	else:
		print 'Unable to select a task with the given summary'
		log('unable to select the task','error')
except:
	log('Unable to delete a Task','error')
	log('the task has been deleted','fail')
	log('Delete a task','testend')
	raise LdtpExecutionError(0)
log('the task has been deleted','pass')
log('Delete a task','testend')
