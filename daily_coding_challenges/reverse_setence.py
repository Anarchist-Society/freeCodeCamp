def reverse_sentence(sentence):
    reverse = ' '.join(s for s in sentence.split()[::-1])
    return reverse
