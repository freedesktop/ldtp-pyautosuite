#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Description:
#  This set of test scripts will test the LDTP framework for correct
#  functioning of its APIs. This is a Regression Suite.
#
#  Author:
#     Prashanth Mohan  <prashmohan@gmail.com>
#
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

from regression import *
import random, os

try:
    check_open('gedit')
except:
    raise

data_object     = LdtpDataFileParser (datafilename)
text            = data_object.gettagvalue ('text')
insert_text     = data_object.gettagvalue ('inserttext')
insert_pos      = data_object.gettagvalue ('insertpos')
cut_start       = data_object.gettagvalue ('cutstart')
cut_stop        = data_object.gettagvalue ('cutstop')
delete_start    = data_object.gettagvalue ('deletestart')
delete_stop     = data_object.gettagvalue ('deletestop')

if text == []:
    text = 'This is the default text for the LDTP Regression Suite'
else:
    text = text[0]

if insert_text == []:
    insert_text = text
else:
    insert_text = insert_text[0]
if insert_pos == []:
    insert_pos = 0
else:
    insert_pos = int(insert_pos[0])
if cut_start == []:
    cut_start = 0
else:
    cut_start = int(cut_start[0])
    
try:
    check_open('gedit')
except:
    raise

log ('settextvalue','teststart')
try:
    if settextvalue ('*gedit','txt0',text) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))

    if verifysettext ('*gedit','txt0',text) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('settextvalue')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('settextvalue')


log ('gettextvalue','teststart')
try:
    present_text = gettextvalue ('*gedit','txt0')
    if present_text != text:
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('gettextvalue')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('gettextvalue')


