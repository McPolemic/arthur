from jinja2 import Environment, FileSystemLoader
import os

import settings

env = Environment(loader=FileSystemLoader('./templates/'))

#Temp code
for key,value in settings.files.iteritems():
	print 'Processing %s' % key
	template = env.get_template(value['template_name'])
	output =  template.render({'g': settings.global_conf,
			    			   'p': value['settings_dict']
			    			   })
	
	#Ensure directory exists
	target_path = os.path.dirname(os.path.abspath(value['output']))

	if not os.path.exists(target_path):
		print 'Creating output directory %s' % target_path
		os.makedirs(target_path)

	out = open(value['output'], 'w')
	out.write(output)
	out.close()