import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import pandas as pd
from scipy.signal import welch
from artifactdetection.explore import SignalProcessor  

class TestSignalProcessor(unittest.TestCase):

    def setUp(self):
        # Set up some example data
        self.data = np.random.rand(1000)  # Example data with 1000 samples
        self.num_epochs = 10
        self.fs = 250.4
        self.nperseg = 1252

        # Create an instance of SignalProcessor
        self.signal_processor = SignalProcessor(self.data, self.num_epochs, self.fs, self.nperseg)

    def test_init(self):
        # Test the initialization of explore class
        self.assertEqual(self.signal_processor.data.all(), self.data.all())
        self.assertEqual(self.signal_processor.num_epochs, self.num_epochs)
        self.assertEqual(self.signal_processor.fs, self.fs)
        self.assertEqual(self.signal_processor.nperseg, self.nperseg)
        self.assertEqual(len(self.signal_processor.chan_split_data), self.num_epochs)

    def test_uncase_array(self):
        # Test the _uncase_array method
        nested_array = [[1, 2], [3, 4]]
        flat_array = self.signal_processor.uncase_array(nested_array)
        self.assertTrue(np.array_equal(flat_array, [1, 2, 3, 4]))

        non_nested_array = [1, 2, 3, 4]
        result_array = self.signal_processor.uncase_array(non_nested_array)
        self.assertTrue(np.array_equal(result_array, non_nested_array))

    @patch('artifactdetection.explore.welch')
    @patch('numpy.polyfit')
    def test_average_slope_intercept(self, mock_polyfit, mock_welch):
        # Mock the welch and polyfit functions
        mock_welch.return_value = (np.array([1, 2, 3]), np.array([4, 5, 6]))
        mock_polyfit.return_value = (0.5, 2.0)

        epoch = np.random.rand(100)
        freq, power, slope, intercept = self.signal_processor.average_slope_intercept(epoch)

        # Assertions
        mock_welch.assert_called_once_with(epoch, window='hann', fs=self.fs, nperseg=self.nperseg)
        np.testing.assert_array_equal(mock_polyfit.call_args[0][0], np.array([1, 2, 3]))
        np.testing.assert_array_equal(mock_polyfit.call_args[0][1], np.array([4, 5, 6]))
        self.assertEqual(mock_polyfit.call_args[0][2], 1)
        self.assertTrue(np.array_equal(freq, [1, 2, 3]))
        self.assertTrue(np.array_equal(power, [4, 5, 6]))
        self.assertEqual(slope, 0.5)
        self.assertEqual(intercept, 2.0)
        
        
    @patch('artifactdetection.explore.welch')
    @patch('numpy.polyfit')
    def test_process_single_channel(self, mock_polyfit, mock_welch):
        # Mock the welch and polyfit functions
        mock_welch.side_effect = [(np.array([1, 2, 3]), np.array([4, 5, 6])) for _ in range(self.num_epochs)]
        mock_polyfit.side_effect = [(0.5, 2.0) for _ in range(self.num_epochs)]

        chan_idx = 1
        animal_id = 'animal1'
        br_state = [0, 1] * (self.num_epochs // 2)

        power_plot_df_ls, slope_int_df_ls = self.signal_processor.process_single_channel(chan_idx, animal_id, br_state)

        # Assertions for DataFrame shapes and content
        self.assertEqual(len(power_plot_df_ls), self.num_epochs)
        self.assertEqual(len(slope_int_df_ls), self.num_epochs)

        for df in power_plot_df_ls:
            self.assertEqual(df.shape, (3, 6))  # 3 frequency points and 6 columns
            self.assertListEqual(list(df.columns), ['Frequency', 'Power', 'Animal_ID', 'Channel', 'Epoch', 'Br_State'])

        for df in slope_int_df_ls:
            self.assertEqual(df.shape, (1, 6))  # 1 slope/intercept per epoch and 6 columns
            self.assertListEqual(list(df.columns), ['Animal_ID', 'Channel', 'Epoch', 'Intercept', 'Slope', 'Br_State'])

if __name__ == '__main__':
    unittest.main()
