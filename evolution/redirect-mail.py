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

# Redirect a mail.

from ldtp import *
from ldtputils import *

def getrowindex(subject):
   try:
       noofchild=getrowcount ('frmEvolution-*','ttblMessageList')
       for ind in range (noofchild):
           if getcellvalue('frmEvolution-Mail','ttblMessageList',ind,4) == subject:
               return ind
       if ind == noofchild-1:
           log ('Message not present','cause')
           raise LdtpExecutionError (0)
   except:
       log ('Unable to get index of message','error')
       raise LdtpExecutionError (0)

def read_data():

	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	fldr = data_object.gettagvalue ('fldr')[0]
	subject = data_object.gettagvalue ('subject')[0]
	redirect_to = data_object.gettagvalue ('redirect_to')[0]
	return fldr, subject, redirect_to
	
def redirect(fldr, subject, redirect_to):
	try:
		log('redirect a mail','teststart')
		windowname = 'frmComposeMessage'
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',fldr) == 1:
			time.sleep(2)
			log('Folder identified','info')
			Row_index = getrowindex(subject)
			if selectrowindex('frmEvolution-Mail','ttblMessageList',int(Row_index)) == 1:
				log('Message selected','info')
				
				from_id = getcellvalue('frmEvolution-Mail','ttblMessageList',int(Row_index),3)
				selectmenuitem('frmEvolution-*','mnuMessage;mnuRedirect')
				time.sleep(2)
				#setcontext('Compose a message',subject)	
				if waittillguiexist(windowname) == 1:
					print 'Redirect Window opened, hence verified'

#					if settextvalue(windowname,'txtTo',redirect_to) == 1:
					if verifyselect (windowname, 'cboFrom', from_id) == 1:
						print 'From name set correctly'
						log('From name verified','info')
						print 'Redirect a mail verified'
						log('Redirect verified','info')
					else:
						print 'From is set wrongly'
					selectmenuitem(windowname,'mnuFile;mnuClose')
					time.sleep(3)
					if guiexist('dlgWarning:ModifiedMessage'):
						click('dlgWarning:ModifiedMessage','btnDiscardChanges')
					
				else:
					print 'Reply window not found'
					log('Reply to all verify failed','error')					
			else:
				print 'Unable to select the menu item \"Reply\"'
				log('Unable to find the menu item','error')
		else:		
			print 'Unable to find the folder'
			log('Unable to find the folder','error')
		#undoremap('evolution','frmEvolution-Mail')
		log('Reply to all','testend')
	except:
		log('Unable to reply','error')
		print 'Unable to reply'
		log('Reply to all','testend')
		raise LdtpExecutionError (0)

fldr, subject, redirect_to = read_data()
redirect(fldr, subject, redirect_to)
