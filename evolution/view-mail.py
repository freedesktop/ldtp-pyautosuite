#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Nagashree <mnagashree@novell.com>
#     Premkumar <jpremkumar@novell.com>
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

#To view mail
def view_mail (folder_name,i,ref_image):
    try:
        verifymailwithimage (folder_name,i,ref_image)
    except:
        log ('View mail failed','error')
        raise LdtpExecutionError (0)

#Reading inputs from file
file = open ('view-mail.dat','r')
argmts = file.readlines()
folder_name = argmts[0].strip()
i = argmts[1].strip()
ref_image = argmts[2].strip()

log ('View mail verification','teststart')
time.sleep(2)
view_mail (folder_name,i,ref_image)
time.sleep(2)
log ('View mail verification','testend')
