# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:28:49 2022

key = bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD
@author: ryanm
"""

import cohere
import csv
import pandas as pd

api_key = "bVBDxyqnmSkyQvWF8JTAm4nb0szv5Cy5gyivcysD"
co = cohere.Client(api_key)

def summarize(sin):
    n_generations = 10

    prediction = co.generate(
        model='large',
        prompt=sin,
        return_likelihoods = 'GENERATION',
        stop_sequences=['"'],
        max_tokens=50,
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
    print(df)
    
def summarizeReviews():
    with open('reviews.csv') as reviewInput:
        reviewReader = csv.reader(reviewInput, delimiter = ',')
        summaryOutput = open('summarized.csv', mode = 'w', newline='')
        summaryWriter = csv.writer(summaryOutput)
        for line in reviewReader:
            temp = [line[0], summarize(line[1])]
            summaryWriter.writerow(line)
        reviewInput.close()
        summaryOutput.close()

def adjuster():
    
    pass
    
#summarizeReviews()
summarize("In Ao Ashi, this rarely happens. The only match in which there is a greater build-up of opponents is the match against team Musashino, the last match of the season. If you notice, in the other matches, it's all about Tokyo Esperion F.C. I don't even remember the names of the other teams and their players, and I can count on my fingers the number of faces I would recognize. This isn't because my memory is bad, it's because they don't really matter. Aoi's matches do indeed function as a vehicle for the rise of the team and the characters, but at some point the author seems to have forgotten to reconcile this with the other side's point of view, so that the opponents are just random people and have nothing to offer but responsiveness to tactics. In summary, Ao Ashi was a very mixed and conflicting experience before my eyes. In one of the fields of vision, I see a skeleton of sports seinen with great portrayals of football and pertinent discussions, as well as a protagonist whose character work and development will drag any fan into the whirlpool of history. On the other hand, I see a production and filling of the molds in an insufficient way. A soulless adaptation of an uninspired direction that could have given me more. There are many things to talk about, and it is not my biggest challenge to understand or organize them, but to limit myself so that this text doesn't get even bigger than it already is.")
adjuster()