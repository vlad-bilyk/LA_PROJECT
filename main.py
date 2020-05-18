from data_modules.newdata_funcs import *
from calc_modules.model_funcs import *
from calc_modules.algebra import *
from interface.recommendations import *
import random

if __name__ == '__main__':
    model = load_model("data/first.model")
    df = get_df()
    bands = set(df.band)
    chosen_bands = set()
    user_bands = dict()
    n = 3
    while len(user_bands) < 3:
        bands = bands.difference(chosen_bands)
        chosen_bands = random.sample(bands, 10)
        print(['{} - {}'.format(i, chosen_bands[i - 1]) for i in range(1, 11)])
        inp = input("Choose a band (1 - 10), 0 - to reroll\n")
        if int(inp) != 0:
            user_bands[chosen_bands[int(inp) - 1]] = ''
        while inp != '0' and len(user_bands) < 3:
            inp = input("Choose a band (1 - 10), 0 - to reroll\n")
            if int(inp) != 0:
                user_bands[chosen_bands[int(inp) - 1]] = ''

    for band in user_bands.keys():
        band_songs = ''
        chosen_songs = []
        songs = set(df.name[df.band == band])
        while len(band_songs) < 1:
            songs = songs.difference(set(chosen_songs))
            print(len(songs))
            if len(songs) == 0:
                break
            print("Current band: ", band)
            n = 6 if len(songs) >= 6 else len(songs)
            chosen_songs = random.sample(songs, n)
            print(['{} - {}'.format(i, chosen_songs[i - 1]) for i in range(1, n + 1)])
            inp = input("Choose a song (1 - 6), 0 - to reroll\n")
            if int(inp) != 0:
                band_songs = (chosen_songs[int(inp) - 1])
            while inp != '0' and len(band_songs) < 1:
                inp = input("Choose a song (1 - 6), 0 - to reroll\n")
                if int(inp) != 0:
                    band_songs = (chosen_songs[int(inp) - 1])

        user_bands[band] += band_songs
    print(user_bands)

    lyrics = []
    for k, v in user_bands.items():
        print(k, v)
        artist = df[df.band == k]
        song = artist[df.name == v]
        lyr = song.lyrics.item().split(';')
        lyrics.append(song2matrix(most_freq_words(lyr), model))

    matrix = []
    for mat in lyrics:
        matrix = add_matices(matrix, mat)

    for i in get_recommendations(matrix, model):
        print(i)
        print(get_band(i))
        print(get_name(i))
        print("\n")
