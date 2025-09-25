#Q8. Count the Frequency of Words in a String using a Dictionary.
s = "python is easy and python is fun"
words = s.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("Word frequency:", freq)
