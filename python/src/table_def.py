#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
This class module deals with table creation as required to implemment the method described in the paper
"Detecting CSV file dialects by table uniformity measurement and data type inference", available 
at https://content.iospress.com/articles/data-science/ds240062. 

"""
import csv
import os
import sys
import codecs

from csv_dialect import Dialect
from typing import List

class table_constructor:
    """
    This container holds methods for create the structures to be used in the Table Uniformity method.
    The created tables are List of string Lists and are created from a CSV file.

    Parameters
    ----------
    file_path : str
        Full path to the CSV file.

    threshold : int
        Number of records to be loaded from the CSV file.

    encoding : str
        Codec to be used to read the CSV file.

    """
    def __init__(
        self,
        file_path: str,
        threshold: int = 10,
        encoding: str = 'utf_8',
    ) -> None:
        self.file_path = file_path
        self.threshold = threshold
        self.encoding = encoding
    
    def validate(self) -> None:
        if self.file_path is None or len(self.file_path) == 0:
            raise ValueError(
                "The basepath should be provided, got: %r"
                % self.file_path
            )
    
    def fromCSV(
        self, _dialect: Dialect
    ) -> List[List[str]]:
        
        """
        Create a table by parsing a CSV file with the given dialect.

        Parameters
        ----------
        dialect: Dialect
            the dialect to be used to read the file

        Returns
        -------
            a list of string list generated by parsing the CSV file

        """

        self.validate()
        dataSample = []
        record = []
        ts = self.threshold
        #Get data
        try:
            #with open(self.file_path, encoding=self.encoding) as csvfile:
            with open(self.file_path) as csvfile:
                """
                reader_obj = csv.reader(CommentStripper(csvfile), 
                                        delimiter=_dialect.delimiter,
                                        quotechar=_dialect.quotechar, 
                                        lineterminator=_dialect.records_delimiter
                                        )
                """
                reader_obj = csv.reader(EmptyLineStripper(csvfile), 
                                        delimiter=_dialect.delimiter,
                                        quotechar=_dialect.quotechar, 
                                        lineterminator=_dialect.records_delimiter
                                        )
                #Loop records up to threshold
                i = 0
                for record in reader_obj:
                    if record[0] != '':
                        if record[0][0] != '#': #Skip comment
                            i +=1
                            dataSample.append(record)
                    if i == ts:
                        break
            return dataSample
        except Exception as e:
            pass

"""

Credits 
   Daniel Dittmar (https://bytes.com/topic/python/513222-csv-comments)
   WyattBlue, Stack Over Flow user (https://stackoverflow.com/a/73316105) 
   
"""

def EmptyLineStripper (iterator):
    for line in iterator:
        if not line.strip ():
            continue
        yield line

def CommentStripper (iterator):
    for line in iterator:
        if line [:1] == '#':
            continue
        if not line.strip ():
            continue
        """
        rp = line.split(" #").pop()
        line = line.replace(' #' + rp, '')
        if line.strip() == "":
            continue
        """
        yield line