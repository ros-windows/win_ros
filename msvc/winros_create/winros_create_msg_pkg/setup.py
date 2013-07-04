from distutils.core import setup

import sys
sys.path.insert(0, 'src')

#from qt_create import __version__

setup(name='winros_create_msg_pkg',
#      version= __version__,
      version= '0.1.0',
      packages=['winros_create_msg_pkg'],
      package_dir = {'':'src'},
      scripts = ["scripts/winros_create_msg_pkg"],
      package_data = {'winros_create_msg_pkg': [
           'templates/comms/CMakeLists.txt',
           'templates/comms/mainpage.dox',
           'templates/comms/package.xml',
           'templates/comms/msg/Dude.msg',
           'templates/comms/srv/HelloDude.srv',
           ]},
      author = "Yeong-il Choe",
      author_email = "yichoe@yujinrobot.com",
      url = "http://www.rog.org/",
      download_url = "https://github.com/ros-windows/win_ros.git",
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License" ],
      description = "Creates catkin message package templates",
      long_description = open('Readme.md').read(),
      license = "BSD"
      )
