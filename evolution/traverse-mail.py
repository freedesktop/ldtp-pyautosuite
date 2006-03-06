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

# Traverse Through the mails

from ldtp import *
from ldtputils import *

def getrowct_based_properties(property_val):
   try:
       ct = 0
       colmn = 4
       noofchild = getrowcount ('frmEvolution-*','ttblMessages')
       if property_val == 'Important':
	    colmn = 2
       elif property_val == 'Unread':
	    colmn = 0
       else:
	    ct = noofchild - 1

       for ind in range (noofchild):
           if getcellvalue('frmEvolution-*','ttblMessages',ind,colmn) == '1':
               ct = ct + 1
       if colmn == 0:
	   ct = noofchild - ct
       return ct
   except:
       log ('Unable to get index of message','error')
       raise LdtpExecutionError (0)

def read_data():

	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	fldr = data_object.gettagvalue ('fldr')[0]
	subject = data_object.gettagvalue ('subject')[0]
	traverse_method = data_object.gettagvalue ('traverse_method')[0]
	return fldr, subject, traverse_method
	
def Traverse(fldr, subject, traverse_method):
	try:
		log('Traverse Mail','teststart')
		windowname = 'frmWelcometoEvolution!'
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch ('frmEvolution-*','ttblMailFolderTree',fldr) == 1:
			time.sleep(3)
			log('Folder identified','info')
			selectrow('frmEvolution-*','ttblMessages',subject)
			if traverse_method == 'NextUnread' or traverse_method == 'PreviousUnread':
				property_val = 'Unread'
			elif traverse_method == 'NextImportant' or traverse_method == 'PreviousImportant':
				property_val = 'Important'
			else:
				property_val = ''
			row_ct = getrowct_based_properties(property_val)
			if row_ct >= 2:
				row_ct = 2  
			elif row_ct <= 1:
				print 'Less than 1 mail in the specified folder, Unable to traverse'
				log('Less than 1 mail in the specified folder, Unable to traverse','error')
			
			for i in range(0,row_ct):  # Find another method to stop the execution.

				if traverse_method == 'Next' or traverse_method == 'Previous' \
				or traverse_method == 'NextUnread' or traverse_method == 'PreviousUnread' \
				or traverse_method == 'NextImportant' or traverse_method == 'PreviousImportant' \
				or traverse_method == 'NextThread':
					if selectmenuitem('frmEvolution-Mail','mnuMessage;mnuGoTo;mnu'+traverse_method+'Message') == 1:
						time.sleep(3)
#						summary = getcellvalue('frmEvolution-Mail','ttblMessageList',int(i),4)
					else:
						print 'End of messages'
						log('end of messages','error')
				else:
					print 'Traverse method unknown'
					log('unknown traverse method','error')
		else:
			log('Unable to find a message with the given subject ','error')
			print 'Verify your subject'
	except:
		log('Unable to traverse through the message list','error')
		print 'Unable to traverse through the message list'
		log('Traverse Mails','testend')
		raise LdtpExecutionError (0)

	log('Traverse Mails','testend')

fldr, subject, traverse_method = read_data()
Traverse(fldr, subject, 'Next')
Traverse(fldr, subject, 'Previous')
Traverse(fldr, subject, 'NextImportant')
Traverse(fldr, subject, 'PreviousImportant')
Traverse(fldr, subject, 'NextUnread')
Traverse(fldr, subject, 'PreviousUnread')

