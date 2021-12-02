import string

chars = []
alphabet = list(string.ascii_lowercase)
results = []

with open("words.txt", "r") as f:
    for word in f.readlines():
        for char in word.rstrip("\n-.").lower():
            chars.append(char)

total = len(chars)

for letter in alphabet:
    n = chars.count(letter)
    results.append((letter, round(n / total * 100, 3), n))

results.sort(key=lambda x: x[1], reverse=True)

for result in results:
    print(result)
