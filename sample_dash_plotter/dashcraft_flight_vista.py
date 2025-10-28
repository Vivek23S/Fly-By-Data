# ============================================================================
# File Name:        dashcraft_flight_vista.py
# Author:           Vivek23
# Description:      sample file
# Notes:            if any error comes try to put everything in same folder
# ============================================================================

import sys
sys.path.insert(0,".\main libraries") # folder which has main loading libs
from dash_drone_plot import mavlink_plotter


filename        = '2024-03-25 16-42-23.bin-792718.mat'
path            = r'E:\I I T M\R E S E A R C H\S C R I P T S\Fly-By-Data\sample_mavlink'
mission_name    = 'sample-file'


app = mavlink_plotter(path, filename, mission_name)

if __name__ == '__main__':
    app.run_server(debug=True,port=2254)