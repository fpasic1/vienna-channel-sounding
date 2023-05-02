'''
Example script for "Dataset: Multi-band Wireless Channel Measurements in a Controlled High-Mobility Environment"

Author :        Faruk Pasic 
Email :         faruk.pasic@tuwien.ac.at
Institution :   TU Wien 
Location :      Vienna, Austria

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq, fftshift
from IPython import get_ipython;  


# Clear all
get_ipython().magic('reset -sf')

# Close all figures
plt.close('all')

'''
CTF - Channel Transfer Function
CIR - Channel Impulse Response
'''
# Initialize parameters
scenario    = 'A'       # choose scenario
x_pos       = 0         # choose x-position
y_pos       = 0         # choose y-position

plot_snapshots      = [0, 50, 70, 100, 200, 300, 400] # choose snaphots to plot
plot_subcarriers    = [0, 25, 50, 65,  70,  80,  90]  # choose subcarriers to plot

bandwidth           = 100e6

if scenario == 'A':
    filename = '2_55GHz_Scenario_A_50kmh'
    delay_axis = np.arange(-100, 100)/(bandwidth) * 1e9
elif scenario == 'B':
    filename = '2_55GHz_Scenario_B_100kmh'  
    delay_axis = np.arange(-50, 50)/(bandwidth) * 1e9
elif scenario == 'C':
    filename = '25_5GHz_Scenario_C_50kmh'  
    delay_axis = np.arange(-100, 100)/(bandwidth) * 1e9
elif scenario == 'D':
    filename = '25_5GHz_Scenario_D_100kmh'  
    delay_axis = np.arange(-50, 50)/(bandwidth) * 1e9

# Load channel transfer function
h_est           = np.load(f'{filename}\\estimated_channel_{filename}_X{x_pos}Y{y_pos}.npy')

plt.figure('Spectrum Channel')
plt.title('Spectrum Channel')
for i_snapshot in range(0, np.size(plot_snapshots)):
    plt.plot(20 * np.log10(np.abs(h_est[i_snapshot, :])), label=f'snapshot_{plot_snapshots[i_snapshot]}')
plt.grid()
plt.legend()
plt.xlabel('Subcarriers')
plt.ylabel('|h$_{CTF}$|$^{2}$ in dB ')

plt.figure('Channel over Time (CTF)')
plt.title('Channel over Time')
for i_subcarrier in range(0, np.size(plot_subcarriers)):
    plt.plot(20 * np.log10(np.abs(h_est[:, i_subcarrier])), label=f'subcarrier_{plot_subcarriers[i_subcarrier]}') 
plt.grid()
plt.legend()
plt.xlabel('Snapshots')
plt.ylabel('|h$_{CTF}$|$^{2}$ in dB ')

# Set parameter
snapshots       = np.size(h_est, 0)
num_subcarrier  = np.size(h_est, 1)

# Convert CTF to CIR
h_est_cir       = ifft(h_est, axis=1)

plt.figure('Channel Impulse Response')
plt.title('Channel Impulse Response')
for i_snapshot in range(0, np.size(plot_snapshots)):
    plt.plot(delay_axis, 20 * np.log10(np.abs(h_est_cir[i_snapshot, :])), label=f'snapshot_{plot_snapshots[i_snapshot]}') 
plt.grid()
plt.legend()
plt.xlabel('Delay [ns]')
plt.ylabel('|h$_{CIR}$|$^{2}$ in dB ')


plt.figure('Channel over Time (CIR)')
plt.title('Channel over Time')
for i_subcarrier in range(0, np.size(plot_subcarriers)):
    plt.plot(20 * np.log10(np.abs(h_est_cir[:, i_subcarrier])), label=f'subcarrier_{plot_subcarriers[i_subcarrier]}') 
plt.grid()
plt.legend()
plt.xlabel('Snapshots')
plt.ylabel('|h$_{CIR}$|$^{2}$ in dB ')
