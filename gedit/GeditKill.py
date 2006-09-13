#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     N Srinivasan  <raiden.202@gmail.com>
#
#  Copyright 2004-2006 Novell, Inc.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#

from ldtp import *
from ldtputils import *
import os,subprocess
try:
    log('gedit-ungraceful-kill-test','teststart')
    a = file('/dev/null','w')
    
    subprocess.Popen("ulimit -c unlimited && gedit --disable-crash-dialog",
    stderr=a,shell=True)
    time.sleep(3)
    subprocess.Popen("kill -11 `pgrep gedit`",shell=True)
    time.sleep(5)
    print "<DEBUG>"
    if guiexist('*gedit') == 0:
        if os.path.exists(os.path.abspath('') + '/core') == True:
            log('Gedit dumped core','info')
        else:
            log('No core dump found ..','error')
            raise LdtpExecutionError(0)
    else:
        log('Crash dialog appeared','error')
        raise LdtpExecutionError(0)
except:
    log('gedit-ungraceful-kill-test failed','error')
    raise LdtpExecutionError(0)
log('gedit-ungraceful-kill-test','testend')
