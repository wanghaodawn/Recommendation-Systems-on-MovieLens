from classes import *

def read_data_links(file_name):
    f = open(file_name, 'r')
    dic_links = dict()

    # Traverse the file
    while True:
        line = str(f.readline()).strip()
        # If line is null
        if not line:
            break

        data = line.split(',')
        movie_id = data[0]
        imdb_id = data[1]
        tmdb_id = data[2]

        dic_links[movie_id] = Link(movie_id, imdb_id, tmdb_id)

    return dic_links


def read_data_movies(file_name):
    f = open(file_name, 'r')
    dic_movies = dict()

    # Traverse the file
    while True:
        line = str(f.readline()).strip()
        # If line is null
        if not line:
            break

        data = line.split(',')
        movie_id = data[0]
        title = data[1]
        genres = data[2].split('|')

        dic_movies[movie_id] = Movie(movie_id, title, genres)

    return dic_movies


def read_data_ratings(file_name):
    f = open(file_name, 'r')
    dic_ratings = dict()

    # Traverse the file
    while True:
        line = str(f.readline()).strip()
        # If line is null
        if not line:
            break

        data = line.split(',')
        user_id = data[0]
        movie_id = data[1]
        rating = data[2]
        timestamp = data[3]

        dic_ratings[user_id + ',' + movie_id] = Rating(user_id, movie_id, rating, timestamp)

    return dic_ratings


def read_data_tags(file_name):
    f = open(file_name, 'r')
    dic_tags = dict()

    # Traverse the file
    while True:
        line = str(f.readline()).strip()
        # If line is null
        if not line:
            break

        data = line.split(',')
        user_id = data[0]
        movie_id = data[1]
        tag = data[2]
        timestamp = data[3]

        dic_tags[user_id + ',' + movie_id] = Tag(user_id, movie_id, tag, timestamp)

    return dic_tags

