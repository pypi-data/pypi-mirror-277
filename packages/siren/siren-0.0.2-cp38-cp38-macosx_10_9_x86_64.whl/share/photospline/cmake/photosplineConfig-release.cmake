#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "photospline" for configuration "Release"
set_property(TARGET photospline APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(photospline PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/./libphotospline.2.1.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libphotospline.2.dylib"
  )

list(APPEND _cmake_import_check_targets photospline )
list(APPEND _cmake_import_check_files_for_photospline "${_IMPORT_PREFIX}/./libphotospline.2.1.0.dylib" )

# Import target "cphotospline" for configuration "Release"
set_property(TARGET cphotospline APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(cphotospline PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/./libcphotospline.2.1.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libcphotospline.2.dylib"
  )

list(APPEND _cmake_import_check_targets cphotospline )
list(APPEND _cmake_import_check_files_for_cphotospline "${_IMPORT_PREFIX}/./libcphotospline.2.1.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
