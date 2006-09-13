#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Prashanth Mohan  <prashmohan@gmail.com>
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

from ldtp import *
from ldtputils import *
from contact import *

def basicsearch(name):
    log ('searching for a name from the toolbar','teststart')
    try:
        #print name
        selectContactPane()

        if gettextvalue ('frmEvolution-Contacts','txtSearchTextEntry')!='':
            settextvalue ('frmEvolution-Contacts','txtSearchTextEntry','')
        settextvalue ('frmEvolution-Contacts','txtSearchTextEntry',name)
        settextvalue ('frmEvolution-Contacts','txtSearchTextEntry',name)
        time.sleep (2)
        click ('frmEvolution-Contacts','btnFindNow')
    except:
        log ('Error while searching through the Toolbar','error')
        log ('searching for a name from the toolbar','testend')
        raise LdtpExecutionError(0)
    log ('searching for a name from the toolbar','testend')
    
def verifybasicsearch (name):
    log ('Verifying Basic Search Results','teststart')
    try:
        selectpanel ('frmEvolution-Contacts','pnlcurrentaddressbookfolderhas1card',1)
        selectpanel ('frmEvolution-Contacts','pnlcurrentaddressbookfolderhas1card',1)
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        appendtext=titleappend(name)
        time.sleep (1)
        setcontext ('Contact Editor','Contact Editor -'+appendtext)
        waittillguiexist ('dlgContactEditor')
        if gettextvalue ('dlgContactEditor','txtFullName').find(name)==-1:
            raise LdtpExecutionError(0)
        click ('dlgContactEditor','btnCancel')
    except:
        log ('Basic Search did not provide correct results')
        log ('Verifying Basic Search Results','testend')
    log ('Verifying Basic Search Results','testend')

data_object = LdtpDataFileParser (datafilename)
Name=data_object.gettagvalue ('Name')
basicsearch (Name[0])
