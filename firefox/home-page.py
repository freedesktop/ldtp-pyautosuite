#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     S. Aginesh <sraginesh@novell.com>
# 
#  Copyright 2004 Novell, Inc.
# 
#  This script is free software; you can redistribute it and/or
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


log ('Changing Home Page', 'teststart')

status = -1;
home_url = 'http://www.google.co.in'
#setting the home page to google.co.in

try:
	selectmenuitem('mozilla', 'mnuEdit;mnuPreferences')
	log ('opened the preferences dialog', 'info')
	status = 1
except:
	log('unable to open the preferences window', 'info')
	status = 0
res = 0
if status == 1:
	try:
		reinitldtp()
		settextvalue ('DeerParkPreferences', 'txtLocation', home_url)
		grabfocus ('DeerParkPreferences', 'txtLocation')
		click ('DeerParkPreferences', 'btnClose')
		log ('changed the home page', 'info')
		res = 1
	except:
		log ('the home page could not be changed', 'error')
		status = 0

if res == 1:
	try:
		click ('mozilla', 'btnHome')
		wait (10)
		url_text = gettextvalue('mozilla', 'txtUrl')
		if url_text == home_url:
			log ('home page loaded properly', 'info')
		else:
			log ('the newly set homepage not loaded', 'error')
	except:	
		('changing home page test failed', 'error')
		
#setting the home page to blank
try:
	selectmenuitem('mozilla', 'mnuEdit;mnuPreferences')
	log('opened the preferences dialog', 'info')
	click('DeerParkPreferences', 'btnUseBlankPage')
	click('DeerParkPreferences', 'btnClose')
	click('mozilla', 'btnHome')
	url = gettextvalue('mozilla', 'txtUrl')
	if url == '':
		log ('home page set to blank page', 'info')
	else:
		log ('could not set home page to blank', 'error')
except:
	log('could not set or change the home page to blank', 'error')

log ('Changing Home Page', 'testend')

