#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
#     Prashanth Mohan <prashmohan@gmail.com>
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
from ldtp import *
from ldtputils import *
from evoutils import *


def selectfolder(windowname,fldr,dest=''):
	try:
		log('Selecting a given folder','teststart')

		if waittillguiexist(windowname) == 1:
			if gettreetablerowindex (windowname, 'ttblMailFolderTree', fldr) == -1:
				click(windowname,'btnNew')
				time.sleep(3)
				waittillguiexist ('dlgCreatefolder')	
			        settextvalue('dlgCreatefolder','txtFoldername',fldr)
				selectrowpartialmatch ('dlgCreatefolder', 'ttblMailFolderTree',dest)
				click('dlgCreatefolder','btnCreate')
				time.sleep(2)
				if guiexist('dlgEvolutionError'):
					click('dlgEvolutionError','btnOK')
					time.sleep(2)
					click('dlgCreatefolder','btnCancel')
					print 'Folder Name already exist'
					log('Folder Already exists','error')
		
			selectrowpartialmatch (windowname, 'ttblMailFolderTree',fldr)
			waittillguiexist ('frmEvolution-'+fldr+'*')
			log('Required folder selected','info')
			log('Selecting a given folder','testend')
			return 1
		else:
			log('Unable to find the window','error')
			log('Selecting a given folder','testend')
	except:	
		log('Unable to select the folder/create it','error')
		log('Selecting a given folder','testend')

	
def verify_folder_exist(Folder_name):
	try:
		#log('Verify Folder Exists','teststart')
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',Folder_name) == 1:
			waittillguiexist ('frmEvolution-'+Folder_name+'*')
			log('Verify succeeded')
		#undoremap('evolution','frmEvolution-Mail')
		#log('Verify Folder Exists','testend')
		return 1
	except:
		log('verify Failed','error')
		#log('Verify Folder Exists','testend')
		raise LdtpExecutionError (0)

def create_folder(Folder_name, location=''):

	try:
		log('Create a new folder','teststart')
		windowname = 'dlgCreatefolder'
		waittillguiexist (windowname)	
	        settextvalue(windowname,'txtFoldername',Folder_name)
		selectrowpartialmatch ('dlgCreatefolder', 'ttblMailFolderTree',location)
		log('User Value Entered','info')
		click(windowname,'btnCreate')
		time.sleep(3)
		if guiexist('dlgEvolutionError') == 1:
			click('dlgEvolutionError','btnOK')
			time.sleep(3)
			click(windowname,'btnCancel')
			print 'Folder Name \''+Folder_name+'\' already exist'
			log('Folder Already exists','cause')
			log('Create a new folder','testend')
			return 0
		else:
			log('Folder created','info')
			print 'Folder with the name \''+Folder_name+'\' created'
			if verify_folder_exist(Folder_name) != 1:
				print 'Folder Creatation Verify failed'
				log('Verification failed','error')
                                log ('Create a new folder','fail')
				log('Create a new folder','testend')
				return 0
			else:
				print 'Folder Creation verified'
				log('Folder Verified','info')
                                log ('Create a new folder','pass')
				log('Create a new folder','testend')
				return 1
	except :
		log('Cannot create a folder','error')
                log ('Create a new folder','fail')
		log('Create a new folder','testend')
		print 'Cannot create a folder'
		raise LdtpExecutionError (0)

	log('Create a new folder','testend')

def copy_to (from_fldr,to_fldr):

	try:
		log('Copy a folder','teststart')
		windowname = 'dlgSelectfolder'
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',from_fldr) == 1:
			waittillguiexist ('frmEvolution-'+from_fldr+'*')
			log('From folder selected','info')
			selectmenuitem('frmEvolution-*','mnuFolder;mnuCopyFolderTo*')
			time.sleep(3)
			if selectfolder(windowname,to_fldr) == 1:
				log('Destionation folder selected')
			else:
				log('Unable to get hold of destination folder','error')
				log('Copy a folder','testend')
				return 0
			time.sleep(2)
			click(windowname,'btnCopy')
			if guiexist ('dlgEvolutionError') == 1:
				log ('Evolution is offline','cause')
				click('dlgEvolutionError','btnOK')
				log('Copy a folder','testend')
				raise LdtpExecutionError (0)

		else:
			print 'Unable to find the source folder'
			log('Unable to find the source folder','cause')
			log('Copy a folder','testend')
			return 0
		#undoremap('evolution','frmEvolution-Mail')	
		print from_fldr+ ' has been copied to '+ to_fldr
		log('folder copied','info')
		log('Copy a folder','testend')
		return 1
	except :
		
		log('Cannot copy the folder','error')
		log('Copy a folder','testend')
		raise LdtpExecutionError (0)

