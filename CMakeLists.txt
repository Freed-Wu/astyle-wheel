cmake_minimum_required(VERSION 3.10)
# cmake-format: off
set(VERSION 3.4.13 CACHE STRING "version of astyle")
# cmake-format: on

include(FetchContent)
FetchContent_Declare(astyle URL "https://gitlab.com/saalen/astyle/-/archive/${VERSION}/astyle-${VERSION}.tar.gz")
FetchContent_MakeAvailable(astyle)
