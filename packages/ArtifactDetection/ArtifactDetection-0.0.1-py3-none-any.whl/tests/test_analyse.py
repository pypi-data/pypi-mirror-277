import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
from artifactdetection.analyse import Analysis  # Adjust the import according to your module structure

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        self.directory_path = '/path/to/data/'
        self.analysis_ls = ['animal1', 'animal2']
        self.analysis = Analysis(self.directory_path, self.analysis_ls)

    @patch('pandas.read_csv')
    def test_read_files(self, mock_read_csv):
        # Mocking read_csv return value
        mock_power_df = pd.DataFrame({'data': [1, 2, 3]})
        mock_slope_df = pd.DataFrame({'data': [4, 5, 6]})
        mock_read_csv.side_effect = [mock_power_df, mock_slope_df]

        power_file, slope_file = self.analysis.read_files('animal1')

        mock_read_csv.assert_any_call(f'{self.directory_path}animal1_power.csv')
        mock_read_csv.assert_any_call(f'{self.directory_path}animal1_slope.csv')
        self.assertTrue(power_file.equals(mock_power_df))
        self.assertTrue(slope_file.equals(mock_slope_df))

    def test_filter_data(self):
        slope_data = {'Slope': [-9, -7, -5, -10], 'Epoch': [0, 1, 2, 3]}
        power_data = {'Epoch': [0, 1, 2, 3], 'Power': [10, 20, 30, 40]}
        slope_file = pd.DataFrame(slope_data)
        power_file = pd.DataFrame(power_data)

        clean_power, noise_power, clean_df, noisy_df = self.analysis.filter_data(slope_file, power_file, threshold=-8)

        expected_clean_power = pd.DataFrame({'Epoch': [1, 2], 'Power': [20, 30]}).reset_index(drop=True)
        expected_noise_power = pd.DataFrame({'Epoch': [0, 3], 'Power': [10, 40]}).reset_index(drop=True)
        expected_clean_df = pd.DataFrame({'Slope': [-7, -5], 'Epoch': [1, 2]}).reset_index(drop=True)
        expected_noisy_df = pd.DataFrame({'Slope': [-9, -10], 'Epoch': [0, 3]}).reset_index(drop=True)

        pd.testing.assert_frame_equal(clean_power.reset_index(drop=True), expected_clean_power)
        pd.testing.assert_frame_equal(noise_power.reset_index(drop=True), expected_noise_power)
        pd.testing.assert_frame_equal(clean_df.reset_index(drop=True), expected_clean_df)
        pd.testing.assert_frame_equal(noisy_df.reset_index(drop=True), expected_noisy_df)

    def test_create_analytics_df(self):
        clean_df = pd.DataFrame({'Slope': [-7, -5], 'Epoch': [1, 2]})
        noisy_df = pd.DataFrame({'Slope': [-9, -10], 'Epoch': [0, 3]})

        analytics_df = self.analysis.create_analytics_df('animal1', clean_df, noisy_df)

        expected_analytics_df = pd.DataFrame({
            'Animal_ID': ['animal1'], 
            'Noisy_Epochs': [2],
            'Clean_Epochs': [2]
        })

        pd.testing.assert_frame_equal(analytics_df, expected_analytics_df)

    @patch('pandas.read_csv')
    @patch('os.path.join')
    @patch('pandas.DataFrame.to_csv')
    def test_process_animal(self, mock_to_csv, mock_path_join, mock_read_csv):
        # Mocking read_csv return value
        mock_power_df = pd.DataFrame({'Epoch': [0, 1, 2, 3], 'Power': [10, 20, 30, 40]})
        mock_slope_df = pd.DataFrame({'Slope': [-9, -7, -5, -10], 'Epoch': [0, 1, 2, 3]})
        mock_read_csv.side_effect = [mock_power_df, mock_slope_df]

        mock_path_join.side_effect = lambda *args: '/'.join(args)

        clean_power, noise_power, analytics_df = self.analysis.process_animal('animal1', save=True, save_path='/save/path')

        mock_read_csv.assert_any_call(f'{self.directory_path}animal1_power.csv')
        mock_read_csv.assert_any_call(f'{self.directory_path}animal1_slope.csv')

        mock_to_csv.assert_any_call('/save/path/animal1_clean_power.csv')
        mock_to_csv.assert_any_call('/save/path/animal1_noise_power.csv')

        expected_clean_power = pd.DataFrame({'Epoch': [1, 2], 'Power': [20, 30]}).reset_index(drop=True)
        expected_noise_power = pd.DataFrame({'Epoch': [0, 3], 'Power': [10, 40]}).reset_index(drop=True)
        expected_analytics_df = pd.DataFrame({
            'Animal_ID': ['animal1'],
            'Noisy_Epochs': [2],
            'Clean_Epochs': [2]
        })

        pd.testing.assert_frame_equal(clean_power.reset_index(drop=True), expected_clean_power)
        pd.testing.assert_frame_equal(noise_power.reset_index(drop=True), expected_noise_power)
        pd.testing.assert_frame_equal(analytics_df, expected_analytics_df)

    @patch('concurrent.futures.ThreadPoolExecutor.map')
    def test_analyze(self, mock_map):
        mock_map.return_value = [
            (pd.DataFrame({'Epoch': [1, 2], 'Power': [20, 30]}), pd.DataFrame({'Epoch': [0, 3], 'Power': [10, 40]}), pd.DataFrame({
                'Animal_ID': ['animal1'], 
                'Noisy_Epochs': [2],
                'Clean_Epochs': [2]
            })),
            (pd.DataFrame({'Epoch': [1, 2], 'Power': [20, 30]}), pd.DataFrame({'Epoch': [0, 3], 'Power': [10, 40]}), pd.DataFrame({
                'Animal_ID': ['animal2'], 
                'Noisy_Epochs': [2],
                'Clean_Epochs': [2]
            }))
        ]

        self.analysis.analyze()

        self.assertEqual(len(self.analysis.analytics_df_ls), 2)
        self.assertEqual(self.analysis.clean_power_df.shape, (4, 2))
        self.assertEqual(self.analysis.noise_power_df.shape, (4, 2))
        self.assertEqual(self.analysis.analytics_df_concat.shape, (2, 3))

    @patch('matplotlib.pyplot.savefig')
    @patch('seaborn.lineplot')
    def test_plot_results(self, mock_lineplot, mock_savefig):
        data_to_plot = pd.DataFrame({
            'Frequency': [1, 2, 3, 4],
            'Power': [10, 20, 30, 40],
            'Animal_ID': ['animal1', 'animal1', 'animal2', 'animal2']
        })

        self.analysis.plot_results(data_to_plot, save_folder='/save/path/', save_as='test_plot')

        mock_lineplot.assert_called_once()
        mock_savefig.assert_any_call('/save/path/test_plot.png')
        mock_savefig.assert_any_call('/save/path/test_plot.svg')

if __name__ == '__main__':
    unittest.main()
