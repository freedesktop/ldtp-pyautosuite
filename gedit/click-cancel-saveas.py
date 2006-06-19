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

# Click cancel in open dialog box, after selecting a file
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


log ('Click Cancel In Open Dialog Box', 'teststart')
try:
    #setcontext ('Unsaved Document 1 - gedit', 'gedit')
    selectmenuitem ('*gedit', 'mnuFile;mnuOpen')

    # Wait for 3 seconds, let the open dialog box window appear
    time.sleep (3)

    if guiexist ('dlgOpenFiles...') == 1:
        # TODO
        # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
        click ('dlgOpenFiles...', 'btnCancel')
        time.sleep (2)
        if guiexist ('dlgOpenFiles...') == 0:
            log ('Click Cancel In Open Dialog Box', 'pass')
        else:
            log ('Open dialog box still appears', 'error')
            log ('Click Cancel In Open Dialog Box', 'fail')
    else:
        log ('Open dialog box does not appear', 'error')
        log ('Click Cancel In Open Dialog Box', 'fail')
except error, msg:
    log (str(msg), 'error')
    log ('Click Cancel In Open Dialog Box', 'fail')
log ('Click Cancel In Open Dialog Box', 'testend')
