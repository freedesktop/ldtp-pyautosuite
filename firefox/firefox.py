#!/usr/bin/python
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
import string, sys, os, commands, time, filecmp

appmap_path = ''
default_dir = os.getcwd ()
default_image_dir = default_dir + '/images'
default_doc_dir = default_dir + '/doc'
default_tmp_dir = default_dir + '/tmp'
firefox_exe_path = '/home/ldtp/firefox/firefox'

log ('Firefox Test Report', 'begin')

if len (sys.argv) == 1:
  if os.access ('./mozilla.map', os.F_OK | os.R_OK) == 0:
    log ('Appmap path missing', 'error')
    log ('Firefox Test Report', 'end')
    sys.exit (0)
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/mozilla.map')

if os.access (default_tmp_dir, os.F_OK | os.R_OK | os.W_OK | os.X_OK) == 0:
  os.mkdir (default_tmp_dir)

try:
  execfile ('launch.py')
except LdtpExecutionError:
  log ('Unable to launch firefox', 'error')
  log ('Firefox Test Report', 'end')
  sys.exit (0)

# On my laptop it tooks at-least 5 seconds to load Firefox
time.sleep (15)

try:
  execfile ('default-browser-check.py')
except LdtpExecutionError:
  log ('Loaded default browser / browser window does not exist')

try:
  execfile ('throbber-icon.py')
except LdtpExecutionError:
  print 'Throbber icon action failed'

try:
   execfile ('browse-url.py')
except LdtpExecutionError:
   print 'Browse URL execution failed'

#try:
#  execfile("page-setup.py")
#except LdtpExecutionError:
#  print 'Page setup execution failed'


execfile ('search.py')

execfile ('page-load-control.py')

execfile ('security.py')

execfile ('home-page.py')

execfile ('exit-browser.py')

log ('Firefox Test Report', 'end')
