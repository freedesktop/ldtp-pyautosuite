#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Khasim Shaheed <sshaik@novell.com>
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

#Move And Verify Move of Mails
import time

#Move mails
def move (source, destination, account_name, start, end):
	try:
		selectrowindex ('Evolution-Mail', 'treetblMails', start)
                click ('Evolution-Mail', 'btnMove')
                click ('dlgSelectFolder', 'btnNew')
                settextvalue ('dlgCreateNewFolder', 'txtFoldername', destination)
                selectrow ('dlgCreateNewFolder', 'treetblMailFolderTree', account_name)
                click ('dlgCreateNewFolder', 'btnCreate')
                selectrow ('dlgSelectFolder', 'treetblMails', destination)
                click ('dlgSelectFolder', 'btnMove')
		for i in range(start+1, end+1):
			selectrowindex ('Evolution-Mail', 'treetblMails', start)
			click ('Evolution-Mail', 'btnMove')
			selectrow ('dlgSelectFolder', 'treetblMails', destination)
			click ('dlgSelectFolder', 'btnMove')
		log ('Move Mails', 'pass')
	except:
		log ('Move Mails', 'fail')

#Verify moving of mails
def verify_move (source, destination, no_mails, prev_scount):
	try:
		click ('Evolution-Mail', 'tbtnMail')
		time.sleep (2)
		selectrow ('Evolution-Mail', 'treeTabFolder', destination)
		new_dcount = getrowcount ('Evolution-Mail', 'treetblMails')
                selectrow ('Evolution-Mail', 'treeTabFolder', source)
		new_scount = getrowcount ('Evolution-Mail', 'treetblMails')
		if (new_scount == (prev_scount-no_mails) and new_dcount == no_mails):
			log ('Verify Move Mails', 'pass')
	        else:
			log ('Verify Move Mails', 'fail')
        except:
		log ('Verify Move Mails', 'fail')

#Getting the data from a file		
file = open('move_mails_new_folder.dat', 'r')
argmts = file.readlines()
source = argmts[1].strip( )
destination = argmts[2].strip( )
account_name = argmts[3].strip( )
start = int (argmts[4].strip( ))
end = int (argmts[5].strip( ))

#Calling the functions and getting the initial
#message count of source and destination folders
log('Move And Verify Moving of Mails', 'teststart')
log('Move Mails' ,'teststart')
click ('Evolution-Mail', 'tbtnMail')
time.sleep (2)
selectrow ('Evolution-Mail', 'treeTabFolder', source)
time.sleep (1)
prev_scount = getrowcount ('Evolution-Mail', 'treetblMails')
move (source, destination, account_name, start, end)
log('Move Mails' ,'testend')
log('Verification of Move Mails', 'teststart')
no_mails = end-start+1
verify_move (source, destination, no_mails, prev_scount)
log('Verification of Move Mails' ,'testend')
log('Move Mails and Verify Moveing of Mails','testend')
