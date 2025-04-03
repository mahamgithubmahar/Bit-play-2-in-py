def reverse_bits(n):
    reversed = 0
    while n > 0:
        bit = n & 1
        reversed = reversed << 1
        reversed = reversed | bit
        n = n >> 1
    
    return reversed

n = int(input("Enter a decimal number: "))
reversed_number = reverse_bits(n)
print("Reversed number:", reversed_number)