# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_moveit_resources_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED moveit_resources_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(moveit_resources_FOUND FALSE)
  elseif(NOT moveit_resources_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(moveit_resources_FOUND FALSE)
  endif()
  return()
endif()
set(_moveit_resources_CONFIG_INCLUDED TRUE)

# output package information
if(NOT moveit_resources_FIND_QUIETLY)
  message(STATUS "Found moveit_resources: 3.1.1 (${moveit_resources_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'moveit_resources' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT moveit_resources_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(moveit_resources_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${moveit_resources_DIR}/${_extra}")
endforeach()