def move_to (from_fldr,to_fldr):

	try:
		log('move a folder','teststart')
		windowname = 'dlgSelectfolder'
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',from_fldr) == 1:
			waittillguiexist ('frmEvolution-'+from_fldr+'*')
			log('From folder selected','info')
			selectmenuitem('frmEvolution-*','mnuFolder;mnuMoveFolderTo')
			time.sleep(3)
			if selectfolder(windowname,to_fldr) == 1:
				log('Destionation folder selected')
			else:
				log('Unable to get hold of destination folder','error')
				log('Move a folder','testend')
				return 0
			time.sleep(2)
			#remap('evolution',windowname)
			click(windowname,'btnMove')
			time.sleep (1)
			if guiexist ('dlgEvolutionError') == 1:
				log ('Evolution is offline','cause')
				#undoremap('evolution',windowname)
				click('dlgEvolutionError','btnOK')
				log('Move a folder','testend')
				raise LdtpExecutionError (0)
			#undoremap('evolution',windowname)
		else:
			print 'Unable to find the source folder'
			log('Unable to find the source folder','cause')
			log('Move a folder','testend')
			return 0

		#undoremap('evolution',windowname)
		log('Move a folder','testend')
		return 1
	except :
		log('Cannot copy the folder','error')
		log('Move a folder','testend')
		raise LdtpExecutionError (0)
	
	log('Move a folder','testend')
			

def select_all (fldrname):	
	try:
		#log('select all mails in a folder','teststart')
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',fldrname) == 1:
			waittillguiexist ('frmEvolution-'+fldrname+'*')
			log('From folder selected','info')
			time.sleep (3)
			if selectmenuitem('frmEvolution-*','mnuFolder;mnuSelectAllMessages') == 1:
				log('All items have been selected','info')	
				#log('select all mails in a folder','testend')
				return 1
			else:
				print 'Unable to select all mails'
				#log('select all mails in a folder','testend')
				return 0
		else:
			print 'Unable to find the folder'
			log('Unable to find the folder','cause')
			#log('select all mails in a folder','testend')
			return 0
	except :
		print 'Cannot select all items in the folder'
		log('Cannot select all the items','error')
		raise LdtpExecutionError (0)


def mark_all_read(fldrname):	
	try:
		log('Mark all as read','teststart')
		select_all(fldrname)
		if selectmenuitem('frmEvolution-*','mnuFolder;mnuMarkAllMessagesasRead') == 1:
			print 'All messages has been marked read'
			log('All items have been selected','info')	
		else:
			print 'Unable to select the mails'
			log('Unable to select the menu Markas;Read','error')
		log('Mark all as read','testend')
	except:
		print 'Cannot set all items in the folder as read'
		log('Cannot mark as read','error')
		log('Mark all as read','testend')
		raise LdtpExecutionError(0)

def mark_read (subject, fldr=''):
	try:
		if fldr != '':
			selectrowpartialmatch ('frmEvolution-*','ttblMessageFolderTree',fldr)
			waittillguiexist ('frmEvolution-'+fldr+'*')
		selectrowpartialmatch ('frmEvolution-*','ttblMessages',subject)
		try:
			selectmenuitem ('frmEvolution-*','mnuMessage;mnuMarkas;mnuRead')
		except:
			log ('Already in Read state','info')
	except:
		log ('Unable to mark message as read','error')
		raise LdtpExecutionError (0)
	

def mark_unread (subject, fldr=''):
	try:
		if fldr != '':
			selectrowpartialmatch ('frmEvolution-*','ttblMessageFolderTree',fldr)
			waittillguiexist ('frmEvolution-'+fldr+'*')
		selectrowpartialmatch ('frmEvolution-*','ttblMessages',subject)
		try:
			selectmenuitem ('frmEvolution-*','mnuMessage;mnuMarkas;mnuUnread')
		except:
			log ('Already in Unread state','info')
	except:
		log ('Unable to mark message as Unread','error')
		raise LdtpExecutionError (0)

def mark_junk (subject, fldr=''):
	try:
		if fldr != '':
			selectrowpartialmatch ('frmEvolution-*','ttblMessageFolderTree',fldr)
			waittillguiexist ('frmEvolution-'+fldr+'*')
		selectrowpartialmatch ('frmEvolution-*','ttblMessages',subject)
		try:
			selectmenuitem ('frmEvolution-*','mnuMessage;mnuMarkas;mnuJunk')
		except:
			log ('Already in Junk state','info')
	except:
		log ('Unable to mark message as Junk','error')
		raise LdtpExecutionError (0)

