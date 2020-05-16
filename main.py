# Python program to generate word vectors using Word2Vec

# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

import gensim
from gensim.models import Word2Vec

# Reads ‘alice.txt’ file
sample = open("alice.txt", "r")
s = sample.read()
# print(s)

# Replaces escape character with space
f = s.replace("\n", " ")
# print(f)

data = []
# print(sent_tokenize(f))

# iterate through each sentence in the file
for i in sent_tokenize(f):
    temp = []

    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())

    # print(temp)

    data.append(temp)
# print(data)
# Create CBOW model

for sg, method in zip([0, 1], ['CBOW', 'Skip Gram']):
    model1 = gensim.models.Word2Vec(data, min_count=1,
                                    size=100, window=5, sg=sg)
    # # Print results
    # for word in ['wonderland', 'machine']:
    #     print("Cosine similarity between 'alice' " +
    #           "and '{}' - {} : ".format(word, method),
    #           model1.similarity('alice', word))

    print(model1.similar_by_word('alice'))


# # Create Skip Gram model
# model2 = gensim.models.Word2Vec(data, min_count=1, size=100,
#                                 window=5, sg=1)
#
# # Print results
# print("Cosine similarity between 'alice' " +
#       "and 'wonderland' - Skip Gram : ",
#       model2.similarity('alice', 'wonderland'))
#
# print("Cosine similarity between 'alice' " +
#       "and 'machines' - Skip Gram : ",
#       model2.similarity('alice', 'machines'))
