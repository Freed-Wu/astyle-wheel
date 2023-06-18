cmake_minimum_required(VERSION 3.10)
# cmake-format: off
set(VERSION 3.3.1 CACHE STRING "version of astyle")
# cmake-format: on
include(ExternalProject)
ExternalProject_Add(
  astyle
  URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz"
  INSTALL_COMMAND ""
  USES_TERMINAL_DOWNLOAD 1
  USES_TERMINAL_CONFIGURE 1
  USES_TERMINAL_BUILD 1)
if(NOT DEFINED SKBUILD_PLATLIB_DIR)
  set(SKBUILD_PLATLIB_DIR ${CMAKE_SOURCE_DIR}/src)
endif()
if(NOT DEFINED SKBUILD_DATA_DIR)
  set(SKBUILD_DATA_DIR ${CMAKE_INSTALL_PREFIX}/share)
endif()
include(GNUInstallDirs)
install(PROGRAMS ${CMAKE_BINARY_DIR}/astyle-prefix/src/astyle-build/AStyle/astyle${CMAKE_EXECUTABLE_SUFFIX}
        DESTINATION ${SKBUILD_PLATLIB_DIR}/astyle/data/${CMAKE_INSTALL_BINDIR})
install(FILES ${CMAKE_BINARY_DIR}/astyle-prefix/src/astyle/AStyle/man/astyle.1
        DESTINATION ${SKBUILD_DATA_DIR}/${CMAKE_INSTALL_MANDIR}/man1)
