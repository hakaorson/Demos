import re
import reprlib
from collections import abc
RE_WORD = re.compile(r'\w+')


class Sentence():
    def __init__(self):
        self.words = [1, 2, 3, 4, 5]

    def __iter__(self):
        return Sentence_itor()


class Sentence_itor(Sentence):
    def __init__(self):
        super().__init__()
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


for temp in Sentence():
    pass

print(issubclass(Sentence, abc.Iterable))
