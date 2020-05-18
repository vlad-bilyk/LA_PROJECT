from gensim.models import Word2Vec
import time
import numpy as np


# model = Word2Vec.load('first.model')

# model.predict_output_word(['making', 'somebody', 'question'])
# happy = model['happy']
# print(happy)

# print(model.most_similar(positive=['chimp', 'smart'], negative=[], topn=10))
# print(model.similarity('dog', ))


def load_model(filename):
    return Word2Vec.load(filename)


def song2matrix(lyrics, model):
    """
    :param model: Word2Vec object
    :param lyrics: list - filtered lyrics of a song
    :return: 2d array - matrix representation of a song
    """

    mat = []
    for word in lyrics:
        try:
            wvec = model[word]
        except KeyError:

            return []
        mat.append(wvec)
    return mat


# def words2matrix(words, model):
#     """
#     :param words:
#     :param model:
#     :return:
#     """
#
#     mat = []
