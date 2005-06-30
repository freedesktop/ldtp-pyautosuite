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

#deletion of meeting
log('delete the Meeting','teststart')
def delete_meeting():
	
		
	selecteventindex('Evolution-Calendars','calview',1)
	#x=execfile('verifymeeting.py')
	#if x==1:
	selectmenuitem('Evolution-Calendars','mnuEdit;mnuDelete')
	click('dlgEvolutionQuery','btnDelete')	
        click('dlgEvolutionQuery','btnSendNotice')	
delete_meeting()
log('delete the Meeting','testend')
