#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "aff3ct::aff3ct-static-lib" for configuration "Release"
set_property(TARGET aff3ct::aff3ct-static-lib APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(aff3ct::aff3ct-static-lib PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/aff3ct-ON.lib"
  )

list(APPEND _cmake_import_check_targets aff3ct::aff3ct-static-lib )
list(APPEND _cmake_import_check_files_for_aff3ct::aff3ct-static-lib "${_IMPORT_PREFIX}/lib/aff3ct-ON.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
