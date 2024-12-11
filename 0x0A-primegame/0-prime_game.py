#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
    """
    Determines the winner of a prime game.
    """

    def is_prime(num):
        """Checks if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """Generates a list of prime numbers up to n."""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def solve_round(n):
        """Solves a single round of the game."""
        if n == 1:
            return False  # Ben wins if n is 1

        primes = get_primes(n)

        return len(primes) % 2 != 0  # Maria wins if the number of primes is odd

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if solve_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
