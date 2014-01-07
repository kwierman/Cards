cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(Cards)

if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
    message(STATUS "CARDS requires an out-of-source build.")
    message(STATUS "Please remove these files from ${CMAKE_BINARY_DIR} first:")
    message(STATUS "CMakeCache.txt")
    message(STATUS "CMakeFiles")
    message(STATUS "Once these files are removed, create a separate directory")
    message(STATUS "and run CMake from there")
    message(FATAL_ERROR "in-source build detected")
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install" CACHE PATH "Install path prefix, prepended onto install directories." FORCE)
endif()

add_subdirectory(Documentation)

include(cmake/FindROOT.cmake)
include(cmake/python.cmake)

file(GLOB sources ${PROJECT_SOURCE_DIR}/Source/*.py)
python_add_packages( ${sources} )
file(GLOB scripts ${PROJECT_SOURCE_DIR}/Scripts/*.py)
python_add_scripts( ${scripts} )

python_build()
python_install()


configure_file(cardEnv.sh "${CMAKE_INSTALL_PREFIX}/cardEnv.sh" @ONLY)