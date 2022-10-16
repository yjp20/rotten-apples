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
examples = [Example("1", "hello"), 
    Example("2", "hello"), Example("3", "hi"), Example("4", "hi")]
blah = ["aaaa",
    "bbbb"]
    
#helper function to summarize sin, returns 0th value of generation column
def summarizer(sin, loop=True):
    try:
        sin = sin[:100]
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
    except Exception as err:
        print(err)
        if loop:
            return summarizer(sin, false)
        else:
            return 0
    print(df['generation'].iat[0])
    return df['generation'].iat[0]
    
#adjuster helper function, returns classified value of sin\
#not working rn ignore
def classifier(sin):
    print("classifying")
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
def applyReview(filename, newFilename, func, columnName):
    df = pd.read_csv(filename, on_bad_lines='skip')
    df[columnName] = ""
    pool = Pool(15)
    results = [pool.apply_async(func, [row['review_text']]) for idx, row in df.iterrows()]
    for idx, row in df.iterrows():
        df.loc[idx, columnName] = results[idx].get()
    df.to_csv(newFilename, index = False)