def mark_notjunk (subject, fldr=''):
	try:
		if fldr != '':
			selectrowpartialmatch ('frmEvolution-*','ttblMessageFolderTree',fldr)
			waittillguiexist ('frmEvolution-'+fldr+'*')
		selectrowpartialmatch ('frmEvolution-*','ttblMessages',subject)
		try:
			selectmenuitem ('frmEvolution-*','mnuMessage;mnuMarkas;mnuNotJunk')
		except:
			log ('Already in Not Junk state','info')
	except:
		log ('Unable to mark message as not junk','error')
		raise LdtpExecutionError (0)



def rename (old_name,new_name):

	try:
		#log('Rename a folder','teststart')
		windowname = 'dlgRenameFolder'
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',old_name) == 1:
			waittillguiexist ('frmEvolution-'+old_name+'*')
			log('From folder selected','info')
			selectmenuitem('frmEvolution-*','mnuFolder;mnuRename')

			time.sleep(3)
			waittillguiexist(windowname)
			settextvalue(windowname,'txt0',new_name)
			time.sleep(3)
			#undoremap('evolution','frmEvolution-Mail')
			click(windowname,'btnOK')
                        time.sleep(3)
			if guiexist('dlgEvolutionError'):
				click('dlgEvolutionError','btnOK')
				time.sleep(3)
				if guiexist (windowname)==1:
					click(windowname,'btnCancel')
					print 'Folder Name already exist'
					log('Folder Already exists','error')
				else:
					log ('Evolution is Offline','cause')
			else:
				print '\''+old_name+'\' has been renamed to \''+new_name
				log('Rename sucessfull','info')
				#log('Rename a folder','testend')
				return 1	
		else:
			print 'Unable to find the folder'
			log('Unable to find the folder','cause')
			#log('Rename a folder','testend')
			return 0
	except :
		print 'Unable to rename'
		log('Cannot rename the folder','error')
		#log('Rename a folder','testend')
		raise LdtpExecutionError (0)

	log('Rename a folder','testend')
	return 0
def delete_nonsys_folder (fldr):	
	try:
		windowname = 'dlgDelete' 
		#defaultname = '\"Inbox/ashwin\"?'
		sysfolder = ['Inbox','Drafts','Junk','Outbox','Sent','Trash']
		if fldr in sysfolder: 
			log ('A system folder has been selected','error')
			print 'You cannot delete a system folder'
		else:
			selectrow ('frmEvolution-*', 'ttblMailFolderTree', fldr)
			selectmenuitem('frmEvolution-*','mnuFolder;mnuDelete')
			time.sleep(2)
			#if waittillguiexist (windowname + defaultname) == 1:
                        print windowname + '\"'+fldr+'\"?'
                        if waittillguiexist (windowname + '*') == 1:
				click(windowname + '*', 'btnDelete')
				time.sleep(2)
				if guiexist('dlgEvolutionError') ==1:
					click('dlgEvolutionError','btnOK')
					log('The folder has subfolders or evolution is offline','cause')
					log('delete a non system folder','testend')
					return 0
				else:				
					print 'the folder has been deleted'
					log('the folder has been deleted','info')	
			else:
				log('unable to find the delete window','error')
				log('delete a non system folder','testend')
				raise LdtpExecutionError (0)
			return 1
	except :
		print 'Cannot delete the folder'
		log('Cannot delete the folder','error')
		raise LdtpExecutionError (0)

def insert_followup_details (follow_up_flag, due_date, time, progress):

	try:
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
		time.sleep (3)
		click(windowname,'btnOK')
		log('Inserted the followup details')
		print 'Follow up details entered'
		log('Insert Follow up details','testend')
	except:
		log('Unable to enter the given details','error')
		log('Insert Follow up details','testend')
		print 'Unable to enter the follow up details'
		raise LdtpExecutionError (0)
	

def expunge():

	try:
		log('Expunge mails','teststart')
		# Assuming that only the mails in the trash can be expunged.
		fldr = 'Trash'
		remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', fldr):
			waittillguiexist ('frmEvolution-'+fldr+'*')
			log('fldr has been selected','info')
			time.sleep(2)
			if selectmenuitem('frmEvolution-Mail','mnuFolder;mnuExpunge') == 1:
				log('Expunge successfull','info')
				print 'Mails have been permanently removed'
			else:
				log('Expunge not completed','info')
				print 'Probs in permanently removing the mails'
				raise LdtpExecutionError (0)
		else:
			print fldr+ 'not found'
			log('Unable to find trash','error')
		time.sleep (2)
		if getrowcount ('frmEvolution-Mail','mnuFolder;mnuExpunge') == 0:
			log ('Expunge Verified','info')
		else:
			log ('Expunge Failed during verification','cause')
			raise LdtpExecutionError (0)
	except:
		log('Unable to expunge the mails','error')
		log('Expunge mails','testend')
		print 'Unable to expunge'
		raise LdtpExecutionError (0)
	log('Expunge mails','testend')
