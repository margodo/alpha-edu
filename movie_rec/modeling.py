import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

ratings_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings_df = pd.read_csv('u.data', sep='\t', names=ratings_cols, encoding='latin-1')
print("Структура данных рейтингов пользователей:")
print(ratings_df.head())

movies_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure',
               'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
               'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies_df = pd.read_csv('u.item', sep='|', names=movies_cols, encoding='latin-1', usecols=['movie_id', 'title'])
print("Структура данных о фильмах:")
print(movies_df.head())
print(movies_df.info())

ratings_df = ratings_df.merge(movies_df, on='movie_id')
print("Структура объединенных данных:")
print(ratings_df.head())

user_movie_matrix = ratings_df.pivot_table(index='title', columns='user_id', values='rating')
print("Фрагмент матрицы пользователь-фильм:")
print(user_movie_matrix.head())
print(user_movie_matrix.info())

user_movie_matrix.fillna(0, inplace=True)

# * all pandas dataframes
user_similarity = cosine_similarity(user_movie_matrix)

user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
print("Фрагмент матрицы сходства пользователей:")
print(user_similarity_df.head())

# Функция для рекомендации фильмов на основе схожести пользователей
def recommend_movies(user_id, num_recommendations=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:6]
    print(f"Похожие пользователи для {user_id}: {similar_users.index.tolist()}")
    
    movies_watched_by_user = user_movie_matrix.loc[user_id]
    recommended_movies = pd.Series(dtype='float64')
    
    for similar_user in similar_users.index:
        similar_user_ratings = user_movie_matrix.loc[similar_user]
        similar_user_unwatched = similar_user_ratings[movies_watched_by_user == 0]
        recommended_movies = pd.concat([recommended_movies, similar_user_unwatched])

    recommended_movies = recommended_movies.groupby(recommended_movies.index).mean()
    recommended_movies = recommended_movies.sort_values(ascending=False).head(num_recommendations)
    
    print("Рекомендованные фильмы:")
    print(recommended_movies)
    
    return recommended_movies.index.tolist()

recommended = recommend_movies(1, 5)
print("Рекомендуемые фильмы:", recommended)