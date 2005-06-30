#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bhargavi <kbhargavi_83@yahoo.co.in>
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

#  Delete a mail
def delete_mail():	      
        selectlastrow ('Evolution-Mail', 'treetblMails')
	log('Selects-the-last-message','pass')
	selectmenuitem ('Evolution-Mail', 'mnuEdit;mnuDelete')
	log('Deletes-the-message','pass')
	
def verify_delete():
	selectrow ('Evolution-Mail', 'treeTabFolder', 'Sent')
	selectrowpartialmatch('Evolution-Mail', 'treeTabFolder', 'Mailbox')

	

# Call the function
try:
	log('DeletionofMail' ,'teststart')	
	wait(3)
	selectrowpartialmatch('Evolution-Mail', 'treeTabFolder', 'Mailbox')
	row_before = getrowcount('Evolution-Mail', 'treetblMails') 
	log('row-count-before-'+str(row_before),'pass')       
	delete_mail ()
	log('DeletionofMail' ,'testend')
	log('Verification-of-deletion-of-Mail' ,'teststart')
	wait(3)
	verify_delete()
	row_after = getrowcount('Evolution-Mail', 'treetblMails')
	if(row_after == (row_before - 1)):
		log('row-count-after-'+str(row_after),'pass')
		log('Verification-of-delete ','pass')
	log('Verification-of-deletion-of-Mail' ,'testend')
except error:
	print 'Delete mail failed'
	log('Deletion-and-verification-of-mail','fail') 

#finally:
#	print 'Delete works fine'




