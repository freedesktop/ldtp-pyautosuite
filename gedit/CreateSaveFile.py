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

import os

try:
    obj = LdtpDataFileParser (datafilename)
    fname = obj.gettagvalue ('newfile')[0]
    new_text = 'LDTP Testing'
    log ('Gedit-create-file', 'teststart')
    launchapp ('gedit',  1)
    waittillguiexist ('*gedit')
    selectmenuitem ('*gedit', 'mnuFile;mnuNew')
    default_dir = os.getcwd ()
    if selecttabindex ('*gedit', 'ptl1', getrowcount ('*gedit', 'tbl*') - 1) == 1:
            log ('New, unsaved document exists', 'info')
            #insert some txt into the now opened tab
            settextvalue ('*gedit',
            'txt' + str (getrowcount ('*gedit', 'tbl0')-1), 
            new_text)
            log ('Inserted some text', 'info')
            selectmenuitem ('*gedit', 'mnuFile;mnuSaveAs')
            if waittillguiexist ('dlgSaveAs...') == 0:
                log ('Save as dialog does not appear', 'error')
                raise LdtpExecutionError (0);
            else:
                settextvalue ('dlgSaveAs...', 'txtName', default_dir + '/' + fname)
                click ('dlgSaveAs...', 'btnSave')
		time.sleep (2)
		if guiexist ('dlgQuestion') == 1:
			log ('File already exists.. Replacing', 'warning')
			log ('Change file name in gedit-data.xml to prevent this', 'info')
			click ('dlgQuestion', 'btnReplace')
			waittillguinotexist ('dlgQuestion')
                time.sleep (5)
    if guiexist ('dlgSaveAs...') == 0:
        log ('File Saved', 'info')
    else:
        raise LdtpExecutionError (0)
    selectmenuitem ('*gedit', 'mnuDocuments;mnuCloseAll')
    log ('Checking if file was created', 'info')
    f = open (default_dir + '/' + fname,  'r')
    a = f.read ()
    print 'Junk ', a, a.find (new_text)
    if a.find (new_text) >= 0:
        log ('File was created, containing entered text', 'info')
    else:
        log ('File was not created or has invalid data', 'error')
        raise LdtpExecutionError (0)
    selectmenuitem ('*gedit', 'mnuFile;mnuQuit')
except LdtpExecutionError, msg:
    log ('Gedit-create-file failed', 'error')
    raise LdtpExecutionError (str (msg))
log ('Gedit-create-file', 'testend')

