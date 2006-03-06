#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
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
# To Preview the message before printing.

from menu_reorganization import *
	
def print_preview(fldr, subject):

	try:
		log('Print preview','teststart')
		windowname = 'frmPrintPreview'
		if select_mail (fldr,subject) == 1:
			#remap('evolution','frmEvolution-Mail')
			selectmenuitem('frmEvolution-*','mnuFile;mnuPrintPreview')
			if waittillguiexist(windowname)	== 1:
				time.sleep(3)
				print 'Previewing message : '+fldr+' -> '+subject
				log('The print Preview window has emerged, hence verified','info')
				#remap('evolution',windowname)
				click(windowname,'btnclose')
				#undoremap('evolution',windowname)
			else:
				log('Unable to find the print preview window','cause')
				log('Print preview','testend')		
				#undoremap('evolution','frmEvolution-Mail')
		else:
			log('Unable to find the fldr/mail','cause')
			log('Print preview','testend')		
			#undoremap('evolution','frmEvolution-Mail')
		#undoremap('evolution','frmEvolution-Mail')
	except:
		log('Unable to preview the message','error')
		log('Print preview','testend')		
		#undoremap('evolution','frmEvolution-Mail')
		
	log('Print preview','testend')
# Read data from xml file.
data_object = LdtpDataFileParser (datafilename)
fldr = data_object.gettagvalue ('fldr')[0]
subject = data_object.gettagvalue ('subject')[0]

# Call the function

if fldr and subject:
	print_preview(fldr, subject)
else:
	if not (fldr):
		log ('fldr not provided in data xml file', 'error')
	if not (subject):
		log ('subject not provided in data xml file', 'error')
	log ('print preview', 'fail')
