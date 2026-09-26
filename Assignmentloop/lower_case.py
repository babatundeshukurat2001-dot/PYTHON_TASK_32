text = "Hello World 123"
result = ""
for ch in text:
    if 'a' <= ch <= 'z':
        
        result += chr(ord(ch) - 32)
    else:
        result += ch
print(result, "\n")

