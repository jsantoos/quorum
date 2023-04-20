"""
This script imports the pandas library, which is a powerful data manipulation and
analysis library. It provides data structures like DataFrame and Series, which are
used for handling tabular data.

In this script, pandas is used for reading CSV files, manipulating and processing
data, and performing various operations such as merging, grouping, and filtering data.
"""
import pandas as pd


class LegislatorVoteAnalyzer:
    """
    A class to analyze legislator votes.

    This class calculates the number of bills supported and opposed for each legislator
    using the provided dataframes. It provides a method to obtain a DataFrame containing
    the count of bills supported and opposed by each legislator.

    Attributes:
        legislators_df (pd.DataFrame): DataFrame containing legislator information.
        vote_results_df (pd.DataFrame): DataFrame containing vote results.
    """

    def __init__(self, legislators_df, vote_results_df):
        self.legislators_df = legislators_df
        self.vote_results_df = vote_results_df

    def calculate_legislator_votes(self):
        """
        Calculate the number of bills supported and opposed for each legislator.

        This method processes the legislators_df and vote_results_df dataframes to calculate
        the number of bills supported and opposed by each legislator. It returns a DataFrame
        containing the count of bills supported and opposed by legislator.

        Returns:
            pd.DataFrame: A DataFrame containing the count of bills supported and opposed by legislator.
        """
        legislator_votes = self.vote_results_df.merge(
            self.legislators_df,
            left_on="legislator_id",
            right_on="id",
            suffixes=("", "_legislator"),
        )

        legislator_votes_count = (
            legislator_votes.groupby(["legislator_id", "name", "vote_type"])
            .size()
            .unstack(fill_value=0)
            .reset_index()
        )
        legislator_votes_count.columns = [
            "id",
            "name",
            "num_supported_bills",
            "num_opposed_bills",
        ]

        all_legislator_ids = set(self.legislators_df["id"])
        voting_legislator_ids = set(legislator_votes_count["id"])
        non_voting_legislator_ids = all_legislator_ids - voting_legislator_ids

        non_voting_legislators = self.legislators_df[
            self.legislators_df["id"].isin(non_voting_legislator_ids)
        ].copy()
        non_voting_legislators["num_supported_bills"] = 0
        non_voting_legislators["num_opposed_bills"] = 0
        non_voting_legislators = non_voting_legislators[
            ["id", "name", "num_supported_bills", "num_opposed_bills"]
        ]

        combined_legislator_votes = pd.concat(
            [legislator_votes_count, non_voting_legislators], ignore_index=True
        )

        return combined_legislator_votes
