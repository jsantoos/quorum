"""
This script imports the pandas library, which is a powerful data manipulation and
analysis library. It provides data structures like DataFrame and Series, which are
used for handling tabular data.

In this script, pandas is used for reading CSV files, manipulating and processing
data, and performing various operations such as merging, grouping, and filtering data.
"""
import pandas as pd


class DataLoader:
    """
    DataLoader class responsible for loading data from CSV files.

    The DataLoader class provides methods for loading CSV files containing
    information about bills, legislators, votes, and vote results. It returns
    the data in the form of pandas DataFrames, which can be further processed
    and analyzed.
    """

    def __init__(self, bills_file, legislators_file, votes_file, vote_results_file):
        self.bills_df = pd.read_csv(bills_file)
        self.legislators_df = pd.read_csv(legislators_file)
        self.votes_df = pd.read_csv(votes_file)
        self.vote_results_df = pd.read_csv(vote_results_file)

    def get_dataframes(self):
        """
        Load the dataframes from CSV files.

        This method reads the CSV files specified during the instantiation of the DataLoader class
        and returns a tuple containing the dataframes of bills, legislators, votes, and vote results.

        Returns:
            Tuple[pd.DataFrame]: A tuple containing the dataframes of bills, legislators, votes, and vote results.
        """
        return self.bills_df, self.legislators_df, self.votes_df, self.vote_results_df
