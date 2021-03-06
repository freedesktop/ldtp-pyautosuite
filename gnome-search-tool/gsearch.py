#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bharani <pbk_1983@rediff.com>
#     Khasim Shaheed <sshaik@novell.com>
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

#!/usr/bin/python
                                                           
from ldtp import *
import string, sys, os
                                                           
appmap_path = ''
                                                           
if len (sys.argv) == 1:
  if os.access ('./gnome-search-tool.map', os.F_OK | os.R_OK) == 0:
    print 'Appmap path missing'
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]
                                                           
#Initialize Appmap
initappmap (appmap_path + '/gnome-search-tool.map')
                                                           
launchapp ('gnome-search-tool')

log ('Sanity Suite for gnome-search-tool', 'teststart')
execfile('simplesearch.py')
#execfile('browsefiles.py')
execfile('search_with_text.py')
log ('Sanity Suite for gnome-search-tool', 'testend')
