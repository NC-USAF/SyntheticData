cmake_minimum_required(VERSION 3.15)
project(csvparser)
option (CSVTEST "create csv test program " OFF)


add_library(csvparser STATIC csv_parser.cpp)
target_include_directories(csvparser PUBLIC .)

if (CSVTEST)
    add_executable(csvparser_test csv_parser.cpp test.cpp)
endif()


