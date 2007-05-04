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
import random, os

try:
    check_open('gedit')
except:
    raise


log ('listsubmenus','teststart')
try:
    listsubmenus ('*gedit','mnuFile')
    listsubmenus ('*gedit','mnuView')
#     http://bugzilla.gnome.org/show_bug.cgi?id=351234
#     Currently Does not work for more than 1 Level of menus
#     listsubmenus ('*gedit','mnuView;mnuHighlightMode')
except:
    testfail ('listsubmenus')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('listsubmenus')


log ('doesmenuitemexist','teststart')
try:
    if doesmenuitemexist ('*gedit','mnuFile;mnuNew') != 1:
        log ('File-->New is reported as non existent','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if doesmenuitemexist ('*gedit','mnuFile;mnuTESTVALUE') != 0:
        log ('non existent item reported as existent','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    if doesmenuitemexist ('*gedit','mnuFile') != 0:
        log ('File is reported as end node','cause')
        raise LdtpExecutionError (str (traceback.format_exc ()))
    ## Long Heirarchy
    # http://bugzilla.gnome.org/show_bug.cgi?id=351802
#     if doesmenuitemexist ('*gedit','mnuView;mnuHighlightMode;mnuNormal') != 1 or \
#            doesmenuitemexist ('*gedit','mnuView;mnuHighlightMode;mnuSources;mnuC') != 1:
#         log ('Long Heirarchy is reported as non existent','cause')
#         raise LdtpExecutionError (str (traceback.format_exc ()))
except:
    testfail ('doesmenuitemexist')
    raise LdtpExecutionError (str (traceback.format_exc ()))
testpass ('doesmenuitemexist')


# log ('selectmenuitem','teststart')
# try:
#     if doesmenuitemexist ('*gedit','mnuFile;mnuNew') == 1:
#         selectmenuitem ('*gedit','mnuFile;mnuNew')
#         time.sleep (5)
# #         pres_txt = [x for x in getobjectlist ('*gedit') if x.startswith ('txt0')]
# #         remap ('gedit','*gedit')
# #         flag = False
# #         objects = getobjeclist ('*gedit')
# #         for obj in objects:
# #             if obj.startswith ('txt') and obj != 'txt0':
# #                 flag = True
# #                 break
# #         if not flag:
# #             log ('New Tab not opened','cause')
# #             raise LdtpExecutionError (str (traceback.format_exc ()))        
#     else:
#         raise LdtpExecutionError(str (traceback.format_exc ()))
#     if doesmenuitemexist ('*gedit','mnuFile;mnuClose') == 1:
#         selectmenuitem ('*gedit','mnuFile;mnuClose')
#         time.sleep (5)
# #         remap ('gedit','*gedit')
# #         flag = True
# #         objects = getobjeclist ('*gedit')
# #         for obj in objects:
# #             if obj.startswith ('txt') and obj != 'txt0':
# #                 flag = False
# #                 break
# #         if flag:
# #             raise LdtpExecutionError (str (traceback.format_exc ()))        
#     else:
#         raise LdtpExecutionError(str (traceback.format_exc ()))
# except:
#     testfail ('selectmenuitem')
#     raise LdtpExecutionError (str (traceback.format_exc ()))
# testpass ('selectmenuitem')
