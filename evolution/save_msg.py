#!/usr/bin/env python
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
# To save a mail message in home folder.

from menu_reorganization import *
	
def save_msg(fldr, subject, file_name):

	try:
		log('Save a message','teststart')
		windowname = 'dlgSaveMessage...'
		if select_mail (fldr,subject) == 1:
			selectmenuitem('frmEvolution-*','mnuFile;mnuSaveMessage')
			if waittillguiexist(windowname)	== 1:
				settextvalue(windowname,'txtName',file_name)
				time.sleep(3)
				click(windowname,'btnSave')
				time.sleep(3)
				if guiexist('dlgOverwritefile?') == 1:
					log('File Already exists','cause')
					print 'File already exist'
					click('dlgOverwritefile?','btnCancel')
					print 'Cancelling...the job.'
					time.sleep(2)
					click(windowname,'btnCancel')
				else:
					log('The file has been saved','info')
					path = os.environ.get('HOME')
					full_path = path + '/' + file_name
					if os.path.isfile(full_path):
						log('The exixtance od file has been verified','info')
						print 'The file has been saved :'+ full_path
					else:
						print 'file is not actually present, verify failed'
						log('The exixtance od file has not been verified','error')
						raise LdtpExecutionError (0)

			else:
				log('Unable to find the window \'Save Message\'','cause')
				log('Save a message','testend')
				raise LdtpExecutionError (0)
		else:
			log('Unable to select the fldr/mail','cause')
			log('Save a message','testend')
			raise LdtpExecutionError (0)
	except:
		log('Unable to save the message','error')
		log('Save a message','testend')
		raise LdtpExecutionError (0)
	log('Save a message','testend')		
		
# Read data from xml file.
data_object = LdtpDataFileParser (datafilename)
fldr = data_object.gettagvalue ('fldr')[0]
subject = data_object.gettagvalue ('subject')[0]
file_name = data_object.gettagvalue ('file_name')[0]

# Call the function
if fldr and subject and file_name:
	save_msg(fldr, subject, file_name)
else:
	if not (fldr):
		log ('fldr not provided in data xml file', 'error')
	if not (subject):
		log ('subject not provided in data xml file', 'error')
	if not (file_name):
		log ('file_name not provided in data xml file', 'error')
	log ('save message', 'fail')	
