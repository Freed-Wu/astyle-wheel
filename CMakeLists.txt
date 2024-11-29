cmake_minimum_required(VERSION 3.10)
# cmake-format: off
set(VERSION 3.6.4 CACHE STRING "version of astyle")
# cmake-format: on

include(FetchContent)
FetchContent_Declare(astyle URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz")
FetchContent_MakeAvailable(astyle)

find_package(Python COMPONENTS Development.Module)
if(Python_FOUND)
  set(astyle_dir "${astyle_SOURCE_DIR}/AStyle/src")
  aux_source_directory("${astyle_dir}" sources)
  if(NOT SKBUILD)
    set(Python_SOABI ${SKBUILD_SOABI})
    set(SKBUILD_PLATLIB_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src")
  endif()
  python_add_library(__init__ MODULE "src/astyle/__init__.c" "src/astyle/wrap.cc" "${sources}" WITH_SOABI)
  target_compile_definitions(__init__ PRIVATE ASTYLE_LIB)
  target_include_directories(__init__ PRIVATE "${astyle_dir}")
  install(TARGETS __init__ DESTINATION "${SKBUILD_PLATLIB_DIR}/astyle")
endif()
