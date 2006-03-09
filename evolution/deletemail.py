#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bhargavi  <kbhargavi_83@yahoo.co.in>
#     Premkumar <jpremkumar@novell.com>
#     Khasim Shaheed <khasim.shaheed@gmail.com>
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

# Deleting an existing Mail
import time

from ldtp import *
from evoutils.mail import *

# Section to delete a mail
def delete_mail (source_fldr, mail_index):
	try:
		selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', source_fldr)
		time.sleep (2)
		rowcount = getrowcount('frmEvolution-*', 'ttblMessages') 
		if rowcount > 0:
			if mail_index == -1:
				mail_index = rowcount-1
			selectrowindex ('frmEvolution-*', 'ttblMessages', mail_index)
			time.sleep (1)
			selectmenuitem ('frmEvolution-*', 'mnuEdit;mnuDeleteMessage')
			time.sleep (1)
			selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', source_fldr)
			time.sleep (2)
			row_after = getrowcount('frmEvolution-*','ttblMessages')
			if row_after == (rowcount-1):
				log ('Deleting a mail passed successfully', 'info') 
				return 1
			else:
				log ('Row count does not match after delete mail', 'cause')
				log ('Deleting a mail failed', 'info')
				return 0
		else:
			log ('From folder empty!', 'Warning')
			log ('Did not Delete any mail from source folder', 'info')
			return 0
	except ldtp.error,msg:
		log ('Deleting mail failed' + str(msg), 'cause')
		log ('delete mail failed', 'fail')
		raise LdtpExecutionError (0)
			
# Read input from file
data_object = LdtpDataFileParser (datafilename)
source_fldr = data_object.gettagvalue ('source_fldr')
mail_index = data_object.gettagvalue ('mail_index')

# Call the function
try:
	log ('Delete a message', 'teststart')
	result = delete_mail (source_fldr[0], int (mail_index[0]))
        if result == 1:
                log ('Delete a message', 'pass')
        else:
                log ('Delete a message', 'fail')
        log ('Delete a message', 'testend')

except:
        log ('Delete a message', 'error')
        log ('Delete a message', 'testend')
        raise LdtpExecutionError(0)


