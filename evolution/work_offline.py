#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
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
# To print a message. 
# Note Actually it clicks the cancel btn instead of print button.

from ldtp import *
from ldtputils import *
	
def work_offline():
	try:
		log('Work Offline','teststart')
		#remap('evolution','frmEvolution-Mail')
		if doesmenuitemexist ('frmEvolution-*', 'mnuFile;mnuWorkOffline') == 1:
			if selectmenuitem('frmEvolution-*','mnuFile;mnuWorkOffline') == 1:
				time.sleep(3)
				#undoremap('evolution','frmEvolution-Mail')
				#remap('evolution','frmEvolution-Mail')
				if doesmenuitemexist ('frmEvolution-*', 'mnuFile;mnuWorkOnline') == 1:
					print 'Work Offline in the File menu works fine'
					log('Work offline verified','info')
					selectmenuitem('frmEvolution-*','mnuFile;mnuWorkOnline')
				else:
					print 'Unable to see the work online in the file menu after selecting woek offline'
					log('Unable to see the work online in the file menu after selecting woek offline','cause')
			else:
				print 'Unable to select the work offline item in the file menu'
				log('Unable to select the work offline item in the file menu','cause')
		else:
			print 'Already working offline/ evolution-mail is not opened'
			log('Already working offline/ evolution-mail is not opened','cause')
		#undoremap('evolution','frmEvolution-Mail')
		log('Work Offline','testend')
	except:
		log('Unable to go offline','error')
		log('Work Offline','testend')		
		#undoremap('evolution','frmEvolution-Mail')
		raise LdtpExecutionError (0)
		
work_offline()
