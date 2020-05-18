import pandas as pd


df = pd.read_csv('songs_lem_relevant.csv', delimiter=',')


def get_df():
    return df


def get_all_songs():
    return [i.split(";") for i in df.lyrics]


def most_freq_words(song, n=10):
    return sorted(set(song), key=song.count, reverse=True)[:n]



if __name__ == "__main__":
    v = get_all_songs()
    s1 = v[0]
    print(s1)
    # print(s1.count('could'))
    # print(s1.count('wonderful'))
    print(most_freq_words(s1))