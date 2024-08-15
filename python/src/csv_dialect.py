#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
Class module developed to share CSV dialects, or group of specific and related
configuration, which instructs the parser on how to interpret the character set read from a
CSV file.

Credits: Ideas come from Gertjan van den Burg's work on CleverCSV

"""
import csv
import functools

from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

class Dialect:
    """
    Class provided to hold the CSV dialects/file configuration used to
    parse CSV files.

    Parameters
    ----------
    delimiter : str
        Fields delimiter, used to split records from the CSV file.

    records_delimiter : str
        Used to split CSV content into a set of lines.

    quotechar : str
        The token used to quote/encapsulate fields in the file.

    escapechar : str
        The character used to escape/skip special tokens in 
        fields from the file.
    """

    def __init__(
        self,
        delimiter: Optional[str],
        records_delimiter: Optional[str],
        quotechar: Optional[str],
        escapechar: Optional[str]
    ):
        self.delimiter = delimiter
        self.records_delimiter = records_delimiter
        self.quotechar = quotechar
        self.escapechar = escapechar

    def validate(self) -> None:
        if self.delimiter is None or len(self.delimiter) > 1 or len(self.delimiter) == 0:
            raise ValueError(
                "Delimiter should be a one character string, got: %r"
                % self.delimiter
            )
        if self.records_delimiter is None or len(self.records_delimiter) > 1 or len(self.records_delimiter) == 0:
            raise ValueError(
                "Delimiter should be a one character string, got: %r"
                % self.records_delimiter
            )
        if self.quotechar is None or len(self.quotechar) > 1 or len(self.quotechar) == 0 :
            raise ValueError(
                "Quotechar should be a one character string, got: %r"
                % self.quotechar
            )
        if self.escapechar is None or len(self.escapechar) > 1 or len(self.escapechar) == 0:
            raise ValueError(
                "Escapechar should be a one character string, got: %r"
                % self.escapechar
            )
    
    @classmethod
    def from_dict(
        cls: Type["Dialect"], d: Dict[str, Any]
    ) -> "Dialect":
        dialect = cls(
            d["delimiter"], d["records_delimiter"], d["quotechar"], d["escapechar"]
        )
        return dialect
    
    @classmethod
    def from_csv_dialect(
        cls: Type["Dialect"], d: csv.Dialect
    ) -> "Dialect":
        #The default value is COMMA, as per RFC-4180
        delimiter = "," if d.delimiter is None else d.delimiter 
        #The default value is CRLF, as per RFC-4180
        records_delimiter = "\r\n" if d.records_delimiter is None else d.records_delimiter 
        #The default value is DOUBLE_QUOTE, as per RFC-4180
        quotechar = '"' if d.quoting == csv.QUOTE_NONE else d.quotechar 
        #The default value is DOUBLE_QUOTE, as per RFC-4180
        escapechar = '"' if d.escapechar is None else d.escapechar 
        return cls(delimiter, records_delimiter, quotechar, escapechar)
    
    def to_csv_dialect(self) -> csv.Dialect:
        class cDialect(csv.Dialect): #Complete dialect
            assert self.delimiter is not None
            delimiter = self.delimiter
            quotechar = '"' if self.quotechar == "" else self.quotechar
            escapechar = '"' if self.escapechar == "" else self.escapechar
            doublequote = True
            quoting = (
                csv.QUOTE_NONE if self.quotechar == "" else csv.QUOTE_MINIMAL
            )
            skipinitialspace = True
            lineterminator = self.records_delimiter

        return cDialect()
    
    def to_dict(self) -> Dict[str, Union[str, bool, None]]:
        self.validate()
        d = dict(
            delimiter=self.delimiter,
            records_delimiter=self.records_delimiter,
            quotechar=self.quotechar,
            escapechar=self.escapechar
        )
        return d
    
    def __repr__(self) -> str:
        #return "Dialect(%r, %r, %r, %r)" % (
        return "Dialect(%r, %r, %r)" % (
            self.delimiter,
            #self.records_delimiter,
            self.quotechar,
            self.escapechar,
        )
    
    def __key(
        self,
    ) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
        return (self.delimiter, self.records_delimiter, self.quotechar, self.escapechar)
    
    def __hash__(self) -> int:
        return hash(self.__key())
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Dialect):
            return False
        return self.__key() == other.__key()