#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     S. Aginesh <sraginesh@novell.com>
#     A. Nagappan <anagappan@novell.com>
# 
#  Copyright 2004 Novell, Inc.
# 
#  This script is free software; you can redistribute it and/or
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

def browse_local_file (file_name):
    try:
        settextvalue ('MozillaFirefox', 'txtUrl', file_name)
        ret = verifysettext ('MozillaFirefox', 'txtUrl', file_name)
        if ret == 0:
            log ('Unable to set text ' + file_name + ' in URL bar', 'fail')
            return 0
        else:
            log (file_name + ' typed successfully', 'info')
    except error:
        log ('Could not set ' + file_name, 'fail')
        return 0
    try:
        click ('mozilla','btnGo')
        time.sleep (2)
    except error:
        log ('Could not set ' + file_name, 'fail')
        return 0
    return 1

def click_ok ():
    try:
        click ('PageSetup', 'btnOk')
        return 1
    except error:
        log ('Could not quit from page setup window', 'error')
        return 0

def invoke_page_setup ():
    try:
        status = selectmenuitem ('Mozilla', 'mnuFile;mnuPageSetup')
    except error:
        log ('Unable to select page setup menu', 'fail')
        return 0

    # wait for 3 seconds, so that page setup dialog may appear
    time.sleep (3)

    # Due to a bug in Firefox accessibility, we have to reinitialize SPI_init
    reinitldtp ()

    if guiexist ('PageSetup') == 1:
        log ('Page setup dialog appeared', 'info')
    else:
        log ('Page setup dialog does not appear', 'fail')
        log ('Page Setup', 'testend')
        return 0
    return 1

def invoke_print_to_file ():
    try:
        status = selectmenuitem ('Mozilla', 'mnuFile;mnuPrint')
    except error:
        log ('Unable to select print menu', 'fail')
        return 0

    # wait for 3 seconds, so that page setup dialog may appear
    time.sleep (3)

    # Due to a bug in Firefox accessibility, we have to reinitialize SPI_init
    reinitldtp ()

    if guiexist ('Print') == 1:
        log ('Print dialog appeared', 'info')
    else:
        log ('Print dialog does not appear', 'fail')
        log ('Page Setup', 'testend')
        return 0
    return 1

def print_contents_to_file ():
    # Browse local file url.txt
    if browse_local_file (default_dir + '/url.txt') == 1:
        if invoke_print_to_file () == 1:
            try:
                click ('Print', 'chkPrinttoFile')
            except error:
                log ('Could not click print to file option', 'error')
                return 0
            try:
                # GTK File selector is not accessibility enabled when
                # integrated with Mozilla Firefox
                # click ('Print', 'btnOk')
                # Due to firefox bug clicking cancel
                # FIXME:
                # Using ltfx, somebody can select file and save
                click ('Print', 'btnCancel')
            except error:
                log ('Could not click cancel option', 'error')
                return 0
    return 1

def compare_file (file1, file2):
    if os.access (file1, os.F_OK | os.R_OK) == 0:
        log ('File ' + file1 + ' not found', 'error')
        return False
    if os.access (file2, os.F_OK | os.R_OK) == 0:
        log ('File ' + file2 + ' not found', 'error')
        return False
    diff = filecmp (file1, file2)
    if diff == True:
        log ('File contents are same', 'info')
    else:
        log ('File contents are different')
    return diff

status = 1
log ('Page Setup', 'teststart')

log ('Print Landscape', 'teststart')
if invoke_page_setup () == 1:
    try:
        click ('PageSetup', 'rdoLandscape')
        log ('Radio button Landscape clicked', 'info')
        click_ok ()
        time.sleep (1)
        if print_contents_to_file () == 1:
            if compare_file (default_doc_dir + 'url-ls.ps', default_tmp_dir + 'url-ls.ps') == False:
                status = 0
                log ('File comparison', 'error')
                log ('Print Landscape', 'fail')
            else:
                log ('Landscape outputs are same', 'info')
                log ('Print Landscape', 'pass')
    except error:
        status = 0
        log ('Could not click on Portrait radio button', 'error')
        log ('Print Portrait', 'fail')
log ('Print Landscape', 'testend')

log ('Print Portrait', 'teststart')
if invoke_page_setup () == 1:
    try:
        click ('PageSetup', 'rdoPortrait')
        log ('Radio button Portrait clicked', 'info')
        click_ok ()
        time.sleep (1)
        if print_contents_to_file () == 1:
            if compare_file (default_doc_dir + 'url-pr.ps', default_tmp_dir + 'url-pr.ps') == False:
                status = 0
                log ('File comparison', 'error')
                log ('Print Portrait', 'fail')
            else:
                log ('Portrait outputs are same', 'info')
                log ('Print Portrait', 'pass')
    except error:
        status = 0
        log ('Could not click on Portrait radio button', 'error')
        log ('Print Portrait', 'fail')
log ('Print Portrait', 'testend')

log ('Shrink To Fit Page Width', 'teststart')
if invoke_page_setup () == 1:
    try:
        click ('PageSetup', 'chkShrinkToFitPageWidth')
        log ('Checked Shrink to fit page width', 'info')
        click_ok ()
        time.sleep (1)
        if print_contents_to_file () == 1:
            if compare_file (default_doc_dir + 'url-aft-shrink.ps', default_tmp_dir + 'url-aft-shrink.ps') == False:
                status = 0
                log ('File comparison', 'error')
                log ('Shrink To Fit Page Width', 'fail')
            else:
                log ('Portrait outputs are same', 'info')
                log ('Shrink To Fit Page Width', 'pass')
    except error:
        status = 0
        log ('Could not click on Shrink to fit page width check box', 'error')
        log ('Shrink To Fit Page Width', 'fail')
log ('Shrink To Fit Page Width', 'testend')

# Redo click operation
log ('Shrink To Fit Page Width', 'teststart')
if invoke_page_setup () == 1:
    try:
        click ('PageSetup', 'chkShrinkToFitPageWidth')
        log ('Checked Shrink to fit page width', 'info')
        click_ok ()
        time.sleep (1)
        if print_contents_to_file () == 1:
            if compare_file (default_doc_dir + 'url-bef-shrink.ps', default_tmp_dir + 'url-bef-shrink.ps') == False:
                status = 0
                log ('File comparison', 'fail')
                log ('Shrink To Fit Page Width', 'fail')
            else:
                log ('Portrait outputs are same', 'pass')
    except error:
        status = 0
        log ('Could not click on Shrink to fit page width check box', 'error')
        log ('Shrink To Fit Page Width', 'fail')
log ('Shrink To Fit Page Width', 'testend')

if status == 0:
    log ('Page Setup test execution', 'fail')
else:
    log ('Page Setup test execution', 'pass')

log ('Page Setup', 'testend')
