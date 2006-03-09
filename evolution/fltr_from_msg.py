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

#To create a filter from the existing messages.
from ldtp import *
from ldtputils import *

def verify_filter(rule_name):
	windowname = 'dlgFilters'
	selectmenuitem('frmEvolution-*','mnuEdit;mnuMessageFilters')
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
	#remap('evolution',windowname)
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
	details = data_object.gettagvalue ('details')[0]
	fldr = data_object.gettagvalue ('fldr')[0]
	then_actions = data_object.gettagvalue ('then_actions')[0]
	then_values = data_object.gettagvalue ('then_values')[0]
	return fldr, filter_on, details ,then_actions, then_values

def filter_from_msg(fldr,filter_on,details,then_actions,then_values):
	try:
		windowname = 'dlgAddFilterRule'
		log('create a filter from the existing message','teststart')
		selectrowpartialmatch('frmEvolution-*','ttblMailFolderTree',fldr)
		time.sleep(2)
		selectrow('frmEvolution-*','ttblMessages',details)
                print 'mnuMessage;mnuCreateRule;mnuFilteron'+filter_on+'*'
		selectmenuitem('frmEvolution-*','mnuMessage;mnuCreateRule;mnuFilteron'+filter_on+'...')
		waittillguiexist(windowname)
		#remap('evolution',windowname)
		
		if verifyselect (windowname, 'cbo' + filter_on, filter_on) == 1 and gettextvalue (windowname,'txt1') == details:
			log('the details has been correctly entered','info')
			print 'The details present are correct'

		then_actions = then_actions.split(':')
		then_values = then_values.split(':')
		if len(then_actions) == len(then_values):
			length_actions = len(then_actions)
			for i in range(0,length_actions):
				time.sleep(2)
#				#remap('evolution',windowname)	
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
#				#undoremap('evolution',windowname)
			rule_name = gettextvalue(windowname,'txtRulename')
			click(windowname,'btnOK')
			time.sleep(3)
			if guiexist('dlgEvolutionError') == 1:
				print 'The rule name already exist'
				log('Need to change the name','error')
				click('dlgEvolutionError','btnOK')
				time.sleep(1)
				click(windowname,'btnCancel')
			else:
				print 'The Filter has been created'
				print rule_name,'.5'
				if verify_filter(rule_name) == 1:
					print 'filter creatation verified'
					log('filter creation verified','info')
				else:
					print 'filter not created'
					log('filter not found','error')
					raise LdtpExecutionError (0)
				log('Filter created','info')
			
		else:
			print 'The details entered automatically might not be correct'
			log('The details entered automatically might not be correct','error')
			click(windowname,'btnCancel')
	except:
		log('Unable to create a filter from message','error')
		raise LdtpExecutionError (0)
	log('create a filter from the existing message','testend')
	

fldr, filter_on, details, then_actions, then_values = read_data()
filter_from_msg(fldr, filter_on, details, then_actions, then_values)
