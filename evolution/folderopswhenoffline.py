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
from offline import *

try:
    try:
        data_object = LdtpDataFileParser (datafilename)
        delfolder = data_object.gettagvalue ('delfolder')
        location = data_object.gettagvalue ('location')
        from_folder = data_object.gettagvalue ('from_folder')
        to_folder = data_object.gettagvalue ('to_folder')
        crefolder = data_object.gettagvalue ('crefolder')
        oldfolder = data_object.gettagvalue ('oldfolder')
        newfolder = data_object.gettagvalue ('newfolder')
    except:
        log ('Error while reading values for folder tests','cause')
        raise LdtpExecutionError (0)
    try:
        go_offline ()
        selectMailPane ()
        create_folder_when_offline (crefolder[0],location[0])
        delete_folder_when_offline (delfolder[0])
        move_folder_when_offline (from_folder[0],to_folder[0])
        copy_folder_when_offline (from_folder[0],to_folder[0])
        rename_folder_when_offline (oldfolder[0],newfolder[0])
    except:
        log ('folder operations when offline test failed','error')
        raise LdtpExecutionError (0)
except:
    raise LdtpExecutionError (0)
