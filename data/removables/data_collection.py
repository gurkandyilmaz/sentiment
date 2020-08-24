"""
Combine all the files into a single balanced dataframe.
"""

##{
import pandas as pd
##}

##{
def df_info(df_list):
    shape, value_counts, sums = [], [], {}
    for df in df_list:
        shape.append(df.shape)
        value_counts.append(df['label'].value_counts())
        
    return shape, value_counts


film_file = "film_yorum_2k.tsv"
turkcell_large_file = "turkcell_53k.csv"
hepsiburada_file = "hepsiburada_240k.csv"
vodafone_large_file = "vodafone_32k.csv"
turktelekom_large_file = "turktelekom_96k.csv"
movie_reviews_file = "movie_ratings_83k.csv"

film = pd.read_csv(film_file, sep='\t') #usecols=['Review','Sentiment']
turkcell = pd.read_csv(turkcell_large_file)
hepsiburada = pd.read_csv(hepsiburada_file)
vodafone = pd.read_csv(vodafone_large_file)
turktelekom = pd.read_csv(turktelekom_large_file)
movie_reviews = pd.read_csv(movie_reviews_file) #usecols=['comment', 'point']

film.drop(columns = ['ID'], inplace=True)
film.columns = ['text','label']
film.dropna(axis='index', inplace=True)
film['label'] = film['label'].apply(lambda label: int(label))
turkcell.drop(columns = ['DATE'], inplace=True)
turkcell.columns = ['text', 'label']
vodafone.drop(columns = ['DATE'], inplace=True)
vodafone.columns = ['text','label']
turktelekom.drop(columns=['DATE'], inplace=True)
turktelekom.columns=['text', 'label']
hepsiburada.columns = ['label', 'text']
movie_reviews['comment'] = movie_reviews['comment'].apply(lambda row: row.strip())
movie_reviews.drop(columns = ['film_name'], inplace=True)
movie_reviews.columns = ['text', 'label']
movie_reviews['label'] = movie_reviews['label'].str.replace(',', '.')
movie_reviews['label'] = movie_reviews['label'].apply(lambda rating: 1 if float(rating)>3.0 else 0)

dfs = (film, turkcell, vodafone, turktelekom, hepsiburada, movie_reviews)
shape, value_counts = df_info(dfs)
##}


##{
unbalanced_df = pd.concat(dfs, axis=0)
unbalanced_df.to_csv('sentiment_unbalanced.csv', index=False)
pos_df = unbalanced_df[unbalanced_df['label']==1].sample(n=unbalanced_df['label'].value_counts()[0])
neg_df = unbalanced_df[unbalanced_df['label']==0]
balanced_df = pd.concat((pos_df,neg_df), axis=0)
balanced_df.to_csv('sentiment_balanced.csv', index=False)
##}

