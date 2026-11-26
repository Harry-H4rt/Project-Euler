from typing import Any

"""
TODO - The prime factors of 13195 are 5,7,13 and 29.
TODO - What is the largest prime factor of 600851475143
"""

"""

What even is a prime factor?
 -  any factor of a number that is itself a prime number
 
 so for example to find 28s prime factor youd
 
        28
      /    \
     7      4
     
7 x 4 is 28 and 7 is a prime number 
also the 2x2 which are also primes
https://www.youtube.com/shorts/WP0d2d02gL4
   
Reminder - a prime is a number thats greater than one and cant be divided evenly by any other whole number witout leaving 
a remainder. Only has 2 factors, one and itself

the smallest number in a factor pair will never be > n**0.5 so list the numbers out from n**0.5


"""


def prime_checker(number: int) -> bool:

    sqrt = int(number**0.5)
    tot = 0
    for factor in range(sqrt):
        factor+=1
        remainder = number % factor
        if remainder == 0:
            tot += 1
    if tot <= 1:
        return True
    else:
        return False

def factor_finder(number: int) -> tuple[list[Any], list[Any]]:
    sqrt = int(number**0.5)
    factor_list = []
    partner_list = []
    for factor in range(sqrt):
        factor+=1
        fits = number % factor
        if fits == 0 and factor > 1:
            partner = number // factor
            factor_list.append(factor)
            partner_list.append(partner)

    return factor_list, partner_list


def main(number: int) -> int:

    factors, partners = factor_finder(number)

    prime_factors = []
    biggest_num = 0
    for i in factors:
        if prime_checker(i):
            prime_factors.append(i)
            biggest_num = max(prime_factors)

    for i in partners:
        if prime_checker(i):
            prime_factors.append(i)
            biggest_num = max(prime_factors)

    if biggest_num == 0:
        return number
    else:
        return biggest_num

if __name__ == "__main__":
    print(main(number = 600851475143))