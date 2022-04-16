# Dataset

The dataset consists of indoor channel sounding measurements at 2.55GHz and 25.5GHz center frequency. 

### Measurement Testbed

We employ a rotation unit to spin the transmit antenna around a central axis to perform measurements at a constant but adjustable velocity. 
The transmit antenna is moving on a circular trajectory with a diameter of 2m. 
The receive antenna is located in the neighboring office, approximately 10m from the transmitter and is static.

The measurement testbed is described in
> F. Pasic, S. Pratschner, R. Langwieser, D. Schützenhöfer, E. Jirousek, H. Groll, S. Caban and M. Rupp, "Sub 6 GHz versus mmWave Measurements in a Controlled High-Mobility Environment," in Proceedings of the 25th International ITG Workshop on Smart Antennas (WSA 2021), Nov. 2021.

The paper is available via IEEE Explore at: https://ieeexplore.ieee.org/document/9739087

### Channel Sounding

The channel sounding system uses OFDM with a low PAPR Zadoff-Chu transmit sequence. 
In each measurement run we transmit a sequence of 50.000 identical OFDM symbols (500 snapshots of 100 symbols each). 
We assume the wireless channel between the moving antenna and the static receiver to be constant in time for the duration of one snapshot.
At the receiver side, we exploit the first OFDM symbol of each snapshot as a cyclic prefix, discard it, and perform averaging of the remaining 99 symbols to improve the signal-to-noise ratio (SNR).
At 2.55GHz, the measurement bandwidth is 100MHz while it is 500MHz at 25.5GHz. 
We perform triggered measurements at different transmit antenna velocities. 
The transmit antenna is therefore moving on a circular arc segment during the measurement duration. 
Through a hardware triggering unit, we ensure that measurements are performed for the same transmit antenna position at every measurement run, for both center frequencies. 
This leads to a good comparability of different employed center frequencies and velocities.
As measurement results, we obtain a time-variant channel transfer function for discrete-time (snapshots) and frequency (subcarriers).

The measurement methodology is described in
> F. Pasic, D. Schützenhöfer, E. Jirousek, R. Langwieser, H. Groll, S. Pratschner, S. Caban, S. Schwarz, M. Rupp, "Comparison of Sub 6 GHz and mmWave Wireless Channel Measurements at High Speeds," in Proceedings of the 16th European Conference on Antennas and Propagation (EuCAP 2022), Apr. 2022.

The paper is available at: https://publik.tuwien.ac.at/files/publik_303834.pdf
