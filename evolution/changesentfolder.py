from evoutils.mailpreferences import *
from ldtputils import *

# Read data from a file
data_object = LdtpDataFileParser (datafilename)
accountname = data_object.gettagvalue ('accountname')
sent_folder = data_object.gettagvalue ('sent_folder')

if sent_folder:
	sent_folder = sent_folder[0]
else:
	sent_folder = 'Sent Items'

# Call the function
if accountname:
	change_sentfolder (accountname[0], sent_folder)
else:
	log ('accountname not provided in data xml file', 'error')
	raise LdtpExecutionError (0)

