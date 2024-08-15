#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
This class module is the main driver for detect CSV dialects with Table Uniformity 
method as described in the paper "Detecting CSV file dialects by table uniformity 
measurement and data type inference", available at 
https://content.iospress.com/articles/data-science/ds240062. 

"""

from typing import List
from typing import Union
from csv_dialect import Dialect
from table_score import t_score
from potential_dialects import p_dialects

class sniffer:
    """
    This class module is used to detect a CSV file dialect.

    Parameters
    ----------
    file_path : str
        path to the target CSV file.

    threshold : int
        Count of records to be loaded to dialect determination.

    delimiter_list : List[str]
        List of delimiters to be considered in dialect detecttion.

    quotechar_list : List[str]
        List of escape characters to be considered in dialect detecttion.

    encoding : str
        Codec to be used to read the CSV file.

    """
    def __init__(
        self,
        file_path: str,
        threshold : int=10,
        delimiter_list: List[str]=[',', ';', '\t', ':', ' '],
        quotechar_list: List[str]=['"', "'", '~'],
        encoding: str = 'utf_8',
    ):
        self.file_path = file_path
        self.threshold = threshold
        self.delimiter_list = delimiter_list
        self.quotechar_list = quotechar_list
        self.encoding = encoding

    def validate(self) -> None:
        if self.file_path is None or len(self.file_path) == 0:
            raise ValueError(
                "The path to the target CSV file should be provided, got: %r"
                % self.file_path
            )
    
    def sniff(self) ->Union[Dialect, None]:
        self.validate
        #Initialize Dialects and scores
        dialects = p_dialects.get_dialects(p_dialects(self.delimiter_list,self.quotechar_list))
        n = len(dialects)
        scores =[0]*n
        #Compute scores
        j = 0
        for d in dialects:
            t_scoring = t_score(csv_path=self.file_path, 
                                dialect=d, 
                                threshold=self.threshold, 
                                encoding=self.encoding)
            try:
                scores[j] = t_scoring.compute()
            except:
                scores[j] = 0
            j += 1
        return get_best_dialect(scores, dialects)
    
def get_best_dialect(
            scores_: List[float], 
            dialects_: List[Dialect]
)->Union[Dialect, None]:
    max_score = max(scores_)
    if max_score > 0:
        return dialects_[scores_.index(max_score)]
    else:
        return None