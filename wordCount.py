"""Word Count Program"""
# pylint: disable=invalid-name

import sys
import time

start = time.time()
filename = sys.argv[1]
word_count = {}

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        words = line.split()

        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

end = time.time()
elapsed = end - start

for word in word_count:
    print(word, ":", word_count[word])
print("Time:", elapsed)

with open("WordCountResults.txt", "w", encoding="utf-8") as out:
    for word in word_count:
        out.write(f"{word}: {word_count[word]}\n")
    out.write(f"Time: {elapsed}\n")
