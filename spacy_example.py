from __future__ import unicode_literals
import spacy
import numpy as np
from numpy import dot
from numpy.linalg import norm
import math

nlp = spacy.load("en_core_web_lg")
doc = nlp(open("alice.txt").read())

tokens = list(set([w.text.lower() for w in doc if w.is_alpha]))

def vec(s):
    return nlp.vocab[s].vector

def distance(coord1, coord2):
    # note, this is VERY SLOW, don't use for actual code
    return math.sqrt(sum([(i - j)**2 for i, j in zip(coord1, coord2)]))

def subtractv(coord1, coord2):
    return [c1 - c2 for c1, c2 in zip(coord1, coord2)]

def addv(coord1, coord2):
    return [c1 + c2 for c1, c2 in zip(coord1, coord2)]

def meanv(coords):
    # assumes every item in coords has same length as item 0
    sumv = [0] * len(coords[0])
    for item in coords:
        for i in range(len(item)):
            sumv[i] += item[i]
    mean = [0] * len(sumv)
    for i in range(len(sumv)):
        mean[i] = float(sumv[i]) / len(coords)
    return mean

def closest(space, coord, n=10):
    closest = []
    for key in sorted(space.keys(),
                        key=lambda x: distance(coord, space[x]))[:n]:
        closest.append(key)
    return closest

def cosine(v1, v2):
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

def spacy_closest(token_list, vec_to_check, n=10):
    return sorted(token_list,
                  key = lambda x: cosine(vec_to_check, vec(x)),
                  reverse=True)[:n]

def closest_cosine(token_list, vec_to_check, n=10):
    return [(w, cosine(vec_to_check, vec(w))) for w in spacy_closest(token_list, vec_to_check)]

print(spacy_closest(tokens, subtractv(vec("Alice"), vec("cat"))))
