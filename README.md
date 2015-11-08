#Authoritizer

A GUI tool for reconciling messy data to a canonical list of authorized terms using fuzzy string matching

##Purpose
Do you have list of names, tags, or other text data that may have been created by users of a website or survey respondents? Do they contain spelling errors, variant forms, or other inconsistencies? Do you want to interactively reconcile those text strings with a consistent list of "canonical" authorized terms using fuzzy string matching? Then Authoritizer is for you.

Authoritizer is written completely in Python, and will run on any OS for which the PyQt GUI library is available. In addition, there is a .exe compiled using PyInstaller for use on Windows.

##Alternatives
Authoritizer was written to fill a need that was not being met by current free software alternatives.

In some ways, it is most similar to [reconcile-csv](http://okfnlabs.org/reconcile-csv/), which provides a local reconciliation server for [OpenRefine](http://openrefine.org). However, `reconcile-csv` has [a serious bug](https://github.com/okfn/reconcile-csv/issues/23) which renders it unusable on some platforms.

Other alternatives include software for "record linkage" such as [FRIL](http://fril.sourceforge.net/) and the [RecordLinkage package for R](https://cran.r-project.org/web/packages/RecordLinkage/index.html). However, their main purpose is the merging of two (or more) statistical or epidemiological data sets based on the simultaneous fuzzy matching of multiple text, numeric, or date fields (e.g. first name, last name, date of birth, age, city, zip code), possibly after preprocessing and cleanup. As such, they are overkill for the use case envisioned by Authoritizer, where preprocessing can be done in other software (e.g. `OpenRefine` or a spreadsheet app), and where only text comparison between two data colums is being done.

In addition, all of the above software only provides the "best match" linkage between the two data sets based on a chosen similarity measure. There is no reason to assume that an arbitrary metric will always return the "correct" match as the top-scoring hit (as opposed to the second- or third-best). Authoritizer allows the user to view a "short list" of the best scoring authorized terms for each "messy" term, from which the correct match can be chosen interactively.

##Example use case
Suppose we have a set of company names that were listed by respondents to a survey. Some of these companies are publicly traded, and some are not. In addition, this list may have misspellings or may be written differently from the official name of the company as listed on the stock exchange. We also have a list of publicly traded US companies, containing their official names, ticker symbols, and other business information. We wish to reconcile the nonstandard "messy" survey data with the authorized "canonical" list of official company names.

Here is how `authoritizer` handles this type of problem:
![screenshot]()

##Usage
###Launch the program
####From source
Running Authoritizer from source requires the following dependencies:
* Python 2.7 (not 3.x)
* PyQt4
* jellyfish
* unicodecsv (for .csv import)
* openpyxl (for .xslx import)

Once those are installed, you can run `python authoritizer.py` from your command prompt.

####From Windows executable
Users of Windows 7 and higher can simply double-click on the executable in the `/dist` directory of the git repository. Depending on your system configuration, you may receive warnings about untrusted software...

###Import data

###Run matching

###Interactively chose and/or confirm matchings

###Export matchings to a CSV file



##Known bugs:
* Font size issue in the "Matched authorities" box. It's either too small for MacOS, or too big for Windows.
