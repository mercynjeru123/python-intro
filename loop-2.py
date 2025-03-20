for number in range(100,0,-1):
    print(number)

#PRIME NUMBERS
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sort_primes_in_range(start, end):
    """Filter primes from a range and sort them."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return sorted(primes)

# Example usage
start = 10
end = 50
primes = sort_primes_in_range(start, end)
print(primes)




#MULTIPLICATION
print()