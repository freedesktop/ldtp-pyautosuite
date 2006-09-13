#!/usr/bin/env python
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
# This script will create a new assigned task.

from ldtp import *
from ldtputils import *
from task import *
from meeting import *



def new_task():
   """ Routine to add a new task """ 	
   try:
      log('Create new assigned task','teststart')
      Group, Summary, Desc, Start_date, Start_time, \
             End_date, End_time, Time_zone, Categories, \
             addr_book, attendee, email = read_assignedtask_data (datafilename)
      window_id = 'frmAssignedTask-*' 
      
      selectmenuitem('frmEvolution-Tasks','mnuFile;mnuNew;mnuAssignedTask')
      waittillguiexist('frmAssignedTask-Nosummary')
      no_rows_b4creat = getrowcount ('frmEvolution-Tasks', 'tblTasks') 
      fill_task (Group, Summary, Desc, Start_date, Start_time,
                 End_date, End_time, Time_zone, Categories,
                 window_id)
      print 'Filled in the details'
      time.sleep(2)
      addattendees (attendee, email, addr_book, window_id)
      time.sleep(2)
      log('User data Loaded','info')

   except:
      log('Unable to enter the values','error')
      log('Create a new assigned task','fail')
      log('Create a new assigned task','testend')
      raise LdtpExecutionError(0)

   # Click Save and then exit.
   try:
      click(window_id,'btnSave')
      time.sleep(3)
      if guiexist('dlgEvolutionQuery') == 1:
         click('dlgEvolutionQuery','btnDonotSend')
         log('Assigned Task Creation Completed','info')
         print 'Task has been created'
   except:
      log('Unable to save the task', 'cause')
      log('Create a new assigned task','fail')
      log('Create a new assigned task','testend')
      raise LdtpExecutionError(0)

   try:
      no_rows_aftercreat = getrowcount ('frmEvolution-Tasks', 'tblTasks') 
      if no_rows_aftercreat == no_rows_b4creat + 1 \
         and selectrow('frmEvolution-Tasks','tblTasks',Summary[0]) == 1:
         
         verify_task (Group, Summary, Desc, Start_date, Start_time,
                      End_date,End_time, Time_zone, Categories, window_id)
         click (window_id,'btnClose')
      else:
         click (window_id,'btnClose')
         raise LdtpExecutionError (0)
   except:
      log ('Verification Failed','cause')
      log('Create a new assigned task','fail')
      log('Create a new assigned task','testend')
   log('Create a new assigned task','pass')
   log('Create a new assigned task','testend')

new_task()
