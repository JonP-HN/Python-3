import requests_with_caching
import json

def get_movies_from_tastedive (movie_name):
    base_url = "https://tastedive.com/api/similar"
    parameters = {}
    parameters["q"] = movie_name
    parameters["type"] = "movies"
    parameters["limit"]= "5"
    movies = requests_with_caching.get(base_url,params = parameters)
    return movies.json()

def extract_movie_titles(title):
    movie_titles = []
    for item in title['Similar']['Results']:
        movie_titles.append(item['Name'])
        print('Name')
        print(movie_titles)
    return movie_titles

def get_related_titles(extracted_movies):
    similar_movies = []
    for movie in extracted_movies:
        lst = extract_movie_titles(get_movies_from_tastedive(movie))
        for movie in lst:
            if movie not in similar_movies:
                similar_movies.append(movie)
    print(similar_movies)
    return similar_movies

def get_movie_data(movie):
    baseurl = "http://www.omdbapi.com/"
    params = {}
    params['t'] = movie
    params['r'] = "json"
    resp = requests_with_caching.get(baseurl, params=params)
    filmdata = resp.json()
    return filmdata

def get_movie_rating(rate):  
    rating = 0
    for i in rate["Ratings"]:
        if i["Source"] == "Rotten Tomatoes":
            str1 = i["Value"]
            str_r = str1.replace("%", "")
            rating = int(str_r)
            break
        else:
            rating = 0
    return(rating)

def get_sorted_recommendations(movie_list):
    recommended = sorted(get_related_titles(movie_list), key=lambda m: (get_movie_rating(get_movie_data(m)),m), reverse=True)
    return recommended

print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
