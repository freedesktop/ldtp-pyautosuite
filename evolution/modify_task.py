#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
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
# This script will modify a particular task.

from task import *


# The script begins here.
# Modifying the task , by doubleclicking the task in the table.
try:	
   log('Modify a task','teststart')
   selectTaskPane()
   Group, Summary, Desc, Start_date, Start_time, \
          End_date, End_time, Time_zone, \
          Categories = gettaskdata (datafilename)
   selectrow ('frmEvolution-Tasks', 'tblTasks', Summary[0])
   selectmenuitem('frmEvolution-Tasks', 'mnuFile;mnuOpenTask')
   time.sleep(2)
   waittillguiexist('frmTask-*')
except:
   log('Unable to open Task window','error')
   log('Modify a task','fail')
   log('Modify a task','testend')
   raise LdtpExecutionError(0)

# Modifies the task according to users wish.
try:
   fill_task (Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories)
   click('frmTask-*','btnSave')
   waittillguinotexist ('frmTask-*')
   selectrow ('frmEvolution-Tasks', 'tblTasks', Summary[0])
   selectmenuitem('frmEvolution-Tasks', 'mnuFile;mnuOpenTask')
   time.sleep(2)
   waittillguiexist('frmTask-*')
   verify_task (Group, Summary, Desc, Start_date,
                Start_time, End_date, End_time,
                Time_zone, Categories)
   click ('frmTask-*','btnClose')		
except:
   log ('Verification of Modified Task failed','cause')
   log('Modify a task','fail')
   log('Modify a task','testend')
   click ('frmTask-*','btnClose')		
   raise LdtpExecutionError(0)
log('Modify a task','pass')
log('Modify a task','testend')
