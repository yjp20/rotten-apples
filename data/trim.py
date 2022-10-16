import pandas as pd
import sys

#run this script with the arg *.csv in the data directory

#trimming the reviews for fine tuning data
def trimReview(filename, newFilename):
    df = pd.read_csv(filename, usecols=["review_text", "review_rating"])
    df.to_csv(newFilename, index = False)

def trim_files():
    for filename in sys.argv[1:]:
        trimReview(filename, "trimmed" + filename)

#catenate the trimmed files into single csv
def cat_trimmed():
    combined_csv = pd.concat([pd.read_csv(file) for file in sys.argv[1:])
    combined_csv.to_csv("finetuning.csv", index=False, encoding='utf-8-sig')
    
trim_files()
cat_trimmed()