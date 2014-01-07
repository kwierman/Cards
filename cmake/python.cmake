
set(PYTHON_BUILD_FILES)
set(PYTHON_INSTALL_FILES)

#adding a package puts it onto the list of things to be copied over and compiled with
#the python compile command at the build stage since python is stop level, it should be 
macro(python_add_packages)
  foreach(file ${ARGN})
    GET_FILENAME_COMPONENT(STRIPPED_NAME ${file} NAME_WE )
    set(BINARY_OUT ${CMAKE_CURRENT_BINARY_DIR}/Source/${STRIPPED_NAME}.pyc)
    SET(OUTNAME ${CMAKE_CURRENT_BINARY_DIR}/Source/${STRIPPED_NAME}.pyc)
    add_custom_command(OUTPUT ${OUTNAME}
	    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_CURRENT_BINARY_DIR}/Source/
	    COMMAND ${CMAKE_COMMAND} -E copy ${file} ${CMAKE_CURRENT_BINARY_DIR}/Source/${STRIPPED_NAME}.py
	    COMMAND python -mcompileall ${CMAKE_CURRENT_BINARY_DIR}/Source/
	    COMMENT "Copying Files over"
  		VERBATIM
    )
    list(APPEND PYTHON_BUILD_FILES ${OUTNAME})
    add_custom_command(OUTPUT ${CMAKE_INSTALL_PREFIX}/${STRIPPED_NAME}.pyc
  		COMMAND ${CMAKE_COMMAND} -E copy ${BINARY_OUT} ${CMAKE_INSTALL_PREFIX}/${STRIPPED_NAME}.pyc
	)
	list(APPEND PYTHON_INSTALL_FILES ${CMAKE_INSTALL_PREFIX}/${STRIPPED_NAME}.pyc)
  endforeach()
endmacro()

macro(python_add_scripts)
  foreach(file ${ARGN})
    GET_FILENAME_COMPONENT(STRIPPED_NAME ${file} NAME_WE )
    add_custom_command(OUTPUT ${CMAKE_INSTALL_PREFIX}/Scripts/${STRIPPED_NAME}.py
	    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_INSTALL_PREFIX}/Scripts/
  		COMMAND ${CMAKE_COMMAND} -E copy ${file} ${CMAKE_INSTALL_PREFIX}/Scripts/${STRIPPED_NAME}.py
	)
	list(APPEND PYTHON_INSTALL_FILES ${CMAKE_INSTALL_PREFIX}/Scripts/${STRIPPED_NAME}.py)
  endforeach()
endmacro()


macro(python_build)
	add_custom_target(python_build
		DEPENDS ${PYTHON_BUILD_FILES}
	  	COMMENT "Compiling Python binaries" VERBATIM	
	)
endmacro()
macro(python_install)
	add_custom_target(python_install
		DEPENDS python_build ${PYTHON_INSTALL_FILES}
		COMMENT "Installing Python binaries and scripts" VERBATIM
	)	
endmacro()


