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

# Open a message in a new window.

from ldtp import *
from ldtputils import *

def getrowindex(subject):
   try:
       noofchild=getrowcount ('frmEvolution-*','ttblMessages')
       for ind in range (noofchild):
           if getcellvalue('frmEvolution-*','ttblMessages',ind,4) == subject:
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
#	Row_index = data_object.gettagvalue ('Row_index')[0]
	subject = data_object.gettagvalue ('subject')[0]
	return fldr, subject
	
def openmsg(fldr, subject):
	try:
		log('Open in a new window','teststart')
		windowname = 'frmWelcometoEvolution!'
		#remap('evolution','frmEvolution-Mail')
		if selectrowpartialmatch('frmEvolution-*','ttblMailFolderTree',fldr) == 1:
                        waittillguiexist ('frmEvolution-'+fldr+'*')
			time.sleep(2)
			log('Folder identified','info')
			selectrow('frmEvolution-*','ttblMessages',subject)
			Row_index = getrowindex(subject)
			selectrowindex('frmEvolution-*','ttblMessages',int(Row_index))
			selectmenuitem('frmEvolution-*','mnuMessage;mnuOpeninNewWindow')
			time.sleep(3)
			setcontext('Welcome to Evolution!',subject)	
			if waittillguiexist(windowname) == 1:
				log('Message opened in a new window','info')
				print 'the selected message has been opened in a new window'
				time.sleep(3)
				selectmenuitem(windowname,'mnuFile;mnuClose')
			else:
				print 'Verification failed'
				log('verify failed','error') 
			#undoremap('evolution','frmEvolution-Mail')
		else:
			log('The folder cannot be identified','error')
	
	except:
		log('Unable to open the message in a new window','error')
		print 'Unable to open the message in a new window' 
	
	log('Open in a new window','testend')

fldr, subject = read_data()	
openmsg(fldr, subject)
