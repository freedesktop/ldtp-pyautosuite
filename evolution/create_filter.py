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

from ldtp import *
from ldtputils import *

def verify_filter(rule_name):
        windowname = 'dlgFilters'
        selectmenuitem('frmEvolution-Mail','mnuEdit;mnuMessageFilters')
        waittillguiexist(windowname)
        if gettablerowindex (windowname,'tblFilterRules',rule_name) == -1:
                print 'rule not found in the table filter rules'
                click(windowname,'btnCancel')
                return 0
        else:
                print 'rule name found'
                click(windowname,'btnOK')
                return 1

def selectfolder(fldr,dest=''):
	
	windowname = 'dlgSelectfolder'
	waittillguiexist(windowname)
	remap('evolution',windowname)
	if gettreetablerowindex (windowname, 'ttblMailFolderTree', fldr) == -1:
		click(windowname,'btnNew')
		time.sleep(3)
		waittillguiexist ('dlgCreatefolder')	
	        settextvalue('dlgCreatefolder','txtFoldername',fldr)
		selectrowpartialmatch ('dlgCreatefolder', 'ttblMailFolderTree',dest)
		log('User Value Entered','info')
		click('dlgCreatefolder','btnCreate')
		time.sleep(3)
		if guiexist('dlgEvolutionError'):
			click('dlgEvolutionError','btnOK')
			time.sleep(3)
			click('dlgCreatefolder','btnCancel')
			print 'Folder Name already exist'
			log('Folder Already exists','error')
		selectrowpartialmatch (windowname, 'ttblMailFolderTree',fldr)
	log('Dest fldr selected','info')
	click(windowname,'btnOK')
	return 1
	undoremap('evolution',windowname)

def read_data():

	data_object = LdtpDataFileParser (datafilename)

	#Extracting imput data from xml file
	filter_on = data_object.gettagvalue ('filter_on')[0]
	rule_name = data_object.gettagvalue ('rule_name')[0]
	if_components = data_object.gettagvalue ('if_components')[0]
	if_properties = data_object.gettagvalue ('if_properties')[0]
	if_values = data_object.gettagvalue ('if_values')[0]
	then_actions = data_object.gettagvalue ('then_actions')[0]
	then_values = data_object.gettagvalue ('then_values')[0]
	execute_action = data_object.gettagvalue ('execute_action')[0]
	print filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action
	return filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action


def create_filter(filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action):
	try:
		log('Create a filter','teststart')
		windowname = 'dlgAddFilterRule'
		
		selectmenuitem('frmEvolution-Mail','mnuMessage;mnuCreateRule;mnuFilteron'+filter_on)
		waittillguiexist(windowname)
		if rule_name == '' :
			print 'Need a valid rule name'
			log('Rule name not specified','error')
		else:
			settextvalue(windowname,'txtRulename',rule_name)
			log('Rule name has been set','info')
		if execute_action == '':
			print 'Execute actions not specified, hence the default has been taken'
		else:
			comboselect(windowname,'cboifanycriteriaaremet',execute_action)	
			log('type of execution set','info')
		if_components = if_components.split(':')
		if_properties = if_properties.split(':')
		if_values = if_values.split(':')
		if len(if_components) == len(if_properties) == len(if_values):
			comboselect(windowname,'cboSubject',if_components[0])
			time.sleep(2)
			remap('evolution',windowname)
			comboselect(windowname,'cbocontains',if_properties[0])
			settextvalue(windowname,'txt1',if_values[0])
			time.sleep(3)
			length = len(if_components)
			undoremap('evolution',windowname)
			for i in range(1,length):
				time.sleep(1)
				click(windowname,'btnAdd')
				time.sleep(3)
				remap('evolution',windowname)
				comboselect(windowname,'cboSender',if_components[i])
				time.sleep(2)
				undoremap('evolution',windowname)
				remap('evolution',windowname)
				comboselect(windowname,'cbocontains',if_properties[i])
				settextvalue(windowname,'txt1',if_values[i])					
				undoremap('evolution',windowname)
#				time.sleep(2)
		else:
			print 'you must enter the values for if clause correctly'
			log('Unable to create filter, because of unequal length','error')
		then_actions = then_actions.split(':')
		then_values = then_values.split(':')
		if len(then_actions) == len(then_values):
			length_actions = len(then_actions)
			for i in range(0,length_actions):
				time.sleep(2)
#				remap('evolution',windowname)	
				time.sleep(2)
				comboselect(windowname,'cboMovetoFolder',then_actions[i])
				if then_actions[i] == 'Move to Folder' or then_actions[i] == 'Copy to Folder':
					click(windowname,'btn<clickheretoselectafolder>')
					time.sleep(3)
					setcontext('Select folder','Select Folder') #if this is fixed remove this line.
					waittillguiexist('dlgSelectfolder')
					chk_value = selectfolder(then_values[i])
					time.sleep(3)
				elif then_actions[i] == 'Delete' or then_actions[i] == 'Stop Processing' or then_actions[i] == 'Beep':
					pass # there will be no work to do in these cases.Hence nothin to be set.
				else:
					pass # Shud write for all other cases.
				time.sleep(2)
				if i < length_actions-1:
					click(windowname,'btnAdd1')
#				undoremap('evolution',windowname)
			click(windowname,'btnOK')
			time.sleep(3)
			if guiexist('dlgEvolutionError') == 1:
				print 'The rule name already exist'
				log('Need to change the name','error')
				click('dlgEvolutionError','btnOK')
				time.sleep(1)
				click(windowname,'btnCancel')
			else:
				if verify_filter(rule_name) == 1:
					print 'The Filter has been created'
					log('Filter created','info')
				else:
					print 'Filter verification failed'
					log('Filter Verify failed','error')
		else:
			print 'you must enter the values for then clause correctly'
			log('Unable to create filter, because of unequal length in then clause','error')
	except:
		print 'Unable to create a filter'
		click(windowname,'btnCancel')
		log('Unable to create a filter','error')
	log('Create a filter','testend')

