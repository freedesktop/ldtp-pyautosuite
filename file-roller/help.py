#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Nagashree M <mnagashree@novell.com>
# 
#  Copyright 2004 Novell, Inc.
# 
#  This library is free software; you can redistribute it and/or
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
#  Help Menu

try:
	selectmenuitem ('FileRoller','mnuHelp;mnuAbout')
	click ('dlgAboutFileRoller','btnCredits')
	#click ('dlgCredits','btnClose')
	wait (3)
	selecttab ('dlgCredits','ptabWrittenby')
	wait (3)
	selecttab ('dlgCredits','ptabDocumentedby')
	wait (3)
	click ('dlgCredits','btnClose')
	wait (3)
	click ('dlgAboutFileRoller','btnClose')
	#selectmenuitem ('FileRoller','mnuHelp;mnuContents')
except error:
	log ('Viewing Help topics failed', 'fail')	
