
import numpy as np
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('users.data', sep='\t', names=column_names)

df.head()

len(df)

movie_titles = pd.read_csv("movie_id_titles.csv")
movie_titles.head()

len(movie_titles)

df = pd.merge(df, movie_titles, on='item_id')
df.head()

moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()

type(moviemat)

starwars_user_ratings = moviemat['Star Wars (1977)']
starwars_user_ratings.head()

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

similar_to_starwars

type(similar_to_starwars)

corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()

corr_starwars.sort_values('Correlation',ascending=False).head(10)

df.head()

df.drop(['timestamp'], axis = 1)

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

ratings.sort_values('rating',ascending=False).head()

ratings['rating_oy_sayisi'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

ratings.sort_values('rating_oy_sayisi',ascending=False).head()

corr_starwars.sort_values('Correlation',ascending=False).head(10)

corr_starwars = corr_starwars.join(ratings['rating_oy_sayisi'])
corr_starwars.head()

corr_starwars[corr_starwars['rating_oy_sayisi']>100].sort_values('Correlation',ascending=False).head()