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
# To open a new window.

from ldtp import *
from ldtputils import *

def open_new_window():

	try:
		log('open new window','teststart')
		if selectmenuitem('frmEvolution-Mail','mnuFile;mnuNewWindow') == 1:
			log('Selected new window in the menu','info')
		else:
			print 'Unable to select the menu item'
			log('Unable ot select the menu item','cause')
	except:
				
		print 'Unable to select the menu item'
		log('Unable ot select the menu item','cause')
		raise LdtpExecutionError (0)

open_new_window()
