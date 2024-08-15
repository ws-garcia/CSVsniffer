#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
This class module helps to create potential dialects collection as described in the paper
"Detecting CSV file dialects by table uniformity measurement and data type inference", available 
at https://content.iospress.com/articles/data-science/ds240062. 

"""
from typing import Type
from typing import List
from csv_dialect import Dialect

class p_dialects:
    """
    This container holds a list of potential dialects.

    Parameters
    ----------
    delimiter_list : List[str]
        List of delimiters to be included in dialect creation.

    quotechar_list : List[str]
        List of escape characters to be included in dialect creation.

    """
    def __init__(
        self,
        delimiter_list: List[str]=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
        escapechar_list: List[str]=['"', "'", '~'],
    ):
        self.delimiter_list = delimiter_list
        self.quotechar_list = escapechar_list

    def validate(self) -> None:
        if self.delimiter_list is None or len(self.delimiter_list) == 0:
            raise ValueError(
                "The list of potential dialects should be provided, got: %r"
                % self.delimiter_list
            )
        
        if self.quotechar_list is None or len(self.quotechar_list) == 0:
            raise ValueError(
                "The list of potential escape characters should be provided, got: %r"
                % self.quotechar_list
            )
    
    def get_dialects(self) -> List[Dialect]:
        self.validate
        dialects_=[]
        newlines_list = ['\n', '\r'] #Pandas doesn't support \r\n sequence
        for sep in self.delimiter_list:
            for quotechr in self.quotechar_list:
                for newline in newlines_list:
                    dialects_.append(Dialect(delimiter=sep, 
                                             records_delimiter=newline, 
                                             quotechar=quotechr,
                                             escapechar=quotechr)
                    )
        return dialects_
        