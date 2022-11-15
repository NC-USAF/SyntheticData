cmake_minimum_required(VERSION 3.15)

project(irig106)

add_library(irig106 STATIC
./src/i106_data_stream.c
./src/i106_decode_1553f1.c
./src/i106_decode_16pp194.c
./src/i106_decode_arinc429.c
./src/i106_decode_can.c
./src/i106_decode_discrete.c
./src/i106_decode_ethernet.c
./src/i106_decode_index.c
./src/i106_decode_pcmf1.c
./src/i106_decode_time.c
./src/i106_decode_tmats_b.c
./src/i106_decode_tmats_c.c
./src/i106_decode_tmats_d.c
./src/i106_decode_tmats_g.c
./src/i106_decode_tmats_m.c
./src/i106_decode_tmats.c
./src/i106_decode_tmats_p.c
./src/i106_decode_tmats_r.c
./src/i106_decode_uart.c
./src/i106_decode_video.c
./src/i106_index.c
./src/i106_time.c
./src/irig106ch10.c
./src/sha-256.c
)

target_compile_definitions(irig106
    PRIVATE
    _FILE_OFFSET_BITS=64
    _LARGEFILE64_SOURCE
    IRIG_NETWORKING
    SHA256ENABLE
    )
target_include_directories(irig106 PUBLIC ./src)
set_property(TARGET irig106 PROPERTY POSITION_INDEPENDENT_CODE ON)



#i106_data_stream.o: $(SRC_DIR)/i106_data_stream.c
#i106_decode_1553f1.o: $(SRC_DIR)/i106_decode_1553f1.c
#i106_decode_16pp194.o: $(SRC_DIR)/i106_decode_16pp194.c
#i106_decode_analogf1.o: $(SRC_DIR)/i106_decode_analogf1.c
#i106_decode_arinc429.o: $(SRC_DIR)/i106_decode_arinc429.c
#i106_decode_can.o: $(SRC_DIR)/i106_decode_can.c
#i106_decode_discrete.o: $(SRC_DIR)/i106_decode_discrete.c
#i106_decode_ethernet.o: $(SRC_DIR)/i106_decode_ethernet.c
#i106_decode_index.o: $(SRC_DIR)/i106_decode_index.c
#i106_decode_pcmf1.o: $(SRC_DIR)/i106_decode_pcmf1.c
#i106_decode_time.o: $(SRC_DIR)/i106_decode_time.c
#i106_decode_tmats_b.o: $(SRC_DIR)/i106_decode_tmats_b.c
#i106_decode_tmats_c.o: $(SRC_DIR)/i106_decode_tmats_c.c
#i106_decode_tmats_d.o: $(SRC_DIR)/i106_decode_tmats_d.c
#i106_decode_tmats_g.o: $(SRC_DIR)/i106_decode_tmats_g.c
#i106_decode_tmats_m.o: $(SRC_DIR)/i106_decode_tmats_m.c
#i106_decode_tmats.o:   $(SRC_DIR)/i106_decode_tmats.c
#i106_decode_tmats_p.o: $(SRC_DIR)/i106_decode_tmats_p.c
#i106_decode_tmats_r.o: $(SRC_DIR)/i106_decode_tmats_r.c
#i106_decode_uart.o: $(SRC_DIR)/i106_decode_uart.c
#i106_decode_video.o: $(SRC_DIR)/i106_decode_video.c
#i106_index.o:  $(SRC_DIR)/i106_index.c
#i106_time.o:   $(SRC_DIR)/i106_time.c
#irig106ch10.o: $(SRC_DIR)/irig106ch10.c
#sha-256.o: $(SRC_DIR)/sha-256.c
