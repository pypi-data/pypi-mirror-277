import unittest
from unittest.mock import patch
import numpy as np
from scipy import signal
from artifactdetection.noisefilter import NoiseFilter  

class TestNoiseFilter(unittest.TestCase):

    def setUp(self):
        self.unfiltered_data = np.random.rand(4, 1000)  # Example data with 4 channels, 1000 samples each
        self.num_epochs = 10
        self.chan_idx = 1  # test filtering on the second channel

        # Create an instance of NoiseFilter
        self.noise_filter = NoiseFilter(self.unfiltered_data, self.num_epochs, self.chan_idx)

    @patch('scipy.signal.butter')
    @patch('scipy.signal.filtfilt')
    def test_filter_data_type(self, mock_filtfilt, mock_butter):
        # mock butter and filtfilt functions
        mock_butter.return_value = (np.array([1, 0]), np.array([1, 0]))
        mock_filtfilt.return_value = np.random.rand(1000)  # example filtered data

        filtered_data = self.noise_filter.filter_data_type()

        # Assertions
        mock_butter.assert_called_once_with(self.noise_filter.order, [self.noise_filter.low, self.noise_filter.high], btype='band', analog=False)
        mock_filtfilt.assert_called_once()
        self.assertEqual(filtered_data.shape, (1000,))
        self.assertTrue(np.all(filtered_data >= 0) and np.all(filtered_data <= 1))

    def test_butter_bandpass(self):
        data = self.unfiltered_data[self.chan_idx, :]
        filtered_data = self.noise_filter.filter_data_type()

        # ensures the input and output data have the same shape
        self.assertEqual(filtered_data.shape, data.shape)

if __name__ == '__main__':
    unittest.main()
