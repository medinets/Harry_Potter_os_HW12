from title_films import films_titles
from award_films import films_awards
import pprint
import os
import string
awards_with_titles = {}
for i in range(len(films_awards)):
    awards = []
    title = films_awards[i]['results'][0]['movie']['title'].replace(':' , '') #(◑‿◐)
    for award in films_awards[i]['results']:
        award_dict = {'type': award['type'], 'award_name': award['award_name'], 'award': award['award']}
        awards.append(award_dict)
    awards = sorted(awards, key=lambda x: x['award_name'])
    awards_with_titles.update({f'{title}': awards})


os.mkdir('Harry Potter')
os.chdir('Harry Potter')
for i in range(len(films_titles['results'])):
    title = films_titles['results'][i]['title'].replace(':' , '') #(◑‿◐)
    os.mkdir(f'{title}')
    os.chdir(f'{title}')
    for letter in string.ascii_uppercase:
        os.mkdir(f'{letter}')
        os.chdir(f'{letter}')
        for titled_awards in awards_with_titles[f'{title}']:
            if titled_awards['award_name'][0] == letter:
                award_title = titled_awards['award_name']
                with open(f'{award_title}.txt', 'a', encoding='utf-8') as file:
                    file.write(titled_awards['award']+'\n')
        os.chdir('..')
    os.chdir('..')
