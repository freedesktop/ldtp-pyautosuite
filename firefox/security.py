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
#  This script is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Library General Public License for more details.
# 
#  You should have received a copy of the GNU Library General Public
#  License along with this library; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#

def security_warning ():
    if guiexist('frmSecuritywarning') == 1:
	log ('Security warning window appeared', 'info')
	log ('Security warning window', 'pass')
	wait (5)
	reinitldtp()
	click('frmSecuritywarning', 'btnOk')
    else:
        log ('Security warning window does not appear', 'error')
        log ('Security Warning Window', 'fail')


log ('Security Windows', 'teststart')
try:
    settextvalue ('Mozilla', 'txtUrl', 'https://sf.net')
    click ('Mozilla', 'btnGo')
    # Wait for 10 seconds

    # TODO
    # - Wait till the window appears or till connection timed out
    # - Image comparison maybe implemented
    time.sleep (10)
    if guiexist ('SecurityError:DomainNameMismatch') == 1:
        log ('Security error window appeared', 'info')
        log ('Security error Window', 'pass')
	wait (5)
	reinitldtp()
	click ('SecurityError:DomainNameMismatch', 'btnOk')
    else:
        log ('Security error window does not appear', 'error')
        log ('Security error Window', 'fail')
	wait (5)
    wait (5)	
    security_warning()	
    wait (5)
#sometimes the security window comes up again
    if guiexist('frmSecuritywarning') == 1:
	security_warning()

#coming out of the secure web pages
    settextvalue ('mozilla', 'txtUrl', 'http://www.novell.com')
    click ('mozilla', 'btnGo')
	
    wait (10)
    if guiexist ('frmSecuritywarning') == 1:
	security_warning()
    	     
    
except error, msg:
    log (str(msg), 'error')


log ('Security Windows', 'testend')
