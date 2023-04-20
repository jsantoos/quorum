import sys
import argparse

from pathlib import Path

SRC_DIR = str(Path(__file__).resolve().parent / "src")
sys.path.append(SRC_DIR)

from scripts.main import main

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
