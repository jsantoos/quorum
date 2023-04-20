from classes.data_loader import DataLoader
from classes.legislator_vote_analyzer import LegislatorVoteAnalyzer
from classes.bill_vote_analyzer import BillVoteAnalyzer
from classes.csv_exporter import CSVExporter


def main(arg):
    """
    Main function that runs the analysis process and saves the results.

    arg:
        arg (Namespace): Command line arguments.
    """
    data_loader = DataLoader(arg.bills, arg.legislators, arg.votes, arg.vote_results)
    bills_df, legislators_df, votes_df, vote_results_df = data_loader.get_dataframes()

    legislator_vote_analyzer = LegislatorVoteAnalyzer(legislators_df, vote_results_df)
    legislator_votes_count = legislator_vote_analyzer.calculate_legislator_votes()

    bill_vote_analyzer = BillVoteAnalyzer(
        bills_df, legislators_df, votes_df, vote_results_df
    )
    final_bills = bill_vote_analyzer.calculate_bill_votes()

    CSVExporter.save_results(legislator_votes_count, final_bills)
