#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SIREN" for configuration "Release"
set_property(TARGET SIREN APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SIREN PROPERTIES
  IMPORTED_LOCATION_RELEASE "/tmp/downloads/local/lib/libSIREN.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libSIREN.dylib"
  )

list(APPEND _cmake_import_check_targets SIREN )
list(APPEND _cmake_import_check_files_for_SIREN "/tmp/downloads/local/lib/libSIREN.dylib" )

# Import target "delabella" for configuration "Release"
set_property(TARGET delabella APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(delabella PROPERTIES
  IMPORTED_LOCATION_RELEASE "/tmp/downloads/local/lib/libdelabella.dylib"
  IMPORTED_SONAME_RELEASE "libdelabella.dylib"
  )

list(APPEND _cmake_import_check_targets delabella )
list(APPEND _cmake_import_check_files_for_delabella "/tmp/downloads/local/lib/libdelabella.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
