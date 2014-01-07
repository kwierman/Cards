#macros for 
#
#macro(add_python_target tgt)
#  foreach(file ${ARGN})
#    set(OUT ${CMAKE_CURRENT_BINARY_DIR}/Source/${file}.pyc)
#    list(APPEND OUT_FILES ${OUT})
#    add_custom_command(OUTPUT ${OUT}
#        COMMAND python -mcompileall ${file}.py)
#  endforeach()
#  add_custom_target(${tgt} ALL
#    DEPENDS ${OUT_FILES} )
#endmacro()


macro(python_add_packages)
  foreach(file ${ARGN})
  	message(${file})
  endforeach()
endmacro()

macro(python_add_scripts)
  foreach(file ${ARGN})
  	message(${file})
  endforeach()
endmacro()