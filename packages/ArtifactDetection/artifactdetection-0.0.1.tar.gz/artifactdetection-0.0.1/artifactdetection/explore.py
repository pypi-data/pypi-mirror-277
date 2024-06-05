import numpy as np
import pandas as pd
from scipy.signal import welch

class SignalProcessor():
    """
    Class to calculate power and slope for all epochs and return DataFrames with all power values and all slope values.

    Attributes:
    data (np.ndarray): The raw data to be processed.
    num_epochs (int): The number of epochs to split the data into.
    fs (float): The sampling frequency of the data. Default is 250.4 Hz.
    nperseg (int): The length of each segment for Welch's method. Default is 1252.
    chan_split_data (list): The data split into epochs.
    """
    def __init__(self, data, num_epochs, fs=250.4, nperseg=1252):
        self.data = data
        self.num_epochs = num_epochs
        self.fs = fs
        self.nperseg = nperseg
        self.chan_split_data = np.array_split(data, num_epochs)
    
    def uncase_array(self, array):
        """
        Checks if the power array is nested and flattens it if necessary.

        Parameters:
        array (list or np.ndarray): The array to be checked and flattened if nested.

        Returns:
        np.ndarray: The flattened array if nested, otherwise the original array.
        """
        if isinstance(array, (list, np.ndarray)) and any(isinstance(i, (list, np.ndarray)) for i in array):
            return np.ravel(array)
        return array

    def average_slope_intercept(self, epoch):
        """
        Calculates the average slope and intercept for a given epoch using Welch's method and linear regression.

        Parameters:
        epoch (np.ndarray): The epoch data to process.

        Returns:
        tuple: A tuple containing:
            - freq (np.ndarray): The frequency values.
            - power (np.ndarray): The power values.
            - slope (float): The slope of the linear fit.
            - intercept (float): The intercept of the linear fit.
        """
        
        freq, power = welch(epoch, window='hann', fs=self.fs, nperseg=self.nperseg)
        power = self.uncase_array(power)
        slope, intercept = np.polyfit(freq, power, 1)
        return freq, power, slope, intercept

    def process_single_channel(self, chan_idx, animal_id, br_state):
        """
        Processes a single channel to calculate power and slope for all epochs and returns the results in DataFrames.

        Parameters:
        chan_idx (int): The index of the channel being processed.
        animal_id (str): The identifier for the animal.
        br_state (list): The brain state for each epoch.

        Returns:
        tuple: A tuple containing:
            - power_plot_df_ls (list of pd.DataFrame): DataFrames with power values for each epoch.
            - slope_int_df_ls (list of pd.DataFrame): DataFrames with slope and intercept values for each epoch.
        """
        power_plot_df_ls = []
        slope_int_df_ls = []

        # Power calculations for all epochs
        freqs, powers = [], []
        for epoch in self.chan_split_data:
            freq, power = welch(epoch, window='hann', fs=self.fs, nperseg=self.nperseg)
            freqs.append(freq)
            powers.append(power)

        # Initialize lists to store slopes and intercepts
        slopes, intercepts = [], []

        # Compute slope and intercept for all epochs
        for i in range(len(freqs)):
            slope, intercept = np.polyfit(freqs[i], powers[i], 1)
            slopes.append(slope)
            intercepts.append(intercept)

        # Format results into dataframes
        for idx in range(self.num_epochs):
            power_data = {
                'Frequency': freqs[idx],
                'Power': powers[idx],
                'Animal_ID': [animal_id] * len(powers[idx]),
                'Channel': [chan_idx] * len(powers[idx]),
                'Epoch': [idx] * len(powers[idx]),
                'Br_State': [br_state[idx]] * len(powers[idx])
            }
            slope_data = {
                'Animal_ID': [animal_id],
                'Channel': [chan_idx],
                'Epoch': [idx],
                'Intercept': [intercepts[idx]],
                'Slope': [slopes[idx]],
                'Br_State': [br_state[idx]]
            }
        
            power_plot_df_ls.append(pd.DataFrame(data=power_data))
            slope_int_df_ls.append(pd.DataFrame(data=slope_data))

        return power_plot_df_ls, slope_int_df_ls
