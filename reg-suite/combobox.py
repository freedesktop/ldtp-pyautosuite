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
import tempfile

try:
    check_open('gedit')
except:
    raise

data_object     = LdtpDataFileParser (datafilename)
value           = data_object.gettagvalue ('language')
text            = data_object.gettagvalue ('text')
if value == []:
    value = 'C'
else:
    value = value[0]
if text == []:
    text = 'test text'
else:
    text = text[0]
    
pref = '*Pref*'

log ('comboselect','teststart')
try:
    if guiexist (pref) == 0:
        open_pref()
    if selecttab (pref,'ptl0','Syntax Highlighting') != 1:
        log ('Unable to select tab','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if comboselect (pref,'cboHighlightmode',value) != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    verifyselect (pref,'cboHighlightmode', value)
except:
    testfail ('comboselect')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('comboselect')


log ('capturetofile','teststart')
try:
    file_name = tempfile.NamedTemporaryFile()
    if capturetofile (pref,'cboHighlightmode',file_name.name) != 1:
        log ('Undefined return Value','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    contents = file_name.file.read().split('\n')[:-1]
    for value in contents:
        comboselect (pref,'cboHighlightmode',value)
        #time.sleep (1)
        verifyselect (pref,'cboHighlightmode', value)
    click (pref,'btnClose')
    file_name.close ()
except:
    testfail ('capturetofile')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('capturetofile')
        

## http://bugzilla.gnome.org/show_bug.cgi?id=352149
log ('selectindex','teststart')
try:
    selectmenuitem ('*gedit','mnuSearch;mnuFind')
    index = 0
    file_name = tempfile.NamedTemporaryFile()
    waittillguiexist ('*Find')
    if capturetofile ('*Find','cboSearchfor',file_name.name) != 1:
        log ('Undefined return Value','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    contents = file_name.file.read().split('\n')
    for value in contents:
        if selectindex ('*Find', 'cboSearchfor', index) != 1:
            log ('Undefined return value','cause')
            raise LdtpExecutionError (str (traceback.format_exc ()))
        #time.sleep (1)
        verifyselect ('*Find', 'cboSearchfor', value)
except:
    testfail ('selectindex')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('selectindex')
        

log ('settextvalue on combobox','teststart')
try:
    if guiexist ('*Find') != 1:
        log ('Find window not open','cause')
        raise LdtpExecutionError ('Find window not open')
    if settextvalue ('*Find','cboSearchfor', text) != 1:
        log ('settextvalue failed','cause')
        raise LdtpExecutionError ('settextvalue failed')
    #time.sleep (0)
    verifyselect ('*Find', 'cboSearchfor', text)
except:
    testfail ('settextvalue on combobox')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('settextvalue on combobox')


log ('showlist','teststart')
try:
    if showlist ('*Find','cboSearchfor') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    #time.sleep (1)
    if verifyshowlist ('*Find','cboSearchfor') != 1:
        log ('List not being shown','cause')
        raise LdtpExecutionError ('List not being shown')
except:
    testfail ('showlist')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('showlist')


log ('hidelist','teststart')
try:
    if hidelist ('*Find','cboSearchfor') != 1:
        log ('Undefined return value','cause')
        raise LdtpExecutionError ('Undefined return value')
    #time.sleep (1)
    if verifyhidelist ('*Find','cboSearchfor') != 1:
        log ('List still being shown','cause')
        raise LdtpExecutionError ('List still being shown')
    click ('*Find','btnClose')
except:
    testfail ('hidelist')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('hidelist')
