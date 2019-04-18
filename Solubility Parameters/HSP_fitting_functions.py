# -*- coding: utf-8 -*-
"""
HSP Fitting Functions

This is a simulation of diffusion in 1-D with a surface energy term
Written by:  Andrew J. Guenthner
Started:  April 17, 2019
Version Number:  0.1
Version Completed:  April 17, 2019

Expects:  a CSV file in the same directory with labeled columns including:
1. an index code in the first column 
2. a header in the first row with column names
3. columns labeled "delta_d", "delta_h", and "delta_p" with no missing values 
4. optional name or other info columns 

Functions:
HSP_chi2_from_CAS (dd, dp, dh, r_int, solv_tests{}) -- computes chi values for proposed 
HSP values, proposed radius of interaciton, and dictionary of solvent tests, uses
Hansen's rules for doubling distance delta-d distance components


"""
import pandas as pd 

def HSP_chi2_from_CAS (dd = 0.0, dp = 0.0, dh = 0.0, r_int = 1.0, solv_tests = {'64-17-5':False}):
    """
    Computes chi-squared goodness-of-fit value (higher is better) for HSP values of
    delta-d =dd, delta-p = dp, delta-h = dh, and radius of interaction = r_int and 
    a series of solvent test results, stored in a dictionary solv_tests with CAS #s as
    keys and solubility results (True = good solubility) as booleans.  Conforms to Hansen's
    distance rules (e.g. distance in delta-d space are multiplied by 2).  Returns the value
    of the chi-squared parameter.
    """
    chi2 = 0.0
    return chi2