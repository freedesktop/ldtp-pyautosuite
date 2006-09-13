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
import os
def launch_app(fname):
    try:
	if os.path.exists(os.getcwd() + '/' + fname) == False:
		a = open(fname,'w')
		a.write('File 0')
		a.close()
        launchapp('nautilus ' + os.getcwd(),1)
        waittillguiexist('frm*FileBrowser')
        click('frm*FileBrowser','mnuViewasList') #ViewasList is a radio menu item
	time.sleep(3)
        selectrow('frm*FileBrowser','tblListView',fname)
        doubleclickrow('frm*FileBrowser','tblListView',fname)
    except:
        raise LdtpExecutionError(0)
    
def change(new_text):
    try:
        appendtext('*gedit',
        'txt' + str(getrowcount('*gedit','tbl0')-1),
        new_text)
        changed_count = len(new_text)
        return  changed_count
    except:
        raise LdtpExecutionError(0)

def revert(new_text,old_char_count):
    try:
        #change content and revert(gedit-08)  
        log('Gedit-revert','teststart')
        change(new_text)
        
        #revert..
        selectmenuitem('*gedit','mnuFile;mnuRevert')
        time.sleep(3)
        if guiexist('dlgQuestion') == 1:
            click('dlgQuestion','btnRevert')
        else:
            log('Revert confirmation does not appear','error')
            raise LdtpExecutionError(0)
        time.sleep(3)
        if getcharcount('*gedit',
        'txt' + str(getrowcount('*gedit','tbl0')-1)) == old_char_count :
            log('Successfully reverted','info')
        else:
                log('Revert failed','error')
                raise LdtpExecutionError(0)
    except:
        log('Gedit-revert failed','error')
        log('Gedit-revert','testend')
        raise LdtpExecutionError(0)
    log('Gedit-revert','testend')
    
def undo_redo(new_text,old_char_count): 
    #make 3 changes, undo all 3 one-by-one, then redo them one-by-one
    try:
        log('Test-undo-and-redo','teststart')
	time.sleep(3)
        i = count = 0
	selectmenuitem('*gedit','mnuEdit;mnuSelectAll')
	selectmenuitem('*gedit','mnuEdit;mnuCopy')
			  
        while i < 3:
	#making changes ..
	    setcursorposition('*gedit','txt0',getcharcount('*gedit','txt0'))
	    selectmenuitem('*gedit','mnuEdit;mnuPaste')
            time.sleep(2)
            if i == 0:
                count = (getcharcount('*gedit','txt0') - old_char_count)
            i = i + 1
        changed_count = old_char_count + (i * count)
        print i,count,changed_count
        while i > 0:
            changed_count = changed_count - count
            selectmenuitem('*gedit','mnuEdit;mnuUndo')
            if getcharcount('*gedit',
            'txt' + str(getrowcount('*gedit','tbl0')-1)) == changed_count:
                log('Undo success','info')
            else:
                log('Undo failed','error')
                raise LdtpExecutionError(0)
            i = i - 1
        time.sleep(3)
        while i < 3:
            changed_count = changed_count + count
            selectmenuitem('*gedit','mnuEdit;mnuRedo')
            if getcharcount('*gedit',
            'txt' + str(getrowcount('*gedit','tbl0')-1)) == changed_count:
                log('Redo success','info')
            else:
                log('Redo failed','error')
                raise LdtpExecutionError(0)
            i = i + 1
        selectmenuitem('*gedit','mnuFile;mnuRevert')
        time.sleep(3)
        click('dlgQuestion','btnRevert')
        time.sleep(5)
    except:
        log('Test-undo-and-redo-failed','error')
        log('Test-undo-and-redo','testend')
        raise LdtpExecutionError(0)
    log('Test-undo-and-redo','testend')

def save_existing(new_text,old_char_count):
    try:
        log('Gedit-edit-existing-file','teststart')
        #add some text and save (gedit-03)
        changed_count = change(new_text)
        selectmenuitem('*gedit','mnuFile;mnuSave')
	time.sleep(8)
        #close tab..
	selectmenuitem('*gedit','mnuFile;mnuQuit')
	f = open(fname,'r')
	a = f.read()
	if a.find(new_text) >= 0:
            log('Successfully added text','info')
        else:
                log('Text was not added','error')
                raise LdtpExecutionError(0)
    except:
        log('Gedit-edit-existing-file failed','error')
        log('Gedit-edit-existing-file','testend')
        raise LdtpExecutionError(0)
    log('Gedit-edit-existing-file','testend')
    return a    

