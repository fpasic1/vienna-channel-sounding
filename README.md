# Dataset

The dataset consists of indoor channel sounding measurements at 2.55GHz and 25.5GHz center frequency. 

### Measurement Testbed

We employ a rotation unit to spin the transmit antenna around a central axis to perform measurements at a constant but adjustable velocity. 
The transmit antenna is moving on a circular trajectory with a diameter of 2m. 
The receive antenna is located in the neighboring office, approximately 10m from the transmitter and is static.

The measurement testbed is described in "https://ieeexplore.ieee.org/document/9739087" .

### Channel Sounding

The channel sounding system uses OFDM with a low PAPR Zadoff-Chu transmit sequence. 
In each measurement run we transmit a sequence of 50.000 identical OFDM symbols. 
At 2.55GHz, the measurement bandwidth is 100MHz while it is 500MHz at 25.5GHz. 
We perform triggered measurements at different transmit antenna velocities. 
The transmit antenna is therefore moving on a circular arc segment during the measurement duration. 
Through a hardware triggering unit, we ensure that measurements are performed for the same transmit antenna position at every measurement run, for both center frequencies. 
This leads to a good comparability of different employed center frequencies and velocities.
