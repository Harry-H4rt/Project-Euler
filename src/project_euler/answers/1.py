"""
TODO - If we list all the natural numbers below 10 that are multiples of 3 or 5 we get 3,5,6 and 9. The sum of these multiples is 23.
TODO - Find the sum of all multiples of 3 or 5 below 1000
"""



def main(number) -> int:
    tot = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            tot+=i
    return tot


if __name__ == "__main__":
    print(main(number=1000))
