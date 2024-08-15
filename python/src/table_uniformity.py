#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2024 W. García
Creative Commons Attribution 4.0 | https://creativecommons.org/licenses/by/4.0/

GENERAL INFO:
This class module deals with computation of the table uniformity as described in the paper
"Detecting CSV file dialects by table uniformity measurement and data type inference", available 
at https://content.iospress.com/articles/data-science/ds240062. 

"""
import math

from typing import List

class t_uniformity:
    """
    This container holds methods for compute Table Uniformity parameters.

    Parameters
    ----------
    table : list[list[str]]
        Target table.

    """
    def __init__(
        self,
        table: list[list[str]],
    ) -> None:
        self.table = table
    
    def validate(self) -> None:
        if self.table is None :
            raise ValueError(
                "The target table should be provided, got: %r"
                % self.table
            )
        
    def avg_fields(self) -> float:
        nk = 0
        for record in self.table:
            nk += len(record)
        return nk / len(self.table)

    def compute(self) -> List[float]:
        self.validate()
        phi = self.avg_fields()
        mu, c, sm, alpha, beta = 0, 0, 0, 0, 0
        n = len(self.table) #Number of records
        for i in range (0, n):
            k_i = len(self.table[i]) #Number of fields in current record
            mu += math.pow(k_i - phi, 2) #Deviations
            if i == 0:
                c += 1
                k_max = k_i
                k_min = k_i
                if n== 1:
                    sm = c
            else:
                if k_i > k_max:
                    k_max = k_i
                if k_i < k_min:
                    k_min = k_i
                k_prev = len(self.table[i - 1])
                if k_prev != k_i:
                    alpha += 1
                    if c > sm:
                        sm = c #Segmented mode
                    c = 0
                else:
                    c += 1
                    if i == n - 1:
                        if c > sm:
                            sm = c
        if n > 1:
            sigma = math.sqrt(mu / (n - 1)) #Standard deviation
        else:
            sigma = math.sqrt(mu / n)

        tau_0 = 1 / (1 + 2 * sigma) #Consistency factor
        r = k_max - k_min #Range of fields
        if alpha > 0:
            beta = sm / n #Records variability factor
        tau_1 = 2 * r * (math.pow(alpha, 2) + 1) * ((1 - beta) / sm) #Records dispersion
        return [tau_0, tau_1]