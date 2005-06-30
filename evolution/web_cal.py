#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Manu <manunature@rediffmail.com>
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

def create_web_calendar(name, url):
	try:
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuCalendar')
                comboselect ('dlgNewCalendar','cmbType','On The Web')
		settextvalue ('dlgNewCalendar', 'txtName', name)
		settextvalue ('dlgNewCalendar', 'txtURL', url)
	        try:
		  click ('dlgNewCalendar', 'btnOk')
	        except:
		  print "Ok button state disabled"
	        log ('Create Web Calendar', 'pass')
	except:
	   	print "Creation Failed"
		log ('Create Web Calendar', 'fail')

def verify_web_calendar_created(name):
	try:
                click ('Evolution-Calendars', 'tbtnCalendars')
		wait(3)
		selectrow ('Evolution-Calendars', 'tblGnomeCal', 'gnome-cal')
		#Bug related to expanding a row -- yet to be committed
		#checkrow ('Evolution-Mail', 'treeTabFolder', 1)
		click('Evolution-Calendars','btnPreviousButton')
		#click('Evolution-Calendars','btnPreviousButton')
		click('Evolution-Calendars', 'btnList')
		selectlastrow('Evolution-Calendars','tblDayView')
		x = getrowcount('Evolution-Calendars','tblDayView')
		if x > 0 :		
     		#verifyeventexist ('Evolution-Calendars', 'calview' ) 
			print "verificaton passed"
			log ('Verification of Create Web Calendar', 'pass')
	except:
		print "Verification Failed"
		log ('Verification Create Web Calendar', 'fail')


#trying to read from the file
file = open('web_cal.dat', 'r')
argmts = file.readlines()
cal_name = argmts[0].strip( )
url = argmts[1].strip( )

log ('Webcalendarcreate', 'teststart')
create_web_calendar (cal_name, url)
verify_web_calendar_created (cal_name)
log ('Webcalendarcreate', 'testend')
