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

#To create a filter.
from ldtp import *
from ldtputils import *
from create_filter import *

# def verify_filter(rule_name):
#         windowname = 'dlgFilters'
#         selectmenuitem('frmEvolution-Mail','mnuEdit;mnuMessageFilters')
#         waittillguiexist(windowname)
#         if gettablerowindex (windowname,'tblFilterRules',rule_name) == -1:
#                 print 'rule not found in the table filter rules'
#                 click(windowname,'btnCancel')
#                 return 0
#         else:
#                 print 'rule name found'
#                 click(windowname,'btnOK')
#                 return 1

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
	fldr = data_object.gettagvalue ('fldr')[0]
	print fldr, filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action
	return fldr, filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action

def apply_filter(fldr,filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action):
	try:
		log('Create and apply filter','teststart')
		if create_filter(filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action) == 1:
			log('Filter created successfully','info')
		else:
			log('Failure in creating a filter','error')
		
		if selectrowpartialmatch('frmEvolution-Mail','ttblMailFolderTree',fldr) == 1:
			waittillguiexist ('frmEvolution-'+fldr+'*')
			log('fldr selected','info')
		else:
			log('Unable to select the given folder','error')
		remap('evolution','frmEvolution-Mail')
		# Note 0 has been hard coded, the apply filter has to apply to all the files in the folder.
		# so the idea is to select a random msg, and apply filters.
		if selectrowindex ('frmEvolution-Mail', 'ttblMessageList', 0) == 1:
			if selectmenuitem('frmEvolution-Mail','mnuMessage;mnuApplyFilters') == 1:
				print 'Filter has been created and applied to '+fldr
				log('Filter applied','info')
			else:
				print 'Unable to apply the filter'
		else:
			print 'No messages in '+fldr
			raise LdtpExecutionError (0)
	except:
		log('Unable to apply the filter','error')
		raise LdtpExecutionError (0)
	log('Create and apply filter','testend')

fldr,filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action = read_data()
apply_filter(fldr,filter_on, rule_name, if_components, if_properties, if_values, then_actions, then_values, execute_action)
