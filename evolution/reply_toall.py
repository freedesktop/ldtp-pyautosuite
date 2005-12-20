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

# Reply to all.

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

def read_data():

	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	fldr = data_object.gettagvalue ('fldr')[0]
	subject = data_object.gettagvalue ('subject')[0]
	expected_to_emails = data_object.gettagvalue ('expected_to_emails')[0]
	expected_to_names = data_object.gettagvalue ('expected_to_names')[0]
	return fldr, subject, expected_to_names, expected_to_emails
	
def reply_toall(fldr, subject, expected_to_names, expected_to_emails):
	try:
		log('Reply to all','teststart')
		windowname = 'frmComposeamessage'
		remap('evolution','frmEvolution-Mail')
		print fldr,subject
		if selectrowpartialmatch ('frmEvolution-Mail','ttblMailFolderTree',fldr) == 1:
			time.sleep(2)
			log('Folder identified','info')
			Row_index = getrowindex(subject)
			if selectrowindex('frmEvolution-Mail','ttblMessageList',int(Row_index)) == 1:
				log('Message selected','info')
				selectmenuitem('frmEvolution-Mail','mnuMessage;mnuReply')
				time.sleep(2)
				setcontext('Compose a message','Re: '+subject)	
				if waittillguiexist(windowname) == 1:
					expected_to_names = expected_to_names.split(',')
					expected_to_emails = expected_to_emails.split(',')
					to = ''
					if len(expected_to_emails) == len(expected_to_names):
						for i in range(0,len(expected_to_emails)):
							to = to + str(expected_to_names[i]) + ' <' + str(expected_to_emails[i]) + '>, '
						to = to[:-2]
						print to,'to'
						cur_to = gettextvalue(windowname,'txtCc')
						print cur_to,'cur_to'
						if cur_to == to:
							print 'Reply to all working correctly'
						else:
							print 'Probs in to text box'
					else:
						print 'Enter data correctly'
					
					print 'Reply Window opened, hence verified'
					time.sleep(3)
					selectmenuitem(windowname,'mnuFile;mnuClose')
					log('Reply to all verified','info')
				else:
					print 'Reply window not found'
					log('Reply to all verify failed','error')					
			else:
				print 'Unable to select the menu item \"Reply\"'
				log('Unable to find the menu item','error')
		else:		
			print 'Unable to find the folder'
			log('Unable to find the folder','error')
		undoremap('evolution','frmEvolution-Mail')
		log('Reply to all','testend')
	except:
		log('Unable to reply','error')
		print 'Unable to reply'
		raise LdtpExecutionError (0)

fldr, subject, expected_to_names, expected_to_emails = read_data()
reply_toall(fldr, subject, expected_to_names, expected_to_emails)
