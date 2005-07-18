#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bhargavi   <kbhargavi_83@yahoo.co.in>
#     Premkumarr <jpremkumar@novell.com>
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


#To compose a new mail message through File menu
def compose_mail ( to, subject, body, cc=''):
    try:
        selectmenuitem ('evolution', 'mnuTools;mnuMail')
        time.sleep(3)
        selectmenuitem ('evolution', 'mnuFile;mnuFileNew;mnuMailMessage')
        time.sleep(3)
        if guiexist ('Composeamessage') == 0:
            log('Compose message window does not appear','error')
            raise LdtpExecutionError (0)
        else:
            populate_mail_header (to, subject, body, cc)
            click ('Composeamessage', 'btnSend')
            time.sleep(3)
            if guiexist ('Composeamessage') == 1:
                log ('Failed during clicking the send button','error')
                raise LdtpExecutionError (0)
            else:
                releasecontext();
                click ('evolution', 'btnSend/Receive')
                log ('Composeamessage', 'Pass')
    except ldtp.error, msg:
        print 'Compose new message failed ', str (msg)
        log ('Compose new message failed', 'Fail' );

#Reading Input from File
file = open('compose-mail.dat','r')
record = file.readlines();
to = record[0].strip()
cc = record[1].strip()
subject = record[2].strip()
body = record[3].strip()

log ('Compose new message','Start')
time.sleep(3)
compose_mail (to,subject,body,cc)
time.sleep(3)
log ('Compose new message','end')
log ('Compose new message Verification','Start')
time.sleep(3)
verifymailwithimage ('Sent Items',-9,'composemail_refimage.png')
time.sleep(3)
log ('Compose new message Verification','end')