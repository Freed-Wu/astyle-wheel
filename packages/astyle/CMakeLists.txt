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
FetchContent_Declare(astyle URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz")
FetchContent_MakeAvailable(astyle)
