#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Nagashree M <mnagashree@novell.com>
#     S Vishnu Kumar <vishnukumar.sarvade@gmail.com>
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
#  Pre-conditions create a tar named file-roller.tar.gz and save it under HOME directory

from ldtp import *
from ldtputils import *
import string, sys, os, commands, time, filecmp

appmap_path = ''

if len (sys.argv) == 1:
  if os.access ('./file-roller.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/file-roller.map')
launchapp ('file-roller')

#To add the initial XML info to the log script
log ('File-Roller Suite',"begin")

#To create a new archive
log ('Create New Archive', 'teststart')
execfile ('create-archive.py')
log ('Create New Archive', 'testend')

#To open an existing archive and extracing them.
log ('Open Extract Archive ', 'teststart')
execfile ('open-extract.py')
log ('Open Extract Archive', 'testend')

#To delete a file from the archive.
log ('Delete-file', 'teststart')
execfile ('delete-file.py')
log ('Delete-file', 'testend')

#To add a file to a archive
log ('Add-file', 'teststart')
execfile ('add-file.py')
log ('Add-file', 'testend')

#To view file with out extracing 
log ('View-file', 'teststart')
execfile ('view-file.py')
log ('View-file', 'testend')

#To move an archive from one location to other 
#log ('Copy-archive', 'teststart')
#execfile ('copy-archive.py')  Currently this has bug in file roller
#log ('Copy-file', 'testend')

#To rename an existing archive
log ('Rename-archive', 'teststart')
execfile ('rename-archive.py')
log ('Rename-archive', 'testend')

#To move an archive from one location to other
log ('Move-archive', 'teststart')
execfile ('move-archive.py')
log ('Move-archive', 'testend')

log ('File-rollerSuite','end')
