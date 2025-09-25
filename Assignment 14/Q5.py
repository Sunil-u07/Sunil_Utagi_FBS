#Q5. Find the longest common prefix of all strings. Use the Python set.
strs = ["flower","flow","flight"]
prefix = ""
for i in range(min(map(len, strs))):
    chars = {s[i] for s in strs}
    if len(chars) == 1:
        prefix += chars.pop()
    else:
        break
print("Longest common prefix:", prefix)
