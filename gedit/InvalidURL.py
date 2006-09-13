#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     N Srinivasan  <raiden.202@gmail.com>
#
#  Copyright 2004-2006 Novell, Inc.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#

from ldtp import *
from ldtputils import *
from os import system
try:
    log('Invalid-url-and-kill-test','teststart')
    launchapp('gedit',1)
    time.sleep(2)
    obj = LdtpDataFileParser(datafilename)
    url = obj.gettagvalue('invurl')[0]
    if guiexist('*gedit') == 1:
	print len(getobjectlist('*gedit'))
        selectmenuitem('*gedit','mnuFile;mnuOpenLocation')
        time.sleep(2)
        if guiexist('dlgOpenLocation') == 1:
            settextvalue('dlgOpenLocation','txt0',url)
            click('dlgOpenLocation','btnOpen')
            waittillguinotexist('dlgOpenLocation')
            time.sleep(25)
	    #To check, we use the fact that print button is disabled if document is not opened.
	    #If not it is enabled
	    
#	    remap('gedit','*gedit')	
#           a = getobjectlist('*gedit')
#	    print len(a)
#	    if a.index('lblCouldnotopenthefilehttp') >= 0:
#	    	log('Invalid URL not opened','info')
	    if stateenabled('*gedit','btnPrint') == 0:
		log('Invalid URL not opened','info')
        else:
            log('Open URL dialog not appearing','error')
            raise LdtpExecutionError(0)
        log('Killing gedit','info')
        system('pkill gedit')
        time.sleep(10)
#	reinitldtp()
        if guiexist('*gedit*') == 1: #Denotes hang.. crash NOT checked
        #Seems gedit's crash dialog is not accessibility enabled, 
	#so can't check..
            log('Gedit hung on kill','error')
            raise LdtpExecutionError(0)
        else:
            log('Gedit silently killed','info')
    else:
        log('Unable to open gedit','error')
        raise LdtpExecutionError(0)
except:
    log('Invalid-url-and-kill-test failed','error')
    raise LdtpExecutionError(0)
log('Invalid-url-and-kill-test','testend')                
