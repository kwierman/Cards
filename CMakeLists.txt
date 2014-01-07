cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(Cards)

add_subdirectory(Documentation)

include(cmake/FindROOT.cmake)
include(cmake/python.cmake)

file(GLOB sources ${PROJECT_SOURCE_DIR}/Source/*.py)
python_add_packages( ${sources} )
file(GLOB scripts ${PROJECT_SOURCE_DIR}/Scripts/*.py)
python_add_scripts( ${scripts} )
