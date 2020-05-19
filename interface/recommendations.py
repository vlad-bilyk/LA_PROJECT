from data_modules import newdata_funcs
from calc_modules import algebra, model_funcs
import time


def get_recommendations(song_matrix, model, n=10, pvar=None, window=None):
    songs = newdata_funcs.get_all_songs()
    total = len(songs)
    # total = 3000  # for testing
    step = 1000

    lst = []
    for i in range(total):
        if i % step == 0:
            print(i)

            if pvar is not None and window is not None:
                time.sleep(0.1)
                pvar.set((i / total) * 100)
                window.update_idletasks()

        arr = newdata_funcs.most_freq_words(songs[i], n)
        mat = model_funcs.song2matrix(arr, model)

        if len(mat) < 10:
            lst.append(float("inf"))
            continue

        dist = algebra.mat_dist_sq(mat, song_matrix)
        lst.append(dist)

    top10 = [lst.index(i) for i in sorted(lst)[:10]]
    pvar.set(100)
    return top10
