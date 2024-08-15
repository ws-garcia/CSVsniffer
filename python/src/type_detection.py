# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
This is a minor modification made to the CleverCSV detection source. The idea is to implement the 
method presented in the research paper "Detecting CSV file dialects by table uniformity measurement
and data type inference", available at https://content.iospress.com/articles/data-science/ds240062, 
with the least possible effort.

Unlike CleverCSV, whitespaces are always stripped from both ends of fileds strings.

Credits to Gertjan van den Burg
"""

import json
import csv
import math

from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Pattern

from _regexes import DEFAULT_TYPE_REGEXES
from csv_dialect import Dialect

DEFAULT_EPS_TYPE: float = 1e-10


class type_detector:
    def __init__(
        self,
        patterns: Optional[Dict[str, Pattern[str]]] = None,
    ) -> None:
        self.patterns = patterns or DEFAULT_TYPE_REGEXES.copy()
        self._register_type_tests()

    def _register_type_tests(self) -> None:
        self._type_tests = [
            ("empty", self.is_empty),
            ("url", self.is_url),
            ("email", self.is_email),
            ("ipv4", self.is_ipv4),
            ("number", self.is_number),
            ("time", self.is_time),
            ("percentage", self.is_percentage),
            ("currency", self.is_currency),
            ("unix_path", self.is_unix_path),
            ("nan", self.is_nan),
            ("date", self.is_date),
            ("datetime", self.is_datetime),
            ("unicode_alphanum", self.is_unicode_alphanum),
            ("bytearray", self.is_bytearray),
            ("json", self.is_json_obj),
        ]

    def list_known_types(self) -> List[str]:
        return [tt[0] for tt in self._type_tests]

    def is_known_type(self, cell: str) -> bool:
        return self.detect_type(cell, is_quoted=False) is not None

    def detect_type(self, cell: str, is_quoted: bool = False) -> Optional[str]:
        for name, func in self._type_tests:
            if func(cell, is_quoted=is_quoted):
                return name
        return None

    def _run_regex(self, cell: str, patname: str) -> bool:
        pat = self.patterns.get(patname, None)
        assert pat is not None
        match = pat.fullmatch(cell)
        return match is not None
    def is_number(self, cell: str, is_quoted: bool = False) -> bool:
        if cell == "":
            return False
        if self._run_regex(cell, "number_1"):
            return True
        if self._run_regex(cell, "number_2"):
            return True
        if self._run_regex(cell, "number_3"):
            return True
        return False

    def is_ipv4(self, cell: str, is_quoted: bool = False) -> bool:
        return self._run_regex(cell, "ipv4")

    def is_url(self, cell: str, is_quoted: bool = False) -> bool:
        return self._run_regex(cell, "url")

    def is_email(self, cell: str, is_quoted: bool = False) -> bool:
        return self._run_regex(cell, "email")

    def is_unicode_alphanum(self, cell: str, is_quoted: bool = False) -> bool:
        if is_quoted:
            return self._run_regex(cell, "unicode_alphanum_quoted")
        return self._run_regex(cell, "unicode_alphanum")

    def is_date(self, cell: str, is_quoted: bool = False) -> bool:
        # This function assumes the cell is not a number.
        if not cell:
            return False
        if not cell[0].isdigit():
            return False
        return self._run_regex(cell, "date")

    def is_time(self, cell: str, is_quoted: bool = False) -> bool:
        if not cell:
            return False
        if not cell[0].isdigit():
            return False
        return (
            self._run_regex(cell, "time_hmm")
            or self._run_regex(cell, "time_hhmm")
            or self._run_regex(cell, "time_hhmmss")
            or self._run_regex(cell, "time_hhmmsszz")
        )

    def is_empty(self, cell: str, is_quoted: bool = False) -> bool:
        return cell == ""

    def is_percentage(self, cell: str, is_quoted: bool = False) -> bool:
        return cell.endswith("%") and self.is_number(cell.rstrip("%"))

    def is_currency(self, cell: str, is_quoted: bool = False) -> bool:
        pat = self.patterns.get("currency", None)
        assert pat is not None
        m = pat.fullmatch(cell)
        if m is None:
            return False
        grp = m.group(1)
        if not self.is_number(grp):
            return False
        return True

    def is_datetime(self, cell: str, is_quoted: bool = False) -> bool:
        # Takes care of cells with '[date] [time]' and '[date]T[time]' (iso)
        if not cell:
            return False

        if not cell[0].isdigit():
            return False

        if " " in cell:
            parts = cell.split(" ")
            if len(parts) > 2:
                return False
            return self.is_date(parts[0]) and self.is_time(parts[1])
        elif "T" in cell:
            parts = cell.split("T")
            if len(parts) > 2:
                return False
            isdate = self.is_date(parts[0])
            if not isdate:
                return False
            # [date]T[time] or [date]T[time]Z
            if parts[1].endswith("Z") and self.is_time(parts[1][:-1]):
                return True
            if self.is_time(parts[1]):
                return True
            # [date]T[time][+-][time]
            if "+" in parts[1]:
                subparts = parts[1].split("+")
                istime1 = self.is_time(subparts[0])
                if not istime1:
                    return False
                istime2 = self.is_time(subparts[1])
                if istime2:
                    return True
                if self._run_regex(subparts[1], "time_HHMM"):
                    return True
                if self._run_regex(subparts[1], "time_HH"):
                    return True
            elif "-" in parts[1]:
                subparts = parts[1].split("-")
                istime1 = self.is_time(subparts[0])
                if not istime1:
                    return False
                istime2 = self.is_time(subparts[1])
                if istime2:
                    return True
                if self._run_regex(subparts[1], "time_HHMM"):
                    return True
                if self._run_regex(subparts[1], "time_HH"):
                    return True
        return False

    def is_nan(self, cell: str, is_quoted: bool = False) -> bool:
        if cell.lower() in ["n/a", "na", "nan"]:
            return True
        return False

    def is_unix_path(self, cell: str, is_quoted: bool = False) -> bool:
        return self._run_regex(cell, "unix_path")

    def is_bytearray(self, cell: str, is_quoted: bool = False) -> bool:
        return cell.startswith("bytearray(b") and cell.endswith(")")

    def is_json_obj(self, cell: str, is_quoted: bool = False) -> bool:
        if not (cell.startswith("{") and cell.endswith("}")):
            return False
        try:
            _ = json.loads(cell)
        except json.JSONDecodeError:
            return False
        return True


    def gen_known_type(cells):
        """
        Utility that yields a generator over whether or not the provided cells are
        of a known type or not.
        """
        td = type_detector()
        for cell in cells:
            yield td.is_known_type(cell)
        
    @classmethod
    def record_score(self, 
        data: List[List],
        dialect: Dialect
    ) -> float:
        """
        Computes the record score as the sum of detected cells data-type.

        Parameters
        ----------
        data: List[List[str]]
            the data as a List of String List
            
        dialect: Dialect
            the dialect used to read the file

        Returns
        -------
        record_score: float

        """
        try:
            td = type_detector()
            TotalScore = 0
            for record in data:
                tmpSum = 0
                k = 0
                for field in record:
                    k += 1
                    if td.is_known_type(trip_quotes(field, dialect)):
                        tmpSum += 100
                    else:
                        tmpSum += 0.1
                TotalScore += math.pow(tmpSum, 2)/(100 * math.pow(k, 2))
            return TotalScore
        except:
            pass
    
def trip_quotes( 
    field: str,
    dialect: Dialect
) -> str:
    if field != '':
        #Care and removal of spaces at the beginning of fields
        field = field.strip()
        return trip_ends(field, dialect) if field != '' else field
    else:
        return field

def trip_ends(
    field: str,
    dialect: Dialect
) -> str:
    if field[0] == dialect.quotechar and field[-1:] == dialect.quotechar:
        return field[1:-1]
    else:
        return field