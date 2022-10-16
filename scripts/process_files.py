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


#summarize all csv files
#take in example data into examples list
#run classifier for each csv file, clear inputs
#done

def read_files():
    #for urmom in sys.argv[1:]:
        #csv_functions.applyReview(urmom, urmom, csv_functions.summarizer, "summarized")
        #csv_functions.applyReview(urmom, urmom, csv_functions.classifier, "classifier")
    for urmom in sys.argv[1:]:
        df = pd.read_csv(urmom)
        examples = []
        for index, row in df.iterrows():
            examples.append(Example('summarized', 'review_rating'))
        inputs = list(df.loc[:, "summarized"])
        print(inputs)
        csv_functions.classifier(urmom, urmom, inputs, examples, "classified")
    print(examples)

if __name__ == '__main__':
    read_files()
