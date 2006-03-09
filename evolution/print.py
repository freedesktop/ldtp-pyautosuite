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
# To print a message. 
# Note Actually it clicks the cancel btn instead of print button.

from ldtp import *
from ldtputils import *
from menu_reorganization import *
	
def print_msg(fldr, subject, printer):

	try:
		log('Print a message','teststart')
		windowname = 'dlgPrintMessage'
		if select_mail (fldr,subject) == 1:
			#remap('evolution','frmEvolution-Mail')
			selectmenuitem('frmEvolution-*','mnuFile;mnuPrint...')
                        #typekey ('<ctrl>p')
			if waittillguiexist(windowname)	== 1:
				time.sleep(3)
				if selectrow(windowname,'tbl0',printer): 
					print 'Printing message : '+fldr+' -> '+subject
					
					log('The print window has emerged, hence verified','info')
					#remap('evolution',windowname)
					time.sleep(3)
					click(windowname,'btnCancel')
#					click(windowname,'btnPrint')
					#undoremap('evolution',windowname)
				else:
					log('Unable to find the print window','cause')
					log('Print a message','testend')		
					#undoremap('evolution','frmEvolution-Mail')
					raise LdtpExecutionError (0)
			else:
				log('Unable to find the print window','cause')
				log('Print a message','testend')		
				#undoremap('evolution','frmEvolution-Mail')
				raise LdtpExecutionError (0)
		else:
			log('Unable to find the fldr/mail','cause')
			log('Print a message','testend')		
			#undoremap('evolution','frmEvolution-Mail')
			raise LdtpExecutionError (0)
		#undoremap('evolution','frmEvolution-Mail')
	except:
		log('Unable to print the message','error')
		log('Print a message','testend')		
		#undoremap('evolution','frmEvolution-Mail')
		raise LdtpExecutionError (0)
		
# Read data from xml file.
data_object = LdtpDataFileParser (datafilename)
fldr = data_object.gettagvalue ('fldr')[0]
subject = data_object.gettagvalue ('subject')[0]
printer = data_object.gettagvalue ('printer')[0]

# Call the function
if fldr and subject and printer:
	print_msg(fldr, subject, printer)
else:
	if not (fldr):
		log ('fldr not provided in data xml file', 'error')
	if not (subject):
		log ('subject not provided in data xml file', 'error')
	if not (printer):
		log ('printer not provided in data xml file', 'error')

	log ('print message', 'fail')

