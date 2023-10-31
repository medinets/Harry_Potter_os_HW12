from data_films import films_data
from genres import ganres
import json
import os
import csv

ganres = json.loads(ganres)
for i in range(len(ganres['results'])):
    genre = ganres['results'][i]['genre']
    os.mkdir(f'{genre}')
    os.chdir(f'{genre}')
    with open(f'{genre}.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['title', 'year', 'rating', 'type', 'genres'])
        writer.writeheader()
    os.chdir('..')

for i in range(len(films_data)):
    for genre in films_data[i]['gen']:
        genre_dir = genre['genre']
        os.chdir(f'{genre_dir}')
        with open(f'{genre_dir}.csv', 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['title', 'year', 'rating', 'type', 'genres'])
            title = films_data[i]["title"]
            year = films_data[i]["year"]
            rating = films_data[i]["rating"]
            type1 = films_data[i]["type"]
            genres = []
            for genre_1 in films_data[i]['gen']:
                genres.append(genre_1['genre'])
            genres_res = ";".join(genres)
            row_data = {'title': title, 'year': year, 'rating': rating, 'type': type1, 'genres': genres_res}
            writer.writerow(row_data)
        os.chdir('..')

