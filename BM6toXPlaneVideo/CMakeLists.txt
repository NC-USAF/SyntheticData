cmake_minimum_required(VERSION 3.15)
project(BM6toXPlaneVideo)

find_library(LIBSQLITE3 NAMES libsqlite3 sqlite3 libsqlite3.so)

message("LIBSQLITE3 ${LIBSQLITE3}")


add_executable(bm6toxplanevideo
    ./BM6toXPlaneVideo.cpp
    ./DXGIManager.cpp
    ./MpegEncoder.cpp
    ../SynthCh10Gen/Source_BMNavDB.cpp
    ../SynthCh10Gen/Source_BMNavTxt.cpp
    ../XPlaneControl/XPlaneControl.cpp
    )
target_include_directories(bm6toxplanevideo
    PUBLIC
    ../SynthCh10Gen
    ../XPlaneControl)

target_link_libraries(bm6toxplanevideo PUBLIC ${LIBSQLITE3})
