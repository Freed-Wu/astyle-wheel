cmake_minimum_required(VERSION 3.10)
set(VERSION 3.3)
include(ExternalProject)
ExternalProject_Add(
  astyle
  URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz"
  INSTALL_COMMAND ""
  USES_TERMINAL_DOWNLOAD 1
  USES_TERMINAL_CONFIGURE 1
  USES_TERMINAL_BUILD 1)
if(DEFINED SKBUILD_PLATLIB_DIR)
  set(DESTDIR ${SKBUILD_PLATLIB_DIR}/astyle/data/)
else()
  set(DESTDIR ${CMAKE_SOURCE_DIR}/src/astyle/data/)
endif()
include(GNUInstallDirs)
install(
  PROGRAMS
    ${CMAKE_BINARY_DIR}/astyle-prefix/src/astyle-build/AStyle/astyle${CMAKE_EXECUTABLE_SUFFIX}
  DESTINATION ${DESTDIR}${CMAKE_INSTALL_BINDIR})
install(FILES ${CMAKE_BINARY_DIR}/astyle-prefix/src/astyle/AStyle/man/astyle.1
        DESTINATION ${DESTDIR}${CMAKE_INSTALL_MANDIR})
