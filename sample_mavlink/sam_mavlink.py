# ============================================================================
# File Name:        sam_mavlink.py
# Author:           Vivek23
# Description:      sample file
# Notes:            if any error comes try to put everything in same folder
# ============================================================================

import sys
sys.path.insert(0,".\main libraries") # folder which has main loading libs
import mavlab


# ------------------ Loading Mavlink Data From Single '.mat' File ------------------

filename = '2024-03-25 16-42-23.bin-792718.mat'
path      = r'E:\I I T M\R E S E A R C H\S C R I P T S\Fly-By-Data\sample_mavlink'
filename  = '//'.join(path.split('\\')[:]) + '//' + filename

params = ['AHR2','ATT','BARO_0','BAT_0','GPS_0','XKF1_0','RATE','RCOU'] # for more options refer to 'parameters.html'

data = mavlab.data(filename,params)
time = mavlab.timedata_gpscor(filename,params)

roll        = data['XKF1_0']['Roll']
pitch       = data['XKF1_0']['Pitch']
yaw         = data['XKF1_0']['Yaw']
altitude    = -1 * data['XKF1_0']['PD']


# ------------------ Loading Mavlink Data From Multiple '.mat' Files ------------------

filenames = ['2024-03-25 16-42-23.bin-792718.mat',
             '2024-03-27 11-35-14.bin-1011046.mat']

path      = r'E:\I I T M\R E S E A R C H\S C R I P T S\Fly-By-Data\sample_mavlink'

for i in range(len(filenames)):
    filenames[i] = '//'.join(path.split('\\')[:]) + '//' + filenames[i]

params = ['AHR2','ATT','BARO_0','BAT_0','GPS_0','XKF1_0','RATE','RCOU'] # for more options refer to 'parameters.html'

data = mavlab.multiple_data(filenames,params)
time = mavlab.multiple_timedata_gpscor(filenames,params)

roll_1 = data[0]['XKF1_0']['Roll'] # data from 1st file
roll_2 = data[1]['XKF1_0']['Roll'] # data from 2nd file

pitch_1 = data[0]['XKF1_0']['Pitch'] # data from 1st file
pitch_2 = data[1]['XKF1_0']['Pitch'] # data from 2nd file

yaw_1 = data[0]['XKF1_0']['Yaw'] # data from 1st file
yaw_2 = data[1]['XKF1_0']['Yaw'] # data from 2nd file

altitude_1 = -1 * data[0]['XKF1_0']['PD'] # data from 1st file
altitude_2 = -1 * data[1]['XKF1_0']['PD'] # data from 2nd file