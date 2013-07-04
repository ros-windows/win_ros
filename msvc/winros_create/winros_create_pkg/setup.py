from distutils.core import setup

import sys
sys.path.insert(0, 'src')

#from qt_create import __version__

setup(name='winros_create_pkg',
#      version= __version__,
      version= '0.1.0',
      packages=['winros_create_pkg'],
      package_dir = {'':'src'},
      scripts = ["scripts/winros_create_pkg"],
      package_data = {'winros_create_pkg': [
           'templates/cpp/CMakeLists.txt',
           'templates/cpp/mainpage.dox',
           'templates/cpp/package.xml',
           'templates/cpp/include/PACKAGE_NAME/package_name.hpp',
           'templates/cpp/src/CMakeLists.txt',
           'templates/cpp/src/main.cpp',
           'templates/cpp/src/lib/CMakeLists.txt',
           'templates/cpp/src/lib/package_name.cpp',
           'templates/py/CMakeLists.txt',
           'templates/py/mainpage.dox',
           'templates/py/package.xml',
           'templates/py/scripts/PACKAGE_NAME',
           'templates/py/src/PACKAGE_NAME/__init__.py',
           'templates/common/CMakeLists.txt',
           'templates/common/mainpage.dox',
           'templates/common/package.xml',
           ]},
      author = "Yeong-il Choe",
      author_email = "yichoe@yujinrobot.com",
      url = "http://www.rog.org/",
      download_url = "https://github.com/ros-windows/win_ros.git",
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License" ],
      description = "Creates catkin package templates",
      long_description = open('Readme.md').read(),
      license = "BSD"
      )
