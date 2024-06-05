import numpy as np 
import pandas as pd 
import scipy
from scipy import signal 

#from parameters import channelvariables


class NoiseFilter:
    """
    A class to input unfiltered data, return bandpass filtered data, and calculate whether an epoch
    is within a specified noise threshold.

    Attributes:
    order (int): The order of the Butterworth filter. Default is 3.
    sampling_rate (float): The sampling rate of the data in Hz. Default is 250.4 Hz.
    nyquist (float): The Nyquist frequency, calculated as half the sampling rate.
    low (float): The normalized low cutoff frequency for the bandpass filter.
    high (float): The normalized high cutoff frequency for the bandpass filter.

    Instance Attributes:
    unfiltered_data (np.ndarray): The unfiltered input data.
    num_epochs (int): The number of epochs to split the data into.
    chan_idx (int): The index of the channel to be filtered.
    """
    
    order = 3
    sampling_rate = 250.4 
    nyquist = sampling_rate/2
    low = 1/nyquist
    high = 100/nyquist

    
    def __init__(self, unfiltered_data, num_epochs, chan_idx):
        self.unfiltered_data = unfiltered_data 
        self.num_epochs = num_epochs
        self.chan_idx = chan_idx                                  
   
    def filter_data_type(self):
        """
        Applies a bandpass filter to the specified channel of the unfiltered data.

        Returns:
        np.ndarray: The bandpass filtered data for the specified channel.
        """
        def butter_bandpass(data):
            butter_b, butter_a = signal.butter(self.order, [self.low, self.high], btype = 'band', analog = False)
            filtered_data = signal.filtfilt(butter_b, butter_a, data)
            return filtered_data
        
        
        #Select all, emg, or eeg channel indices to apply bandpass filter                                    
        selected_channel = self.unfiltered_data[self.chan_idx, :]     
        bandpass_filtered_data=butter_bandpass(data=selected_channel) 
                        
        return bandpass_filtered_data  
        
        
    def find_packetloss_indices(self, data, num_epochs, noise_limit):   
        
        def packet_loss(epoch):
                return epoch.max() < noise_limit 
        
        def get_dataset(data):
            packet_loss_score = []
            for epoch in data:
                packet_loss_score.append(0) if packet_loss(epoch) else packet_loss_score.append(6) 
            return packet_loss_score
        
        split_data = np.array_split(data, num_epochs)
        packet_loss_score = get_dataset(split_data) 
        print(packet_loss_score)
        packet_loss_indices = [idx for idx, score in enumerate(packet_loss_score) if score == 6]
        
        return packet_loss_indices
        
