from model_use import *
from data_funcs import *
from algebra import *
import numpy as np
import json

model = load_model('first.model')
my_song = filter_lyrics(
    "Look at her face, it's a wonderful face, And it means something special to me, Look at the way that she smiles when she sees me, How lucky can one fellow be?, , She's just my kind of girl, she makes me feel fine, Who could ever believe that she could be mine?, She's just my kind of girl, without her I'm blue, And if she ever leaves me what could I do, what could I do?, , And when we go for a walk in the park, And she holds me and squeezes my hand, We'll go on walking for hours and talking, About all the things that we plan, , She's just my kind of girl, she makes me feel fine, Who could ever believe that she could be mine?, She's just my kind of girl, without her I'm blue, And if she ever leaves me what could I do, what could I do?")

songs = get_all_lyrics()

# s1 = get_lyrics_by_name('Merry Christmas Baby')
# print(s1)


# s1 = songs[3056]
# s2 = songs[15112]

# s3 = songs[475]
lst = []
info = get_all_info()

for i in range(1000):
    if i % 100 == 0:
        print(i)
    if len(songs[i]) == 0:
        continue
    diff = mat_dist_abs(song2matrix(songs[i], model), song2matrix(my_song, model))
    lst.append(diff)

top_10 = sorted(lst)[:10]
print(top_10)
for i in top_10:
    print("Difference: ", i)
    print("Index: ", lst.index(i))
    print("Name: ", info[lst.index(i)])
    print("\n")

# x = np.array(lst)
# np.save("all_songs", x)

# m1 = song2matrix(s1, model)
# m2 = song2matrix(s2, model)
# m3 = song2matrix(s3, model)


# my_string = json.dumps(m1)
# with open("test1.npy", "w") as f:
# data = np.load("test1.npy", allow_pickle=True)
# print(len(data[0][0]))

# d = mat_dist_sq(m1, m2)
# d_big = mat_dist_sq(m1, m3)
# d_big1 = mat_dist_sq(m2, m3)
#
# print(d)
# print(d_big)
# print(d_big1)

# d = mat_dist_abs(m1, m2)
# d_big = mat_dist_abs(m1, m3)
# d_big1 = mat_dist_abs(m2, m3)

# print(d)
# print(d_big)
# print(d_big1)

# with open("test1.npy") as f:
#     f.seek(0)
