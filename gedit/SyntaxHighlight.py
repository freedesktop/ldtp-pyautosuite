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
def chk_lang(lang,keyw,notkeyw,type = 'Sources'):
    if selectmenuitem('*gedit','mnuView;mnuHighlightMode;mnu' 
    + type + ';mnu' + lang) == 1:
        settextvalue('*gedit','txt0',keyw)
        a = gettextproperty('*gedit','txt0',0,len(keyw) - 1)
        if a == None:
	    log('Keyword not highlighted','error')
            return -1
        else:
            settextvalue('*gedit','txt0',notkeyw)
            a = gettextproperty('*gedit','txt0',0,len(notkeyw) - 1)
            if a == None:
                return 0
            else:      #Non-keyword is also colored
                return -1
    else:
        return 1
try:
    log('Syntax-highlighting','teststart')
    launchapp('gedit',1)
    lst = ([])
    lang = {}
    keyw = {}
    nonkeyw = {}
    langtype = {}
    obj = LdtpDataFileParser(datafilename)
    lang[0] = obj.gettagvalue('lang0')[0]
    keyw[0] = obj.gettagvalue('keyw0')[0]
    nonkeyw[0] = obj.gettagvalue('nonkeyw0')[0]
    langtype[0] = obj.gettagvalue('langtype0')[0]

    lang[1] = obj.gettagvalue('lang1')[0]
    keyw[1] = obj.gettagvalue('keyw1')[0]
    nonkeyw[1] = obj.gettagvalue('nonkeyw1')[0]
    langtype[1] = obj.gettagvalue('langtype1')[0]
 
    lang[2] = obj.gettagvalue('lang2')[0]
    keyw[2] = obj.gettagvalue('keyw2')[0]
    nonkeyw[2] = obj.gettagvalue('nonkeyw2')[0]
    langtype[2] = obj.gettagvalue('langtype2')[0]
			    
    lst.append([lang[0],keyw[0],nonkeyw[0],langtype[0]])
    lst.append([lang[1],keyw[1],nonkeyw[1],langtype[1]])
    lst.append([lang[2],keyw[2],nonkeyw[2],langtype[2]])
    
    i = 0
    j = len(lst)
    while i < j :
        if len(lst[i]) < 4:
            a = chk_lang(lst[i][0],lst[i][1],lst[i][2])
        else:
            a = chk_lang(lst[i][0],lst[i][1],lst[i][2],lst[i][3])
        if a == -1:
            flag = 1
            log('Syntax highlighting failed','error')
            raise LdtpExecutionError(0)
        elif a == 0:
            flag = 0
	    i = i + 1
            continue
        else:
            log('The language does not exist in the menu','warning')
            log('Skipping menu item, continuing with next language','warning')
            continue
        if flag == 0:
            log('Syntax highlighting OK','info')
        i = i + 1
except:
    log('Syntax-highlighting test failed','error')
    raise LdtpExecutionError(0)
selectmenuitem('*gedit','mnuFile;mnuQuit')
waittillguiexist('dlgQuestion')
click('dlgQuestion','btnClosewithout*')
waittillguinotexist('*gedit')
log('Syntax-highlighting','testend')
