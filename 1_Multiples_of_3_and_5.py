"""
Project Euler problem #1

If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

answer: 233168

technique:
add together the summation of 3x and 5x and then 
subtract the summation of 15x (to remove redundant additions)
the summation of each goes from 1 to n where
n is the original_number divided by 3, 5 or 15

in the case the original_number is 1000:
summation from 1 to 333: 3x
add the summation from 1 to 199: 5x
subtract the summation from 1 to 66: 15x
"""

answer = 0
sum = 0
try:
    original_number = int(input("Enter an integer "))
except ValueError:
    print("That is not a valid integer")
else:
    # the answer is the summation 1:333 E 3x + 1:200 E 5x - 1:(1000/15) E 15x
    # summation for 3
    summation_total = 0
    summation_end = int(original_number / 3)
    if original_number % 3.0 == 0:
        summation_end = summation_end - 1
    for x in range(1, summation_end + 1):
        summation_total = summation_total + (3 * x)

    answer = answer + summation_total

    # summation for 5
    summation_total = 0
    summation_end = int(original_number / 5)
    if original_number % 5.0 == 0:
        summation_end = summation_end - 1

    for x in range(1, summation_end + 1):
        summation_total = summation_total + (5 * x)

    answer = answer + summation_total

    # summation for 15
    summation_total = 0
    summation_end = int(original_number / 15)
    if original_number % 15 == 0:
        summation_end = summation_end - 1
    for x in range(1, summation_end + 1):
        summation_total = summation_total + (15 * x)

    answer = answer - summation_total

print(answer)
