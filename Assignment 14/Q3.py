#Q3. find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
unique_words = set(words)
print("Unique words:", unique_words)

freq = {w: words.count(w) for w in unique_words}
print("Frequency:", freq)
