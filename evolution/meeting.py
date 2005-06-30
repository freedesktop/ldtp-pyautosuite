#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Sheetal <svnayak18@yahoo.com>
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

#meeting 
s1 = 'Unable to get gui handle'
def call_meeting (summary,location,description,cmbname1,cmbname,date,time,date1,time1):
 try: 
	
	selectmenuitem('Evolution-Calendar','mnuFile;mnuNew;mnuMeeting')
	selecttab('dlgMeeting-Nosummary','ptlMeeting','0')
	settextvalue('dlgMeeting-Nosummary','txtSummary',summary)
	setcontext('Meeting - No summary','Meeting - '+summary)
	settextvalue('dlgMeeting-Nosummary','txtLocation',location)
	comboselect('dlgMeeting-Nosummary','cmbPublic',cmbname1)
	#comboselect('dlgMeeting-Nosummary','cmbPersonal', cmbname)
	execfile('categories.py')
	settextvalue('dlgMeeting-Nosummary','txtEventDescription',description)
	check('dlgMeeting-Nosummary','chkAlldayevent')
	settextvalue('dlgMeeting-Nosummary','txtTextDateEntry2',date)
	settextvalue('dlgMeeting-Nosummary','txtTextDateEntry1',date1)
	click('dlgMeeting-Nosummary','chkAlarm')
	execfile('Alarm.py')
	execfile('recurrence.py')
	execfile('invitation.py')
	click('dlgMeeting-Nosummary','btnOK')
	click('dlgEvolutionQuery','btnSend')
	
 except error,msg:
	if string.find(str(msg),s1) == -1:
		print "File not found(nt cz of gui handle)...so  stilll continuing "
	log('cannotselect','fail')
	log('errorinselecting','error')


#trying to read from the file
file = open('meeting.dat', 'r')
argmts = file.readlines()
summary = argmts[0].strip( )
location = argmts[1].strip( )
description = argmts[2].strip( )
categories = argmts[3].strip( )
cmbname = argmts[4].strip( )
cmbname1 = argmts[5].strip( )
date= argmts[6].strip( )
time= argmts[7].strip( )
date1= argmts[8].strip( )
time1= argmts[9].strip( )
num1=argmts[10].strip( )
num2=argmts[11].strip( )
value=argmts[12].strip( )

# Call the function
log('Open-the-Meeting','teststart')
call_meeting (summary,location,description,cmbname1,cmbname,date,time,date1,time1)
log('Open-the-Meeting','testend')
