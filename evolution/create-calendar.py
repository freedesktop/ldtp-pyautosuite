#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Prem <jpremkumar@novell.com>
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
#To create a Calendar

#Reading inputs from file
file = open ('create-calendar.dat','r')
data = file.readlines ()
name = data[0].strip ()
url = data[1].strip ()
check1 = data[2].strip ()
check2 = data[3].strip ()
timecount = data[4].strip ()
timeunit = data[5].strip ()

#creation fo meeting
log ('Calendar Creation', 'teststart')
try:
    windowname = 'dlgNewCalendar'
    selectmenuitem ('evolution', 'mnuView;mnuWindow;mnuCalendars')
    time.sleep (2)
    selectmenuitem ('evolution', 'mnuFile;mnuFileNew;mnuCalendar')
    time.sleep (2)
    if guiexist (windowname) == 0:
        log ('Failed to open new calendar window', 'cause')
        raise LdtpExecutionError (0)
    else:
        if selectitem (windowname, 'cboOnThisComputer', 'On The Web') != 1:
            log ('Unable to select \'on the web\' item', 'error')
            raise LdtpExecutionError (0)
        if setandverify (windowname, 'txt1', name) == 0:
            log ('Unable to set calendar title', 'cause')
            raise LdtpExecutionError (0)
        else:
            if setandverify (windowname, 'txt0', url) == 0:
                log ('Unable to set url', 'cause')
                raise LdtpExecutionError (0)
            else:
                if check1 == '1':
                    if check (windowname, 'chkCopycalendarcontentslocallyforofflineoperation') != 1:
                        log ('Unable to mark check box: Copy calendar contents ...', 'error')
                if check2 == '1':
                    if check (windowname, 'chkMarkasdefaultfolder') != 1:
                        log ('Unable to mark check bos: Mark as default folder' ,'error')
                if timecount != '$':
                    if setvalue (windowname, 'sbtn0', timecount) != 1:
                        log ('Unable to set time of refreshing', 'error')
                if timeunit != '$':
                    if selectitem (windowname, 'cbominutes', timeunit) != 1:
                        log ('Unable to set combo box (refresh)', 'error')
                click (windowname, 'btnOK')
                time.sleep (2)
                log ('Ignore the follwoing error message, Because of guiexist usage', 'info')
                if guiexist (windowname) == 1:
                    log ('Failed to close new calendar dialog', 'error')
                    raise LdtpExecutionError (0)
                else:
                    log ('Calendar creation', 'Pass')
except error,msg:
    print 'Creation of Calendar failed' + str(msg)
    log ('Creation of Calendar failed', 'error')
    
log ('Calendar Creation', 'testend')
