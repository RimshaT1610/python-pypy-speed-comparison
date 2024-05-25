# primes.py

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    import sys
    import time

    if len(sys.argv) != 2:
        print("Usage: python primes.py <number_of_primes>")
        sys.exit(1)

    n = int(sys.argv[1])
    start_time = time.time()
    primes = generate_primes(n)
    end_time = time.time()

    print(f"Generated {n} prime numbers.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    # Optional: Uncomment the next line to print the prime numbers
    # print(primes)
