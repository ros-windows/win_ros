cmake_minimum_required(VERSION 2.8.3)
project(rosrun)
find_package(catkin)
catkin_package()

catkin_python_setup()

install(PROGRAMS scripts/rosrun
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
