#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#       Prashanth Mohan <prashmohan at gmail dot com>
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


from dicti import *
import time

while guiexist ('*Dictionary'):
    selectmenuitem ('*Dictionary','mnuFile;mnuClose')
    time.sleep (2)

time.sleep (5)
gd = gnome_dictionary(datafilename)

try:
    log ('Find','teststart')
    gd.check_meaning ()
    gd.ordinary_find ()
    gd.find_next ()
    gd.find_prev ()
except:
    log ('Find','fail')
    log ('Find','testend')
    raise
log ('Find','pass')
log ('Find','testend')
