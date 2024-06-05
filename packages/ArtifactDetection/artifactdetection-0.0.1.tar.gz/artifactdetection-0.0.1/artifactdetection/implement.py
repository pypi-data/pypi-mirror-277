'''Script to implement load, filter and explore'''

import os
import numpy as np
import pandas as pd
from .noisefilter import NoiseFilter
from .explore import SignalProcessor


def two_files(load_files, start_times_dict, end_times_dict, animal, chan_idx, num_epochs, save_folder):
    data_1, data_2, br_1, br_2 = load_files.load_two_analysis_files(start_times_dict = start_times_dict,
                                                                        end_times_dict = end_times_dict)
    data = np.concatenate([data_1, data_2], axis = 1)
    nfilter = NoiseFilter(unfiltered_data = data, num_epochs = num_epochs, chan_idx = chan_idx)
    filtered_data = nfilter.filter_data_type()
    process = SignalProcessor(data = filtered_data, num_epochs = num_epochs)
    power, slope = process.process_single_channel(chan_idx = chan_idx, animal_id = animal, br_state = np.concatenate([br_1['brainstate'], br_2['brainstate']]))
    power_animal_df = pd.concat(power)
    slope_animal_df = pd.concat(slope)
    power_animal_df.to_csv(save_folder + f'{animal}_power.csv')
    slope_animal_df.to_csv(save_folder + f'{animal}_slope.csv')
    
def one_file(load_files, start_times_dict, end_times_dict, animal, chan_idx, num_epochs, save_folder):
    data, br = load_files.load_one_analysis_file(start_times_dict = start_times_dict,
                                                end_times_dict = end_times_dict)
    nfilter = NoiseFilter(unfiltered_data = data, num_epochs = num_epochs, chan_idx = chan_idx)
    filtered_data = nfilter.filter_data_type()
    process = SignalProcessor(data = filtered_data, num_epochs = num_epochs)
    power, slope = process.process_single_channel(chan_idx = chan_idx, animal_id = animal, br_state = br['brainstate'])
    power_animal_df = pd.concat(power)
    slope_animal_df = pd.concat(slope)
    power_animal_df.to_csv(save_folder + f'{animal}_power.csv')
    slope_animal_df.to_csv(save_folder + f'{animal}_slope.csv')
    
