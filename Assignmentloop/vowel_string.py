text = "Loops make repetitive tasks easy"
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in text:
    if ch in vowels:
        vowel_count += 1
print(vowel_count, "\n")

