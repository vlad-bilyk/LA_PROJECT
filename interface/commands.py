from data_modules.newdata_funcs import *
from calc_modules.model_funcs import *
from calc_modules.algebra import *
from interface.recommendations import *
import random

model = load_model("../data/first.model")
df = get_df()
bands = list(set(df.band))
# chosen_bands = set()
# user_bands = dict()


def get_next_bands():
    random.shuffle(bands)
    chosen_bands = bands[:6]
    del bands[:6]
    return chosen_bands


def get_band_songs(band):
    return list(df.name[df.band == band])


def get_next_songs(band_songs):
    random.shuffle(band_songs)
    chosen_songs = band_songs[:6]
    del band_songs[:6]
    return chosen_songs
#
# def get_next_songs(band):
#     songs = set(df.name[df.band == band])
#     random.shuffle(songs)
#     chosen_songs = songs[:6]
#     del songs[:6]
#     return chosen_songs


if __name__ == "__main__":
    print(len(bands))
    print(get_next_bands())
    print(len(bands))
    print(get_next_bands())
    print(len(bands))
    print(get_next_bands())