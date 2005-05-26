#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     SR Aginesh <sraginesh@novell.com>
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

# Browse an URL
def get_url_list (file):
	try:
		fp = open (file)
	except IOError:
		log ('Unable to open url.txt file', 'error')
		return None
	url_list = fp.readlines ()
	fp.close ()
	return url_list

url = ''

def browse_url (url_list):
	ret = -1
	url_list_count = 0
	url_success_list_count = 0
	for i in url_list:
		url = string.split (i)
		url_list_count = url_list_count + 1
		try:
			settextvalue ('MozillaFirefox', 'txtUrl', url[0])
			ret = verifysettext ('MozillaFirefox', 'txtUrl', url[0])
			if ret == 0:
				log ('Unable to set text ' + url[0] + ' in URL bar', 'fail')
				return 0
			else:
				log ('URL ' + url[0] + ' typed successfully', 'info')
		except error:
			log ('Could not set ' + url[0], 'fail')
			continue

		if ret == 1:
			try:
				click ('mozilla','btnGo')
				# Wait for 10 seconds
				time.sleep (10)
				flag = 0
				for count in range (0, 3):
					op = commands.getstatusoutput ('digwin -c')
					if string.find (string.upper (op[1]), string.upper (url[2])) == -1:
						log ('Unable to load ' + url[0], 'error')
						log ('Retry count ' + str (count + 1), 'info')
						wait (10)
					else:
						flag = 1
						break
				if flag == 0:
					continue
				url_str_count = len (url)
				title_text = ''
				for j in range (2, url_str_count):
					if title_text == '':
						title_text = url[j]
					else:
						title_text = title_text + ' ' + url[j]
				tmp_image = default_tmp_dir + '/' + url[1] + '.png'
				if imagecapture (title_text + ' - Deer Park Alpha 1', tmp_image) != 0:
					default_image = default_image_dir + '/' + url[1] + 'default.png'
					diff = imagecompare (default_image,  tmp_image)
					if diff < 1:
						log (title_text + ' page opened successfully', 'info')
						url_success_list_count = url_success_list_count + 1
					else:
						log ('Page contents displayed are different', 'fail')
				continue
			except error, msg:
				log (str (msg), 'fail')
				return None
	if url_success_list_count < url_list_count:
		return None
	else:
		return 1

log ('Loading Web Page', 'teststart')
url_list = get_url_list ('url.txt')

status = None
time.sleep(10)
if url_list != None:
	status = browse_url (url_list)

log ('Loading Web Page', 'testend')
if status == None:
	raise LdtpExecutionError (0)
