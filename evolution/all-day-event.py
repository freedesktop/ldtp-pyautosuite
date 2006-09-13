#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
#     Prashanth Mohan <prashmohan@gmail.com>
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

#To create an Appointment
from evoutils import *
from appointment import *

try:
    log ('Create Non Recursive All Day Event','teststart')
    selectCalendarPane ()
    windowname = 'frmAppointment-*'
    selectmenuitem ('frmEvolution-*', 'mnuFile;mnuNew;mnuAppointment')
    
    waittillguiexist (windowname) 
    if guiexist (windowname) == 0:
        log ('Failed to open new appointment window', 'cause')
        raise LdtpExecutionError (0)
    
    menucheck (windowname, 'mnuOptions;mnuAllDayEvent')
    
    create_appointment (datafilename, 'no')
except:
    log ('Create Non Recursive All Day Event','fail')
    log ('Create Non Recursive All Day Event','testend')
    raise LdtpExecutionError (0)
log ('Create Non Recursive All Day Event','pass')
log ('Create Non Recursive All Day Event','testend')    
