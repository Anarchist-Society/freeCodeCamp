ignore_words = ["a", "for", "an", "and", "by", "of"]

def build_acronym(s):
    words = s.split()
    s = ""

    for word in words:
        if word not in ignore_words:
            s += word[0].upper()

    return s
