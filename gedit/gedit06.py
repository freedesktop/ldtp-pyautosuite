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

# Print preview and print a document
log ('Print Preview And Print Document', 'teststart')
try:
    selectmenuitem ('gedit', 'mnuFile;mnuOpen')
    # Wait 3 seconds, let the Open Dialog appear
    time.sleep (3)
    if guiexist ('dlgOpenFile') == 1:
        # TODO
        # - Once GTK File Selector bug is resolved try to select some file from Filesystem shortcuts
        selectrow ('dlgOpenFile', 'tblFiles', 'sample.txt')
        click ('dlgOpenFile', 'btnOpen')
        time.sleep (2)
        # TODO
        # - Check file opened or not
        if guiexist ('dlgOpenFile') == 0:
            log ('Print Preview', 'teststart')
            selectmenuitem ('gedit', 'mnuFile;mnuPrintPreview')
            # Wait for 3 seconds, let the print preview window appear
            time.sleep (3)
            if guiexist ('Printpreview') == 1:
                # TODO
                # - Verify contents dispalyed in print preview frame
                log ('Print Preview window appeared', 'info')
                click ('Printpreview', 'btnclose')
                # Wait for 2 seconds, let the print preview window disappear
                time.sleep (2)
                if guiexist ('Printpreview') == 0:
                    log ('Print Preview', 'pass')
                else:
                    log ('Print preview dialog still appears', 'error')
                    log ('Print Preview', 'fail')
            else:
                log ('Print preview dialog does not appear', 'error')
                log ('Print Preview', 'fail')
            log ('Print Preview', 'testend')

            log ('Print Document', 'teststart')
            selectmenuitem ('gedit', 'mnuFile;mnuPrint')
            # Wait for 3 seconds, let the print dialog appear
            time.sleep (3)
            # Select generic postscript printer, so that we can print the document to local file
            # and later we can compare the output
            selectrow ('dlgPrint', 'tblPrinter', 'Generic Postscript')
            selectmenuitem ('dlgPrint', 'mnuLocation;mnuFile')
            click ('dlgPrint', 'btnSaveAs')

            # Wait for 3 seconds, let the print to file dialog box appear
            time.sleep (3)
            if guiexist ('dlgPrintToFile') == 1:
                settextvalue ('dlgPrintToFile', 'txtName', default_tmp_dir + '/output.ps')
                # TODO
                # - Check output is available in default_tmp_dir
                # - File comparison
                # Let the document get printed to output file and print to file dialog box disappear
                time.sleep (5)
                if guiexist ('dlgPrintToFile') == 1:
                    click ('dlgPrintToFile', 'btnSave')
                    time.sleep (2)
                    if guiexist ('alrtOverWrite') == 1:
                        click ('alrtOverWrite', 'btnYes')
                    click ('dlgPrint', 'btnPrint')
                    # Let the document be printed
                    time.sleep (3)
                    log ('Print Document', 'pass')
                else:
                    click ('dlgPrintToFile', 'btnCancel')
                    log ('Print to file dialog still appears after saving output to file', 'error')
                    log ('Print Document', 'fail')
            else:
                click ('dlgPrint', 'btnCancel')
                log ('Print to file dialog does not appear', 'error')
                log ('Print Document', 'fail')
            log ('Print Document', 'testend')
            log ('Print Preview And Print Document', 'pass')
        else:
            log ('Still open dialog window appears', 'error')
            log ('Print Preview And Print Document', 'fail')
except error, msg:
    log (str (msg), 'error')
    log ('Print Preview And Print Document', 'fail')
log ('Print Preview And Print Document', 'testend')
