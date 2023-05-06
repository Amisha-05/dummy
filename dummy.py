s = input("Enter a string: ")

# Count frequency of each character in the input string
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Sort characters based on their frequency in descending order
sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], s.index(x[0])))

# Print each character along with its frequency in descending order of frequency
for ch, f in sorted_chars:
    print(f"{ch}: {f}")
