from bs4 import BeautifulSoup

import requests

import re

import pandas as pd
 
 
#  movies release 1980 and above

url = 'https://www.imdb.com/search/title/?release_date=1980-01-01,&sort=moviemeter,desc'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select('td.titleColumn')

crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]

ratings = [b.attrs.get('data-value')

        for b in soup.select('td.posterColumn span[name=ir]')]
 
# creating empty list for storing movie information

movielist = []
 
# Iterating over movies to extract ach movie's details

for index in range(0, len(movies)):

    movie_string = movies[index].get_text()

    movie = (' '.join(movie_string.split()).replace('.', ''))

    movie_title = movie[len(str(index))+1:-7]

    year = re.search('\((.*?)\)', movie_string).group(1)

    place = movie[:len(str(index))-(len(movie))]

    data = {"place": place,

            "movie_title": movie_title,

            "rating": ratings[index],

            "year": year,

            "star_cast": crew[index],

            }

    movielist.append(data)
 
df = pd.DataFrame(movielist)

df.to_csv('1980_&_Above_movies.csv',index=False)