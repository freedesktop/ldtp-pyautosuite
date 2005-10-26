#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Authors:
#     Khasim Shaheed <sshaik@novell.com>
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
		
		selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', sent_folder)
		time.sleep (2)
		sent_mail_count = getrowcount ('frmEvolution-Mail', 'ttblMessageList')
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
to, subject, body, cc, attachment, sentitemsfolder, refimg = read_maildata (datafilename)

# Call the functions
compose_mail (to, subject, body, cc, attachment, sentitemsfolder, refimg)

