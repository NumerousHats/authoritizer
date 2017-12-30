# Authoritizer

A GUI tool for reconciling messy data to a canonical list of authorized terms using fuzzy string matching

## Purpose
Do you have list of names, tags, or other text data that may have been created by users of a website or survey respondents? Do they contain spelling errors, variant forms, or other inconsistencies? Do you want to interactively reconcile those text strings with a consistent list of "canonical" authorized terms using fuzzy string matching? Then Authoritizer is for you.

Authoritizer is written completely in Python, and will run on any OS for which the PyQt GUI library is available. In addition, there is a .exe compiled using PyInstaller for use on Windows.
# Authoritizer

A GUI tool for reconciling messy data to a canonical list of authorized terms using fuzzy string matching

## Purpose
Do you have list of names, tags, or other text data that may have been created by users of a website or survey respondents? Do they contain spelling errors, variant forms, or other inconsistencies? Do you want to interactively reconcile those text strings with a consistent list of "canonical" authorized terms using fuzzy string matching? Then Authoritizer is for you.

Authoritizer is written completely in Python, and will run on any OS for which the PyQt GUI library is available. In addition, there is a .exe compiled using PyInstaller for use on Windows.

## Alternatives
Authoritizer was written to fill a need that was not being met by current free software alternatives.

In some ways, it is most similar to [reconcile-csv](http://okfnlabs.org/reconcile-csv/), which provides a local reconciliation server for [OpenRefine](http://openrefine.org). However, `reconcile-csv` has [a serious bug](https://github.com/okfn/reconcile-csv/issues/23) which renders it unusable on some platforms.

Other alternatives include software for "record linkage" such as [FRIL](http://fril.sourceforge.net/) and the [RecordLinkage package for R](https://cran.r-project.org/web/packages/RecordLinkage/index.html). However, their main purpose is the merging of two (or more) statistical or epidemiological data sets based on the simultaneous fuzzy matching of multiple text, numeric, or date fields (e.g. first name, last name, date of birth, age, city, zip code), possibly after preprocessing and cleanup. As such, they are overkill for the use case envisioned by Authoritizer, where preprocessing can be done in other software (e.g. `OpenRefine` or a spreadsheet app), and where only text comparison between two data colums is being done.

In addition, all of the above software only provides the "best match" linkage between the two data sets based on a chosen similarity measure. There is no reason to assume that an arbitrary metric will always return the "correct" match as the top-scoring hit (as opposed to the second- or third-best). Authoritizer allows the user to view a "short list" of the best scoring authorized terms for each "messy" term, from which the correct match can be chosen interactively.

## Example use case
Suppose we have a set of company names that were listed by respondents to a survey. Some of these companies are publicly traded, and some are not. In addition, this list may have misspellings or may be written differently from the official name of the company as listed on the stock exchange. We also have a list of publicly traded US companies, containing their official names, ticker symbols, and other business information. We wish to reconcile the nonstandard "messy" survey data with the authorized "canonical" list of official company names.

Here is how `authoritizer` handles this type of problem:
![screenshot](https://github.com/MAndrecPhD/authoritizer/blob/develop/screen-shot.png)

## Usage
### Launch the program
#### From source
Running Authoritizer from source requires the following dependencies:
* Python 2.7 (not 3.x)
* PyQt4
* jellyfish
* unicodecsv (for .csv import)
* openpyxl (for .xslx import)

Once those are installed, you can run `python authoritizer.py` from your command prompt.

#### From Windows executable
Users of Windows 7 and higher can simply double-click on the executable in the `/dist` directory of the git repository. Depending on your system configuration, you may receive warnings about untrusted software...

### Import data
The authorized and non-standard terms that are to be matched can currently be imported from a CSV file or Excel `.xlsx` file (`File->Import Authorities...` and `File->Import Nonstandard terms...`).

### Run matching
Once both authorized and non-standard terms have been loaded, matching can be run via `Run->Match...`. Note that matching is run all-against-all. No "blocking" (e.g. as in [this work](http://datamining.anu.edu.au/publications/2003/kdd03-6pages.pdf)) is done. Therefore, this may be impractical for very large term sets. Both the authorized and non-standard terms are deduplicated prior to matching.

### Interactively chose and/or confirm matchings
After the matching is complete, the user can review the matches, which appear in the "match table" on the left portion of the window. Authority terms which match better than a given cutoff (which can be adjusted in `Preferences`) are automatically pre-populated into the "match table". Clicking on any row in the "match table" will display the 10 closest matches to that non-standard term in the "matched authorities" box in the upper right. Matches can be manually adjusted by double-clicking on a term in the "matched authorities" box, entering an arbitrary new authority term, or deleting an existing match.

### Export matchings to a CSV file
The matches in the "match table" can be exported to a CSV file using `File->Export CSV...`. Saving the results of a matching run so that the interactive adjustment of matches can be re-started is not yet implemented.



