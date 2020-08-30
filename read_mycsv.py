import pandas as pd
df = pd.read_csv("path_to_file.cvs")
#in our case https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-08-29/metadata.csv
#displays rows and cols
print(df.shape)
#columns
print(df.columns)

#displying dataset
print(df)
for i in df['column_name'].values:
    print(i)
