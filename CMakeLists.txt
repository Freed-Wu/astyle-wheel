cmake_minimum_required(VERSION 3.10)
# cmake-format: off
set(VERSION 3.4.8 CACHE STRING "version of astyle")
# cmake-format: on
include(ExternalProject)
if(NOT DEFINED SKBUILD_PLATLIB_DIR)
  set(SKBUILD_PLATLIB_DIR ${CMAKE_SOURCE_DIR}/src)
endif()
ExternalProject_Add(
  astyle
  URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz"
  CMAKE_ARGS "-DCMAKE_INSTALL_PREFIX=${SKBUILD_PLATLIB_DIR}/astyle/data"
  USES_TERMINAL_DOWNLOAD 1
  USES_TERMINAL_CONFIGURE 1
  USES_TERMINAL_BUILD 1)
