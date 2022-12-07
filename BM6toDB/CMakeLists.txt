cmake_minimum_required(VERSION 3.15)
project(BM6toDB)

if(CMAKE_SOURCE_DIR STREQUAL PROJECT_SOURCE_DIR)
    find_library(LIBSQLITE3 NAMES libsqlite3 sqlite3 libsqlite3.so)
    message(STATUS "LIBSQLITE3 ${LIBSQLITE3}")

    add_subdirectory(../3rdParty ./libs)
endif()

add_executable(bm6todb ./BM6toDB.cpp
    ../SynthCh10Gen/Source_BMNavDB.cpp
    ../SynthCh10Gen/Source_BMNavTxt.cpp
    )
target_include_directories(bm6todb PUBLIC ../SynthCh10Gen)
target_link_libraries(bm6todb PUBLIC ${LIBSQLITE3})
