class BillVoteAnalyzer:
    """
    This class represents a BillVoteAnalyzer, which is responsible for analyzing
    legislator votes and bills based on provided data. It processes the data and
    calculates various statistics, such as the number of bills supported and opposed
    by each legislator, and the number of supporters and opposers for each bill.

    The class provides methods for loading data from CSV files, calculating
    legislator and bill vote counts, and saving the results to output files.
    """

    def __init__(self, bills_df, legislators_df, votes_df, vote_results_df):
        self.bills_df = bills_df
        self.legislators_df = legislators_df
        self.votes_df = votes_df
        self.vote_results_df = vote_results_df

    def calculate_bill_votes(self):
        """
        Calculate the number of legislators who supported and opposed each bill and identify the main sponsor.

        This method processes the bills, legislators, votes, and vote results data
        to determine the number of supporters and opposers for each bill, as well as
        the primary sponsor of the bill.

        Returns:
            pd.DataFrame: DataFrame containing the count of supporters and opposers, and the main sponsor of each bill.
        """
        votes_and_results = self.vote_results_df.merge(
            self.votes_df, left_on="vote_id", right_on="id", suffixes=("", "_vote")
        )

        bill_votes_count = (
            votes_and_results.groupby(["bill_id", "vote_type"])
            .size()
            .unstack(fill_value=0)
            .reset_index()
        )
        bill_votes_count.columns = ["id", "supporter_count", "opposer_count"]

        bills_with_vote_counts = bill_votes_count.merge(self.bills_df, on="id")

        final_bills = bills_with_vote_counts.merge(
            self.legislators_df,
            left_on="sponsor_id",
            right_on="id",
            how="left",
            suffixes=("", "_legislator"),
        )

        final_bills = final_bills[
            ["id", "title", "supporter_count", "opposer_count", "name"]
        ]
        final_bills.columns = [
            "id",
            "title",
            "supporter_count",
            "opposer_count",
            "primary_sponsor",
        ]

        final_bills["primary_sponsor"].fillna("Unknown", inplace=True)

        return final_bills
