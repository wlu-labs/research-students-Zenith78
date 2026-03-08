
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ExternalDataCleaning:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_name,sep=";",decimal=",")
        print("Data loaded successfully.")

    def clean_data(self, subset=None):
        # Check for missing values
        missing_values = self.data.isnull().sum()
        print("Missing values in each column:\n", missing_values)
        self.data['Start_plugin'] = pd.to_datetime(self.data['Start_plugin'], format='%d.%m.%Y %H:%M') #format the string to a datetime object
        self.data['End_plugout'] = pd.to_datetime(self.data['End_plugout'], format='%d.%m.%Y %H:%M')
        # Fill missing values with the mean of the respective columns
        self.data.fillna(self.data.mean(), inplace=True)
        print("Missing values filled with mean.")

    def visualize_data(self):
        # Plotting the distribution of EV loads
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['EV_Load'], bins=30, kde=True)


        plt.title('Distribution of EV Loads')

        plt.xlabel('EV Load')
        plt.ylabel('Frequency')
        plt.show()

if __name__ == "__main__":
    file_name ="src/data/external/Dataset 2_Hourly EV loads - Per user.csv" 
    data_cleaner = ExternalDataCleaning(file_name)
    data_cleaner.load_data()
    data_cleaner.clean_data(subset=['End_plugout','Start_plugin'])
    data_cleaner.visualize_data()