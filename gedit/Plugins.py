#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     N Srinivasan  <raiden.202@gmail.com>
#
#  Copyright 2004-2006 Novell, Inc.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#

from ldtp import *
from ldtputils import *
import time

def clear_text():
    selectmenuitem('*gedit','mnuEdit;mnuSelectAll')
    time.sleep(1)
    selectmenuitem('*gedit','mnuEdit;mnuDelete')
    time.sleep(3)
def check(chars,words,lines):
    i = j = 0
#   time.sleep(5)
#   print "<DEBUG>"
    if guiexist('dlg*Statistics') == 1:
#	print "<DEBUG>"
#	time.sleep(2)
#	remap('dlg*Statistics')
        a = getobjectlist('*Statistics')
    else:
        return 0
    print "<DEBUG>"
    bytes = chars #Since we type only plain text
    if a.count('lbl' + str(lines)) > 0 and a.count('lbl' + 
    str(words)) > 0 and a.count('lbl' + 
    str(chars)) > 0 and a.count('lbl' + 
    str(chars - 1) + '1') and a.count('lbl' +
    str(bytes) + '2') > 0:
        return 1
    else:
        return 0

def select_plugin(name,flag):
    selectmenuitem('*gedit','mnuEdit;mnuPreferences')
    waittillguiexist('dlggedit*')
    selecttab('dlggedit*','ptl0','Plugins')
    ind = gettablerowindex('dlggedit*','tbl1',name)
    selectrowindex('dlggeditPreferences','tbl1',ind)
    checkrow('dlggeditPreferences','tbl1',ind)
    if flag == 1:
        click('dlggeditPreferences','btnClose')
        waittillguinotexist('dlggeditPreferences')
        return
    else:
        return

def test_stats():
    log('Testing document statistics plugin..','info')
    select_plugin('Document Statistics',1)
    settextvalue('*gedit','txt0','LDTP')
    if selectmenuitem('*gedit','mnuTools;mnu*Statistics') == 1:
        time.sleep(3)
        if guiexist('dlg*Statistics') == 1:
            log('Checking overall doc stats..','info')
            if check(len('LDTP'),1,1) == 0:
                log('Updating text..','info')
                appendtext('*gedit','txt0',' Testing')
                click('dlg*Statistics','btnUpdate')
                if check(len('LDTP Testing'),2,1) == 0:
                    log('Document statistics displayed correctly','info')
                    click('dlg*Statistics','btnClose')
                    return 0
                else:
                    log('Document statistics not updated','error')
                    log('Document statistics plugin test failed','error')
                    return 1
            else:
                log('Document statistics incorrect/not displayed','error')
                log('Document statistics plugin test failed','error')
                return 1
            return 0
        else:
            log('Statistics dialog does not appear','error')
            log('Document statistics plugin test failed','error')
            return 1
    else:
        log('Cannot find menu item','error')
        log('Document statistics plugin test failed','error')
        return 1

def test_username(user):
    log('Testing insert user name plugin','info')
    select_plugin('User name',1)
    if selectmenuitem('*gedit','mnuEdit;mnuInsertUserName') == 1:
        time.sleep(2)
        if gettextvalue('*gedit','txt0') == user + ' ':
            log('User name inserted','info')
            return 0
        else:
            log('User name not entered','error')
            log('Insert User name test failed','error')
            return 1

def test_date():
    log('Testing Insert Date/Time plugin','info')
    select_plugin('Insert Date/Time',0)
    selectrow('dlggeditPreferences','tbl1','Insert Date/Time')
    click('dlggeditPreferences','btnConfigurePlugin')
    waittillguiexist('dlgConfigure*')
    click('dlgConfigure*','rbtnUsetheselectedformat')
    date = time.strftime('%m/%d/%Y',time.localtime())
    selectrow('dlgConfigure*','tbl0',date)
    click('dlgConfigure*','btnOK')
    waittillguinotexist('dlgConfigure*')
    click('dlggeditPreferences','btnClose')
    waittillguinotexist('dlggeditPreferences')
    if selectmenuitem('*gedit','mnuEdit;mnuInsertDateandTime') == 1:
        time.sleep(2)
        if gettextvalue('*gedit','txt0') == date + ' ' :
            log('Date inserted correctly','info') 
            log('Checking with custom formatted date/time','info')
            clear_text()
            select_plugin('Insert Date/Time',0)
            selectrow('dlggeditPreferences','tbl1','Insert Date/Time')
            click('dlggeditPreferences','btnConfigurePlugin')
            waittillguiexist('dlgConfigure*')
            click('dlgConfigure*','rbtnPromptforaformat')
            click('dlgConfigure*','btnOK')
            waittillguinotexist('dlgConfigure*')
            click('dlggeditPreferences','btnClose')
            waittillguinotexist('dlggeditPreferences')
            selectmenuitem('*gedit','mnuEdit;mnuInsertDateandTime')
            time.sleep(3)
            if guiexist('dlgInsert*') == 1:
                log('Gedit prompts for date format','info')
                log('Inserting a custom formatted date..','info')
                click('dlgInsert*','rbtnUsecustom*')
                
                settextvalue('dlgInsert*','txt0','%d-%m-%Y %H:%M')
                click('dlgInsert*','btnInsert')
                waittillguinotexist('dlgInsert*')
                now = time.strftime('%d-%m-%Y %H:%M',time.localtime())
                if gettextvalue('*gedit','txt0') == now + ' ':
                    log('Custom formatted time inserted correctly','info')
                else:
                    log('Custom format time not inserted','error')
                    log('Insert date/time plugin test failed','error')
                    return 1
            else:
                log('Insert Date/time dialog not does not appear','error')
                log('Insert date/time plugin test failed','error')
                return 1
        else:
            log('Date not inserted','error')
            log('Insert date/time plugin test failed','error')
            return 1

