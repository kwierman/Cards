cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(Cards)


add_subdirectory(Documentation)

include(cmake/FindROOT.cmake)
include(cmake/python.cmake)

file(GLOB sources ${PROJECT_SOURCE_DIR}/*.py)
foreach(source ${sources})
	install(TARGETS source DESTINATION)
endforeach()

#TODOs:
#1. make sure that this compiles each of the modules in their final destination