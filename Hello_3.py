# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (Manual Calculations)
# -----------------------------------------------------------------------------

def compute_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def compute_average(numbers):
    # Total divided by total count of elements
    total = compute_sum(numbers)
    return total / len(numbers)

def compute_maximum(numbers):
    # Assume the first number is the largest to start
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def compute_minimum(numbers):
    # Assume the first number is the smallest to start
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def main():
    # Prompt for how many numbers to collect
    n = int(input("How many numbers? "))
    
    # Validation: N must be a positive integer (> 0)
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    numbers_list = []
    
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        numbers_list.append(num)

    total_sum = compute_sum(numbers_list)
    avg_val = compute_average(numbers_list)
    max_val = compute_maximum(numbers_list)
    min_val = compute_minimum(numbers_list)

    print("\nResults:")
    print(f"Sum:     {total_sum if total_sum % 1 != 0 else int(total_sum)}")
    print(f"Average: {round(avg_val, 2)}")
    print(f"Maximum: {max_val if max_val % 1 != 0 else int(max_val)}")
    print(f"Minimum: {min_val if min_val % 1 != 0 else int(min_val)}")

if __name__ == "__main__":
    main()