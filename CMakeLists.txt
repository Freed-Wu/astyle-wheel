cmake_minimum_required(VERSION 3.10)
# cmake-format: off
set(VERSION 3.4.8 CACHE STRING "version of astyle")
# cmake-format: on

include(FetchContent)
FetchContent_Declare(astyle URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz")
FetchContent_MakeAvailable(astyle)

if(DEFINED SKBUILD_NULL_DIR)
  set(CMAKE_INSTALL_PREFIX ${SKBUILD_NULL_DIR})
endif()
include(GNUInstallDirs)
if(NOT DEFINED SKBUILD_DATA_DIR)
  set(SKBUILD_DATA_DIR ${CMAKE_INSTALL_FULL_DATADIR})
endif()
if(NOT DEFINED SKBUILD_SCRIPTS_DIR)
  set(SKBUILD_SCRIPTS_DIR ${CMAKE_INSTALL_FULL_BINDIR})
endif()
install(TARGETS astyle DESTINATION ${SKBUILD_SCRIPTS_DIR})
install(FILES ${astyle_SOURCE_DIR}/AStyle/doc/astyle.html ${astyle_SOURCE_DIR}/AStyle/doc/install.html
              ${astyle_SOURCE_DIR}/AStyle/doc/news.html ${astyle_SOURCE_DIR}/AStyle/doc/notes.html
              ${astyle_SOURCE_DIR}/AStyle/doc/styles.css DESTINATION ${SKBUILD_DATA_DIR}/share/doc/astyle/html)
install(FILES ${astyle_SOURCE_DIR}/AStyle/man/astyle.1 DESTINATION ${SKBUILD_DATA_DIR}/share/man/man1)
