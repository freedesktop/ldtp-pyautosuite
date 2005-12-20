#!/usr/bin/env python
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

def modify_task(Due_date, Progress, Summary, old_Summary):

	""" Routine to modify a task """ 	
	
	# read the row index from the user and delete that particular task.
	try:
		log('Modify an assigned task','teststart')
		remap('evolution','frmEvolution-Tasks')
		selectrow ('frmEvolution-Tasks', 'tblTaskTable', old_Summary[0])
		selectmenuitem('frmEvolution-Tasks', 'mnuFile;mnuOpenTask')
		setcontext('Assigned Task - No summary','Assigned Task - ' + old_Summary[0])
		waittillguiexist('frmAssignedTask-Nosummary')
		remap('evolution','frmAssignedTask-Nosummary')
		log('The window opened' ,'info')

	except:	
		log('unable to read the data','error')
		log('Modify an assigned task','testend')
		undoremap('evolution','frmEvolution-Tasks')
		raise LdtpExecutionError(0)

	# Modifies the task according to users wish.
	try:
		settextvalue ('frmAssignedTask-Nosummary', 'txtTextDateEntry',Due_date[0])
		settextvalue ('frmAssignedTask-Nosummary', 'txtSummary',Summary[0])
		setcontext('Assigned Task - No summary','Assigned Task - ' + Summary[0])
		log('User data Loaded','info')
		time.sleep(2)
		if stateenabled ('frmAssignedTask-Nosummary','btnSave')==1:
			click('frmAssignedTask-Nosummary','btnSave')
			log('The required task list has been modified','info')
		else:
			log('The Task is not modified because of no change in summary','info')
			click('frmAssignedTask-Nosummary','btnClose')
		time.sleep(2)
	
		if guiexist('dlgEvolutionQuery'):
			click('dlgEvolutionQuery','btnDon\'tSend')
			log('Task has been modified successfully','info')
		print 'The Assigned task has been modifed'

	except:
		log('Unable to load the user data','error')
		log('Modify an assigned task','testend')
		undoremap('evolution','frmEvolution-Tasks')
		raise LdtpExecutionError(0)

	#Change the Progress of the task.
	try:

		Row_no = getrowindex(Summary[0])
		if Progress[0] == 'complete':
			checkrow ('frmEvolution-Tasks', 'tblTaskTable', Row_no, 1)
		elif Progress[0] == 'Not started':
			uncheckrow ('frmEvolution-Tasks', 'tblTaskTable', Row_no, 1)
		log('progress of the task has been modified','info')
		print 'The Progress has been modified'
	except:
		log('unable to change the progress of the task','error')
		log('Modify an assigned task','testend')
		undoremap('evolution','frmEvolution-Tasks')
		raise LdtpExecutionError(0)

	log('modify an assigned task','testend')


# Reading the values from the data xml.

data_object = LdtpDataFileParser (datafilename)
Due_date = data_object.gettagvalue ('due_date')
Progress = data_object.gettagvalue ('progress')
Summary = data_object.gettagvalue ('summary')
old_Summary = data_object.gettagvalue ('old_summary')
# Calling the function
modify_task(Due_date, Progress, Summary, old_Summary)
