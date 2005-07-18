#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bhargavi  <kbhargavi_83@yahoo.co.in>
#     Premkumar <jpremkumar@novell.com>
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

#Moving an existing Mail

# Section to select and move mail
def delete_mail (source_fldr):
	#TODO: Currently deletes only the last mail. Should be extended to delete
	#any arbitary mail
	try:
		selectrowpartialmatch ('evolution', 'ttblMailFolderTree',
				       source_fldr)
		rowcount = getrowcount('evolution', 'ttblMessageList') 
		if rowcount > 0:
			#selectlastrow ('evolution', 'ttblMessageList')
			selectrowindex ('evolution', 'ttblMessageList',
					rowcount-3)
			selectmenuitem ('evolution',
					'mnuEdit;mnuDeleteMessage')
			time.sleep (3)
			selectrowpartialmatch ('evolution',
					       'ttblMailFolderTree',to_fldr)
			time.sleep (5)
			row_after = getrowcount('evolution',
						'ttblMessageList')
			selectmenuitem ('evolution', 'mnuFile;mnuClose')
			if row_after < rowcount:
				log ('Deleting a mail passed successfully',
					     'pass') 
			else:
				log ('Deleting a mail failed','fail')
		else:
			log ('From folder empty!', 'Warning')
			log ('Did not Delete any mail from source folder',
			     'Pass')
	except ldtp.error,msg:
		print 'Deleting mail between folders failed',str(msg)
		log ('Moving mail failed','fail')
			
#Read input from file
file = open ('deletemail.dat', 'r')
argmts = file.readlines()
source_fldr = argmts[0].strip( )

# Call the function
log ('deletemail', 'teststart')	
delete_mail (source_fldr)
log ('deletemail', 'testend')
log ('Deleting mail succeeded', 'pass') 
                                                                           
