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

# Create a new mail from the sent messages.

from ldtp import *
from ldtputils import *

def read_data():

	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	Row_index = data_object.gettagvalue ('Row_index')[0]
	summary_to_append = data_object.gettagvalue ('summary_to_append')[0]
	subject = data_object.gettagvalue ('subject')[0]
	to = data_object.gettagvalue ('to')[0]
	return Row_index, summary_to_append, subject, to
	
def create_fromsent():
	try:
		log('create a message from sent mails','teststart')
		windowname = 'frmComposeamessage'
		fldr = 'Sent'
		Row_index, summary_to_append, subject, to = read_data()
		remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-Mail','ttblMailFolderTree',fldr) == 1:
			time.sleep(3)
			log('Folder identified','info')
			print Row_index
			selectrowindex('frmEvolution-Mail','ttblMessageList',int(Row_index))
			summary = getcellvalue('frmEvolution-Mail','ttblMessageList',int(Row_index),4)
			selectmenuitem('frmEvolution-Mail','mnuMessage;mnuEditasNewMessage')
			time.sleep(3)
			setcontext('Compose a message',summary)	
			if waittillguiexist(windowname) == 1:
				print 'here'
				panel_ct = getpanelchildcount(windowname,'pnlPanelcontainingHTML')
				print panel_ct
				if appendtext (windowname, 'txt'+str(6+panel_ct-1), summary_to_append) == 1:
					print '1'
					time.sleep(3)
					settextvalue(windowname,'txtSubject',subject)
					setcontext('Compose a message',subject)
					settextvalue(windowname,'txtTo',to)
					click(windowname,'btnSend')
					log('The message has been modified and sent','info')
				else:
					print 'Unable to modify the existing messsage'
					log('Unable to edit the existing message','error')
				undoremap('evolution','frmEvolution-Mail')
				log('Message created from an existing mail','info')
				print 'Message created from an exixting mail'
			else:
				print 'Unable to open the window'
				log('Unable to open the window','error') 
		else:
			log('The folder cannot be identified','error')
			print 'Folder not found'
	
	except:
		log('Unable to edit as a new message','error')
		print 'Unable to edit as a new message' 
	
	log('create a message from sent mails','testend')
	
create_fromsent()
