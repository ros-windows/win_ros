##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 2.8.0)
project(%(package)s)

##############################################################################
# Catkin
##############################################################################

find_package(catkin REQUIRED COMPONENTS %(cmake_depends)s)

include_directories(include)
include_directories(${catkin_INCLUDE_DIRS})

catkin_package(
	INCLUDE_DIRS include
	LIBRARIES %(package)s
	CATKIN_DEPENDS %(cmake_depends)s
)

##############################################################################
# Sources
##############################################################################

add_subdirectory(src)

##############################################################################
# Additional Installs
##############################################################################

install(DIRECTORY include/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp"
        PATTERN ".svn" EXCLUDE
        )
