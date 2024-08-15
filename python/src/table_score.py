#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
This is the core class module to perform dialect detection as described in the paper
"Detecting CSV file dialects by table uniformity measurement and data type inference", available 
at https://content.iospress.com/articles/data-science/ds240062. 

"""

import math

from typing import List
from csv_dialect import Dialect
from table_def import table_constructor 
from type_detection import type_detector
from table_uniformity import t_uniformity

class t_score:
    """
    This container holds methods for compute the table score.

    Parameters
    ----------
    csv_path : str
        Path to the target CSV file.

    dialect : Dialect
        Confguration used to load the data from the CSV.

    threshold : int
        Count of records to load from CSV file, default value is 10.

    encoding : str
        Codec to be used to read the CSV file.

    """
    def __init__(
        self,
        csv_path: str,
        dialect: Dialect,
        threshold: int = 10,
        encoding: str = 'utf_8',
    ) -> None:
        self.csv_path = csv_path
        self.dialect = dialect
        self.threshold = threshold
        self.encoding = encoding

    def validate(self) -> None:
        if self.csv_path is None or len(self.csv_path) == 0:
            raise ValueError(
                "The path to the target CSV file should be provided, got: %r"
                % self.file_path
            )
        
        if self.dialect is None or not self.dialect.validate:
            raise ValueError(
                "The dialect should be provided, got: %r"
                % self.dialect
            )
        
    def compute(self) -> float:
        self.validate
        #Initialize table object
        table_obj = table_constructor(file_path=self.csv_path, threshold=self.threshold, encoding=self.encoding)

        """
        Construct a sample table from CSV. Lines starting with '#' will be skiped.
        """
        sample = table_obj.fromCSV(_dialect=self.dialect)

        #Compute record score by infering fields data type
        detector = type_detector()
        record_score = detector.record_score(data=sample, dialect=self.dialect) 
        #Compute Table Uniformity parameters
        _uniformity = t_uniformity(table=sample)
        tau = _uniformity.compute() 
        n = len(sample)
        if n > 1:
            gamma = tau[0] / self.threshold + (1 / (tau[1] + n))
        else:
            eta = math.sqrt(record_score) / 10
            k = len(sample[0])
            gamma = (eta + (1 / k)) / (k - math.floor(eta * k) + 1)
        return gamma * record_score