import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

class Analysis:
    def __init__(self, directory_path, analysis_ls):
        self.directory_path = directory_path
        self.analysis_ls = analysis_ls
        self.analytics_df_ls = []
        self.clean_power_df = pd.DataFrame()
        self.noise_power_df = pd.DataFrame()
    
    def read_files(self, animal):
        power_file = pd.read_csv(f'{self.directory_path}{animal}_power.csv')
        slope_file = pd.read_csv(f'{self.directory_path}{animal}_slope.csv')
        return power_file, slope_file
    
    def filter_data(self, slope_file, power_file, threshold = None):
        if threshold is None:
            threshold = -8
        clean_mask = slope_file['Slope'] >= threshold
        noisy_mask = slope_file['Slope'] < threshold
        
        clean_df = slope_file[clean_mask]
        noisy_df = slope_file[noisy_mask]

        clean_indices = clean_df['Epoch'].unique()
        noisy_indices = noisy_df['Epoch'].unique()

        clean_power = power_file[power_file['Epoch'].isin(clean_indices)]
        noise_power = power_file[power_file['Epoch'].isin(noisy_indices)]
        
        return clean_power, noise_power, clean_df, noisy_df
    
    def create_analytics_df(self, animal, clean_df, noisy_df):
        return pd.DataFrame({
            'Animal_ID': [animal], 
            'Noisy_Epochs': [len(noisy_df)],
            'Clean_Epochs': [len(clean_df)]
        })
    
    def process_animal(self, animal, save=False, save_path=None, threshold = None):
        power_file, slope_file = self.read_files(animal)
        clean_power, noise_power, clean_df, noisy_df = self.filter_data(slope_file, power_file, threshold = None)
    
        analytics_df = self.create_analytics_df(animal, clean_df, noisy_df)
    
        if save:
            if save_path is None:
                raise ValueError("save_path must be provided if save is True")
            clean_power.to_csv(os.path.join(save_path, f'{animal}_clean_power.csv'))
            noise_power.to_csv(os.path.join(save_path, f'{animal}_noise_power.csv'))
    
        return clean_power, noise_power, analytics_df
    
    def analyze(self):
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(self.process_animal, self.analysis_ls))
        
        for clean_power, noise_power, analytics_df in results:
            self.clean_power_df = pd.concat([self.clean_power_df, clean_power], ignore_index=True)
            self.noise_power_df = pd.concat([self.noise_power_df, noise_power], ignore_index=True)
            self.analytics_df_ls.append(analytics_df)
        
        self.analytics_df_concat = pd.concat(self.analytics_df_ls, ignore_index=True)
    
    
    def plot_results(self, data_to_plot, palette=None, hue = 'Animal_ID', xlim = [1, 48],
                     ylim = [10**-2, 10**4], title = 'Plot Title', save_folder = None, save_as = None):
    
        """
        Plots the power spectrum of the given data with options to customize the palette, hue, axes limits, and title.

        Parameters:
        data_to_plot (pd.DataFrame): The DataFrame containing the data to be plotted.
        palette (list, optional): A list of colors to use for the plot. Defaults to a predefined list of colors.
        hue (str, optional): The column name in the DataFrame to use for color coding. Possible options:
            - 'Animal_ID': Color code by animal identifiers.
            - 'Channels': Color code by different channels.
            - 'Brainstates': Color code by different brain states.
        xlim (list, optional): The limits for the x-axis. Defaults to [1, 48].
        ylim (list, optional): The limits for the y-axis (in logarithmic scale). Defaults to [10**-2, 10**4].
        title (str, optional): The title of the plot. Defaults to 'Plot Title'.
        ax (matplotlib.axes.Axes, optional): The axes object to plot on. If None, a new figure and axes are created.
        """
    
        if palette is None:
            palette = ['orange', 'orangered', 'lightsalmon', 'darkred', 'gold', 'yellowgreen', 'darkseagreen',
                       'darkolivegreen', 'teal', 'skyblue', 'darkblue', 'black', 'slategrey',
                       'palevioletred', 'plum', 'deeppink', 'mediumpurple', 'peru']
    
        sns.set_style("white")
        fig, axs = plt.subplots(nrows = 1, ncols = 1, figsize=(10, 8), sharex=True, sharey=True)
        sns.lineplot(data=data_to_plot, x='Frequency', y='Power', hue= hue, 
                     errorbar=('se'), linewidth=2, palette=palette)
        
        sns.despine()
        axs.set_yscale('log')
        axs.set_xlim(1, 48)
        axs.set_ylim(ylim[0], ylim[1])
        axs.set_xlabel("Frequency (Hz)")
        axs.set_ylabel(r"log Power ($\mu V^2$)")
        fig.suptitle(title, y=0.96, fontsize=15, fontweight='bold')
        
        axs.spines['bottom'].set_linewidth(2)
        axs.spines['left'].set_linewidth(2)
    
        axs.set_xlabel("Frequency (Hz)", fontsize=14)
        axs.set_ylabel(r"log Power ($\mu V^2$)", fontsize=14)
        axs.tick_params(axis='both', which='major', labelsize=12)
        
        legend = axs.legend(title=hue, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., frameon=False)
        legend.set_title(hue, prop={'size': 12})
        for text in legend.get_texts():
            text.set_fontsize(12)
    
        if save_folder and save_as is not None:
            plt.savefig(f'{save_folder + save_as}.png', bbox_inches='tight', bbox_extra_artists=[legend])
            plt.savefig(f'{save_folder + save_as}.svg', bbox_inches='tight', bbox_extra_artists=[legend])
    
        plt.show()