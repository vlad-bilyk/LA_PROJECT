from data_modules import newdata_funcs
from calc_modules import algebra, model_funcs


def get_recommendations(song_matrix, model, n=10):
    songs = newdata_funcs.get_all_songs()
    # my_song = model_funcs.song2matrix(newdata_funcs.most_freq_words(songs[song_index], n), model)

    lst = []
    for i in range(len(songs)):
        if i % 1000 == 0:
            print(i)
        arr = newdata_funcs.most_freq_words(songs[i], n)
        mat = model_funcs.song2matrix(arr, model)

        if len(mat) < 10:
            lst.append(float("inf"))
            continue

        lst.append(algebra.mat_dist_sq(mat, song_matrix))

    top15 = [lst.index(i) for i in sorted(lst)[:10]]
    return top15
