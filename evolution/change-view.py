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

#To change the properties of the folders

from ldtp import *
from ldtputils import *

def addcontacts(attendee,email,addrbook):
   log ('Add Attendees','teststart')
   try:

       windowname = 'dlgSelectContactsfromAddressBook'
       comboselect (windowname,'cboAddressBook',addrbook)
       remap ('evolution',windowname)
       attendee=attendee[0].split (':')
       email=email[0].split (':')
       if len(attendee)!=len(email):
           log ('Mismatch in contacts name and email','error')
           raise LdtpExecutionError (0)
       for ind in range(len(attendee)):
           try:
	       att=attendee[ind] + ' <'+ email[ind] + '>'
               selectrow (windowname,'tblContacts',att)
               time.sleep(2)
               click (windowname, 'btnAdd')
               time.sleep (1)
           except:
               log ('User not found','cause')
               raise LdtpExceptionError(0)
       click (windowname, 'btnClose')
       undoremap ('evolution',windowname)
   except:
       log ('Attendee Addition failed','error')
       log ('Add Attendees','testend')
       raise LdtpExecutionError (0)
   log ('Add Attendees','testend')


def read_data():

	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	read_msg_body_data = data_object.gettagvalue ('read_msg_body_data')[0]
	fldr = data_object.gettagvalue ('fldr')[0]
	share_type = data_object.gettagvalue ('share_type')[0]
	addr_book = data_object.gettagvalue ('addr_book')[0]
	contacts = data_object.gettagvalue ('contacts')
	emails = data_object.gettagvalue ('emails')
	#print read_msg_body_data, fldr, share_type, addr_book, contacts, emails
	return read_msg_body_data, fldr, share_type, addr_book, contacts, emails


log('Change Properties','teststart')
try:
	read_msg_body_data, fldr, share_type, addr_book, contacts, emails = read_data()
	windowname = 'dlgFolderProperties'
	#remap('evolution','frmEvolution-Mail')
	if selectrow ('frmEvolution-*','ttblMailFolderTree',fldr) == 1:
		time.sleep (3)
		selectmenuitem('frmEvolution-*','mnuFolder;mnuProperties')
		time.sleep(3)
		waittillguiexist (windowname)	
	
		if read_msg_body_data == 'uncheck':
			uncheck (windowname, 'chkCopyfoldercontentlocallyforofflineoperation')
		elif read_msg_body_data == 'check':
			check (windowname, 'chkCopyfoldercontentlocallyforofflineoperation')
		else:
			print 'Data not relevant'
			log('Check box status not set properly')
	
		if selecttab (windowname,'ptl0','Sharing') == 1:
			if share_type == 'shared_with':
				click (windowname, 'rbtnSharedWith')
				time.sleep(2)
				click(windowname,'btnContacts')		
				waittillguiexist('dlgSelectContactsfromAddressBook')
				time.sleep(2)
				addcontacts(contacts,emails,addr_book)				
				time.sleep(3)
				click(windowname,'btnAdd')
		time.sleep(3)
		click(windowname,'btnOK')
	else:
		print 'Unable to select the specified folder'

except:	
		print 'Unable to modify the properties'
		log('Unable to modify the properties of the folder'+fldr,'error')
		log('Change Properties','testend')
		raise LdtpExecutionError (0)
log('Change Properties','testend')
		
