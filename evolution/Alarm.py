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

#Alarm Setting
s1 = 'Unable to get gui handle'

def call_alarm():
  try:
	click('dlgMeeting-Nosummary','btnCustomize')
	click('dlgAlarms','btnAdd')
	execfile('addalarm.py')
	#execfile('checkalarm.py')
	wait(5)
	selectrowindex('dlgAlarms','tblAlarm',1)
	#selectrow('dlgAlarms','tblAlarm','Play a sound 15 minutes before the start of the appointment')
	click('dlgAlarms','btnOK')
  except error,msg:
	if string.find(str(msg),s1)== -1:
				print "File not found(nt cz of gui handle)...so  stilll continuing"	
	print "--File  nt found..bt  stilll continuing"
call_alarm()
