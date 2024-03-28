# single thread frequency checker
import time
import unicodedata


def process_text(txt):
    frequency = {}
    for char in txt:
        if char.isalpha() and 'LATIN' in unicodedata.name(char):
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency


def single_thread():
    with open('TheStory.txt', "r", encoding="utf-8") as f:
        txt = f.read()
        start = time.perf_counter()
        freq = process_text(txt)
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print('freq: ', freq)
        end = time.perf_counter()
        total = end - start
        print('total: ', total)


single_thread()
