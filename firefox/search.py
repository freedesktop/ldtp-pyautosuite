#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     S. Aginesh <sraginesh@novell.com>
#     A. Nagappan <anagappan@novell.com>
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

# search text in google

log ('testing the search text box', 'teststart')
status = 0
try:
	settextvalue ('mozilla', 'txtSearch', 'ldtp')
	status = verifysettext ('mozilla', 'txtSearch', 'ldtp')
	if status == 0:
		log ('Unable to set text in search text bar', 'fail')
except:
	log ('could not open Google search', 'fail')

try:
	# control + k will take the control to search tool bar
	# return will generate return key event
	typekey('<ctrl>k<return>')
except:
	log ('Unable to search', 'fail')

# - TODO
#   - Capture screen shot after search
#   - Do a comparison


		
