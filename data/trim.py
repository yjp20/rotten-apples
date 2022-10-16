import pandas as pd
import sys

#trimming the reviews for fine tuning data
def trimReview(filename, newFilename):
    df = pd.read_csv(filename, usecols=["review_text", "review_rating"])
    df.to_csv(newFilename, index = False)

def trim_files():
    for filename in sys.argv[1:]:
        trimReview(filename, "trimmed" + filename)

trim_files()