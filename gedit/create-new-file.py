#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Aishoo Team, Fasila
#     A. Nagappan <anagappan@novell.com>
#     J. Premkumar <jpremkumar@novell.com>
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

# Create a new document and save it
from ldtp import *
from ldtputils import *
import string, sys, commands, time, filecmp
import re, os

default_dir = os.getcwd ()
default_image_dir = default_dir + '/images'
default_doc_dir = default_dir + '/doc'
default_tmp_dir = default_dir + '/tmp'
gedit_exe_path = 'gedit'

if os.access (default_tmp_dir, os.F_OK | os.R_OK | os.W_OK | os.X_OK) == 0:
  os.mkdir (default_tmp_dir)

log ('Create New Document', 'teststart')

try:
    try:
        # Close all opened tab
        selectmenuitem ('*-gedit', 'mnuDocuments;mnuCloseAll')
    except error:
        log ('There maybe no documents opened', 'info')

    selectmenuitem ('*gedit', 'mnuFile;mnuNew')
    # TODO
    # - Verify new document window is opened
    # - Get text from pre-defined file maybe from default_doc_dir and use it in settextvalue function
    settextvalue ('*gedit', 'txt0', 'Testing gedit using GNU/Linux Desktop Testing Project')

    # TODO
    # - Verify text content placed properly
    selectmenuitem ('*gedit', 'mnuFile;mnuSaveAs')

    # Wait for 3 seconds, so that save as dialog window will appear
    time.sleep (3)

    # Check for dialog window
    if waittillguiexist ('dlgSaveAs...') == 1:
        settextvalue ('dlgSaveAs...', 'txtName', default_tmp_dir + '/sample.txt')
        click ('dlgSaveAs...', 'tbtnBrowseforotherfolders')
        selectrowindex ('dlgSaveAs...', 'tblShortcuts', 0)
        click ('dlgSaveAs...', 'btnSave')
        time.sleep (3)
        if guiexist ('*Question') == 1:
            click ('*Question', 'btnReplace')
        mo = re.match (os.path.expandvars ('$HOME'), default_tmp_dir)
        if str(mo) != "<type 'NoneType'>":
            newcontext = '~' + default_tmp_dir [mo.end():]
        else:
            newcontext = default_tmp_dir
        waittillguinotexist ('dlgQuestion')
        waittillguinotexist ('dlgSaveAs...')
        time.sleep (5)
        selectmenuitem ('*gedit', 'mnuDocuments;mnuCloseAll')
        # TODO
        # - Verify saved text file content using compare function
        log ('Create New Document', 'pass')
    else:
        log ('Save dialog does not appear', 'error')
        log ('Create New Document', 'fail')
except error, msg:
    log (str (msg), 'error')
    log ('Create New Document', 'fail')
    log ('Create New Document', 'testend')

log ('Create New Document', 'testend')
