import os 
import numpy as np 
import pandas as pd


class LoadFiles():
    
    """
    Class to load all recording files and corresponding brain state files (REM, NREM, wake).

    This class handles the loading of recording files in .npy format and brain state files in .pkl format.
    
    Attributes:
    directory_path (str): The path to the directory containing the recording and brain state files.
    animal_id (str): The identifier for the animal whose files are being loaded.

    Methods:
    load_two_analysis_files(start_times_dict, end_times_dict): Loads two sets of analysis files based on provided time dictionaries.
    load_one_analysis_file(start_times_dict, end_times_dict): Loads one set of analysis files based on provided time dictionaries.
    """
    
    def __init__(self, directory_path, animal_id):
        self.directory_path = directory_path
        self.animal_id = animal_id
        self.brain_1 = animal_id + '_BL1.pkl'
        self.brain_2 = animal_id + '_BL2.pkl'
        self.start_dict_1 = animal_id + '_1'
        self.start_dict_2 = animal_id + '_2'
        self.end_dict_1 = animal_id + '_1A'
        self.end_dict_2 = animal_id + '_2A'
        
        
    def load_two_analysis_files(self, start_times_dict, end_times_dict):
        animal_recording = [filename for filename in os.listdir(self.directory_path) if filename.startswith(self.animal_id) and filename.endswith('.npy')]
        recording = np.load(os.path.join(self.directory_path, animal_recording[0])) 
        brain_file_1 = [filename for filename in os.listdir(self.directory_path) if filename == self.brain_1]
        brain_state_1 = pd.read_pickle(os.path.join(self.directory_path, brain_file_1[0]))
        brain_file_2 = [filename for filename in os.listdir(self.directory_path) if filename == self.brain_2]
        brain_state_2 = pd.read_pickle(os.path.join(self.directory_path, brain_file_2[0]))
        
        start_time_1 = start_times_dict[self.start_dict_1]
        start_time_2 = start_times_dict[self.start_dict_2]
        
        end_time_1 = end_times_dict[self.end_dict_1]
        end_time_2 = end_times_dict[self.end_dict_2]

        recording_1 = recording[:, start_time_1: end_time_1 + 1]
        recording_2 = recording[:, start_time_2: end_time_2 + 1]
        
        return recording_1, recording_2, brain_state_1, brain_state_2
    
    def load_one_analysis_file(self, start_times_dict, end_times_dict):
        animal_recording = [filename for filename in os.listdir(self.directory_path) if filename.startswith(self.animal_id) and filename.endswith('.npy')]
        recording = np.load(os.path.join(self.directory_path, animal_recording[0])) 
        brain_file_1 = [filename for filename in os.listdir(self.directory_path) if filename == self.brain_1]
        brain_state_1 = pd.read_pickle(os.path.join(self.directory_path, brain_file_1[0]))
        
        start_time_1 = start_times_dict[self.start_dict_1]
        end_time_1 = end_times_dict[self.end_dict_1]
        
        recording_1 = recording[:, start_time_1: end_time_1 + 1]

        return recording_1, brain_state_1 
    
    def extract_br_state(self, recording, br_state_file, br_number):
        split_epochs = np.split(recording, len(br_state_file), axis = 1)
        br_indices = br_state_file.loc[br_state_file['brainstate'] == br_number].index.to_list()
        br_epochs = np.array(split_epochs)[br_indices]
        return br_epochs
    

class PreprocessingDat():
    """
    Class to convert EEG recordings into appropriate format. 
    This analysis pipeline requires that files are in .npy format,
    if your files are in .dat - apply the functions from this class
    to convert them to .npy
    
    Parameters:
    downsampling = 1 (if no downsampling)
    montage_name = montage file (should be in .elc)
    number of electrodes = 16 
    
    """
    
    def __init__(self, downsampling, montage_name, num_electrodes):
        self.downsampling = downsampling
        self.montage_name = montage_name
        self.num_electrodes = num_electrodes
    
    '''load a .dat file by interpreting it as int16 and then de-interlacing the 16 channels'''
    def parse_dat(self, filename, sample_rate):
        sample_datatype = 'int16'
        display_decimation = 1

        #load the raw (1-D) data
        dat_raw = np.fromfile(filename, dtype = sample_datatype)

        #reshape the (2-D) per channel data
        step = self.num_electrodes * display_decimation
        dat_chans = [dat_raw[c::step] for c in range(self.num_electrodes)]

        #build the time array 
        t = np.arange(len(dat_chans[0]), dtype = float) / sample_rate

        return dat_chans, t

    def convert_dat_to_npy(self, filename, path_to_folder, path_to_save_folder, sample_rate, save_as_name):

        os.chdir(path_to_folder)
        dat_chans, t = self.parse_dat(filename, self.num_electrodes, sample_rate)
        data_to_save = np.array(dat_chans)

        os.chdir(path_to_save_folder)
        np.save(save_as_name, data_to_save)

        print('data saved for ' + save_as_name)


##example of how to implement functions
#animal_ID_list = ['424', '430', '433']

#for animal in animal_ID_list:
#    print(dat_recording[0])
#    dat_recording = [GRIN2B_file for GRIN2B_file  in os.listdir(path_to_folder) if GRIN2B_file.endswith(animal + '.dat')]
#    convert_dat_to_npy(filename = dat_recording[0], path_to_folder= path_to_folder, path_to_save_folder=path_to_save_folder, sample_rate=1000,
#    number_electrodes=16, save_as_name = animal + '_GRIN2B')
    