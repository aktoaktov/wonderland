cmake_minimum_required(VERSION 4.0)
project(garage)

set(CMAKE_CXX_STANDARD 14)

add_library(arithmetic/montgomery STATIC montgomery.h)
target_include_directories(montgomery PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(garage
        test2.cpp
        test.cpp
        arithmetic/montgomery.h
        constants.h
)
