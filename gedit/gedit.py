#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Aishoo, Fasila
#     A. Nagappan <anagappan@novell.com>
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

from ldtp import *
from ldtputils import *
import string, sys, os, commands, time, filecmp

appmap_path = ''
default_dir = os.getcwd ()
default_image_dir = default_dir + '/images'
default_doc_dir = default_dir + '/doc'
default_tmp_dir = default_dir + '/tmp'
gedit_exe_path = 'gedit'

startlog ('gedit-execution.xml', 1)

log ('Gedit Test Report', 'begin')

if len (sys.argv) == 1:
  if os.access ('./gedit.map', os.F_OK | os.R_OK) == 0:
    log ('Appmap path missing', 'error')
    log ('Gedit Test Report', 'end')
    stoplog ()
    sys.exit(0);
  else:
    appmap_path = '.'
else:
  appmap_path = sys.argv[1]

initappmap (appmap_path + '/gedit.map')

if os.access (default_tmp_dir, os.F_OK | os.R_OK | os.W_OK | os.X_OK) == 0:
  os.mkdir (default_tmp_dir)

try:
  execfile ('launch.py')
except LdtpExecutionError:
  log ('Unable to launch gedit', 'Error')
  log ('Gedit Test Report', 'end')
  stoplog ()
  sys.exit (0)

time.sleep (5)

#to create a new document and can be saved in gedit.
execfile ('gedit02.py')
#time.sleep (3)
#to open and edit an existing document in gedit.
execfile ('gedit03.py')
time.sleep (3)
#to cancel the operation 'open a file' after the operation was initiated. .
execfile ('gedit04.py')
time.sleep (3)
#to cancel the operation 'Save as' after the operation was initiated. .
execfile ('gedit05.py')
time.sleep (3)
#to print preview and print a document in gedit.
execfile ('gedit06.py')
log ('Gedit Test Report', 'end')
stoplog ()
sys.exit (0)
time.sleep (3)
#to close the currently opened document in gedit .
execfile ('gedit07.py')
time.sleep (3)
#to save all the currently open and modified documents in gedit even if one of those documents is a new document 
#execfile ('gedit08.py')
time.sleep (3)
#to close all the documents that are opened currently in gedit.
execfile ('gedit09.py')
time.sleep (3)
#to open a document from URL.
execfile ('gedit10.py')
sys.exit (0)
time.sleep (3)
#to cancel the operation 'Open a document from URL' after it was initiated.
execfile ('gedit11.py')
time.sleep (3)
#to revert to a saved version of a currently opened document.
execfile ('gedit12.py')
time.sleep (3)
#to 'undo' or 'redo' changes made to a document in gedit.
execfile ('gedit13.py')
time.sleep (3)
#to highlight the contents of the currently opened document.
execfile ('gedit14.py')
time.sleep (3)
# to copy and paste text in gedit.
execfile ('gedit15.py')
time.sleep (3)
#to cut and paste text in gedit.
execfile ('gedit16.py')
time.sleep (3)
# to do a search for any specified word/phrase in the currently opened document in gedit.
execfile ('gedit17.py')
time.sleep (3)
#to replace any word/phrase in the currently opened document with another word/phrase in gedit.
execfile ('gedit18.py')
time.sleep (3)
#to go to any line in the currently opened document..
execfile ('gedit19.py')
time.sleep (3)
#to view installed & uninstalled plugins in gedit.
execfile ('gedit20.py')
time.sleep (3)
#to view information about any currently available(installed or uninstalled ) plugins in gedit .
execfile ('gedit21.py')
time.sleep (3)

log ('Gedit Test Report', 'end')
