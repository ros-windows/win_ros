
import os
import sys
import shutil
import utils

def get_templates(package):
    template_dir = os.path.join(os.path.dirname(__file__),'templates', 'comms') 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_dir,'mainpage.dox'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['package.xml'] = utils.read_template(os.path.join(template_dir,'package.xml'))
    templates[os.path.join('msg','Dude.msg')] = utils.read_template(os.path.join(template_dir,'msg','Dude.msg'))
    templates[os.path.join('srv','HelloDude.srv')] = utils.read_template(os.path.join(template_dir,'srv','HelloDude.srv'))
    return templates

def create_package_directory(package):
    p = os.path.abspath(package)
    os.makedirs(p) 
    print("Created package directory " + p)
    os.makedirs(os.path.join(p,"msg"))
    print("Created package directory " + os.path.join(p,"msg"))
    os.makedirs(os.path.join(p,"srv"))
    print("Created package directory " + os.path.join(p,"srv"))

def create_winros_catkin_package():
    (package, depends) = utils.parse_arguments(['std_msgs'])
    create_package_directory(package)
    templates = get_templates(package)
    package_depends = ''.join(['  <depend package="%s"/>\n'%d for d in depends])
    cmake_depends = ''.join(['%s '%d for d in depends])
    for filename, template in templates.iteritems():
        contents = utils.instantiate_template(template, package, package, utils.author_name(), package_depends, cmake_depends)
        try:
            p = os.path.abspath(os.path.join(package, filename))
            f = open(p, 'w')
            f.write(contents.encode('utf-8'))
            print "Created package file", p
        finally:
            f.close()
    print "\nPlease edit package.xml, mainpage.dox, CMakeLists.txt, and add the package subdirectory."
