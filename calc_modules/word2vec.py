from gensim.models import Word2Vec
import time


def model_from_vocab(songs_lyrics, min_count, window, size, sample, alpha, negative):
    """
    Create a Word2Vec model
    :param songs_lyrics: list of lists with song lyrics
    :param min_count:
    :param window:
    :param size:
    :param sample:
    :param alpha:
    :param negative:
    :return: Word2Vec Object
    """

    model = Word2Vec(min_count=min_count, window=window, size=size, sample=sample, alpha=alpha, negative=negative, sg=1)

    start = time.time()
    model.build_vocab(songs_lyrics)
    end = round((time.time() - start) / 60, 2)
    print('model created in: {}m'.format(end))

    return model


def train_model(model, songs_lyrics, exn, epochs):
    '''
    Train a model and save it
    :param model: Word2Vec Object
    :param songs_lyrics: list of lists with songs lyrics
    :param exn: number of sentences (songs)
    :param epochs: number of iterations over songs_lyrics in training
    :return:
    '''

    start = time.time()
    model.train(songs_lyrics, total_examples=exn, epochs=epochs)
    end = round((time.time() - start) / 60, 2)
    print('model trained in: {}m'.format(end))

    model.save('first.model')


if __name__ == "__main__":
    from data_modules.newdata_funcs import *
    songs = get_all_songs()
    n = len([i for i in songs if len(i) > 0])
    print(len(songs))
    print(n)
    model = model_from_vocab(songs, 6, 2, 200, 6e-5, 0.04, 10)
    train_model(model, songs, n, 30)
    # model = Word2Vec(min_count=8, window=2, size=250, sample=6e-5, alpha=0.04, negative=10, sg=1)
