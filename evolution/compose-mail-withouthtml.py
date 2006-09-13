#!/usr/bin/env python
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
from evoutils.mail import *
from evoutils.composemail import *
from evoutils.mailpreferences import *


def send_HTML_to_HTMLrecepient(datafilename):
    log ('Send HTML mail to a recepient who wants HTML mails','teststart')
    try:
        to, subject, body, cc, attachment, sentitemsfolder, refimg = read_maildata (datafilename)
        if get_HTML_pref(to[0])==1:
            composemail (to, subject, body, cc, attachment, sentitemsfolder, refimg,['HTML'])
        else:
            log ('User does not want HTML mail','cause')
            raise LdtpExecutionError(0)
    except:
        log ('Sending HTML mail to HTML recepient failed','error')
        log ('Send HTML mail to a recepient who wants HTML mails','testend')
        raise LdtpExecutionError(0)
    log ('Send HTML mail to a recepient who wants HTML mails','testend')


def send_HTML_to_NonHTMLrecepient(datafilename):
    log ('Send HTML mail to a recepient who does not want HTML mails','teststart')
    try:
        to, subject, body, cc, attachment, sentitemsfolder, refimg = read_maildata (datafilename)
        if get_HTML_pref(to[0])==0:
            composemail (to, subject, body, cc, attachment, sentitemsfolder, refimg,['HTML'])
        else:
            log ('User wants HTML mail','cause')
            raise LdtpExecutionError(0)
    except:
        log ('Sending HTML mail to NonHTML recepient failed','error')
        log ('Send HTML mail to a recepient who does not want HTML mails','testend')
        raise LdtpExecutionError(0)
    log ('Send HTML mail to a recepient who does not want HTML mails','testend')

def send_plaintext(datafile):
    log ('Send Plain Text Mail','teststart')
    try:
        to, subject, body, cc, attachment, sentitemsfolder, refimg = read_maildata (datafilename)
        composemail (to, subject, body, cc, attachment, sentitemsfolder, refimg,['Plain Text'])
    except:
        log ('Could not send plain text mail','error')
        log ('Send Plain Text Mail','testend')
        raise LdtpExecutionError (0)
    log ('Send Plain Text Mail','testend')
