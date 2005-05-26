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

#test cases on forward, back and stop buttons
def get_url_list (file):
	try:
		fp = open (file)
	except IOError:
		log ('Unable to open url.txt file', 'error')
		return None
	url_list = fp.readlines ()
	fp.close ()
	return url_list

def set_text(window, component, text):
	try:
		settextvalue(window, component, text)
		i = verifysettext(window, component, text)
		if i == 1:
			log (text + 'is set in ' + component, 'info')
		else:
			log (text + 'could not be set in ' + component)
			return 0
		return 1
	except:
		log ('could not set ' + text + ' to ' + 'component', 'info')
		return 0


def browse_url (url):
	try:
		i = set_text('mozilla', 'txtUrl', url)
		if i == 1:
			try:
				click ('mozilla', 'btnGo')
				wait (5)
			except:
				log('some error while clicking btnGo', 'error')
				return 0
		return 1
	except:
		log ('could browse the requested url:' + url, 'error')
		return 0


		

log ('Page Load Control', 'teststart')
url_list = get_url_list ('url.txt')

i = browse_url ((url_list[0].split(' '))[0])
if i == 0:
	print 'could not browse through the required pages hence further testing wont be done in this file'
	log ('could not browse through the required pages hence further testing wont be done in this file', 'error')
	raise LdtpExecutionError (0)

i = browse_url ((url_list[1].split(' '))[0])
if i == 0:
	print 'could not browse through the required pages hence further testing wont be done in this file'
	log ('could not browse through the required pages hence further testing wont be done in this file', 'error')
	raise LdtpExecutionError (0)


click('mozilla', 'btnBack')
wait(10)

url = gettextvalue('mozilla', 'txtUrl')

if url == (url_list[0].split(' '))[0]:
	log ('back button gets back the required web page', 'info')
else:
	log ('back button action failed', 'error')
	print 'back button action failed'

click('mozilla', 'btnForward')
wait(10)

url = gettextvalue('mozilla', 'txtUrl')
if url == (url_list[1].split(' '))[0]:
	log ('forward button goes to the required page', 'info')
else:
	log ('forward button action failed', 'error')
	print 'forward button action failed'

wait(10)

try:
	enabled = stateenabled('mozilla', 'btnStop')
	if enabled == 1:
		log ('Stop button active when page enabled', 'error')
	else:
		log ('Stop button disabled when page is loaded fully', 'info')
	settextvalue ('mozilla', 'txtUrl', 'http://www.novell.com')
	click ('mozilla', 'btnGo')
	enabled = stateenabled('mozilla', 'btnStop')
	if enabled == 1:
		log ('Stop button active while page is being loaded', 'info')
	else:
		log ('Stop button not getting enabled while loading of page', 'error')
except:
	log ('testing on stop button could not be performed', 'error')
	print ('testing on stop button failed')
	
log ('Page Load Control', 'testend')
