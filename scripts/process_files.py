# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:28:49 2022

key = bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD
@author: ryanm
"""

import cohere
from cohere.classify import Example
import csv
import pandas as pd
import csv_functions
import sys

api_key = "bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD"
co = cohere.Client(api_key)
examples = [Example("", "")]
inputs = ["aaaa",
    "bbbb"]
   
def read_files():
    for urmom in sys.argv[1:]:
            csv_functions.applyReviews(urmom, urmom, csv_functions.summarizer, "summarized")
            csv_functions.applyReviews(urmom, urmom, csv_functions.summarizer, "classifier")
            
# read_files()