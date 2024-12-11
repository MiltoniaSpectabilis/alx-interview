#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game
    Args:
        x (int): number of rounds
        nums (list): array of n
    Returns:
        str: name of the player that won the most rounds
        None: if winner cannot be determined
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    # Create sieve of Eratosthenes array
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # Mark non-prime numbers in sieve
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Count prime numbers up to each n in nums
    maria_wins = 0
    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if sieve[i])
        # If number of primes is odd, Maria wins
        if prime_count % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == x:
        return None
    return 'Maria' if maria_wins * 2 > x else 'Ben'
