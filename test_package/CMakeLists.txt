cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 17)

find_package(Threads REQUIRED)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(basic_demo basic_demo.cpp demo.cpp track_objects.cpp cross_thread_calls.cpp)

target_link_libraries(basic_demo 
  PRIVATE ${CONAN_LIBS} Threads::Threads)

