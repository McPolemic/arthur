#!/usr/bin/python

import os
import sys
import shutil
from tools import windows_pause
from jinja2 import Environment
from jinja2 import ChoiceLoader, PackageLoader, FileSystemLoader
import arthur

import settings

#Module internal loader
loader = ChoiceLoader([
    FileSystemLoader('./templates'),
    PackageLoader('arthur', 'templates')
])
env = Environment(loader=loader)

def usage():
    print """
Usage: %s [command]

Commands that arthur recognizes are:
    init   Initializes the current directory to run arthur commands.
    run    Runs the arthur templates.
    """ % sys.argv[0]

def init(path):
    arthur_dir = os.path.dirname(arthur.__file__)

    #Copy application files
    for target in ('main.py', 'settings.py'):
        shutil.copy(os.path.join(arthur_dir, target), path)

    #Copy Template directory
    template_dir = os.path.join(arthur_dir, 'templates')
    new_dir = os.path.join(path, 'templates')

    #Prompt to write over templates directory if it already exists
    if os.path.exists(new_dir):
    	answer = raw_input('Warning: Template directory %s already exists.  Overwrite? (Y/N) ' % new_dir)
    	if (answer.capitalize()[0] != 'Y'):
    		print "Preserving existing template directory."
    		print "Initialization complete."
    		return
        else:
            shutil.rmtree(new_dir)
    
    shutil.copytree(template_dir, new_dir)
    print "Initialization complete."

def init_here():
    init(os.getcwd())

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

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'init':
            init_here(os.getcwd())
        elif sys.argv[1] == 'run':
            run()
        else:
            usage()
    else:
        run()
    windows_pause()

if __name__ == '__main__':
    main()
