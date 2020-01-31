#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:08:52 2020

@author: Jakob Dörr (jdo043

Example script for functions in GFPy.Ocean
"""

from GFPy.Ocean import read_CTD,plot_CTD_section,plot_CTD_station,plot_CTD_map,plot_CTD_ts
import matplotlib.pyplot as plt

# =============================================================================
# read in some CTD data
# =============================================================================

# Document Data location (absolute or relative to current location)
data_loc = './testdata/CTD/'

# Read all station files in specified folder, and save result in a .npy file
CTD_all = read_CTD(data_loc,'test_cruise',outpath='./')
 
# Read specific stations in the folder
stations = range(401,410)
CTD_part = read_CTD(data_loc,'test_cruise',stations=stations) 

# =============================================================================
# Plot a CTD section
# =============================================================================

#define stations included in the CTD section
stations = range(401,410)

# plot the section, given the variable CTD_all from above
plot_CTD_section(CTD_all,stations,
                 cruise_name='test_cruise',section_name='A')

# plot the section, given the path to the .npy file given above
plot_CTD_section('./test_cruise_CTD.npy',stations,
                 cruise_name='test_cruise',section_name='A')
# save the current figure
plt.savefig('./test_image.pdf')

# =============================================================================
# Plot a CTD profile
# =============================================================================
# define the station for which to plot a profile
station = 402

# plot a single profile
plot_CTD_station(CTD_all, station)
plt.savefig('./test_profile.pdf')

# plot several single profiles in one plot with subplots
plt.figure()
plt.subplot(121)
plot_CTD_station(CTD_all, station,add = True)
plt.subplot(122)
plot_CTD_station(CTD_all, station+1,add = True)
# if you want to manipulate the figure afterwards, you have to get the
# axes using plt.gcf().axes. There are 4 axes in this example, 2 for each
# subplot, because we have two x-axes in each subplot. To, i.e. change the
# temperaure range and xlabel in the first sublplot, do:
axx = plt.gcf().axes
axx[0].set_xlim(0,15)
axx[0].set_xlabel('Liberal temperature [˚C]')

# =============================================================================
# Plot a map of CTD stations
# =============================================================================
# define the stations to plot on the map
stations = range(401,410)
bathy_file = '/Users/jakobdorr/Documents/PhD/teaching/MATLAB_TO_PYTHON_CRUISE2020'\
            '/2019_Masfjorden/Data/Bathymetry/Masfjorden_bathy.mat'
 
#plot_CTD_map(CTD_all,stations,topofile=bathy_file)
#plt.savefig('./test_map.pdf')
plt.figure()
plot_CTD_map(CTD_all) # (you should not plot all stations in one map...)


# =============================================================================
# Plot a TS diagram with CTD data
# =============================================================================
plot_CTD_ts(CTD_all,[400])