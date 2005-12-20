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

# Change status of a mail.

from ldtp import *
from ldtputils import *

def getrowindex(subject):
   try:
       noofchild=getrowcount ('frmEvolution-Mail','ttblMessageList')
       for ind in range (noofchild):
           if getcellvalue('frmEvolution-Mail','ttblMessageList',ind,4) == subject:
               return ind
       if ind == noofchild-1:
           log ('Message not present','cause')
           raise LdtpExecutionError (0)
   except:
       log ('Unable to get index of message','error')
       raise LdtpExecutionError (0)

def insert_followup_details (follow_up_flag, due_date, time, progress):
	try:
		print 'inside'
		log('Insert Follow up details','teststart')
		windowname = 'dlgFlagtoFollowUp'
		waittillguiexist (windowname)
		settextvalue (windowname,'txtFlag',follow_up_flag)
		settextvalue (windowname,'txtTextDateEntry',due_date)
		settextvalue (windowname,'txt1',time)
		if progress == 'completed':
			check(windowname,'chkCompleted')
		elif progress == 'not started':
			uncheck(windowname,'chkCompleted')
#		time.sleep (3)
		click(windowname,'btnOK')
		log('Inserted the followup details')
		print 'Follow up details entered'
	except:
		log('Unable to enter the given details','error')
		print 'Unable to enter the follow up details'
	log('Insert Follow up details','testend')


def read_data():

	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	fldr = data_object.gettagvalue ('fldr')[0]
	subject = data_object.gettagvalue ('subject')[0]
	status = data_object.gettagvalue ('status')[0]
	importance = data_object.gettagvalue ('importance')[0]
	junk_status = data_object.gettagvalue ('junk_status')[0]
	follow_up_flag = data_object.gettagvalue ('follow_up_flag')[0]
	due_date = data_object.gettagvalue ('due_date')[0]
	time = data_object.gettagvalue ('time')[0]
	progress = data_object.gettagvalue ('progress')[0]
	print fldr, subject, status, importance, junk_status, follow_up_flag, due_date, time, progress
	return fldr, subject, status, importance, junk_status, follow_up_flag, due_date, time, progress
	
def change_status(fldr, subject, status, importance, junk_status, follow_up_flag, due_date, time, progress):
	try:
		log('Change status of mails','teststart')
		windowname = 'dlgFlagtoFollowUp'
		remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-Mail','ttblMailFolderTree',fldr) == 1:
#			time.sleep(2)
			log('Folder identified','info')
			Row_index = getrowindex(subject)
			print Row_index
			# 0,2 are the colmn no.s denote the status, importance of the mails.
			cur_status = getcellvalue('frmEvolution-Mail','ttblMessageList',int(Row_index),0)
			cur_importance = getcellvalue('frmEvolution-Mail','ttblMessageList',int(Row_index),2)
			if selectrowindex('frmEvolution-Mail','ttblMessageList',int(Row_index)) == 1:
				print status,cur_status
				if status == 'read' and  int(cur_status) == 0:
					selectmenuitem('frmEvolution-Mail','mnuMessage;mnuMarkas;mnuRead')
					print 'Mail marked as read'
					log('Mail marked as read','info')
				elif status == 'read' and  int(cur_status) == 1:
					print 'Mail Already read, no modifications are made'
					log('Mail Already read, no modifications are made','info')
				elif status == 'unread' and  int(cur_status) == 1:
					selectmenuitem('frmEvolution-Mail','mnuMessage;mnuMarkas;mnuUnread')
					print 'Status changed to unread'
					log('Status changed to unread','info')
				elif status == 'unread' and  int(cur_status) == 0:
					print 'Mail not read, hence no modifications done'
					log('Mail not read, hence no modifications done','info')

				if importance == 'important' and cur_importance == '1':
					print 'The mail is already marked as important'
					log('The mail is already important','info')
				elif importance == 'important' and cur_importance == '0':
					selectmenuitem('frmEvolution-Mail','mnuMessage;mnuMarkas;mnuImportant')
					print 'Mail has been marked as important'
					log('Mail has been marked as important','info')
				elif importance == 'unimportant' and cur_importance == '0':
					print 'The mail is already marked as unimportant'
					log('The mail is already unimportant','info')
				elif importance == 'unimportant' and cur_importance == '1':
					selectmenuitem('frmEvolution-Mail','mnuMessage;mnuMarkas;mnuUnimportant')
					print 'Mail has been marked as unimportant'
					log('Mail has been marked as unimportant','info')
				
				selectmenuitem('frmEvolution-Mail','mnuMessage;mnuMarkas;mnuFollowUp')
#				time.sleep(3)
				insert_followup_details(follow_up_flag, due_date, time, progress)
				print 'The status has been modified'
			else:
				print 'Verify the given row index'
				log('Verify the row index specified','error')
		else:
			print 'Check the folder name specified'
			log('Check the folder name specified','error')
	except:
		print 'Unable to change the status of the message'
		log('Unable to change the status of the message','error')
		log('Change status of mails','testend')
		raise LdtpExecutionError (0)
	log('Change status of mails','testend')

fldr, subject, status, importance, junk_status, follow_up_flag, due_date, time, progress = read_data()
change_status(fldr, subject, status, importance, junk_status, follow_up_flag, due_date, time, progress)
