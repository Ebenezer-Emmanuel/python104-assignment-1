def is_prime(number):
    """
    Checks if a number is prime.
    Returns True if prime, False otherwise.
    """
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check for factors up to the square root of the number
    # We use int(number ** 0.5) + 1 because if a factor exists, 
    # at least one factor must be less than or equal to the square root.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, so it's not prime

    return True


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is NOT a prime number.")
    except ValueError:
        print("Please enter a valid integer.")