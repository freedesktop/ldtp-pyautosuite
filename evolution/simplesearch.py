from search import *
# Read input from file
data_object = LdtpDataFileParser (datafilename)
search_type = data_object.gettagvalue ('search_type')
search_folder = data_object.gettagvalue ('search_folder')
search_text = data_object.gettagvalue ('search_text')

# Call the function
if search_type and search_folder and search_text:
	search (search_type[0], search_folder[0], search_text[0])
else:
	if not (search_type):
		log ('search_type is not provided in data xml file', 'error')
	if not (search_folder):
		log ('search_folder is not provided in data xml file', 'error')
	if not (search_text):
		log ('search_text is not provided in data xml file', 'error')
	log ('search mail', 'fail')
