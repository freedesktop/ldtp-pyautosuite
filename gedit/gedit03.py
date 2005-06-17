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

# Open existing document, edit it and save it to a new document
log ('Edit Existing Document', 'teststart')

try:
    try:
        # Close all opened tab
        #selectmenuitem ('gedit', 'mnuDocuments;mnuCloseAll')
        print 'Test'
    except error:
        log ('There maybe no documents opened', 'info')
    selectmenuitem ('gedit', 'mnuFile;mnuOpen')
    # Wait for 3 seconds, let the open dialog window appear
    time.sleep (3)
    # Verify open dialog appears or not
    if guiexist ('dlgOpenFile') == 1:
        # TODO
        # - Select file from default_doc_dir
        selectrowindex ('dlgOpenFile', 'tblShortcuts', 0)
        # TODO
        # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
        #selectrow ('dlgOpenFile', 'tblFiles', default_doc_dir + '/sample.txt')
        selectrow ('dlgOpenFile', 'tblFiles', 'sample.txt')
        # TODO
        # - Handle if, file not found
        click ('dlgOpenFile', 'btnOpen')
        # TODO
        # - Verify file is opened or not
        # - Get text from file and use it to set new text value
        print "flag"
        # Set new text
        settextvalue ('gedit', 'txtGedit', 'Edit existing document and test it using GNU/Linux Desktop Testing Project')
        # TODO
        # - Verify new text is set or not
        # Invoke save as dialog
        selectmenuitem ('gedit', 'mnuFile;mnuSaveAs')
        # Wait for 3 seconds, let the save dialog window appear
        time.sleep (3)
        # Verify save as dialog appears or not
        if guiexist ('dlgSaveas') == 1:
            settextvalue ('dlgSaveas', 'txtName', default_tmp_dir + '/edit.txt')
            click ('dlgSaveas', 'btnSave')

            time.sleep (2)
            # If file already exist, then replace it with this new content
            if guiexist ('alrtOverWrite') == 1:
                click ('alrtOverWrite', 'btnReplace')
            # TODO
            # - Verify file contents properly saved or not after editing

            # Close current file
            #selectmenuitem ('gedit', 'mnuFile;mnuClose')
            log ('Edit Existing Document', 'pass')
        else:
            log ('Save as dialog box does not appear', 'error')
            log ('Edit Existing Document', 'fail')
    else:
        log ('Open dialog box does not appear', 'error')
        log ('Edit Existing Document', 'fail')
except error, msg:
    log (str(msg), 'error')
    log ('Edit Existing Document', 'fail')
log ('Edit Existing Document', 'testend')
