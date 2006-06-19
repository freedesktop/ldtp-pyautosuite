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

# Click cancel in save as dialog box, after selecting a file

from ldtp import *
from ldtputils import *
import string, sys, os, commands, time, filecmp

default_dir = os.getcwd ()
default_image_dir = default_dir + '/images'
default_doc_dir = default_dir + '/doc'
default_tmp_dir = default_dir + '/tmp'
gedit_exe_path = 'gedit'

if os.access (default_tmp_dir, os.F_OK | os.R_OK | os.W_OK | os.X_OK) == 0:
  os.mkdir (default_tmp_dir)

log ('Click Cancel In Save As Dialog Box', 'teststart')
try:
    #setcontext ('Unsaved Document 1 - gedit', 'gedit')
    selectmenuitem ('*gedit', 'mnuFile;mnuOpen')

    # Wait for 3 seconds, let the open dialog box window appear
    #time.sleep (3)

    if waittillguiexist ('dlgOpenFiles...') == 1:
        # TODO
        try:
          time.sleep (1)
          selectrow ('dlgOpenFiles...', 'tblFiles', 'EXAMPLES')
          click ('dlgOpenFiles...', 'btnOpen')
        except LdtpExecutionError:
          None
        try:
          time.sleep (1)
          selectrow ('dlgOpenFiles...', 'tblFiles', 'gedit')
          click ('dlgOpenFiles...', 'btnOpen')
        except LdtpExecutionError:
          None
        try:
          time.sleep (1)
          selectrow ('dlgOpenFiles...', 'tblFiles', 'tmp')
          click ('dlgOpenFiles...', 'btnOpen')
        except LdtpExecutionError:
          None
        time.sleep (1)
        # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
        selectrow ('dlgOpenFiles...', 'tblFiles', 'sample.txt')
        # TODO
        # - Check if file does not exist
        click ('dlgOpenFiles...', 'btnOpen')

        if waittillguinotexist ('dlgOpenFiles...') == 0:
            log ('Open dialog box appears after opening file', 'error')
            log ('Click Cancel In Save As Dialog Box', 'fail')
        else:
            # TODO
            # Check if file opened successfully
            # Wait for 2 seconds, Let the file be loaded
            time.sleep (2)
            mo = re.match (os.path.expandvars ('$HOME'), default_tmp_dir)
            if str(mo) != "<type 'NoneType'>":
              newcontext = '~' + default_tmp_dir [mo.end():]
            else:
              newcontext = default_tmp_dir
            #releasecontext ()
            #setcontext ('Unsaved Document 1 - gedit', 'sample.txt ' + '(' + newcontext  + ') - gedit')
            selectmenuitem ('*gedit', 'mnuFile;mnuSaveAs')
            # Wait for 2 seconds, Let the file be loaded
            time.sleep (2)
            if guiexist ('dlgSaveAs...') == 1:
                # btncancel is not working (hanged) - comment by fasila
                click ('dlgSaveAs...', 'btnCancel')
                # Wait for 2 seconds, Let the file be loaded
                time.sleep (2)
                if waittillguinotexist ('dlgSaveAs...') == 1:
                    log ('Click Cancel In Save As Dialog Box', 'pass')
                else:
                    log ('Save As dialog box still appears', 'error')
                    log ('Click Cancel In Open Dialog Box', 'fail')
            else:
                log ('Save As dialog box does not appear', 'error')
                log ('Click Cancel In Save As Dialog Box', 'fail')
    else:
        log ('Open dialog box does not appear', 'error')
        log ('Click Cancel In Save As Dialog Box', 'fail')
    #releasecontext ()
    selectmenuitem ('*gedit','mnuFile;mnuQuit')
except error, msg:
    #releasecontext ()
    log (str (msg), 'error')
    log ('Click Cancel In Save As Dialog Box', 'fail')
log ('Click Cancel In Save As Dialog Box', 'testend')
