import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import pandas as pd

from artifactdetection.load import LoadFiles

class TestLoadFiles(unittest.TestCase):

    def setUp(self):
        self.directory_path = '/path/to/files'
        self.animal_id = 'animal1'
        self.load_files = LoadFiles(self.directory_path, self.animal_id)

    @patch('os.listdir')
    @patch('numpy.load')
    @patch('pandas.read_pickle')
    def test_load_two_analysis_files(self, mock_read_pickle, mock_load, mock_listdir):
        # Mock the return values for os.listdir
        mock_listdir.return_value = ['animal1_recording.npy', 'animal1_BL1.pkl', 'animal1_BL2.pkl']
        
        #mock the npy and pkl returnse
        mock_load.return_value = np.random.rand(2, 1000)
        mock_read_pickle.side_effect = [pd.DataFrame({'br_state': [0, 1]}), pd.DataFrame({'br_state': [1, 0]})]

        # Define the start and end times
        start_times_dict = {'animal1_1': 100,'animal1_2': 200}
        end_times_dict = {'animal1_1A': 300,'animal1_2A': 400}

        recording_1, recording_2, brain_state_1, brain_state_2 = self.load_files.load_two_analysis_files(start_times_dict, end_times_dict)

        # Assertions to check the correct slices are taken
        self.assertEqual(recording_1.shape, (2, 201))
        self.assertEqual(recording_2.shape, (2, 201))
        self.assertTrue((brain_state_1['br_state'] == pd.Series([0, 1])).all())
        self.assertTrue((brain_state_2['br_state'] == pd.Series([1, 0])).all())

    @patch('os.listdir')
    @patch('numpy.load')
    @patch('pandas.read_pickle')
    def test_load_one_analysis_file(self, mock_read_pickle, mock_load, mock_listdir):
        #mock files 
        mock_listdir.return_value = [
            'animal1_recording.npy', 'animal1_BL1.pkl'
        ]
        
        #mock the npy and pkl returns 
        mock_load.return_value = np.random.rand(2, 1000)
        mock_read_pickle.return_value = pd.DataFrame({'br_state': [0, 1]})

        # Define the start and end times
        start_times_dict = {'animal1_1': 100}
        end_times_dict = {'animal1_1A': 300}
        recording_1, brain_state_1 = self.load_files.load_one_analysis_file(start_times_dict, end_times_dict)

        # Assertions to check the correct slices are taken
        self.assertEqual(recording_1.shape, (2, 201))
        self.assertTrue((brain_state_1['br_state'] == pd.Series([0, 1])).all())

if __name__ == '__main__':
    unittest.main()
