#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    :param x: Number of rounds
    :param nums: Array of integers representing the maximum number for each round
    :return: Name of the player that won the most rounds, or None if it's a tie
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_primes(n):
        """Get all prime numbers up to n."""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(n):
        """Determine if the first player can win given n."""
        primes = get_primes(n)
        if not primes:
            return False
        return len(primes) % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
