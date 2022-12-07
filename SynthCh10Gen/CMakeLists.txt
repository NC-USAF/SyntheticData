cmake_minimum_required(VERSION 3.15)

project(SynthCh10Gen)

if(CMAKE_SOURCE_DIR STREQUAL PROJECT_SOURCE_DIR)
     # I am top-level project.
    find_library(LIBSQLITE3 NAMES libsqlite3 sqlite3 libsqlite3.so)
    message(STATUS "LIBSQLITE3 ${LIBSQLITE3}")

    add_subdirectory(../3rdParty ./libs)
else()
    # I am called from other project with add_subdirectory().
endif()


add_executable(synth_ch10gen
    Ch10Format_1553.cpp
    Ch10Format_1553_Nav.cpp
    Ch10Format_A429_AR100.cpp
    Ch10Format_A429.cpp
    Ch10Format_PCM.cpp
    Ch10Writer_1553.cpp
    Ch10Writer_A429.cpp
    Ch10Writer_Index.cpp
    Ch10Writer_PCM.cpp
    Ch10Writer_Time.cpp
    Ch10Writer_Video.cpp
    Source_BMNavDB.cpp
    Source_BMNavTxt.cpp
    Source_NasaNavTxt.cpp
    Source_VideoDB.cpp
    Source_CsvTxt.cpp
    SynthCh10Gen.cpp)

target_link_libraries(synth_ch10gen PUBLIC irig106 csvparser)
target_link_libraries(synth_ch10gen PUBLIC ${LIBSQLITE3})