log ('verifysettext','teststart')
try:
    present_text = gettextvalue ('*gedit','txt0')
    if verifysettext ('*gedit','txt0',present_text) != 1:
        log ('Text present but says not present','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if verifysettext ('*gedit','txt0',present_text+'123') != 0:
        log ('Text not present but says present','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if verifysettext ('*gedit','txt0',present_text[:-1]) != 0:
        log ('Text not present but says present','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    # http://bugzilla.gnome.org/show_bug.cgi?id=351227    
#     if verifysettext ('*gedit','txt0','') != 0 and present_text != '':
#         log ('Text not present but says present','cause')
#         raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('verifysettext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass('verifysettext')
    

log ('stateenabled','teststart')
try:
    if istextstateenabled ('*gedit','txt0') == 0:
        log ('State Disabled','info')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    else:
        log ('State Enabled','info')
except:
    testfail ('stateenbled')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('stateenbled')


log ('appendtext','teststart')
try:
    present_text = gettextvalue ('*gedit','txt0')
    if appendtext ('*gedit','txt0',text) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if gettextvalue ('*gedit','txt0') != present_text+text:
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('appendtext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('appendtext')


log ('getcharactercount','teststart')
try:
    present_text = gettextvalue ('*gedit','txt0')
    if getcharcount ('*gedit','txt0') != len(present_text):
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('getcharactercount')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('getcharactercount')


log ('getcursorposition','teststart')
try:
    if getcharcount ('*gedit','txt0') != getcursorposition ('*gedit','txt0'):
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('getcursorposition')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('getcursorposition')


if len (present_text) < insert_pos:
    new_text = present_text+insert_text
else:
    new_text = present_text[:insert_pos]+insert_text+present_text[insert_pos:]

log ('inserttext','teststart')
try:
    if inserttext ('*gedit', 'txt0', insert_pos, insert_text) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))

    if gettextvalue ('*gedit','txt0') != new_text:
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('inserttext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('inserttext')
    

log ('cuttext','teststart')
try:
    if cut_stop == []:
        cut_stop = getcharactercount ('*gedit','txt0')
    else:
        cut_stop = int(cut_stop[0])

    present_text = gettextvalue ('*gedit','txt0')
    length = getcharcount ('*gedit','txt0')

    if cut_stop < cut_start or cut_start > length or cut_stop > length:
        log ('Input not proper','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    new_text = present_text[:cut_start]+present_text[cut_stop:]
    cut_text = present_text[cut_start:cut_stop]

    if cuttext ('*gedit','txt0',cut_start, cut_stop) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if gettextvalue ('*gedit','txt0') != new_text:
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('cuttext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('cuttext')


log ('pastetext','teststart')
try:
    present_text = gettextvalue ('*gedit','txt0')
    new_text = present_text[:cut_start]+cut_text+present_text[cut_start:]

    if pastetext ('*gedit','txt0',cut_start) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if gettextvalue ('*gedit','txt0') != new_text:
        raise LdtpExecutionError (str (traceback.format_exc ()))

except:
    testfail ('pastetext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('pastetext')


log ('copytext','teststart')
try:
    length = getcharcount ('*gedit','txt0')
    if cut_stop < cut_start or cut_start > length:
        log ('Input not proper','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if cut_stop > length:
        cut_stop = length-1
        
    present_text = gettextvalue ('*gedit','txt0')
    copy_text = present_text[cut_start:cut_stop]
    
    if copytext ('*gedit','txt0',cut_start, cut_stop) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if gettextvalue ('*gedit','txt0') != present_text:
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('copytext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('copytext')


log ('pastetext','teststart')
try:
    present_text = gettextvalue ('*gedit','txt0')
    new_text = present_text[:cut_start]+copy_text+present_text[cut_start:]

    if pastetext ('*gedit','txt0',cut_start) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if gettextvalue ('*gedit','txt0') != new_text:
        raise LdtpExecutionError (str (traceback.format_exc ()))

except:
    testfail ('pastetext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('pastetext')


log ('deletetext','teststart')
try:
    length = getcharcount ('*gedit','txt0')
    present_text = gettextvalue ('*gedit','txt0')
    if delete_start == []:
        delete_start = 0
    else:
        delete_start = int (delete_start[0])
    if delete_stop == []:
        if delete_start+1 <= length:
            log ('Not enough text on screen','cause')
            raise LdtpExecutionError (str (traceback.format_exc ()))
        delete_stop = delete_start + 1
    else:
        delete_stop = int (delete_stop[0])
        
    if delete_stop < delete_start  or delete_start > length or delete_stop > length:
        log ('Input not proper','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
        
    new_text = present_text[:delete_start]+present_text[delete_stop:]

    if deletetext ('*gedit','txt0',delete_start, delete_stop) == 0:
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if gettextvalue ('*gedit','txt0') != new_text:
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('deletetext')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('deletetext')


log ('cursorposition','teststart') #tests for getcursorposition and setcursorposition
try:
    length = getcharcount ('*gedit','txt0')
    setcursorposition ('*gedit','txt0',0)
    if getcursorposition ('*gedit','txt0') != 0:
        log ('Unable to Set Cursor position to 0','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if length == 0:
        val = 0
    else:
        val = length - 1
    setcursorposition ('*gedit','txt0',val)
    if getcursorposition ('*gedit','txt0') != val:
        log ('Unable to Set Cursor position to end of sentence','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    val = length/2
    setcursorposition ('*gedit','txt0',val)
    if getcursorposition ('*gedit','txt0') != val:
        log ('Unable to Set Cursor position to middle of sentence','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('cursorposition')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('cursorposition')


log ('verifypartialmatch','teststart')
try:
    present_text = gettextvalue ('*gedit','txt0')
    length = len (present_text)
    middle = random.randint (0,length-1)
    if verifypartialmatch ('*gedit','txt0',
                           present_text[middle:random.randint (middle, length-1)]) != 1:
        log ('Does not do correct matching','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if verifypartialmatch ('*gedit','txt0',text+'123') != 0:
        log ('Does not check for overflow','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if verifypartialmatch ('*gedit','txt0','123'+text) != 0:
        log ('Does not check for overflow','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('cursorposition')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('cursorposition')


log ('selecttextbyname','teststart')
try:
    selecttextbyname ('*gedit','txt0')
    ## FIXME :: Find a way to verify this!!!
    setcursorposition ('*gedit','txt0',0)
except:
    testfail ('selecttextbyname')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('selecttextbyname')
    

## FIXME :: Add test for text properties -- gettextproperty and comparetextproperty
# try:
#     close_gedit()
# except:
#     raise