def test_indent():
    log('Testing indent lines plugin..','info')
    select_plugin('Indent lines',1)
    settextvalue('*gedit','txt0','LDTP Linux Desktop Testing Project')
    selectmenuitem('*gedit','mnuEdit;mnuSelectAll')
    if selectmenuitem('*gedit','mnuEdit;mnuIndent') == 1:
    	time.sleep(2)
    	print "HHHHH" + gettextvalue('*gedit','txt0',0,1)
        if gettextvalue('*gedit','txt0',0,1) == '\t':
            log('Indentation success','info')
            if selectmenuitem('*gedit','mnuEdit;mnuUnindent') == 1:
                if gettextvalue('*gedit','txt0',0,1) != '\t':
                    log('Unindent success','info')
                    return 0
                else:
                    log('Unindent failed','error')
                    log('Indent lines plugin test failed','error')
                    return 1
        else:
            log('Indentation did not succeed','error')
            log('Indent lines plugin test failed','error')
            return 1

def test_taglines():
    log('Testing tag lines plugin..','info')
    select_plugin('Tag list',1)
    selectmenuitem('*gedit','mnuView;mnuSidePane')
    selecttab('*gedit','ptl0','Tags')
#    comboselect('*gedit','cboAvailableTagLists','HTML-Tags') 
    log('Selecting the <HTML> tag','info')
    selectrow('*gedit','tblAvailable*','HTML root element')
    doubleclickrow('*gedit','tblAvailable*','HTML root element')
    time.sleep(2)
    if gettextvalue('*gedit','txt0') == '<HTML>  </HTML>':
        log('Selected tag inserted correctly','info')
        return 0
    else:
        log('Tag not inserted','error')
        log('Tag lines plugin test failed','error')
        return 1
def foo(mnu,str):    
    selectmenuitem('*gedit','mnuEdit;mnuSelectAll')
    selectmenuitem('*gedit','mnuEdit;mnuChangeCase;' + mnu)
    time.sleep(2)
    if gettextvalue('*gedit','txt0') == str:
        selectmenuitem('*gedit','mnuEdit;mnuUndo')
        return 0
    else:
        return 1
    
def test_change_case():
    inp = 'LDTP Testing'
    log('Testing change case..','info')
    settextvalue('*gedit','txt0',inp)
    select_plugin('Change Case',1)
    up = 'mnuAllUppercase'
    lp = 'mnuAllLowercase'
    if doesmenuitemexist('*gedit',
    'mnuEdit;mnuChangeCase;' + up) == 1 and doesmenuitemexist('*gedit',
    'mnuEdit;mnuChangeCase;' + lp) == 1 and doesmenuitemexist('*gedit',
    'mnuEdit;mnuChangeCase;mnuInvertCase') == 1 and doesmenuitemexist('*gedit',
    'mnuEdit;mnuChangeCase;mnuTitleCase') == 1:
        log('Change case menu item exists with all options','info')
        if foo('mnuAllUppercase',inp.upper()) == 0:
            log('All Upper case OK','info')
        else:
            log('Menu All upper case not working','error')
            log('Change case test failed','error')
            return 1
        if foo('mnuAllLowercase',inp.lower()) == 0:
            log('All lower case OK','info')
        else:
            log('Menu All lower case not working','error')
            log('Change case test failed','error')
            return 1
        if foo('mnuInvertCase',inp.swapcase()) == 0:
            log('Invert Case OK','info')
        else:
            log('Menu invert case not working','error')
            log('Change case test failed','error')
            return 1
        if foo('mnuTitleCase',inp.title()) == 0:
            log('Title case OK','info')
            return 0
        else:
            log('Menu item title case not working','error')
            log('Change case test failed','error')
            return 1
    else:
        log('Menu item does not exist','error')
        return 1

try:
    log('Plugins-test','teststart')
    obj = LdtpDataFileParser(datafilename)
    user = obj.gettagvalue('usrname')[0]
#    user = 'Srinivasan N' 
    launchapp('gedit',1)
    waittillguiexist('*gedit')

    if test_stats() == 1:
        raise LdtpExecutionError(0)
    time.sleep(2)
    clear_text()

    if test_username(user) == 1:
        raise LdtpExecutionError(0)
    time.sleep(2)
    clear_text()
    
    if test_date() == 1:
        raise LdtpExecutionError(0)
    time.sleep(2)
    clear_text()
    
    if test_indent() == 1:
        raise LdtpExecutionError(0)
    time.sleep(2)
    clear_text()
    
    if test_taglines() == 1:
        raise LdtpExecutionError(0)
    time.sleep(2)
    clear_text()

    if test_change_case() == 1:
        raise LdtpExecutionError(0)
    
    selectmenuitem('*gedit','mnuFile;mnuQuit')
    waittillguiexist('dlgQuestion')
    click('dlgQuestion','btnClosewithout*')
    waittillguinotexist('*gedit')

except:
    log('Plugins-test failed','error')
    raise LdtpExecutionError(0)
log('Plugins-test','testend')
