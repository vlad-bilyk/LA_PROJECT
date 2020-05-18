import pandas as pd
from text_funcs import filter_lyrics


df = pd.read_csv('songs.csv', delimiter=',')


def get_all_lyrics():
    """
    :return: list of filtered songs' lyrics
    """

    songs_lyrics = []

    for i in df.lyrics:
        try:
            filtered = filter_lyrics(i)
        except ValueError:
            songs_lyrics.append([])
            continue
        songs_lyrics.append(filtered)

    return songs_lyrics


def get_lyrics_by_name(song_name):
    return df.lyrics[df.name == song_name]


def get_lyrics_by_index(ind):
    return df.loc[ind, 'lyrics']


# def get_lyrics(n)


