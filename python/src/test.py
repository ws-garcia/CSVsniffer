#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from typing import List
from csv_dialect import Dialect
from table_score import t_score
from potential_dialects import p_dialects
from csv_sniffer import sniffer

def main(basePath:str, fileName:str):
    #Parent folder
    mainPath = os.path.dirname(basePath)
    #CSV file path
    CSVpath = os.path.join(mainPath, 'testing CSV')
    filePath = os.path.join(CSVpath, fileName)
    #Sniff dialect
    iDialect = sniffer.sniff(sniffer(filePath,
                                     threshold=50,
                                     delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'])
                                     )
    """
    or
        obj_sniffer = sniffer(filePath,threshold=25)
        iDialect = obj_sniffer.sniff()
    """
    print(iDialect)

if __name__ == "__main__":
    #Working dir
    path = os.getcwd()
    filename = 'iometeroutput.csv'
    main(path, filename)