import os 
import numpy as np
import pandas as pd

class Preprocess():
    """
    Class to convert .dat recording file to .npy.

    Attributes:
    raw_folder (str): Path to the folder containing the raw .dat file.
    raw_file (str): Name of the raw .dat file.
    save_fold_path (str): Path to the folder where the .npy file will be saved.
    save_as (str): Name to save the .npy file as.
    downsampling (int): Factor by which to downsample the data.
    num_channels (int): Number of channels in the recording.
    sampling_rate (int): Sampling rate of the recording in Hz.
    """
    
    def __init__(self, raw_folder, raw_file, save_fold_path, save_as, downsampling = 1, num_channels = 16, sampling_rate = 250.4):
        self.raw_folder = raw_folder
        self.raw_file = raw_file
        self.save_fold_path = save_fold_path
        self.save_as = save_as
        self.downsampling = downsampling
        self.num_channels = num_channels
        self.sample_rate = sampling_rate
        
    def parse_dat(self, file):
        """
        Parses the .dat file and extracts channel data and time array.

        Parameters:
        file (str): Path to the .dat file.

        Returns:
        dat_chans (list): List of numpy arrays, each containing data for one channel.
        t (numpy.ndarray): Time array corresponding to the data.
        """
        sample_datatype = 'int16'
        display_decimation = 1

        #load the raw (1-D) data
        dat_raw = np.fromfile(file, dtype = sample_datatype)

        #reshape the (2-D) per channel data
        step = self.num_channels * display_decimation
        dat_chans = [dat_raw[c::step] for c in range(self.num_channels)]

        #build the time array 
        t = np.arange(len(dat_chans[0]), dtype = float) / self.sample_rate

        return dat_chans, t
    
    def convert_dat_to_npy(self):
        """
        Converts the .dat file to a .npy file and saves it.

        This method reads the .dat file, parses the data into channels, and saves the data as a .npy file.

        Raises:
        FileNotFoundError: If the .dat file cannot be found.
        """
        data_file_path = os.path.join(self.raw_folder, self.raw_file)
        
        # check if the file exists
        if not os.path.exists(data_file_path):
            raise FileNotFoundError(f"The file {self.raw_file} was not found in the directory {self.raw_folder}.")
        
        dat_chans, t = self.parse_dat(data_file_path)
        data_to_save = np.array(dat_chans)
    
        save_file_path = os.path.join(self.save_fold_path, self.save_as)
        np.save(save_file_path, data_to_save)

        print(f'data saved for {self.raw_file}')
        
        
def reformat_br_file(unformatted_folder, unformatted_file, save_folder, save_as):
    file_path = os.path.join(unformatted_folder, unformatted_file)
    file = pd.read_excel(file_path)
    x = [0] 
    br_values = x + file[0].to_list()
    start_epoch = np.arange(0, 86400, 5)
    end_epoch = np.arange(5, 86405, 5 )
    br_dict = {'brainstate': br_values, 'start_epoch': start_epoch, 'end_epoch': end_epoch}
    br_df = pd.DataFrame(data = br_dict)
    save_path = os.path.join(save_folder, save_as)
    br_df.to_pickle(f'{save_path}.pkl')
    print('brainstate file saved')
    return br_df