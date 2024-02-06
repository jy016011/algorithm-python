import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

ones = b % 10
tens = (b % 100 - ones) // 10
hundreds = (b % 1000 - tens - ones) // 100

third = a * ones
fourth = a * tens
fifth = a * hundreds
print(third)
print(fourth)
print(fifth)
print(third + fourth * 10 + fifth * 100)