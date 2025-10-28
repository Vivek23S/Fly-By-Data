# ============================================================================
# File Name:        sam_sensor.py
# Author:           Vivek23
# Description:      sample file
# Notes:            if any error comes try to put everything in same folder
# ============================================================================

import sys
sys.path.insert(0,".\main libraries") # folder which has main loading libs
import senlab

# ------------------ Loading Sensor Data From Single '.csv' File ------------------

filename    = '2024_3_25_16_41_41.csv'
path        = r'E:\I I T M\R E S E A R C H\S C R I P T S\Fly-By-Data\sample_sensor'
filename    = '//'.join(path.split('\\')[:]) + '//' + filename

offset = 408        # update this based on the data point at which data aligns
length = 10000      # update this based on the particular mission (log file) with 'len(data['XKF1_0']['Roll'])'

data = senlab.tsm_data_offset(filename,offset,length)

wind = data['Wind Speed (m/s)']
wind_2d = data['2D Wind Speed (m/s)']
direction = data['Horizontal Wind Direction (Degrees)']

# ------------------ Loading Sensor Data From Multiple '.csv' Files ------------------

filenames = ['2024_3_25_16_41_41.csv',
             '2024_3_27_11_34_7.csv']

path      = r'E:\I I T M\R E S E A R C H\S C R I P T S\Fly-By-Data\sample_sensor'

for i in range(len(filenames)):
    filenames[i] = '//'.join(path.split('\\')[:]) + '//' + filenames[i]

offsets = [408,660]
lengths = [10000,10000]

data = senlab.multiple_tsm_data_offset(filenames,offsets,lengths)

wind_1 = data[0]['Wind Speed (m/s)'] # data from 1st file
wind_2 = data[1]['Wind Speed (m/s)'] # data from 2nd file

wind_2d_1 = data[0]['2D Wind Speed (m/s)'] # data from 1st file
wind_2d_2 = data[1]['2D Wind Speed (m/s)'] # data from 2nd file

direction_1 = data[0]['Horizontal Wind Direction (Degrees)'] # data from 1st file
direction_2 = data[1]['Horizontal Wind Direction (Degrees)'] # data from 2nd file