
# def countOccurrences(arr, n, x):
#     res = 0
#     for i in range(n):
#      if x == arr[i]:
#          res += 1
    
#     return res

# arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
# n = len(arr)
# x = 2
# print (countOccurrences(arr, n, x))

# credit_card=input("Enter your credit card number")
# if len(credit_card) >= 4:
#    last_four_digit = credit_card[-4:]
#    print("Your credit card number is ", last_four_digit)
# else:
#  print("Your credit card number is not valid")

# def decimal_binary(num):
#    if num >= 1:
#         decimal_binary(num//2)
#         print(num %2 , end='')

#         if __name__ == '__main__':
#             dec_val= 28
#             decimal_binary(dec_val)
    
# Write a Python program that takes a string as input and counts the number of occurrences of each character in the string. The program should then print the characters and their corresponding counts in descending order of frequency.
# Input
# * A single string s (1 <= len(s) <= 1000) containing alphanumeric characters and/or symbols.
# Output
# * Print each character in the string s along with its frequency, in descending order of frequency. In case of a tie in frequency, print the characters in the order they appear in the input string.
# Example
# Input: hello_world
# Output: 
# l: 3
# o: 2
# h: 1
# e: 1
# _: 1
# w: 1
# r: 1
# d: 1

from collections import Counter


s = input("Enter a string:")

freq= {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch]= 1

        sorted_chars= sorted(freq.items(), key=lambda x: (-x[1], s.index(x[0])))
        for ch, f in sorted_chars:
            print(f"{ch}: {f}")
