from jinja2 import Environment, FileSystemLoader

import settings

env = Environment(loader=FileSystemLoader('./templates/'))

#Temp code
for key,value in settings.files.iteritems():
	print 'Processing %s' % key
	template = env.get_template(value['template_name'])
	output =  template.render({'g': settings.global_conf,
			    			   'p': value['settings_dict']
			    			   })
	out = open(value['output'], 'w')
	out.write(output)
	out.close()