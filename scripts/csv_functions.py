# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:28:49 2022

key = bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD
@author: ryanm
"""

import cohere
from cohere.classify import Example
from multiprocessing import Pool
import csv
import pandas as pd

api_key = "bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD"
co = cohere.Client(api_key)
examples = [Example("1", "hello"), Example("2", "hello"), Example("3", "hi"), Example("4", "hi")]

#helper function to summarize sin, returns 0th value of generation column
def summarizer(inp, loop=True):
    idx, row = inp
    sin = row['review_text']
    sin = sin[:2400]
    try:
        n_generations = 5

        prediction = co.generate(
            model='large',
            prompt=sin,
            return_likelihoods = 'GENERATION',
            stop_sequences=['"'],
            max_tokens=100,
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
    except Exception as err:
        print(err)
        if loop:
            return summarizer(inp, False)
        else:
            return 0
    print(df['generation'].iat[0])
    return df['generation'].iat[0]

def classifier(filename, newFilename, ins, exs, columnName):
    print("classifying")
    response = co.classify(
      model='68283aef-f7cf-4b9f-8a2c-b638932c8154-ft',
      inputs=ins,
      examples=exs)
    df = pd.read_csv(filename)
    df.loc[:, columnName] = [x.prediction for x in response.classifications]
    df.to_csv(newFilename, index = False)

#opens a csv file
#creates a new column by applying function func to an existing column
#creates a new file named newFilename
def applyReview(filename, newFilename, func, columnName):
    df = pd.read_csv(filename, on_bad_lines='skip')
    df[columnName] = ""
    pool = Pool(15)
    results = pool.map(func, df.iterrows())
    for idx, row in df.iterrows():
        df.loc[idx, columnName] = results[idx]
    df.to_csv(newFilename, index = False)
