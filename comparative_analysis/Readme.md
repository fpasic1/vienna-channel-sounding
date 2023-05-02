# Comparative Analysis

This dataset consists of time-varying channel transfer functions obtained through indoor channel sounding measurements at 2.55GHz and 25.5GHz center frequency. 

The dataset entries are given as complex-valued numpy (.npy) files in which rows and columns represent different snapshots and subcarriers, respectively. 
The entries are classified in four categories depending on the measurement scenarios.

![generateTable](https://user-images.githubusercontent.com/103816150/235702203-b4a9fed7-fb39-4f8b-8c14-978943a8f2e7.jpg)

For each scenario, there are 126 channel realizations obtained by conducting measurements at different positions according to the given rectangular grid.

![generateTable](https://user-images.githubusercontent.com/103816150/235717047-7f7d7c2b-9fe3-4285-9b4f-5fdeece633ab.jpg)

Each name in the dataset is given in the format “frequency_velocity_position”. 
For example, the entry “25_5GHz_100kmh_X6Y2.npy” denotes the time-varying channel transfer function measured at 25.5 GHz at the velocity of 100 km/h for the position six on the x-axis and position two on the y-axis.

## Example file

In addition to the data files, an example Python file called "example.py" is provided.  
The example file extracts dataset entries based on the chosen input parameters, such as scenario, x- and y-position within the rectangular grid.
As a result, the example file shows the channel transfer function and the channel impulse response for the selected parameters. 
The channel impulse response is obtained by performing Inverse Fast Fourier Transform (IFFT) of the channel transfer function over subcarriers.

