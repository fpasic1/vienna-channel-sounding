# Multi-band Wireless Channel Measurements in High-mobility Environment

This dataset consists of indoor channel sounding measurements at 2.55GHz, 5.9GHz and 25.5GHz center frequency. 

### Measurement Testbed

This measurement testbed enables a fair comparison between different frequency bands (sub-6 GHz and mmWave) in a repeatable and controlled high-mobility environment.
Repeatability is the ability to repeat a measurement with equal channel conditions, which is hardly possible by conducting real-world drive-by measurements.
Controllability means being able to control environmental as well as system parameters, for example, the signal-to-noise ratio (SNR).

#### Architecture

We employ a rotary unit to spin the transmit antenna around a central axis to perform measurements at a constant but adjustable velocity. 
The transmit antenna is moving with a constant velocity on a circular trajectory with a diameter of 2m.
The receive antenna is located on a laboratory table in the neighboring room, approximately 10m from the transmitter and is static.
The wireless channel can be measured with the same transmit antenna positions and the same receive antenna position but with different center frequencies and
velocities. 
This allows a direct comparison of the measured wireless channel in terms of fading environment and channel statistics.
For a direct and fair comparison of the measurement scenarios, the fading environment (the laboratory) has to be static.

![rotary_with_raumplan](https://user-images.githubusercontent.com/103816150/164254885-a1b9418a-7282-4c8c-ad05-d33fe0389588.jpg)


#### Synchronization
To provide precise frequency synchronization, the arbitrary waveform generator at the transmitter and the signal analyzer at the receiver are interconnected with
a 100 MHz reference. 
This connection by a cable is a big plus of the proposed setup, not feasible in, for example, drive-by measurements, where expensive rubidium frequency standards need to be employed to ensure precise synchronization.
The same holds true for time synchronization. 
In the proposed setup, we can repeatably trigger a measurement at a precisely defined position of a rotary arm by using a rotational encoder. The signal of the rotary encoder is decoded by a counter and a comparator to form a trigger signal that is fed through cables to the arbitrary waveform generator at the transmitter and the signal analyzer at the receiver.

The measurement testbed is described in
> F. Pasic, S. Pratschner, R. Langwieser, D. Schützenhöfer, E. Jirousek, H. Groll, S. Caban and M. Rupp, "Sub 6 GHz versus mmWave Measurements in a Controlled High-Mobility Environment," in Proceedings of the 25th International ITG Workshop on Smart Antennas (WSA 2021), Nov. 2021.

The paper is available via IEEE Explore at: https://ieeexplore.ieee.org/document/9739087

### Channel Sounding
The channel sounding wireless channel measurements have been performed in a controlled indoor laboratory environment.
The system transmits a series of identical OFDM symbols forming a low PAPR Zadoff-Chu channel sounding sequence.
In each measurement run we transmit a sequence of 50.000 identical OFDM symbols (500 snapshots of 100 symbols each). 
We assume the wireless channel between the moving antenna and the static receiver to be constant in time for the duration of one snapshot.
At the receiver side, we exploit the first OFDM symbol of each snapshot as a cyclic prefix, discard it, and perform averaging of the remaining 99 symbols to improve the signal-to-noise ratio (SNR).
As measurement results, we obtain a time-variant channel transfer function for discrete-time (snapshots) and frequency (subcarriers).
Measured time-variant channel transfer functions are provided above with corresponding measurement parameters.

The transmission is initiated and stopped by the trigger unit when the rotating arm reaches angular position of -40 degrees and +40 degrees, respectively.
Thereby, the transmit antenna is moving on a circular arc segment during the measurement duration.
This leads to a good comparability of different employed center frequencies and velocities.

The whole rotary unit is placed on a sliding board, that can be moved along both x-axis and y-axis.
To obtain different channel realizations, we perform high-speed measurements at different positions that are mutually separated by 0.4 wavelength.
Through a hardware triggering unit, we ensure that measurements are performed for the same transmit antenna position at every measurement run, for different center frequencies. 

The measurement methodology is described in
> F. Pasic, D. Schützenhöfer, E. Jirousek, R. Langwieser, H. Groll, S. Pratschner, S. Caban, S. Schwarz, M. Rupp, "Comparison of Sub 6 GHz and mmWave Wireless Channel Measurements at High Speeds," in Proceedings of the 16th European Conference on Antennas and Propagation (EuCAP 2022), Apr. 2022.

The paper is available at: https://publik.tuwien.ac.at/files/publik_303834.pdf
