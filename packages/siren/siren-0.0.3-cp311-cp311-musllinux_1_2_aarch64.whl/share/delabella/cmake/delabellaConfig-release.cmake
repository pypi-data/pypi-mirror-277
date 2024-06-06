#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "delabella" for configuration "Release"
set_property(TARGET delabella APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(delabella PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/./libdelabella.so"
  IMPORTED_SONAME_RELEASE "libdelabella.so"
  )

list(APPEND _cmake_import_check_targets delabella )
list(APPEND _cmake_import_check_files_for_delabella "${_IMPORT_PREFIX}/./libdelabella.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
