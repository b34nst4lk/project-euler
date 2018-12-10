# Question 1 - Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_or_5(start, end):
    for _ in range(start, end):
        if _ % 3 == 0 or _ % 5 == 0:
            yield _

def main():
    rv = 0
    for _ in multiples_of_3_or_5(0, 1000):
        rv += _
    return rv

if __name__ == "__main__":
    print(main())