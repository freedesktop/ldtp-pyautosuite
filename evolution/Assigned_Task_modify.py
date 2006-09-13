#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
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
# This script will create a new task.

from ldtp import *
from ldtputils import *
from task import *
from meeting import addattendees
def getrowindex(subject):
   try:
       noofchild=getrowcount ('frmEvolution-Tasks','tblTasks')
       for ind in range (noofchild):
           if getcellvalue('frmEvolution-Tasks','tblTasks',ind,2) == subject:
               return ind
       if ind == noofchild-1:
           log ('Message not present','cause')
           raise LdtpExecutionError (0)
   except:
       log ('Unable to get index of message','error')
       raise LdtpExecutionError (0)

def modify_task():
   """ Routine to modify a task """ 	
   
   # read the row index from the user and delete that particular task.
   try:
      log('Modify an assigned task','teststart')
      Group, Summary, Desc, Start_date, Start_time, \
             End_date, End_time, Time_zone, Categories, \
             addr_book, attendee, email = read_assignedtask_data (datafilename)

      selectrow ('frmEvolution-Tasks', 'tblTasks', Summary[0])
      selectmenuitem('frmEvolution-Tasks', 'mnuFile;mnuOpenTask')
      waittillguiexist('frmAssignedTask-*')
      window_id = 'frmAssignedTask-*'
      log('The window opened' ,'info')
   except:
      log('modify an assigned task','fail')
      log('Modify an assigned task','testend')
      raise LdtpExecutionError(0)
   
   # Modifies the task according to users wish.
   try:
      fill_task (Group, Summary, Desc, Start_date, Start_time,
                 End_date, End_time, Time_zone, Categories,
                 window_id)
      print 'Filled in the details'
      time.sleep(2)
      addattendees (attendee, email, addr_book, window_id)
      time.sleep(2)
      log('User data Loaded','info')
      
      if stateenabled (window_id,'btnSave')==1:
         click(window_id,'btnSave')
         log('The required task list has been modified','info')
      else:
         log('The Task is not modified because of no change in summary','info')
         click(window_id,'btnClose')
      time.sleep(2)
         
      if guiexist('dlgEvolutionQuery'):
         click('dlgEvolutionQuery','btnDonotSend')
         log('Task has been modified successfully','info')
         print 'The Assigned task has been modifed'

      if selectrow('frmEvolution-Tasks','tblTasks',Summary[0]) == 1:
         verify_task (Group, Summary, Desc, Start_date, Start_time,
                      End_date,End_time, Time_zone, Categories, window_id)
         click (window_id,'btnClose')
      else:
         click (window_id,'btnClose')
         raise LdtpExecutionError (0)
   except:
      log('Unable to load the user data','error')
      log('modify an assigned task','fail')
      log('Modify an assigned task','testend')
      raise LdtpExecutionError(0)
   log('modify an assigned task','pass')
   log('modify an assigned task','testend')
   
#    #Change the Progress of the task.
#    try:
      
#       Row_no = getrowindex(Summary[0])
#       if Progress[0] == 'complete':
#          checkrow ('frmEvolution-Tasks', 'tblTaskTable', Row_no, 1)
#       elif Progress[0] == 'Not started':
#          uncheckrow ('frmEvolution-Tasks', 'tblTaskTable', Row_no, 1)
#          log('progress of the task has been modified','info')
#          print 'The Progress has been modified'
#    except:
#       log('unable to change the progress of the task','error')
#       log('Modify an assigned task','testend')
#       #undoremap('evolution','frmEvolution-Tasks')
#       raise LdtpExecutionError(0)
   


modify_task()














