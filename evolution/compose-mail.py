#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Authors:
#     Khasim Shaheed <khasim.shaheed@gmail.com>
#
#  Copyright 2004 Novell, Inc.
#
#  This library is free software; you can redistribute it and/or
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

# Compose a new mail through File menu
from evoutils.mail import *
from evoutils.composemail import *
from evoutils.mailpreferences import *

# Section to compose a new mail through File menu
def compose_mail (to, subject, body, cc, attachment, sentitemsfolder, refimg):
	try:
		if sentitemsfolder:
			sent_folder = sentitemsfolder[0]
		else:
			sent_folder = 'Sent Items'
		
		selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', sent_folder)
		time.sleep (2)
		sent_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
		compose (to, subject, body, cc, attachment)
		if verifymailwithimage (sent_folder, sent_mail_count, refimg) == 1:
			log ('Compose new message', 'pass')
		else:
			log ('Compose new message', 'fail')
	except ldtp.error, msg:
		log ('Compose new message failed ' + str (msg), 'cause')
		log ('Compose message failed', 'fail')
		raise LdtpExecutionError (0)
	
# Reading Input from File
#to, subject, body, cc, attachment, sentitemsfolder, refimg = read_maildata (datafilename)
try:
        data_object = LdtpDataFileParser (datafilename)
        to = data_object.gettagvalue ('to')
        cc = data_object.gettagvalue ('cc')
        subject = data_object.gettagvalue ('subject')
        body = data_object.gettagvalue ('body')
        sentitemsfolder = data_object.gettagvalue ('sentitemsfolder')
        refimg = data_object.gettagvalue ('refimg')
        attachment = data_object.gettagvalue ('attachment')
        log('User data read successfull','info')
except:
        log('Unable to read the user data or data file missing','error')
        raise LdtpExecutionError(0)

# Call the functions
compose_mail (to, subject, body, cc, attachment, sentitemsfolder, refimg)

