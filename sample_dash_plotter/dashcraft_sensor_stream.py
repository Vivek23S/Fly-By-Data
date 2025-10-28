# ============================================================================
# File Name:        dashcraft_sensor_stream.py
# Author:           Vivek23
# Description:      sample file
# Notes:            if any error comes try to put everything in same folder
# ============================================================================

import sys
sys.path.insert(0,".\main libraries") # folder which has main loading libs
from dash_drone_plot import tsm_plotter_d1


sensor_path             = r'E:\I I T M\R E S E A R C H\S C R I P T S\Fly-By-Data\sample_sensor'
log_path                = r'E:\I I T M\R E S E A R C H\S C R I P T S\Fly-By-Data\sample_mavlink'
sensor_filename         = '2024_3_25_16_41_41.csv'
log_filename            = '2024-03-25 16-42-23.bin-792718.mat'
mission_name            = 'sample-file'
latency_seconds         = 0
latency_milliseconds    = 0


app = tsm_plotter_d1(sensor_path, log_path, sensor_filename, log_filename, mission_name,latency_seconds,latency_milliseconds)

if __name__ == '__main__':
    app.run_server(debug=True,port=2070)