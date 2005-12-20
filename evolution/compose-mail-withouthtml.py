#!/usr/bin/env python

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
