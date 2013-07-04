##############################################################################
# CMake
##############################################################################

# set(CMAKE_VERBOSE_MAKEFILE TRUE)

##############################################################################
# Catkin
##############################################################################

project(%(package)s)

catkin_project(%(package)s
  INCLUDE_DIRS include
  DEPENDS %(cmake_depends)s
)

# Include actionlib_msgs as a dependency if adding actions
# Move this call to stack.xml if you are calling find_package on a particular
# component alot.
find_package(ROS REQUIRED COMPONENTS genmsg std_msgs)

include_directories(include)

##############################################################################
# Sources
##############################################################################

add_message_files(
  DIRECTORY msg
  FILES
  Dude.msg
)

add_service_files(
  DIRECTORY srv
  FILES HelloDude.srv
)

#add_action_files(
#  DIRECTORY action
#  FILES FooBar.action
#)

# Include actionlib_msgs as a dependency if adding actions
generate_messages(DEPENDENCIES std_msgs %(cmake_depends)s)

##############################################################################
# Install
##############################################################################

install(DIRECTORY include/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h"
        PATTERN ".svn" EXCLUDE
        PATTERN ".git" EXCLUDE)
