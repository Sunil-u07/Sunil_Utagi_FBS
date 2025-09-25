#Q8. Find all anagrams and group them
words = ["bat","tab","cat","act","tac"]
groups = {}

for w in words:
    key = "".join(sorted(w))
    groups.setdefault(key, []).append(w)

print(list(groups.values()))
