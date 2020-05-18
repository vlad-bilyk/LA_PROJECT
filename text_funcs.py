from nltk.corpus import stopwords
from nltk.corpus import words
eng_words = set(words.words())
stop_words = set(stopwords.words('english'))
stop_words.add("im")

to_remove = ["?", "!", ".", ",", ":", ";", "'", "\"", "&", "$", "%", "*", "-"]
brackets = ["(", "[", "{"]


def filter_lyrics(text):
    lyrics = text.lower().strip()
    for r in to_remove:
        if r in lyrics:
            lyrics = lyrics.replace(r, "")

    lyrics = lyrics.split()

    result = []
    non_eng = 0

    for word in lyrics:
        c = 0

        if word in stop_words:
            continue

        for b in brackets:
            if b in word:
                c += 1

        if c == 0:
            result.append(word)
            if word not in eng_words:
                non_eng += 1

    eng_part = 1 - (non_eng / len(result))
    if eng_part < 0.6:
        raise ValueError

    # lyrics = [i for i in lyrics for b in brackets if i not in stop_words and b not in i]

    return result

