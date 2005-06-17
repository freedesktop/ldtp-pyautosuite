#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Aishoo Team, Fasila
#     A. Nagappan <anagappan@novell.com>
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

# To go to any line in the currently opened document
log ('Go To Line No', 'teststart')

try:
    selectmenuitem ('gedit', 'mnuFile;mnuOpen')
    if guiexist ('dlgOpenFile') == 1:
        selectrowindex ('dlgOpenFile', 'tblFiles', 'sample.txt')
        click ('dlgOpenFile', 'btnOpen')
        # NOT COMPLETED
 selectmenuitem( 'gedit', 'mnuSearch;mnuGotoLine')
 settextvalue('dlgGotoLine','txtLinenumber','3')
 click('dlgGotoLine','btnGotoLine')
 click('dlgGotoLine','btnClose')
 selectmenuitem ('gedit', 'mnuFile;mnuQuit')
except:
 print "19 error occured is:", sys.exc_info()[0]

log ('Go To Line No', 'testend')
