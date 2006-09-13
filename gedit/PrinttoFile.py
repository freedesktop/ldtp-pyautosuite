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
def print_to_file(type):
    selectmenuitem('*gedit','mnuFile;mnuPrint')
    waittillguiexist('dlgPrint')
    time.sleep(3)
    if type == 'ps':
        selectrow('dlgPrint','tbl0','Generic Postscript')
        comboselect('dlgPrint','cboLocation','File')
    else:
        selectrow('dlgPrint','tbl0','Create a PDF document')        
    click('dlgPrint','btnPrint')
    waittillguinotexist('dlgPrint')
    time.sleep(3)
def exists_check(name):
    if os.path.exists(os.environ['HOME'] + '/' + name) == True:
        log(name + ' file created..','info')
        return 0
    else:
        log(name + ' file not created','error')
        return 1
try:
    log('Test','teststart')
    app = 'gedit ' + os.environ['HOME'] + '/new.txt'
    print app
    launchapp(app,1)
    waittillguiexist('*gedit')
    settextvalue('*gedit','txt0','LDTP Testing')
    print_to_file('ps')
    if exists_check('output.ps') == 1:
        raise LdtpExecutionError(0)
    print_to_file('pdf')
    if exists_check('output.pdf') == 1:
        raise LdtpExecutionError(0)
except:
    log('Test failed','error')
    raise LdtpExecutionError(0)
log('Test','testend')
