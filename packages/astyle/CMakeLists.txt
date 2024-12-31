cmake_minimum_required(VERSION 3.15)
# cmake-format: off
set(VERSION 3.6.6 CACHE STRING "version of astyle")
# cmake-format: on
project(
  astyle-wheel
  VERSION "${VERSION}"
  DESCRIPTION "wheel for astyle"
  HOMEPAGE_URL https://github.com/Freed-Wu/astyle-wheel)
# https://gitlab.com/saalen/astyle/-/issues/51
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

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
  find_package(Cython MODULE REQUIRED VERSION 3.0)
  include(UseCython)
  # https://github.com/elijahr/python-autopxd2/issues/54
  find_program(autopxd NAMES autopxd REQUIRED)
  execute_process(COMMAND "${autopxd}" "${CMAKE_CURRENT_SOURCE_DIR}/src/astyle/wrap.h" "${CMAKE_CURRENT_BINARY_DIR}/wrap.pxd")
  cython_transpile(src/astyle/__init__.py
    CYTHON_ARGS "-3I${CMAKE_CURRENT_BINARY_DIR}" LANGUAGE C OUTPUT_VARIABLE output)
  python_add_library(__init__ MODULE "${output}" src/astyle/wrap.cc "${sources}" WITH_SOABI)
  target_compile_definitions(__init__ PRIVATE ASTYLE_LIB)
  target_include_directories(__init__ PRIVATE "${astyle_dir}")
  install(TARGETS __init__ DESTINATION "${SKBUILD_PLATLIB_DIR}/astyle")
else()
  message(FATAL "Skip cython extension building")
endif()
