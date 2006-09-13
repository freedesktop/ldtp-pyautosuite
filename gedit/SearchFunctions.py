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
yellow = '65535,65535,30840'
def srh(srhfor):
    try:
        log('Testing Search','info')
        
         #highlight color used by gedit
        c = getcharcount('*gedit','txt0')
        
        i = 0
        l= len(srhfor)
        print srhfor
        while i < c - l :
            if gettextvalue('*gedit','txt0',i,i+l) == srhfor:
                break
            i = i + 1
        selectmenuitem('*gedit','mnuSearch;mnuFind')
        time.sleep(3)
        if guiexist('dlgFind') == 1:
            uncheck('dlgFind','chkMatchcase')
            uncheck('dlgFind','chkMatchentire*')
            uncheck('dlgFind','chkSearchback*')

            settextvalue('dlgFind','txt1',srhfor)
            click('dlgFind','btnFind')
            time.sleep(2)
            click('dlgFind','btnClose')
            time.sleep(2)
            if gettextproperty('*gedit','txt0',i,i+l) == "bg-color:" + yellow:
                log('Search term ' + srhfor + ' highlighted','info')
            else:
                log('Search term not highlighted','error')
                raise LdtpExecutionError(0)
        else:
            log('Find dialog does not appear','error')
            raise LdtpExecutionError(0)
    except:
        log('Search failed','error')
        raise LdtpExecutionError(0)
        return
    log('Search test success','info')

def srh_dialog_options(srhfor):
    try:
        log('Testing search with options ..')
	selectmenuitem('*gedit','mnuSearch;mnuClearHighlight')
	time.sleep(2)
        selectmenuitem('*gedit','mnuSearch;mnuFind')
        time.sleep(3)
        i = l = flag = 0
        if guiexist('dlgFind') == 1:
            check('dlgFind','chkMatchcase')
            settextvalue('dlgFind','txt1',srhfor.upper())
	    time.sleep(2)
            click('dlgFind','btnFind')
	    remap('*gedit','dlgFind')
	    a=getstatusbartext('*gedit','stat*')
            if a == "Phrase not found":
                log('Search term not highlighted','info')
                log('Match case option works','info')
            else:
                log('Match case option not working','info')
                raise LdtpExecutionError(0)

	    uncheck('dlgFind','chkMatchcase')
            check('dlgFind','chkMatchentire*')
	    settextvalue('dlgFind','txt1',srhfor)
	    click('dlgFind','btnFind')
	    time.sleep(2)
            str = gettextvalue('*gedit','txt0')
            a = str.split()
            while i < len(a):
                if a[i] == srhfor:
                    if gettextproperty('*gedit','txt0',l+1,
                    l+len(srhfor)) == "bg-color:" + yellow:  
                        flag = 1
                    else:
                        flag = 0
                        break
		l = l + len(a[i])
                i = i + 1
            if flag == 1:
                log('Only whole words have been highlighted','info')
            else:
                log('Match whole words does not work','error')
                raise LdtpExecutionError(0)
            uncheck('dlgFind','chkMatchentire*')
            click('dlgFind','btnClose')
	    waittillguinotexist('dlgFind')
        else:
            log('Find dialog does not appear','error')
            raise LdtpExecutionError(0)
        
    except:
        log('Testing of search options failed','error')
        raise LdtpExecutionError(0)
        return

def srh_repl(srhfor,replwith):
    try:
        log('Testing Search-Replace','info')
        selectmenuitem('*gedit','mnuSearch;mnuReplace')
        time.sleep(3)
        if guiexist('dlgReplace') == 1:
            settextvalue('dlgReplace','txt1',srhfor)
            settextvalue('dlgReplace','txt0',replwith)
            click('dlgReplace','btnFind')
            time.sleep(2)
            click('dlgReplace','btnReplaceAll')
            time.sleep(2)
            #after replacing, we attempt to find the old text again;
            #we expect a "Phrase not found" in the status bar
            click('dlg*','btnFind')
            a=getstatusbartext('*gedit','stat*')
            click('dlg*','btnClose')
            if a == "Phrase not found":
                log('Search and Replace success','info')
            elif a == None:
                log('Replace failed','error')
                raise LdtpExecutionError(0) 
        else:
            log('Replace dialog does not appear','error')
            raise LdtpExectutionError(0)
    except:
        log('Search-Replace failed','error')
        raise LdtpExecutionError(0)
        return


try:
    log('Search-dialog-test','teststart')
    obj = LdtpDataFileParser(datafilename)
    text = obj.gettagvalue('text')[0]
    srhfor = obj.gettagvalue('srhfor')[0]
    replwith = obj.gettagvalue('replwith')[0]
    launchapp('gedit',1)
    waittillguiexist('*gedit')
    settextvalue('*gedit','txt0',text)
    srh(srhfor)
    srh_dialog_options(srhfor)
    srh_repl(srhfor,replwith)
except:
    log('Search-dialog-test failed','error')
    raise LdtpExecutionError(0)
selectmenuitem('*gedit','mnuFile;mnuQuit')
waittillguiexist('dlgQuestion')
click('dlgQuestion','btnClosewithoutSaving')
log('Search-dialog-test','testend')
