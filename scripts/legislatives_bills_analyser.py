import argparse
import pandas as pd


def load_dataframes(bills_file, legislators_file, votes_file, vote_results_file):
    """
    Load the dataframes from CSV files.

    Returns:
        Tuple[pd.DataFrame]: A tuple containing the dataframes of bills, legislators, votes, and vote results.
    """
    bills_df = pd.read_csv(bills_file)
    legislators_df = pd.read_csv(legislators_file)
    votes_df = pd.read_csv(votes_file)
    vote_results_df = pd.read_csv(vote_results_file)
    return bills_df, legislators_df, votes_df, vote_results_df


def calculate_legislator_votes(legislators_df, vote_results_df):
    """
    Calculate the number of bills supported and opposed for each legislator.

    Args:
        legislators_df (pd.DataFrame): DataFrame containing legislator information.
        vote_results_df (pd.DataFrame): DataFrame containing vote results.

    Returns:
        pd.DataFrame: DataFrame containing the count of bills supported and opposed by legislator.
    """
    legislator_votes = vote_results_df.merge(
        legislators_df,
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

    return legislator_votes_count


def calculate_bill_votes(bills_df, legislators_df, votes_df, vote_results_df):
    """
    Calculate the number of legislators who supported and opposed each bill and identify the main sponsor.

    Args:
        bills_df (pd.DataFrame): DataFrame containing bill information.
        legislators_df (pd.DataFrame): DataFrame containing legislator information.
        votes_df (pd.DataFrame): DataFrame containing vote information.
        vote_results_df (pd.DataFrame): DataFrame containing vote results.

    Returns:
        pd.DataFrame: DataFrame containing the count of supporters and opposers, and the main sponsor of each bill.
    """
    votes_and_results = vote_results_df.merge(
        votes_df, left_on="vote_id", right_on="id", suffixes=("", "_vote")
    )

    bill_votes_count = (
        votes_and_results.groupby(["bill_id", "vote_type"])
        .size()
        .unstack(fill_value=0)
        .reset_index()
    )
    bill_votes_count.columns = ["id", "supporter_count", "opposer_count"]

    bills_with_vote_counts = bill_votes_count.merge(bills_df, on="id")

    final_bills = bills_with_vote_counts.merge(
        legislators_df,
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

    final_bills["primary_sponsor"].fillna("Desconhecido", inplace=True)

    return final_bills


def save_results(legislator_votes_count, final_bills):
    """
    Save the results to CSV files.

    Args:
        legislator_votes_count (pd.DataFrame): DataFrame containing the count of bills supported and opposed by legislator.
        final_bills (pd.DataFrame): DataFrame containing the count of supporters and opposers, and the main sponsor of each bill.
    """
    legislator_votes_count.to_csv("output/legislators-support-oppose-count.csv", index=False)
    final_bills.to_csv("output/bills.csv", index=False)


def main(arg):
    """
    Main function that runs the analysis process and saves the results.

    arg:
        arg (Namespace): Command line arguments.
    """
    bills_df, legislators_df, votes_df, vote_results_df = load_dataframes(
        arg.bills, arg.legislators, arg.votes, arg.vote_results
    )
    legislator_votes_count = calculate_legislator_votes(legislators_df, vote_results_df)
    final_bills = calculate_bill_votes(
        bills_df, legislators_df, votes_df, vote_results_df
    )
    save_results(legislator_votes_count,final_bills)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze legislator votes and bills.")
    parser.add_argument("bills", help="CSV file containing bill information.")
    parser.add_argument(
        "legislators", help="CSV file containing legislator information."
    )
    parser.add_argument("votes", help="CSV file containing vote information.")
    parser.add_argument("vote_results", help="CSV file containing vote results.")
    args = parser.parse_args()

    main(args)
