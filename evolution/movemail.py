#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Nagashree <mnagashree@novell.com>
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
def move_mail (from_fldr, to_fldr, mail_index):
	try:
		time.sleep (10)
		selectrowpartialmatch ('evolution', 'ttblMailFolderTree', to_fldr)
		time.sleep (2)
		row_before = getrowcount('evolution', 'ttblMessageList')
		time.sleep (2)
		selectrowpartialmatch ('evolution', 'ttblMailFolderTree', from_fldr)
		time.sleep (2)
		rowcount = getrowcount('evolution', 'ttblMessageList') 
		if rowcount > 0:
			if mail_index == -1:
				mail_index = rowcount - 1
			selectrowindex ('evolution', 'ttblMessageList', mail_index)
			selectmenuitem ('evolution', 'mnuMessage;mnuMoveToFolder')
			selectrowpartialmatch ('dlgSelectfolder', 'ttblMailFolderTree',to_fldr )
			click ('dlgSelectfolder', 'btnMove')
			time.sleep (3)
			if guiexist('dlgSelectfolder') == 1:
				log ('Select folder dialog not closed', 'error')
				raise LdtpExecutionError(0)
			else:
				selectrowpartialmatch ('evolution', 'ttblMailFolderTree',to_fldr)
				time.sleep (5)
				row_after = getrowcount ('evolution', 'ttblMessageList')
				selectmenuitem ('evolution', 'mnuFile;mnuClose')
				time.sleep(3)
				if row_after > row_before:
					log ('Moving a mail passed successfully', 'pass') 
				else:
					log ('Moving a mail failed', 'fail')
		else:
			log ('From folder empty!', 'Warning')
			log ('Did not move any mails to other folder', 'Pass')
	except ldtp.error,msg:
		print 'Moving mail between folders failed', str(msg)
		log ('Moving mail failed', 'fail')
			
#Read input from file
file = open ('movemail.dat', 'r')
argmts = file.readlines()
from_fldr = argmts[0].strip ()
to_fldr = argmts[1].strip ()
mail_index = argmts[2].strip ()

if mail_index == '$':
	mail_index = -1;

# Call the function
log ('Move mail', 'teststart')	
move_mail (from_fldr, to_fldr, mail_index)
log ('Move mail', 'testend')

                                                                           
