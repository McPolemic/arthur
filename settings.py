from datetime import date
from arthur.settings_defaults import *

global_conf = {
	'number': '15135',
}

#Set revision date to today
for i in (program_specs, unit_test, implementation):
	i['revision_history'][0]['last_update'] = date.today().strftime('%m/%d/%Y')

#The pairs are "file to be generated" and "template file"
#files = {
#    'Implementation Plan': {
#        'template_name': 'Implementation Plan.htm',
#        'settings_dict': implementation,
#        'output': './output/%s - Implementation Plan.html' % global_conf['number']
#    },
#    'Program Specifications': {
#        'template_name': 'Program Specifications.htm',
#        'settings_dict': program_specs,
#        'output': './output/%s - Program Specifications.html' % global_conf['number']
#    },
#    'Unit Testing': {
#        'template_name': 'Unit Testing.htm',
#        'settings_dict': unit_test,
#        'output': './output/%s - Unit Testing.html' % global_conf['number']
#    }
#}