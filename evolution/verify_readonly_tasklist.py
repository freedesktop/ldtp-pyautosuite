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
# verify the Tasks in the server is readonly (while working offline)

from ldtp import *
from ldtputils import *

def read_data():
	#Initialising XML parser with data file
	data_object = LdtpDataFileParser (datafilename)
	
	#Extracting imput data from xml file
	summary = data_object.gettagvalue ('summary')[0]
	return summary

def verify_readonly():

	try:
		log('Verify readonly','teststart')
		summary = read_data()
		windowname = 'frmTask-*'
	        #remap('evolution','frmEvolution-Tasks')
		selectmenuitem('frmEvolution-Tasks','mnuFile;mnuWorkOffline')

		#selectrowpartialmatch ('frmEvolution-Tasks', 'tblTasks', summary)
		
                selectrow ('frmEvolution-Tasks', 'tblTasks', summary)
		selectmenuitem('frmEvolution-Tasks','mnuFile;mnuOpenTask')
		time.sleep(3)
		#setcontext('Task - No summary','Task - ' + summary)
		waittillguiexist(windowname)		
	        time.sleep(3)
                print 'here'
           	if settextvalue (windowname, 'txtDescription', summary+'.') == 0:
			print 'Verify Success'
			log('Verify Success','info')
		else:
			print 'Verify failed'
			log('Verify Failed','error')
		click(windowname,'btnClose')
		#undoremap('evolution','frmEvolution-Tasks')
	        #remap('evolution','frmEvolution-Tasks')
		selectmenuitem('frmEvolution-Tasks','mnuFile;mnuWorkOnline')
		#undoremap('evolution','frmEvolution-Tasks')
		time.sleep(3)
	except:
		print 'Unable to verify'
		log('Unable to verify','error')
		#undoremap('evolution','frmEvolution-Tasks')
	        #remap('evolution','frmEvolution-Tasks')
		selectmenuitem('frmEvolution-Tasks','mnuFile;mnuWorkOnline')
		log('verify readonly','testend')
		raise LdtpExecutionError (0)
	log('verify readonly','testend')

verify_readonly()
