import os
import pandas as pd

MOVIELENS_DIR = 'movie_raw_data'
USER_DATA_FILE = 'users.dat'
MOVIE_DATA_FILE = 'movies.dat'
RATING_DATA_FILE = 'ratings.dat'

AGES = {1: "Under 18", 18: "18-24", 25: "25-34",
        35: "35-44", 45: "45-49", 50: "50-55", 56: "56+"}

OCCUPATIONS = {0: "other or not specified", 1: "academic/educator", 2: "artist", 3: "clerical/admin",
               4: "college/grad student", 5: "customer service", 6: "doctor/health care",
               7: "executive/managerial", 8: "farmer", 9: "homemaker", 10: "K-12 student", 11: "lawyer",
               12: "programmer", 13: "retired", 14: "sales/marketing", 15: "scientist", 16: "self-employed",
               17: "technician/engineer", 18: "tradesman/craftsman", 19: "unemployed", 20: "writer"}

USERS_CSV_FILE = 'users.csv'
MOVIES_CSV_FILE = 'movies.csv'
RATINGS_CSV_FILE = 'ratings.csv'

# Doc file rating raw
ratings = pd.read_csv(os.path.join(MOVIELENS_DIR, RATING_DATA_FILE),
                      sep='::',
                      engine='python',
                      encoding='latin-1',
                      names=['user_id', 'movie_id', 'rating', 'timestamp'])

# Set max_userid to the maximum user_id in the ratings
max_userid = ratings['user_id'].drop_duplicates().max()
# Set max_movieid to the maximum movie_id in the ratings
max_movieid = ratings['movie_id'].drop_duplicates().max()

# Process ratings dataframe for Keras Deep Learning model
# Add user_emb_id column whose values == user_id - 1
ratings['user_emb_id'] = ratings['user_id'] - 1
# Add movie_emb_id column whose values == movie_id - 1
ratings['movie_emb_id'] = ratings['movie_id'] - 1

print (len(ratings)), 'ratings loaded'

# Save into ratings.csv
ratings.to_csv(RATINGS_CSV_FILE, 
               sep='\t', 
               header=True, 
               encoding='latin-1', 
               columns=['user_id', 'movie_id', 'rating', 'timestamp', 'user_emb_id', 'movie_emb_id'])
print ('Saved to'), RATINGS_CSV_FILE

# Read the Users File
users = pd.read_csv(os.path.join(MOVIELENS_DIR, USER_DATA_FILE), 
                    sep='::', 
                    engine='python', 
                    encoding='latin-1',
                    names=['user_id', 'gender', 'age', 'occupation', 'zipcode'])
users['age_desc'] = users['age'].apply(lambda x: AGES[x])
users['occ_desc'] = users['occupation'].apply(lambda x: OCCUPATIONS[x])
print (len(users)), 'descriptions of', max_userid, 'users loaded.'

# Save into users.csv
users.to_csv(USERS_CSV_FILE, 
             sep='\t', 
             header=True, 
             encoding='latin-1',
             columns=['user_id', 'gender', 'age', 'occupation', 'zipcode', 'age_desc', 'occ_desc'])
print ('Saved to'), USERS_CSV_FILE

# Read the Movies File
movies = pd.read_csv(os.path.join(MOVIELENS_DIR, MOVIE_DATA_FILE), 
                    sep='::', 
                    engine='python', 
                    encoding='latin-1',
                    names=['movie_id', 'title', 'genres'])
print (len(movies)), 'descriptions of', max_movieid, 'movies loaded.'

# Save into movies.csv
movies.to_csv(MOVIES_CSV_FILE, 
              sep='\t', 
              header=True, 
              columns=['movie_id', 'title', 'genres'])
print ('Saved to'), MOVIES_CSV_FILE
