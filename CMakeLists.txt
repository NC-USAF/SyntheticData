cmake_minimum_required(VERSION 3.16)
project(synthetic-data)

find_library(LIBSQLITE3 NAMES libsqlite3 sqlite3 libsqlite3.so)
message(STATUS "LIBSQLITE3 ${LIBSQLITE3}")

add_compile_definitions(ARINC429_BUS_SPEED_LOW)
add_compile_definitions(COMPILE_NASA)
add_compile_definitions(LINUX_BUILD)

add_subdirectory(3rdParty)
add_subdirectory(BM6toDB)
add_subdirectory(SynthCh10Gen)

