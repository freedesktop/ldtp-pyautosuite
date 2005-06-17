#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     Aishoo, Fasilla
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

# Launch an instance of Gedit

log ('Launch Gedit', 'teststart')

status = os.fork ()
if status == -1:
	log ('Unable to fork', 'error')
	log ('Launch Gedit', 'testend')
	raise LdtpExecutionError (0)
if status == 0:
	try:
		log ('Gedit is being loaded', 'info')
		#os.execvp (gedit_exe_path, [])
		try:
			status = commands.getstatusoutput (gedit_exe_path)
		except KeyboardInterrupt:
			# interrupted
			print ''
		os._exit (os.EX_OK)
	except OSError, msg:
		log (str (msg), 'error')
		log ('Launch Gedit', 'testend')
		raise LdtpExecutionError (0)

# wait for 5 seconds, let the gedit application be loaded
log ('wait for 5 seconds, let the gedit application be loaded', 'info')
time.sleep (5)

log ('Launch Gedit', 'testend')
