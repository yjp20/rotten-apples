import pandas as pd
import sys
import shutil

#run this script with the arg *.csv in the data directory
#catenate the trimmed files into single csv
def cat_trimmed():
    combined_csv = pd.concat([pd.read_csv(file) for file in sys.argv[1:]])
    combined_csv.to_csv("finetuning.csv", index=False, encoding='utf-8-sig')

cat_trimmed()   