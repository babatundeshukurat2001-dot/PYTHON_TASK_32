
#  Input number
#
#  IF number <= 1 
#    Set is_prime = False
#  Else
#    Set is_prime = True
#    For count from 2 To square_root(number) do
#      IF number Modulo count == 0 
#        Set is_prime = False
#        Break
#    
#  Print is_prime
#

number = int(input("Enter a number: "))

if number <= 1:
    print(False)
else:
    prime = True
    for count in range(2, number):  
        if number % count == 0:
            prime = False
            break
    
    print(prime)
