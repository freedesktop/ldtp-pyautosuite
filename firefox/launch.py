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

# Launch an instance of Firefox
log ('Launch Firefox', 'teststart')

status = os.fork ()
if status == -1:
	log ('Unable to fork', 'error')
	log ('Launch Firefox', 'testend')
	raise LdtpExecutionError (0)
if status == 0:
	try:
		log ('Firefox is being loaded', 'info')
		os.execv (firefox_exe_path, ['sh'])
		os._exit (os.EX_OK)
	except OSError, msg:
		log (str (msg), 'error')
		log ('Launch Firefox', 'testend')
		raise LdtpExecutionError (0)

# wait for 3 seconds, let the firefox application be loaded
log ('wait for 3 seconds, let the firefox application be loaded', 'info')
time.sleep (10)

log ('Launch Firefox', 'testend')
