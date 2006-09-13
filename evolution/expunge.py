#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
#     Prashanth Mohan  <prashmohan@gmail.com>
#
#  Copyright 2004 Novell, Inc.
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

#To expunge all the mails.

from ldtp import *
from ldtputils import *

try:

	log('Expunge mails','teststart')

	# Assuming that only the mails in the trash can be expunged.
	fldr = 'Trash'
	#remap('evolution','frmEvolution-Mail')
	if selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', fldr):
		waittillguiexist ('frmEvolution-'+fldr+'*')
		log('fldr has been selected','info')
		time.sleep(2)
		if selectmenuitem('frmEvolution-*','mnuFolder;mnuExpunge') == 1:
			log('Expunge successfull','info')
			print 'All Mails have been permanently removed from trash'
		else:
			log('Expunge not completed','info')
			print 'Probs in permanently removing the mails'
	else:
		print fldr+ 'not found'
		log('Unable to find trash','error')
except:
	log('Unable to expunge the mails','error')
	print 'Unable to expunge'
	raise LdtpExecutionError (0)

log('Expunge mails','testend')
