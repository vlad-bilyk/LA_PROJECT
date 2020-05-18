from model_use import *
from data_funcs import *
from algebra import *

model = load_model('first.model')

songs = get_all_lyrics()

# s1 = get_lyrics_by_name('Merry Christmas Baby')
# print(s1)


s1 = songs[3056]
s2 = songs[15112]

s3 = songs[475]

m1 = song2matrix(s1, model)
m2 = song2matrix(s2, model)

m3 = song2matrix(s3, model)

# d = mat_dist_sq(m1, m2)
# d_big = mat_dist_sq(m1, m3)
# d_big1 = mat_dist_sq(m2, m3)
#
# print(d)
# print(d_big)
# print(d_big1)

d = mat_dist_abs(m1, m2)
d_big = mat_dist_abs(m1, m3)
d_big1 = mat_dist_abs(m2, m3)

print(d)
print(d_big)
print(d_big1)
