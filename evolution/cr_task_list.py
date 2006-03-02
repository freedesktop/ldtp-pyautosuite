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

def read_data ():
	data_object = LdtpDataFileParser (datafilename)
	Type = data_object.gettagvalue ('Type')
	Name = data_object.gettagvalue ('Name')
	Color = data_object.gettagvalue ('Color')
	Default = data_object.gettagvalue ('Default')
	return Type, Name, Color, Default

def create_tasklist(Type, Name, Color, Default):

	try:
		log('create a task list','teststart')
		#remap('evolution','frmEvolution-Tasks')
		selectmenuitem('frmEvolution-Tasks','mnuFile;mnuNew;mnuTasklist')
		time.sleep(3)
		waittillguiexist('dlgTaskListProperties')
		settextvalue ('dlgTaskListProperties', 'txtName', 'bug')
			
		if Default[0] == 'check':
			check ('dlgTaskListProperties', 'chkMarkasdefaultfolder')
		elif Default[0] == 'uncheck':
			uncheck ('dlgTaskListProperties', 'chkMarkasdefaultfolder')
		log('The window has been modified','info')
	except:	
		log('Unable to see the window','error')
		#undoremap('evolution','frmEvolution-Tasks')
		log('create a task list','testend')
		raise LdtpExecutionError(0)

	try:
		click('dlgTaskListProperties','btnColor')
		waittillguiexist('uknPickacolor')
		settextvalue ('uknPickacolor', 'txtColorName', Color[0])
		time.sleep(2)
		click('uknPickacolor','btnOK')
		settextvalue ('dlgTaskListProperties', 'txtName', Name[0])
		time.sleep(3)
		log('The requested color has been set','info')
	except:
		log('Unable to set the requested color','error')
		#undoremap('evolution','frmEvolution-Tasks')
		log('create a task list','testend')
		raise LdtpExecutionError(0)

	try:
		if stateenabled ('dlgTaskListProperties', 'btnOK') == 1:
			print 'The tasklist has been created'
			click('dlgTaskListProperties','btnOK')
			log('The required task list has been created','info')
		else:
			print 'The task list already exists'
			click('dlgTaskListProperties','btnCancel')
			log('The required task list cannot be created','error')			
	except:
		log('Unable to create the required task list','error')
		#undoremap('evolution','frmEvolution-Tasks')
		log('create a task list','testend')
		raise LdtpExecutionError(0)

	#undoremap('evolution','frmEvolution-Tasks')
	log('create a task list','testend')
	
Type, Name, Color, Default = read_data()	
create_tasklist(Type, Name, Color, Default)