def copy_paste(old_text):
    try:
        log('Gedit-copy-paste','teststart')
	launchapp('gedit ' + fname,1)
        selectmenuitem('*gedit','mnuEdit;mnuSelectAll')
        selectmenuitem('*gedit','mnuEdit;mnuCopy')
        #Open new, temporary file
        selectmenuitem('*gedit','mnuFile;mnuNew')
        time.sleep(3)
        selectmenuitem('*gedit','mnuEdit;mnuPaste')
        if gettextvalue('*gedit',
        'txt' + str(getrowcount('*gedit','tbl0')-1)) == old_text:
            log('Text copied successfully','info')
            #close the temporary file
            selectmenuitem('*gedit','mnuFile;mnuClose')
            waittillguiexist('dlgQuestion')
            click('dlgQuestion','btnClosewithoutSaving')
            time.sleep(3)
        else:
            log('Copy failed','error')
            raise LdtpExecutionError(0)
    except:
        log('Gedit-copy-paste failed','error')
        log('Gedit-copy-paste','testend')
        raise LdtpExecutionError(0)
    log('Gedit-copy-paste','testend')

def cut_paste(old_text):
    try:
        log('Gedit-copy-paste','teststart')
        selectmenuitem('*gedit','mnuEdit;mnuSelectAll')
        selectmenuitem('*gedit','mnuEdit;mnuCut')
        #Open new, temporary file
        selectmenuitem('*gedit','mnuFile;mnuNew')
        time.sleep(3)
        selectmenuitem('*gedit','mnuEdit;mnuPaste')
        if gettextvalue('*gedit',
        'txt' + str(getrowcount('*gedit','tbl0')-1)) == old_text:
            if getcharcount('*gedit',
            'txt' + str(getrowcount('*gedit','tbl0')-2)) == 0:
                log('Text moved successfully','info')
                #close the temporary file
                selectmenuitem('*gedit','mnuFile;mnuClose')
                waittillguiexist('dlgQuestion')
                click('dlgQuestion','btnClosewithoutSaving')
                time.sleep(3)
                selectmenuitem('*gedit','mnuFile;mnuRevert')
                time.sleep(3)
                click('dlgQuestion','btnRevert')
                time.sleep(3)
        else:
            log('Cut-paste failed','error')
            raise LdtpExecutionError(0)
    except:
        log('Gedit-cut-paste failed','error')
        log('Gedit-cut-paste','testend')
        raise LdtpExecutionError(0)
    log('Gedit-cut-paste','testend')

def delete_all():
    try:
        log('Gedit-delete-all-text','teststart')
        selectmenuitem('*gedit','mnuEdit;mnuSelectAll')
        selectmenuitem('*gedit','mnuEdit;mnuDelete')
        if getcharcount('*gedit',
        'txt' + str(getrowcount('*gedit','tbl0')-1)) == 0:
            log('Deleted successfully','info')
            selectmenuitem('*gedit','mnuFile;mnuRevert')  
            time.sleep(3)
            click('dlgQuestion','btnRevert')  
            time.sleep(3)
        else:
            log('Only some or no text was deleted','error')
            raise LdtpExecutionError(0)
    except:
        log('Gedit-delete-all-text failed','error')
        log('Gedit-delete-all-text','testend')
        raise LdtpExecutionError(0)
    log('Gedit-delete-all-text','testend')
        
try:
    obj = LdtpDataFileParser(datafilename)
    fname = obj.gettagvalue('file0')[0]
    new_text = obj.gettagvalue('append-text')[0]
    launch_app(fname)
    time.sleep(10)
    if guiexist('*gedit') == 1:
        log('Opened existing file for edit..','info')
        #get initial character count
        r = getcharcount('*gedit',
        'txt' + str(getrowcount('*gedit','tbl0')-1))
        revert(new_text,r)
        undo_redo(new_text,r)
        content = save_existing(new_text,r)
        copy_paste(content)
        cut_paste(content)
        delete_all()
    else:
        log('Cannot launch gedit','error')
        raise LdtpExecutionError(0)
except:
    log('Gedit-edit-existing-file failed','error')
    raise LdtpExecutionError(0)
selectmenuitem('*gedit','mnuFile;mnuSave')
time.sleep(3)
selectmenuitem('*gedit','mnuFile;mnuQuit')
waittillguinotexist('*gedit')
selectmenuitem('frm*Browser','mnuFile;mnuClose')
waittillguinotexist('frm*Browser')

log('Gedit-edit-existing-file','testend')
