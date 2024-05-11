cmake_minimum_required(VERSION 3.14)
project(PyOpenHC LANGUAGES CXX)

if(NOT DEFINED _DISABLE_INSTALLATION)
  set(_DISABLE_INSTALLATION FALSE)

  macro(install)
    if(NOT _DISABLE_INSTALLATION)
      _install(${ARGN})
    endif()
  endmacro()
endif()

set(_DISABLE_INSTALLATION TRUE)
add_subdirectory(OpenCC)
set(_DISABLE_INSTALLATION FALSE)

set(PYOPENHC ${CMAKE_CURRENT_SOURCE_DIR}/pyopenhc)
install(TARGETS
  libopencc
  LIBRARY DESTINATION ${PYOPENHC} # shared libraries
  RUNTIME DESTINATION ${PYOPENHC} # shared libraries for windows
  # ARCHIVE DESTINATION ${PYOPENHC} # static libraries
)

install(DIRECTORY
  ${CMAKE_CURRENT_BINARY_DIR}/OpenCC/data/
  ${CMAKE_CURRENT_SOURCE_DIR}/OpenCC/data/config/
  DESTINATION ${PYOPENHC}/data
  FILES_MATCHING PATTERN "*.ocd2" PATTERN "*.json"
  PATTERN "CMakeFiles" EXCLUDE
)
