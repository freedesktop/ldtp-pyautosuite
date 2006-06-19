#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#       Prashanth Mohan <prashmohan at gmail dot com>
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

from ldtp import *
from ldtputils import *
import time, os

class gnome_dictionary:
    """Class containing functions for testing the functionalities
    of gnome-dictionary which is a part of the gnome-utils package"""

    def launch (self):
        launchapp ('gnome-dictionary',1)

        
    def __init__ (self, datafilename, appmap_file=''):
        self.data_object = LdtpDataFileParser (datafilename)
        self.term = self.data_object.gettagvalue ('term')
        if self.term != []:
            self.term = self.term[0]
            
        self.meaning = self.data_object.gettagvalue ('meaning')
        if self.meaning != []:
            self.meaning = self.meaning[0]
            
        self.save_file = self.data_object.gettagvalue ('filename')
        if self.save_file != []:
            self.save_file = self.save_file[0]

        self.search_term = self.data_object.gettagvalue ('search')
        if self.search_term != []:
            self.search_term = self.search_term[0]
            self.last_search_term = self.search_term

        self.last_find = 0
        if guiexist ('*Dictionary') != 1:
            print 'OPENING'
            log ('Dictionary not open.. opening','info')
            launchapp ('gnome-dictionary',1)
        print 'OPENED'


    def check_meaning (self, term='', meaning=''):
        if term == '':
            term = self.term
        if meaning == '':
            meaning = self.meaning

        log ('Searching for term: '+term,'info')
        enterstring ('*Dictionary','txtLookup',term+'<return>')

        print 'Sleeping...'
        time.sleep (5) # arbitrary time gap for retreiving information from the server

        real_meaning = gettextvalue ('*Dictionary','txt1')
        if real_meaning != meaning:
            log ('Meanings do not match','cause')
            raise LdtpExecutionError ('Meanings do not match')


    def new_window (self):
        while guiexist ('Dictionary') == 1:
            enterstring ('Dictionary','txtLookup','test<return>')
            time.sleep (5)
        selectmenuitem ('*Dictionary','mnuFile;mnuNew')
        waittillguiexist ('Dictionary')
        if guiexist ('Dictionary') != 1:
            log ('New Window not found','cause')
            raise LdtpExecutionError ('New Window not found')

        
    def save_a_copy (self, file_name=''):
        if file_name == '':
            file_name = self.save_file

        print 'FILENAME: ',file_name
        selectmenuitem ('*Dictionary','mnuFile;mnuSaveaCopy')
        os.environ['GUI_EXIST'] = '5'
        waittillguiexist ('dlgSaveaCopy')
        settextvalue ('dlgSaveaCopy','txtName',file_name)
        click ('dlgSaveaCopy','btnSave')

        if waittillguiexist ('Question') == 1:
            click ('dlgQuestion','btnReplace')
            waittillguinotexist ('Question')

        waittillguinotexist ('Save a Copy')
        contents = gettextvalue ('*Dictionary','txt1')
        fp = open (file_name,"r")
        cont = fp.read()#.strip()

        index1 = 0
        index2 = 0
        while index1 < len (cont) and index2 < len (contents):
            if cont[index1] == '\r':
                index1 += 1
                continue
            if cont[index1] != contents[index2]:
                log ('Contents of file differs','cause')                
                raise LdtpExecutionError ('Contents of file differs')
            index1 += 1
            index2 += 1

        if index1 != len (cont) and index2 != len (contents):
            log ('Contents of file differs','cause')                
            raise LdtpExecutionError ('Contents of file differs')
            

    def close_window(self):
        selectmenuitem ('*Dictionary','mnuFile;mnuClose')
        waittillguinotexist ('*Dictionary')
        if guiexist ('*Dictionary') == 1:
            log ('Window still open','cause')
            raise LdtpExecutionError ('Window still open')


    def check_find (self, term, position):
        meaning = gettextvalue ('*Dictionary', 'txt1')
        
        if self.last_find == position and position != 0:
            return

        if (position == 0 and meaning.find (term) != 0) or position < len (term):
            log ('Find pointing to position 0', 'cause')
            raise LdtpExecutionError ('Find pointing to position 0')

        if meaning [position - len (term): position] != term:
            log ('Find giving wrong results','cause')
            raise LdtpExecutionError ('Find giving wrong results')

        print 'LAST FIND :: ', self.last_find
        print 'TERM :: ',term
        print 'POSITIOn ::', position
        print 'LEN(TERM) ::', len (term)
        time.sleep (5)
        if meaning [self.last_find:].find (term) != position - len(term) - self.last_find:
            log ('Skipped results','cause')
            raise LdtpExecutionError ('Skipped results')

        self.last_find = position
        print 'LAST_FIND :: ',self.last_find


    def ordinary_find (self,term=''):
        if term == '':
            term = self.search_term

        self.last_search_term = term
        selectmenuitem ('*Dictionary','mnuEdit;mnuFind')
        setcursorposition ('*Dictionary','txt1',0)
        settextvalue ('*Dictionary','txtFind',term)
        position = getcursorposition ('*Dictionary','txt1')
        try:
            self.check_find (term,position)
        except:
            raise


    def find_next (self):
        selectmenuitem ('*Dictionary','mnuEdit;mnuFindNext')
        print 'INSIDE FIND NEXT'
        #abc = raw_input()
        time.sleep (5)
        position = getcursorposition ('*Dictionary','txt1')

        try:
            self.check_find (self.last_search_term, position)
        except:
            raise


    def find_prev (self):

        if self.last_find == 0:
            log ('Nothing to find','cause')
            raise LdtpExecutionError ('Nothing to find')

        meaning = gettextvalue ('*Dictionary','txt1')
        term = self.search_term
        selectmenuitem ('*Dictionary','mnuEdit;mnuFindPrevious')
        time.sleep (1)
        position = getcursorposition ('*Dictionary','txt1')

        if meaning [:self.last_find-1].rfind (self.last_search_term) != position - len (term):
            log ('Wrong answer','cause')
            raise LdtpExecutionError ('Wrong answer')
