from gensim.models import Word2Vec


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
            print('irrelevant word for the matrix')
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
