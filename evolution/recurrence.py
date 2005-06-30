#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Anjana <anjana_091@rediffmail.com>
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

#rrecurrence
s1 = 'Unable to get gui handle'

def funct_recur(num1,num2):
 try: 
	
	#selectmenuitem('Evolution-Mail','mnuFile;mnuNew;mnuMeeting')
	selecttab('dlgMeeting-Nosummary','ptlMeeting','1')
	check('dlgMeeting-Nosummary','chkThisappointmentrecurs')
	setvalue('dlgMeeting-Nosummary','sbtnEvery',num1)
	#getvalue('dlgMeeting-Nosummary','sbtnEvery')
	#verifysetvalue('dlgMeeting-Nosummary','sbtnEvery','20')
	comboselect('dlgMeeting-Nosummary','cmbday(s)','week(s)')
	comboselect('dlgMeeting-Nosummary','cmbforever','for')
	setvalue('dlgMeeting-Nosummary','sbtnoccurence',num2)
	click('dlgEvolutionQuery','btnSend')
	
 except error,msg:
	if string.find(str(msg),s1) == -1:
		print "File not found(nt cz of gui handle)...so  stilll continuing "
      
  #      print'Error'

log('Open-the-Recurrence-Meeting','teststart')
funct_recur(num1,num2)
log('Open-the-Recurrence-Meeting','testend')
