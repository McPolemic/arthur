#!/usr/bin/python

import os
from tools import windows_pause
from jinja2 import Environment
from jinja2 import ChoiceLoader, PackageLoader, FileSystemLoader

#Temporarily adding python directory to sys.path
import sys
sys.path.append('C:\\Users\\lukens\\Documents\\Python')

import settings

#Module internal loader
loader = ChoiceLoader([
	FileSystemLoader('./templates'),
	PackageLoader('arthur', 'templates')
])
env = Environment(loader=loader)

def run():
	"""Runs through all files in settings and generates the HTML files"""
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

if __name__ == '__main__':
	run()
	windows_pause()