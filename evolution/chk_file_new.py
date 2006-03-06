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
# to verify all the items in the mnuFile;mnuNew

from ldtp import *
from ldtputils import *

new_items = ['Mail Message','Mail Folder','All Day Appointment','Appointment','Assigned Task','Contact','Contact List','Meeting','Memo','Task','Address Book','Calendar','Memo List','Task List','New Window']

def chk_new_items():

	try:
		log('Verify all items in the mnuNew','teststart')	
		noofitems = 15
		new_items = ['Mail Message','Mail Folder','All Day Appointment','Appointment','Assigned Task','Contact','Contact List','Meeting','Memo','Task','Address Book','Calendar','Memo List','Task List','New Window']
		for i in range(0, noofitems-1):

			mnuitem,windowname = assign_var(i)
			if selectmenuitem('frmEvolution-*','mnuFile;mnuNew;mnu'+mnuitem) == 1:
				time.sleep(3)
			close_win(i,windowname)
	except:
		print 'Must be problem with ' + new_items[i]
		log('Must be problem with ' + new_items[i] , 'cause')
		print 'Some windows failed to open in menu file;new'
		log('Verify all items in the mnuNew','testend')			
		raise LdtpExecutionError (0)
	log('Verify all items in the mnuNew','testend')			

def assign_var(i):

	if new_items[i] == 'Mail Message':
		mnuitem = 'MailMessage'
		windowname = 'frmComposeMessage'
	elif new_items[i] == 'Mail Folder':
		mnuitem = 'MailFolder'
		windowname = 'dlgCreatefolder'
	elif new_items[i] == 'All Day Appointment':
		mnuitem = 'AllDayAppointment'
		windowname = 'frmAppointment-Nosummary'
	elif new_items[i] == 'Appointment':
		mnuitem = 'Appointment'
		windowname = 'frmAppointment-Nosummary'
	elif new_items[i] == 'Assigned Task':
		mnuitem = 'AssignedTask'
		windowname = 'frmAssignedTask-Nosummary'
	elif new_items[i] == 'Contact':
		mnuitem = 'Contact'
		windowname = 'dlgContactEditor'
	elif new_items[i] == 'Contact List':
		mnuitem = 'ContactList'
		windowname = 'dlgContactListEditor'
	elif new_items[i] == 'Meeting':
		mnuitem = 'Meeting'
		windowname = 'frmMeeting-Nosummary'
	elif new_items[i] == 'Memo':
		mnuitem = 'Memo'
		windowname = 'frmJournalentry-Nosummary'
	elif new_items[i] == 'Task':
		mnuitem = 'Task'
		windowname = 'frmTask-Nosummary'
	elif new_items[i] == 'Address Book':
		mnuitem = 'AddressBook'
		windowname = 'dlgNewAddressBook'
	elif new_items[i] == 'Calendar':
		mnuitem = 'Calendar'
		windowname = 'dlgNewCalendar'
		#setcontext('Task List Properties','New Calendar')
	elif new_items[i] == 'Memo List':
		mnuitem = 'Memolist'
		windowname = 'dlgNewMemoList'
	elif new_items[i] == 'Task List':
		mnuitem = 'Tasklist'
		windowname = 'dlgTaskListProperties'
	return mnuitem,windowname

def close_win(i,windowname):

	if new_items[i] == 'Mail Message':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			selectmenuitem(windowname,'mnuFile;mnuClose')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Mail Folder':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnCancel')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'All Day Appointment':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnClose')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Appointment':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnClose')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Assigned Task':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnClose')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Contact':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnCancel')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Contact List':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnCancel')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Meeting':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnClose')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Memo':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnClose')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Task':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnClose')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Address Book':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnCancel')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
	elif new_items[i] == 'Calendar':
		setcontext('Task List Properties','New Calendar')
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnCancel')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
		releasecontext()
	elif new_items[i] == 'Memo List':
		setcontext('Task List Properties','New Memo List')
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnCancel')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)
		releasecontext()
	elif new_items[i] == 'Task List':
		if waittillguiexist(windowname) == 1:
			print new_items[i] + ' Working'
			log(new_items[i] + ' Working','info')
			click(windowname,'btnCancel')
		else:
			print new_items[i] + ' Not Working'
			log(new_items[i] + 'Not Working','info')
			raise LdtpExecutionError (0)

chk_new_items()
