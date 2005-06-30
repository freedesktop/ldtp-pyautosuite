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

#Filter Search and Verify Filter Search on Subject or Sender contains
import string, time

#Filter search
def search (search_folder, data):
	try:
		click ('Evolution-Mail', 'tbtnMail')
		time.sleep (2)
		selectrow ('Evolution-Mail', 'treeTabFolder', search_folder)
		global search_mail_count
		search_mail_count = 0
		total_mail_count = getrowcount ('Evolution-Mail', 'treetblMails')
		for i in range (0, total_mail_count):
			subject = getcellvalue ('Evolution-Mail', 'treetblMails', i, 4)
			sender = getcellvalue ('Evolution-Mail', 'treetblMails', i, 3)
			if (string.find (subject, data) >= 0 or string.find (sender, data) >= 0):
				search_mail_count = search_mail_count + 1
		comboselect ('Evolution-Mail', 'cmbSearchType', 'Subject or Sender contains')
		if (data):
			settextvalue ('Evolution-Mail', 'txtSearchTextEntry', data)
		click ('Evolution-Mail', 'btnFindNow')
		time.sleep (2)
		log('Filter Search on Subject or Sender contains' ,'pass')
	except:
		log('Filter Search on Subject or Sender contains' ,'fail')

#Verify filter search
def verify_search (search_mail_count):
	try:
		filter_mail_count = getrowcount ('Evolution-Mail', 'treetblMails')
		if (search_mail_count == filter_mail_count):
			log ('Verify Filter Search on Subject or Sender contains', 'pass')
		else:
			log ('Verify Filter Search on Subject or Sender contains', 'fail')
		click ('Evolution-Mail', 'btnClear')
        except:
		log ('Verify Filter Search on Subject or Sender contains', 'fail')

#Getting the data from a file		
file = open('filter_search_on_subject_sender.dat', 'r')
argmts = file.readlines()
search_folder = argmts[1].strip( )
data = argmts[2].strip( )

#Calling the functions
log('Filter Search and Verify Filter Search on Subject or Sender contains','teststart')
log('Filter Search on Subject or Sender contains' ,'teststart')
search (search_folder, data)
log('Filter Search on Subject or Sender contains' ,'testend')
log('Verification of Filter Search on Subject or Sender contains', 'teststart')
verify_search (search_mail_count)
log('Verification of Filter Search on Subject or Sender contains' ,'testend')
log('Filter Search and Verify Filter Search on Subject or Sender contains','testend')