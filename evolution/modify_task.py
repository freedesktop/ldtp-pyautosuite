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
# This script will modify a particular task.

from ldtp import *
from ldtputils import *
#from evoutils.Task import getrowindex
def getrowindex(subject):
   try:
       noofchild=getrowcount ('frmEvolution-Tasks','tblTaskTable')
       for ind in range (noofchild):
           if getcellvalue('frmEvolution-Tasks','tblTaskTable',ind,2) == subject:
               return ind
       if ind == noofchild-1:
           log ('Message not present','cause')
           raise LdtpExecutionError (0)
   except:
       log ('Unable to get index of message','error')
       raise LdtpExecutionError (0)

def read_data ():

	log('read user data','teststart')
	try:
 		data_object = LdtpDataFileParser (datafilename)
		Row_no = data_object.gettagvalue ('row_no')
		Due_date = data_object.gettagvalue ('due_date')
		Progress = data_object.gettagvalue ('progress')
		Summary = data_object.gettagvalue ('summary')
		old_summary = data_object.gettagvalue ('old_summary')
		log('User data read successfull','info')
		log('read user data','testend')

		return Row_no, Due_date, Progress, Summary, old_summary
	except:
		log('Unable to read the user data or data file missing','error')
 		log('read user data','testend')
		raise LdtpExecutionError(0)


# The script begins here.
# Modifying the task , by doubleclicking the task in the table.
try:	
	log('Modify a task','teststart')
	waittillguiexist('frmEvolution-Tasks')
	remap('evolution','frmEvolution-Tasks')
	Row_no, Due_date, Progress, Summary, old_summary = read_data()
	selectrow ('frmEvolution-Tasks', 'tblTaskTable', old_summary[0])
	selectmenuitem('frmEvolution-Tasks', 'mnuFile;mnuOpenTask')
	time.sleep(2)
	setcontext('Task - No summary','Task - ' + old_summary[0])
	waittillguiexist('frmTask-Nosummary')
	remap('evolution','frmTask-Nosummary')

except:
	log('Unable to open Task window','error')
	log('Modify a task','testend')
	raise LdtpExecutionError(0)

# Modifies the task according to users wish.
try:
	settextvalue ('frmTask-Nosummary', 'txtTextDateEntry',Due_date[0])
	settextvalue ('frmTask-Nosummary', 'txtSummary',Summary[0])
	setcontext('Task - No summary','Task - ' + Summary[0])
	log('User data Loaded','info')
	time.sleep(3)
	if stateenabled ('frmTask-Nosummary','btnSave')==1:
		click('frmTask-Nosummary','btnSave')
		time.sleep(3)
		log('The required task list has been modified','info')
	else:
		log('The Task list already exists','info')
		click('frmTask-Nosummary','btnClose')

	time.sleep(3)
	if guiexist('dlgEvolutionQuery'):
		remap('evolution','dlgEvolutionQuery')
		click('dlgEvolutionQuery','btnSend')
		time.sleep(3)
		undoremap('evolution','dlgEvolutionQuery')
	log('Task has been modified successfully','info')

except:
	log('Unable to load the user data','error')
	log('modify a task','testend')
	raise LdtpExecutionError(0)

#Change the Progress of the task.
try:
	Row_no = getrowindex(Summary[0])
	if Progress[0] == 'complete':
		checkrow ('frmEvolution-Tasks', 'tblTaskTable', int(Row_no), 1)
	elif Progress[0] == 'Not started':
		uncheckrow ('frmEvolution-Tasks', 'tblTaskTable', int(Row_no), 1)
	print 'The Task has been modified successfully'
	log('progress of the task has been modified','info')
except:
	log('unable to change the progress of the task','error')
	log('modify a task','testend')
	raise LdtpExecutionError(0)

log('Modify a task','testend')
