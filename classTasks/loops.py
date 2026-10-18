#1.
def is_prime(number):
    if number < 2:
        return False
    for count in range(2, int(number**0.5) + 1):
        if number % count == 0:
            return False
    return True

def prime_numbers(arr):
    result = []
    for num in arr:
        if is_prime(num):
            result.append(num)
    result.sort(reverse=True) 
    return result

print(prime_numbers([5,9,3,6,2]))

# 2.
def replace_negative(arr):
    result = []
    for num in arr:
        if num < 0:
            result.append(0)
        else:
            result.append(num)
    return result

print(replace_negative([5,-9,3,-6,2,-11]))

# 3. 
def move_zeros(arr):
    result = []
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)
   
    for _ in range(zero_count):
        result.append(0)
    return result

print(move_zeros([5,0,3,0,2,0]))

# 4. 
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

print(find_duplicates([45,60,3,0,67,2,45,3,22,0]))
