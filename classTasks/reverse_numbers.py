
#  Display "Enter a word: "
#  Input word
#
#  Set reversed_word = ""
#
#  For count = LENGTH(word) - 1 Downto 0
#      reversed_word = reversed_word + word[count]
#  
#
#  Display "Reverse: " + reversed_word
#

word = input("Enter a word: ")

reversed_word = ""
for count in range(len(word) - 1, -1, -1):
    reversed_word += word[count]

print(f"Reverse: {reversed_word}")
