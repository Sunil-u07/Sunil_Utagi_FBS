#Q1. Replace all Occurrences of ‘a’ with $ in a String
s = "Nature beauty is amazing"
print("After replacing 'a' with '$':",s.replace('a', '$'))

#Q2. Remove the nth Index Character from a Non-Empty String
s = "hello"
n = 2  # remove index 2 ('l')
print("After removing index:",s[:n] + s[n+1:])

#Q3. Detect if Two Strings are Anagrams
s1 = "listen"
s2 = "silent"
print("Anagrams strings:",sorted(s1) == sorted(s2))

#Q4. Swap First and Last Character of a String
s = "python"
swapped = s[-1] + s[1:-1] + s[0]
#Note:
# s[-1] last char
# s[1:-1] middle part of the str
# s[0] → first char
print("After swapping first and last:",swapped)

#Q5. Count the Number of Vowels in a String
s = "programming in python"
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Vowel count:", count)

#Q6. Replace Every Blank Space with Hyphen
s = "welcome to python"
print("After replacing spaces with '-':",s.replace(" ", "-"))

#Q7. Calculate the Length of a String Without Using len()
s = "python"
count = 0
for _ in s:
    count += 1
print("Length without using len():", count)

#Q8. Remove the Characters of Odd Index Values in a String
s = "abcdef"

# Remove char at odd indices using slicing
result = s[::2]
print("After removing odd index characters:", result)


#Q9. Calculate Number of Words and Characters in a String
s = "welcome to python programming"
words = s.split()
characters = len(s)
print("Number of words:", len(words))
print("Number of characters:", characters)

#Q10. Take Two Strings and Display the Larger String without Using Built-in Functions
def str_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

s1 = "hello"
s2 = "world!!"

if str_length(s1) > str_length(s2):
    print("The larger string is:", s1)
else: 
    print("The larger string is:", s2)


#Q11. This que reapete same as Q6


#Q12. Count Number of Lowercase Characters in a String
s = "PyThOn ProGRaM"
count = sum(1 for ch in s if ch.islower())
print("Lowercase count:", count)

#Q13. Count Number of Digits and Letters in a String
s = "Python123"
digits = letters = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print("Number of digits:", digits)
print("Number of letters:", letters)

#Q14. Count the Occurrences of Each Word in a String
s = "welcome to python python programming"
words = s.split()
count_words = {}
for w in words:
    count_words[w] = count_words.get(w, 0) + 1
print("Word occurrences:", count_words)

#Q15. Find Larger String Without Using Built-in Functions
def str_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

s1 = "python"
s2 = "java programming"

len1 = str_length(s1)
len2 = str_length(s2)

if len1 > len2:
    print("Larger string is:", s1)
else:
    print("Larger string is:", s2)

