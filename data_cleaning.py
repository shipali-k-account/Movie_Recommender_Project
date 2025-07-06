import pandas as pd
df=pd.read_csv("data/movie.csv") # original data set 
df=df[df['genres'].notna()]# remove the rows with no genres
df["year"]=df["title"].str.extract(r"\((\d{4})\)",expand=False) # extract year from title(new cloumn called year is created)
df["clean_title"]=df["title"].str.replace(r"\(\d{4}\)", "",regex=True).str.strip() # remove the year in title column
df["text"]=df["clean_title"]+ " "+df["genres"].str.replace("|"," ")# combine the 2 col
df.to_csv("data/clean_movie.csv",index=False)
print("cleaned data saved to data/clean_movie.csv")