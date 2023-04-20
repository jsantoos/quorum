class CSVExporter:
    """
    A class to handle the exporting of data to CSV files.

    This class provides functionality to export data stored in
    pandas DataFrames to CSV files. It allows specifying the
    output file path and ensures the data is saved in the correct format.

    Attributes:
        output_path (str): The path where the CSV file will be saved.
    """

    @staticmethod
    def save_results(legislator_votes_count, final_bills):
        """
        Save the results to CSV files.

        This function takes two DataFrames as input, one containing the count of bills
        supported and opposed by each legislator, and the other containing the count of
        supporters and opposers, as well as the main sponsor for each bill. It saves
        each DataFrame to a CSV file in the specified output directory.

        Args:
            legislator_votes_count (pd.DataFrame): DataFrame containing the count of bills
                                                supported and opposed by each legislator.
            final_bills (pd.DataFrame): DataFrame containing the count of supporters and
                                        opposers, and the main sponsor of each bill.
        """
        legislator_votes_count.to_csv(
            "src/output/legislators-support-oppose-count.csv", index=False
        )
        final_bills.to_csv("src/output/bills.csv", index=False)
