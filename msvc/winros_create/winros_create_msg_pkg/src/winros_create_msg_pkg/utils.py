
import os
import re
from optparse import OptionParser
import rospkg

##################
# Author
##################

def author_name():
    """
    Utility to compute logged in user name
    
    :returns: name of current user, ``str``
    """
    import getpass
    name = getpass.getuser()
    try:
        import pwd
        login = name
        name = pwd.getpwnam(login)[4]
        name = ''.join(name.split(',')) # strip commas
        # in case pwnam is not set
        if not name:
            name = login
    except:
        #pwd failed
        pass
    if type(name) == str:
        name = name.decode('utf-8')
    return name

##################
# Templates
##################

# Finds and reads one of the templates.
def read_template(tmplf):
    f = open(tmplf, 'r')
    try:
        t = f.read()
    finally:
        f.close()
    return t

# This inserts the labelled variables into the template wherever the corresponding
# %package, %description %package_depends and %cmake_depends is found.
def instantiate_template(template, package, description, author, package_depends, cmake_depends):
    return template%locals()

##################
# Names
##################

# These routines are originally from roslib
# Todo: might be nice if they were in rospkg, not here.

BASE_RESOURCE_NAME_LEGAL_CHARS_P = re.compile('^[A-Za-z][\w_]*$') #ascii char followed by (alphanumeric, _)
def is_legal_resource_base_name(name):
    """
    Validates that name is a legal resource base name. A base name has
    no package context, e.g. "String".
    """
    # resource names can be unicode due to filesystem
    if name is None:
        return False
    m = BASE_RESOURCE_NAME_LEGAL_CHARS_P.match(name)
    return m is not None and m.group(0) == name

##################
# Argument Parser
##################

def parse_arguments(extra_depends=[]):
	"""
	Parse the command line arguments - in format <package-name> [dependencies]".

	This will need to upgrade from optparse to argparse post python 2.7 
	"""
	parser = OptionParser(usage="usage: %prog <package-name> [dependencies...]")
	options, args = parser.parse_args()
	if not args:
		parser.error("You must specify a package name and optionally also list package dependencies")
	package = args[0]
	if type(package) == str:
		package = package.decode('utf-8')
	depends = args[1:] + extra_depends

	if not is_legal_resource_base_name(package):
		parser.error("illegal package name [%s]\n\nNames must start with a letter and contain only alphanumeric characters\nand underscores."%package)
	if os.path.exists(os.path.abspath(package)):
		parser.error("%s already exists, aborting"%package)

	return (package,depends)
