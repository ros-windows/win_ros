
import os
import sys
import shutil
import utils

def get_cpp_templates(package):
    template_dir = os.path.join(os.path.dirname(__file__),'templates', 'cpp') 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_dir,'mainpage.dox'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['package.xml'] = utils.read_template(os.path.join(template_dir,'package.xml'))
    templates[os.path.join('include',package,package+'.hpp')] = utils.read_template(os.path.join(template_dir,'include','PACKAGE_NAME','package_name.hpp'))
    templates[os.path.join('src','lib','CMakeLists.txt')] = utils.read_template(os.path.join(template_dir,'src','lib','CMakeLists.txt'))
    templates[os.path.join('src','lib',package+'.cpp')] = utils.read_template(os.path.join(template_dir,'src','lib','package_name.cpp'))
    templates[os.path.join('src','CMakeLists.txt')] = utils.read_template(os.path.join(template_dir,'src','CMakeLists.txt'))
    templates[os.path.join('src','main.cpp')] = utils.read_template(os.path.join(template_dir,'src','main.cpp'))
    return templates

def create_cpp_package_directory(package):
    p = os.path.abspath(package)
    os.makedirs(p) 
    print("Created package directory " + p)
    os.makedirs(os.path.join(p,"src"))
    print("Created package directory " + os.path.join(p,"src"))
    os.makedirs(os.path.join(p,"src","lib"))
    print("Created package directory " + os.path.join(p,"src","lib"))
    os.makedirs(os.path.join(p,"include"))
    print("Created package directory " + os.path.join(p,"include"))
    os.makedirs(os.path.join(p,"include",package))
    print("Created package directory " + os.path.join(p,"include",package))

def get_py_templates(package):
    template_dir = os.path.join(os.path.dirname(__file__),'templates', 'py') 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_dir,'mainpage.dox'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['package.xml'] = utils.read_template(os.path.join(template_dir,'package.xml'))
    templates[os.path.join('scripts',package)] = utils.read_template(os.path.join(template_dir,'scripts','PACKAGE_NAME'))
    templates[os.path.join('src',package,'__init__.py')] = utils.read_template(os.path.join(template_dir,'src','PACKAGE_NAME','__init__.py'))
    return templates

def create_py_package_directory(package):
    p = os.path.abspath(package)
    os.makedirs(p) 
    print("Created package directory " + p)
    os.makedirs(os.path.join(p,"scripts"))
    print("Created package directory " + os.path.join(p,"scripts"))
    os.makedirs(os.path.join(p,"src"))
    print("Created package directory " + os.path.join(p,"src"))
    os.makedirs(os.path.join(p,"src",package))
    print("Created package directory " + os.path.join(p,"src",package))

def get_common_templates(package):
    template_dir = os.path.join(os.path.dirname(__file__),'templates', 'common') 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_dir,'mainpage.dox'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['package.xml'] = utils.read_template(os.path.join(template_dir,'package.xml'))
    return templates

def create_common_package_directory(package):
    p = os.path.abspath(package)
    os.makedirs(p) 
    print("Created package directory " + p)
    
def create_winros_catkin_package():
    (package, depends) = utils.parse_arguments([])
    if 'roscpp' in depends:
        create_cpp_package_directory(package)
        templates = get_cpp_templates(package)
    elif 'rospy' in depends:
        create_py_package_directory(package)
        templates = get_py_templates(package)
    else:
        create_common_package_directory(package)
        templates = get_common_templates(package)
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
    print "\nPlease edit package.xml, mainpage.dox and CMakeLists.txt to finish creating your package."
