#write function that takes a strings and return a run_lenght encoded string.
#input:aaabbcc
#output:a3b2c2

def length_encode(alphabet):

    if len(alphabet) == 0:
        return ""

    result = ""
    count = 1

    for index in range(1, len(alphabet)):
        if alphabet[index] == alphabet[index-1]:
            count += 1
        else:
            if count == 1:
                result += alphabet[index-1]
            else:
                result += alphabet[index-1] + str(count)
            count = 1

    if count == 1:
        result += alphabet[-1]
    else:
        result += alphabet[-1] + str(count)

    return result

print(length_encode("aaa bb cc"))      
print(length_encode("aaa  bb ac"))    
print(length_encode("aaab     acck")) 
