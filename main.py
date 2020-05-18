from model_funcs import *
from newdata_funcs import *
from algebra import *
import pandas as pd

# df = pd.read_csv('songs.csv', delimiter=',')

model = load_model('first.model')

songs = get_all_songs()

n = 15  # number of words for matrix

# s1 = most_freq_words(songs[3056], n)
#
# m1 = song2matrix(s1, model)
#
# distances = []
#
# c = 0
# for text in songs:
#     if len(text) == 0:
#         continue
#     if c > 5000:
#         break
#     print(c)
#     m = song2matrix(text, model)
#     d = mat_dist_sq(m1, m)
#     distances.append(d)
#     c += 1
#
# recommended = []
#
# for i in range(10):
#     mind_ind = distances.index(min(distances))
#     recommended.append(mind_ind)
#     del distances[mind_ind]
#
# print("recommendations for :{}".format((df.band[3056], df.name[3056])))
# print([(df.band[i], df.name[i]) for i in recommended])
#
#
# c = 0
# ind = 0
# indexes = []
# for s in songs:
#     freq_w = most_freq_words(s, 10)
#     m = song2matrix(freq_w, model)
#     if len(m) == 0:
#         # print(c)
#         c += 1
#         indexes.append(ind)
#     ind += 1
# print(c)

# df = pd.read_csv('songs_lem.csv', delimiter=',')
# print(len(df))
#
# df = df.drop(indexes)
# print(len(df))
#
# df.to_csv('songs_lem_relevant.csv', index=False)