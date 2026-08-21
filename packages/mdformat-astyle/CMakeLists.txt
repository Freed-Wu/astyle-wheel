cmake_minimum_required(VERSION 3.15)
set(VERSION 3.6.18 CACHE STRING "version of astyle")
project(
  astyle-wheel
  VERSION "${VERSION}"
  DESCRIPTION "Artistic Style is a source code indenter, formatter, and beautifier for the C, C++, C++/CLI, Objective‑C, C# and Java programming languages"
  HOMEPAGE_URL http://astyle.sourceforge.net)
# https://gitlab.com/saalen/astyle/-/issues/51
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

include(FetchContent)
if(SKBUILD)
  # https://scikit-build-core.readthedocs.io/en/latest/cmakelists.html #finding-python
  set(Python_SOABI ${SKBUILD_SOABI})
  set(SKBUILD_SCRIPTS_DIR "${SKBUILD_NULL_DIR}")
else()
  set(SKBUILD_PLATLIB_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src")
endif()
FetchContent_Declare(astyle URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz")
FetchContent_MakeAvailable(astyle)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
set(astyle_dir "${astyle_SOURCE_DIR}/AStyle/src")
aux_source_directory("${astyle_dir}" sources)
find_package(Cython MODULE REQUIRED VERSION 3.0)
include(UseCython)
# https://github.com/elijahr/python-autopxd2/issues/54
find_program(autopxd NAMES autopxd REQUIRED)
execute_process(COMMAND "${autopxd}" "${CMAKE_CURRENT_SOURCE_DIR}/src/astyle/wrap.h" "${CMAKE_CURRENT_BINARY_DIR}/wrap.pxd")
configure_file(src/astyle/binding.pyi src/astyle/binding.py COPYONLY)
cython_transpile("${CMAKE_BINARY_DIR}/src/astyle/binding.py"
  CYTHON_ARGS "-3I${CMAKE_CURRENT_BINARY_DIR}" LANGUAGE C OUTPUT "${CMAKE_BINARY_DIR}/binding.c")
python_add_library(binding MODULE "${CMAKE_BINARY_DIR}/binding.c" src/astyle/wrap.cc "${sources}" WITH_SOABI)
target_compile_definitions(binding PRIVATE ASTYLE_LIB)
target_include_directories(binding PRIVATE "${astyle_dir}")
install(TARGETS binding DESTINATION "${SKBUILD_PLATLIB_DIR}/astyle")
install(FILES src/astyle/mdformat.py src/astyle/binding.pyi src/astyle/py.typed DESTINATION "${SKBUILD_PLATLIB_DIR}/astyle")
