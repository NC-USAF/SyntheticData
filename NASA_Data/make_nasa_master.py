# -*- coding: utf-8 -*-
"""
make_nasa_master.py - A program to make a CSV file with all aircraft
position data available for generating synthentic flight test files.

Created on Tue Nov 29 16:49 2022

@author: Nathan Christiansen
"""

import sys
import os
import argparse

import nasa_mat

# ---------------------------------------------------------------------------
# Main routine
# -----------------------------------------------------------------------------

# make_nasa_ac_nav_csv.py <data dir> <filename.mat>
#
#   <data dir>     - Matlab data directory to process.
#   <filename.mat> - Specific Matlab file to process. If not specified
#                    then all file in <data dir> are processed.

if __name__=='__main__':

    # set up an argument parser to simplify usage
    # parser = argparse.ArgumentParser(description="Convert NASA matlab flight data to csv format")
    # parser.add_argument('data_dir', metavar="Dataset root",nargs=1,type=str,help="Parent directory containing matlab file directory and csv output directory")
    # parser.add_argument('input_files',)

    # Make our NASA Matlab class    
    nm = nasa_mat.NasaMat()
    
    # Setup directories and file names
    root_data_dir  = "./"
    dataset_dir    = None
    data_file_list = None


    # Get the working directory name
    if len(sys.argv) >= 2:
        dataset_dir = sys.argv[1] + "/"
        
    matlab_data_dir = os.path.join(dataset_dir,"Matlab/")
    csv_data_dir    = os.path.join(dataset_dir,"CSV/")


    # If there is no file names list then make one
    if data_file_list == None:
        data_file_list = os.listdir(matlab_data_dir)

    # Set the output filename extension. Necessary to check if output file
    # has already been generated so we can skip in that case. Don't forget to
    # choose the appropriate output routine further down.
