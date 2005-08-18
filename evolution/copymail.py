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

#Copying an existing Mail

# Section to select and copy mail
def copy_mail (from_fldr,to_fldr, mail_index):
	try:
		time.sleep (10)
		selectrowpartialmatch ('evolution', 'ttblMailFolderTree',
				       to_fldr)
		row_before = getrowcount('evolution', 'ttblMessageList')
		time.sleep (2)
		selectrowpartialmatch ('evolution', 'ttblMailFolderTree',
				       from_fldr)
		rowcount = getrowcount('evolution', 'ttblMessageList') 
		if rowcount > 0:
			if mail_index == -1:
				mail_index = getrowcount ('evolution','ttblMessageList') -1
			selectrowindex ('evolution', 'ttblMessageList', mail_index)
			selectmenuitem ('evolution', 'mnuMessage;mnuCopyToFolder')
			time.sleep (2)
			selectrowpartialmatch ('dlgSelectfolder','ttblMailFolderTree', to_fldr )
			click ('dlgSelectfolder', 'btnCopy')
			time.sleep (2)
			if guiexist('dlgSelectfolder') == 0:
				log ('Select folder dialog not closed', 'error')
				raise LdtpExecutionError(0)
			else:
				selectrowpartialmatch ('evolution', 'ttblMailFolderTree', to_fldr)
				time.sleep (5)
				row_after = getrowcount('evolution', 'ttblMessageList')
				selectmenuitem ('evolution', 'mnuFile;mnuClose')
				if row_after > row_before:
					log ('Copying a mail passed successfully','pass') 
				else :
					log ('Copying a mail failed', 'fail')
		else:
			log ('From folder empty!', 'Warning')
			log ('Did not move any mails to other folder', 'Pass')
	except ldtp.error,msg:
		print 'Copying mail between folders failed',str(msg)
		log ('Copying mail failed','fail')
			
#Read input from file
file = open ('copymail.dat', 'r')
argmts = file.readlines ()
from_fldr = argmts[0].strip ()
to_fldr = argmts[1].strip ()
mail_index = argmts[2].strip ()

if mail_index == '$':
	mail_index = -1;

# Call the function
log ('copyingmail', 'teststart')	
copy_mail (from_fldr, to_fldr, mail_index)
log ('copyingmail', 'testend')

                                                                           
