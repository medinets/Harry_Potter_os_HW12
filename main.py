from video_manager.media_player import Player
from video_manager.films_worker import Film
import os
import string

player_1 = Player("rickroll", "https://youtu.be/dQw4w9WgXcQ?si=GWteDv_fY-dFScal", 213)
print(player_1.play("https://youtu.be/dQw4w9WgXcQ?si=GWteDv_fY-dFScal"))
print(player_1.playing)
player_1.pause()
#player_1.pause()
print(player_1.playing)

print(player_1.quality)
player_1.change_quality("4K")
print(player_1.quality)

print(os.getcwd())
os.chdir("film_player")
print(os.getcwd())
os.mkdir("film_storage")
os.chdir("film_storage")
for letter in string.ascii_uppercase:
        os.mkdir(f'{letter}')

film_1 = Film("Drive", 2011)
film_2 = Film("Cars: 2", 2011)
print(film_1.get_film_address())
print(film_2.get_film_address())