# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:28:49 2022

key = bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD
@author: ryanm
"""
#run this script in the scripts directory with the arg *.csv

import cohere
from cohere.classify import Example
import csv
import pandas as pd
import csv_functions
import sys

api_key = "bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD"
co = cohere.Client(api_key)
examples = []
inputs = []
   

#summarize all csv files
#take in example data into examples list
#run classifier for each csv file, clear inputs
#done

def read_files():
    for urmom in sys.argv[1:]:
            csv_functions.applyReview(urmom, urmom, csv_functions.summarizer, "summarized")
            #csv_functions.applyReview(urmom, urmom, csv_functions.classifier, "classifier")
    df = pd.read_csv("reviews.csv")
    for index, row in df.iterrows():
        #print(index)
        examples.append(Example(row['review_rating'], row['summarized']))
    print(examples)
        
read_files()
