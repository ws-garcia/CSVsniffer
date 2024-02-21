# CSVsniffer
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10668894.svg)](https://doi.org/10.5281/zenodo.10668894)

Companion repository for the paper:

[**Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference**](https://www.preprints.org/manuscript/202402.0858) 
[(PDF)](https://www.preprints.org/manuscript/202402.0858/v2/download)

by [W. García](https://sciprofiles.com/profile/3400377).

An application of the new methodology outlined in the paper can be found in the [CSV interface](https://github.com/ws-garcia/VBA-CSV-interface) repository. 

## Introduction

The results from the research can be reproduced by running the `RunTests` method from the macro-enabled Excel workbook `CSVsniffer.xlsm`. To review the results for CleverCSV it is necessary to run the scripts from the `clevercsv_test.py` file. The text files with the results output are stored in the `Current research` and `cleverCSV` folders


## Data

The `CSV` folder contains the files copied from the [Pollock framework](https://github.com/HPI-Information-Systems/Pollock) and other collected test files. Also the dataset used for the [CSV wrangling research](https://github.com/alan-turing-institute/CSV_Wrangling) is available in the `CSV_Wranglin` folder. Note that only link to the files can be provided, in this last case,due to the authors holds the copyright.

The expect configuration for each set CSV tested is saved in the `DialectConf.txt` file, new files can be added.

## Requirements

Below are the requirements for reproducing the experiments.

- Microsoft Office Excel.
- [CleverCSV](https://github.com/alan-turing-institute/CleverCSV) and all its dependencies.