#   output_filename_ext = ".csv"
#   output_filename_ext = ".parquet"
#   output_filename_ext = ".h5"

    # SynthCh10Gen uses these fields
    # "LATP" "LONP" "ALT" "TAS" "TH" "MH" "PTCH" "ROLL" "AOAC" "VRTG"
    # if not limit_cols:
    #     write_cols = None
    # else:
    write_cols = { 
    'ACID',
    # 'DATE.DAY   ',
    # 'DATE.MONTH ',
    # 'DATE.YEAR  ',
    'DVER_1',
    'DVER_2',
    'ECYC_1',
    'ECYC_2',
    'ECYC_3',
    'ECYC_4',
    'EHRS_1',
    'EHRS_2',
    'EHRS_3',
    'EHRS_4',
    'ESN_1',
    'ESN_2',
    'ESN_3',
    'ESN_4',
    'FRMC',
    'A_T',
    'ABRK',
    'ACMT',
    'AIL_1',
    'AIL_2',
    'ALTS',
    'APFD',
    'ATEN',
    'BLV',
    'BPGR_1',
    'BPGR_2',
    'BPYR_1',
    'BPYR_2',
    'CALT',
    'CASS',
    'CRSS',
    'DFGS',
    'DWPT',
    'EAI',
    'ELEV_1',
    'ELEV_2',
    'EVNT',
    'FADF',
    'FADS',
    'FGC3',
    'FIRE_1',
    'FIRE_2',
    'FIRE_3',
    'FIRE_4',
    'FLAP',
    'FQTY_1',
    'FQTY_2',
    'FQTY_3',
    'FQTY_4',
    'GLS',
    'GPWS',
    'HDGS',
    'HF1',
    'HF2',
    'HYDG',
    'HYDY',
    'ILSF',
    'LATP',
    'LGDN',
    'LGUP',
    'LMOD',
    'LOC',
    'LONP',
    'MNS',
    'MRK',
    'MW',
    'N1CO',
    'OIP_1',
    'OIP_2',
    'OIP_3',
    'OIP_4',
    'OIPL',
    'OIT_1',
    'OIT_2',
    'OIT_3',
    'OIT_4',
    'PACK',
    'PH',
    'POVT',
    'PTRM',
    'PUSH',
    'SAT',
    'SMKB',
    'SMOK',
    'SNAP',
    'SPL_1',
    'SPL_2',
    'SPLG',
    'SPLY',
    'TAI',
    'TAT',
    'TCAS',
    'TMAG',
    'TMODE',
    'VHF1',
    'VHF2',
    'VHF3',
    'VMODE',
    'VSPS',
    'WAI_1',
    'WAI_2',
    'WOW',
    'WSHR',
    'APUF',
    'CCPC',
    'CCPF',
    'CWPC',
    'CWPF',
    #'GMT.HOUR   ',
    #'GMT.MINUTE ',
    #'GMT.SEC    ',
    'MSQT_1',
    'MSQT_2',
    'PI',
    'PS',
    'PSA',
    'PT',
    'RUDD',
    'RUDP',
    'SHKR',
    'TOCW',
    'ALT',
    'ALTR',
    'AOA1',
    'AOA2',
    'AOAC',
    'AOAI',
    'BAL1',
    'BAL2',
    'CAS',
    'CASM',
    'DA',
    'EGT_1',
    'EGT_2',
    'EGT_3',
    'EGT_4',
    'FF_1',
    'FF_2',
    'FF_3',
    'FF_4',
    'GS',
    'LATG',
    'LONG',
    'MACH',
    'MH',
    'N1_1',
    'N1_2',
    'N1_3',
    'N1_4',
    'N1C',
    'N1T',
    'N2_1',
    'N2_2',
    'N2_3',
    'N2_4',
    'NSQT',
    'PLA_1',
    'PLA_2',
    'PLA_3',
    'PLA_4',
    'TAS',
    'TH',
    'TRK',
    'TRKM',
    'VIB_1',
    'VIB_2',
    'VIB_3',
    'VIB_4',
    'WD',
    'WS',
    'PTCH',
    'RALT',
    'ROLL',
    'VRTG',
    'BLAC',
    'CTAC',
    'FPAC',
    'IVV',
    }

    # Iterate over the list of files to (maybe) process
    file_num = 1
    for data_filename in data_file_list:

        # Split the file name into various components
        (data_filename_base, data_filename_ext) = os.path.splitext(data_filename)
        input_data_filename  = matlab_data_dir + data_filename
        output_data_filename = csv_data_dir + data_filename_base + ".csv"
 
        # Only process if the file is a ".mat"
        if data_filename.endswith(".mat"):

            print("File {0} - {1}".format(file_num, matlab_data_dir + data_filename, end = ''))
            file_num += 1

            # Only process if output file does not exist yet
            if not os.path.isfile(output_data_filename):

                # Read the matlab data and put it into a dictionary
                nm.read_nasa_matlab(input_data_filename, var_names=write_cols)

                # Make a pandas dataframe of flight test data
                nm.make_flight_dataframe()
                
            
                # If no error making flight data then write it out
                if nm.nasa_frame is not None:
    
                    # First upsample to 100 Hz
                    nm.nasa_frame = nm.nasa_frame.resample("10ms").asfreq()


                    counter = 0

                    #this looks at the data structure in nasa_mat and finds if there is a unit of measure for a certain key
                    #if there is, we interpolate. If not, we forward fill
                    for key in nm.nasa_mat.keys():
                        if len(nm.nasa_mat[key][0][0][2]) == 0:
                            nm.nasa_frame[key].ffill(inplace=True)
                            counter +=1
                        else:
                            nm.nasa_frame[key].interpolate(inplace=True)
                            counter +=1


                    # Now downsample to 25 Hz
                    nm.nasa_frame = nm.nasa_frame.resample("40ms").asfreq()
    
                    # Make sure destination directory exists
                    if not os.path.isdir(csv_data_dir):
                        os.mkdir(csv_data_dir)
                    
                    # Write it out
                    print(" - write {0}".format(output_data_filename))
                    nm.nasa_frame.to_csv(output_data_filename,index_label="DATE_TIME",columns=write_cols)
#                   nm.nasa_frame.to_parquet(data_filename_root+output_filename_ext)
#                   nm.nasa_frame.to_hdf(data_filename_root+output_filename_ext, "data_"+data_filename_base, mode="w", complevel=1)
            
                # There was an error converting
    #            else:
    #                print(" - error making dataframe")
                
            # Input file skipped
            else:
                print(" - skipped")

    print("Done!")
