#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
Helper class module to run dialect detection test against a ground truth.

"""
import collections
import duckdb as DDB
import pandas as pd
import csv
import clevercsv as ccsv
import time
import os
import sys
from csv_dialect import Dialect
from csv_sniffer import sniffer
from typing import Type
from typing import List
from typing import Optional
from typing import Union

class runner:
    """
    This container is used to run dialect detection tests.

    Parameters
    ----------

    ground_truth_csv : str
        Full path to the ground truth annotations CSV file.

    output_path : str
        Path to the folder to be used for results output.

    delimiter_list : List[str]
        List of delimiters to be included in dialect creation.

    quotechar_list : List[str]
        List of quote characters to be included in dialect creation.

    expected_results : dict
        Dictionary holding the expected dialect for each file in the ground truth.

    threshold : int
        Size of the table to be loaded from CSV files.

    encoding : str
        Codec to be used to read the CSV file.

    """
    def __init__(
        self,
        ground_truth_csv: Optional[str],
        output_path: Optional[str],
        delimiter_list: Optional[List[str]],
        quotechar_list: Optional[List[str]],
        expected_results: Optional[dict],
        threshold: int = 10,
        encoding: str = 'utf_8',
        sniffer: str = 'CSVsniffer',
        data_threshold: int = 6144,
    ):
        self.ground_truth_csv = ground_truth_csv
        self.output_path = output_path
        self.delimiter_list = delimiter_list
        self.quotechar_list = quotechar_list
        self.expected_results = expected_results
        self.threshold = threshold
        self.encoding = encoding
        self.sniffer = sniffer
        self.data_threshold = data_threshold

    def set_delimiters(self, d_list: List[str]):
        self.delimiter_list = d_list if d_list is not None else [',', ';', '\t','|', ':', '=', ' ', '#', '*']

    def set_quotes(self, q_list: List[str]):
        self.quotechar_list = q_list if q_list is not None else ['"', "'", '~']              
        
    def detect_csv_dialect(self, file_name: str, path: str)->Union[Dialect, None]:
        try:
            if self.sniffer == 'CSVsniffer':
                dialect = sniffer.sniff(sniffer(file_path=path,
                                        threshold=self.threshold,
                                        delimiter_list=self.delimiter_list,
                                        quotechar_list=self.quotechar_list, 
                                        encoding='utf_8')#encoding=self.get_encoding(self.expected_results[file_name]['encoding']))
                                        )
            elif self.sniffer == 'Python sniffer':
                with open(path, newline='') as csvfile:
                    if self.data_threshold > 0:
                        dialect = Dialect.from_csv_dialect(csv.Sniffer().sniff(\
                                csvfile.read(self.data_threshold), self.delimiter_list))
                    else:
                        dialect = Dialect.from_csv_dialect(csv.Sniffer().sniff(\
                                csvfile.read(), self.delimiter_list))
                    csvfile.close
            elif self.sniffer == 'CleverCSV':
                with open(path, newline='') as csvfile:
                    if self.data_threshold > 0:
                        _dialect = ccsv.Sniffer().sniff(csvfile.read(self.data_threshold), self.delimiter_list)
                    else:
                        _dialect = ccsv.Sniffer().sniff(csvfile.read(), self.delimiter_list)
                if not _dialect is None:
                    dialect = Dialect(_dialect.delimiter,None,_dialect.quotechar,_dialect.escapechar)
            elif self.sniffer == 'DuckDB':
                pd = DDB.sql("FROM sniff_csv(%r, sample_size = %r)" %(path,self.threshold)).to_df()
                if not pd is None:
                    dialect = Dialect(pd.loc[0].at["Delimiter"],None,pd.loc[0].at["Quote"],pd.loc[0].at["Escape"])
            return dialect
        except OSError as err:
            print("Error was: %s" % err)
        except Exception as err:
            print("Error was: %s" % err)

    def import_expected_results(self, check_for_messy: bool=False):
        if self.ground_truth_csv != '':
            try:
                with open(self.ground_truth_csv, newline='') as csvfile:
                    csv_files_dict={}
                    spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
                    i=0
                    for row in spamreader:
                        if len(row)>1:
                            if i>0:
                                if check_for_messy:
                                    csv_row_dict={
                                        'encoding':row[1],
                                        'fields_delimiter':row[2],
                                        'quotechar':row[3],
                                        'escapechar':row[4],
                                        'records_delimiter':row[5],
                                        'normal-file':row[6]
                                    }

                                else:
                                    csv_row_dict={
                                        'encoding':row[1],
                                        'fields_delimiter':row[2],
                                        'quotechar':row[3],
                                        'escapechar':row[4],
                                        'records_delimiter':row[5]
                                    }
                                csv_files_dict[row[0]]=csv_row_dict
                            else:
                                i+=1
                    self.expected_results = csv_files_dict
            except Exception as err:
                print("Error was: %s" % err)
    
    def get_delimiter_name(self, delim:str)->str:
        if delim == ',':
            return 'comma'
        elif delim == ';':
            return 'semicolon'
        elif delim == '\t':
            return 'tab'
        elif delim == ' ':
            return 'space'
        elif delim == '|':
            return 'vslash'
        elif delim== '#':
            return 'nsign'
        elif delim== ':':
            return 'colon'
        elif delim== '=':
            return 'eqsign'
        elif delim== '*':
            return 'star'
    
    def get_encoding(self, _alias: str)->str:
        if _alias == 'utf8':
            return 'utf_8'
        elif _alias == 'utf16':
            return 'utf_16'
        elif _alias == 'ansi' or _alias == 'windows-1251':
            return 'latin_1'
        elif _alias == 'ascii' or _alias == 'gb2312':
            return _alias
        elif _alias == 'shif-jis':
            return 'shift_jis'
        else:
            return 'utf_8' 
        
    def get_quote_name(self, quote:str)->str:
        if quote == '"' or quote == '':
            return 'doublequote'
        elif quote == "'":
            return 'singlequote'
        elif quote == '~':
            return 'tilde'
    """
    base_path: str
        Parent folder for the test_sets subfolder
    
    output_file_names: str
        Names of files to be created for console output
    
    expected_results_csv_names: str
        Names ground truth files containing results annotations
    
    test_sets: str
        Folder holding the CSV data set annotated for ground truth
    """
    def run(self,
            base_path: str, 
            output_file_names: List[str],
            expected_results_csv_names: List[str],
            test_sets: List[str]
        ):
        n=0
        for output_file in output_file_names:
            sys.stdout = open(os.path.join(self.output_path,output_file), 'w')
            #Import expectect results as nested dicts
            self.ground_truth_csv = os.path.join(base_path, 'ground truth',
                                                 expected_results_csv_names[n])
            self.import_expected_results('ONLY MESSY=' in output_file)
            #Get ground truth base path
            current_csv_set = os.path.join(base_path, test_sets[n])
            passed=0
            d_passed = 0
            failures=0
            t=time.time()
            #Run test over all CSV files
            for filename in os.listdir(current_csv_set):
                if self.expected_results.get(filename) != None: #Check for key
                    file = os.path.join(current_csv_set, filename)
                    #File check
                    if os.path.isfile(file):
                        if 'ONLY MESSY= True' in output_file:
                            #Skip non messy files
                            skip_ = (self.expected_results[filename]['normal-file']=='yes')
                        else:
                            skip_ = False
                        if not skip_:
                            try:
                                dialect = self.detect_csv_dialect(file_name=filename, path=file)
                            except:
                                dialect = None
                            if dialect !=None:
                                if self.get_delimiter_name(dialect.delimiter)==self.expected_results[filename]['fields_delimiter'] and \
                                self.get_quote_name(dialect.quotechar)==self.expected_results[filename]['quotechar']:
                                    tflag ='+'
                                    passed += 1
                                    d_passed += 1
                                else:
                                    tflag ='X'
                                    if self.get_delimiter_name(dialect.delimiter)==self.expected_results[filename]['fields_delimiter']:
                                        d_passed += 1
                                if tflag =='+':
                                    print(tflag + '[' + filename + ']: --> ' + self.sniffer + ' detected: delimiter = %r, quotechar = %r' 
                                            % (dialect.delimiter, dialect.quotechar))
                                else:
                                    print(tflag + '[' + filename + ']: --> ' + self.sniffer + ' detected: delimiter = %r, quotechar = %r' 
                                            % (dialect.delimiter, dialect.quotechar) + \
                                            '| EXPECTED:{delimiter = %r, quotechar = %r}' \
                                            % (self.expected_results[filename]['fields_delimiter'], \
                                            self.expected_results[filename]['quotechar']))
                            else:
                                print("X [" + filename + "]: --> No result from " + self.sniffer)
                                failures += 1
            n+=1
            print('[Passed test ratio]--: %r' %(round(100*passed/(len(self.expected_results)-failures),4)) +'%')
            print('[Delimiter ratio]--: %r' %(round(100*d_passed/(len(self.expected_results)-failures),4)) +'%')
            print('[Failure ratio]--: %r' %(round(100*failures/len(self.expected_results),4)) +'%')
            print('[Elapsed time]--: %r seconds' %(round(time.time()-t,2)))
            print('<---------------------------------------------------------------------------------------->')
            tp = passed
            fp = len(self.expected_results)-(passed + failures)
            fn = failures
            p = round(tp / (tp + fp),4)
            r = round(tp / (tp + fn),4)
            f1 = round(2 * (p * r) / (p + r),4)
            print('True Positive (TP): %r' %tp)
            print('False Positive (FP): %r' %fp)
            print('False Negative (FN): %r' %fn)
            print('#')
            print('Precision (P): %r' %p)
            print('Recall (R): %r' %r)
            print('F1 score: %r' %f1)
            print('Weighted F1 score for %r files: %r' %(len(self.expected_results), f1 * tp))
            sys.stdout.close()