# Legislators and Bills Analysis

Usage

To run the script, execute the following command:

```python
python legislatives_bills_analysis.py <bills.csv> <legislators.csv> <votes.csv> <vote_results.csv>
```

Or, in v2 branch (using POO): 


> The architecture needs the <code>&lt;scr&gt;</code> folder.


After git clone, move the folders to src path. The file run.py does not need to be in the folder src. 

```python
python run.py src/data/bills.csv src/data/legislators.csv src/data/votes.csv src/data/vote_results.csv
```

Replace <code>&lt;bills.csv&gt;</code>, <code>&lt;legislators.csv&gt;</code>, <code>&lt;votes.csv&gt;</code>, and <code>&lt;vote_results.csv&gt;</code> with the file paths of the corresponding CSV files.

## Input Data Format

The script expects the following input files:
<li><strong>bills.csv</strong>: A CSV file containing bill information with the columns:<ul><li><code>id</code>: Unique identifier of the bill</li><li><code>title</code>: Title of the bill</li><li><code>sponsor_id</code>: Unique identifier of the bill's main sponsor</li></ul></li><li><strong>legislators.csv</strong>: A CSV file containing legislator information with the columns:<ul><li><code>id</code>: Unique identifier of the legislator</li><li><code>name</code>: Name of the legislator</li></ul></li><li><strong>votes.csv</strong>: A CSV file containing vote information with the columns:<ul><li><code>id</code>: Unique identifier of the vote</li><li><code>bill_id</code>: Unique identifier of the bill being voted on</li></ul></li><li><strong>vote_results.csv</strong>: A CSV file containing vote results with the columns:<ul><li><code>vote_id</code>: Unique identifier of the vote</li><li><code>legislator_id</code>: Unique identifier of the legislator who cast the vote</li><li><code>vote_type</code>: The type of vote cast by the legislator (<code>support</code> or <code>oppose</code>)</li></ul></li>

## Output Data Format

The script generates two CSV files as output:

<li><strong>legislators-support-oppose-count.csv</strong>: A CSV file containing the count of bills supported and opposed by each legislator with the columns:<ul><li><code>id</code>: Unique identifier of the legislator</li><li><code>name</code>: Name of the legislator</li><li><code>num_supported_bills</code>: Number of bills supported by the legislator</li><li><code>num_opposed_bills</code>: Number of bills opposed by the legislator</li></ul></li><li><strong>bills.csv</strong>: A CSV file containing the count of supporters and opposers, and the main sponsor of each bill with the columns:<ul><li><code>id</code>: Unique identifier of the bill</li><li><code>title</code>: Title of the bill</li><li><code>supporter_count</code>: Number of legislators who supported the bill</li><li><code>opposer_count</code>: Number of legislators who opposed the bill</li><li><code>primary_sponsor</code>: Name of the bill's main sponsor</li></ul></li>

### References

<li>Pandas: <a href="https://pandas.pydata.org/" target="_new">https://pandas.pydata.org/</a></li><li>Argparse: <a href="https://docs.python.org/3/library/argparse.html" target="_new">https://docs.python.org/3/library/argparse.html</a></li>
