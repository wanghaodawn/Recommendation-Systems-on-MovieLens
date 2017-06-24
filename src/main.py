import os

data_set_name = 'ml-latest-small'

from read_data import *
from classes import *


def main():
    file_path = os.getcwd()
    file_path = file_path[0: len(file_path) - 3] + 'data/' + data_set_name + '/'

    dic_links = read_data_links(file_path + 'links.csv')
    dic_movies = read_data_movies(file_path + 'movies.csv')
    dic_ratings = read_data_ratings(file_path + 'ratings.csv')
    dic_tags = read_data_tags(file_path + 'tags.csv')


if __name__ == "__main__":
    main()