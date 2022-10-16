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

api_key = "bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD"
co = cohere.Client(api_key)
examples = [Example("", "")]
inputs = ["aaaa",
    "bbbb"]
    
#helper function to summarize sin, returns 0th value of generation column
def summarizer(sin):
    n_generations = 5

    prediction = co.generate(
        model='large',
        prompt=sin,
        return_likelihoods = 'GENERATION',
        stop_sequences=['"'],
        max_tokens=30,
        temperature=0.7,
        num_generations=n_generations,
        k=0,
        p=0.75)
    # Get list of generations
    gens = []
    likelihoods = []
    for gen in prediction.generations:
        gens.append(gen.text)
        sum_likelihood = 0
        for t in gen.token_likelihoods:
            sum_likelihood += t.likelihood
        likelihoods.append(sum_likelihood)
    pd.options.display.max_colwidth = 200
    df = pd.DataFrame({'generation':gens, 'likelihood': likelihoods})
    df = df.drop_duplicates(subset=['generation'])
    df = df.sort_values('likelihood', ascending=False, ignore_index=True)
    return df["generation"].iat[0]
    
#adjuster helper function, returns classified value of sin
def classifier(sin):
    response = co.classify(
      model='medium',
      inputs=sin,
      examples=examples)
    #fix return value
    print(response.classifications)
    return sin


#opens a csv file
#creates a new column by applying function func to an existing column
#creates a new file named newFilename
def applyReviews(filename, newFilename, func, columnName):
    df = pd.read_csv(filename, usecols=["review_text", "review_rating"])
    df[columnName] = df['review_text'].apply(func)
    df.to_csv(newFilename, index = False)
