#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Bhargavi  <kbhargavi_83@yahoo.co.in>
#     Premkumar <jpremkumar@novell.com>
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

#To check for autocompletion 
def test_autocompletion (first_name,full_name):
    try:
        selectmenuitem ('evolution', 'mnuTools;mnuMail')
        time.sleep(3)
        selectmenuitem ('evolution', 'mnuFile;mnuFileNew;mnuMailMessage')
        time.sleep(3)
        if guiexist ('Composeamessage') == 0:
            log('Compose message window does not appear','error')
            raise LdtpExecutionError (0)
        else:
            #FIXME: currently I am not taking care of the case when the
            #given first_name is not in address book. It can be done 
            #after the is_focuson method is implemented in text.c
            grabfocus ('Composeamessage','txtTo')
            typekey (first_name)
            time.sleep(3)
            #selecting the correct to address from the list of suggestions
            typekey ('<down>')
            typekey ('<return>')
            time.sleep(2)
            cur_to = gettextvalue ('Composeamessage','txtTo')
            print cur_to
            i = 2
            while cur_to != full_name:
                settextvalue ('Composeamessage','txtTo','')
                grabfocus ('Composeamessage','txtTo')
                typekey (first_name)
                time.sleep (2)
                for j in range(0,i):
                    typekey ('<down>')
                typekey ('<return>')
                if verifysettext ('Composeamessage','txtTo',cur_to) == 1:
                    break
                else:
                    cur_to = gettextvalue ('Composeamessage','txtTo')
                    i = i + 1
            if cur_to == first_name:
                print 'Autocompletion verification succeeded'
                log ('Autocompletion verification','pass')
            else:
                log ('Autocompletion verification succeeded but failed to find given To id',
                     'warning')
                log ('Autocompletion verification','pass')
                selectmenuitem ('Composeamessage','mnuFile;mnuClose')
                time.sleep(3)
                if guiexist ('Composeamessage') == 1:
                    log('Compose message window does not close','error')
                    raise LdtpExecutionError (0)
    except ldtp.error, msg:
        print 'Compose new message with autocompletion failed ', str (msg)
        log ('Compose new message with autocompletion failed', 'Fail' );

#Reading Input from File
file = open('autocompletion.dat','r')
record = file.readlines();
first_name = record[0].strip()
full_name = record[1].strip()
#to = record[2].strip()

log ('autocompletion verification','Start')
time.sleep(3)
test_autocompletion (first_name,full_name)
time.sleep(3)
log ('autocompletion verification','end')
