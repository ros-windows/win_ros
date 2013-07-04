cmake_minimum_required(VERSION 2.8)
project(msvc_runtime)
find_package(catkin REQUIRED COMPONENTS catkin)
catkin_package()

################################################################
# Macros
################################################################

macro(add_python_batch_helper name)
  if(WIN32)
    set(PYTHON_TARGET ${name})
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/template.bat.in
                        ${CATKIN_DEVEL_PREFIX}/bin/${name}.bat) 
    install(PROGRAMS ${CATKIN_DEVEL_PREFIX}/bin/${PYTHON_TARGET}.bat 
                               DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION})
  endif()
endmacro()

################################################################
# Python Helpers
################################################################

set(USE_BATCH_HELPERS FALSE)

set(NAMES rosbag roscore rosgraph roslaunch rosmaster rosnode 
          rosparam rosservice rosmsg rossrv rostopic rosunit
          roswtf rosrun)

if(${USE_BATCH_HELPERS})
  foreach(name ${NAMES})
    add_python_batch_helper(${name})
  endforeach()
else()  # USE EXE HELPERS
  include_directories(${catkin_INCLUDE_DIRS})
  add_subdirectory(src)
endif()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}) 
