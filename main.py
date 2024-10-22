import time

binary_number = input("Please input a binary number: ")
decimal_number = int(binary_number,2)
print(decimal_number)


def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')

decimal_to_binary(num=int(input("Please input a number: ")))