def plusMinus():
    # Take input from user
    try:
        n = int(input("Enter the length of the array: "))
        if n <= 0:
            raise ValueError("The length of the array must be a positive integer.")

        arr = list(map(int, input(f"Enter {n} elements of the array separated by spaces: ").split()))
        if len(arr) != n:
            raise ValueError(f"Exactly {n} elements are required.")

        # Counters for positive, negative, and zero elements
        positive_count = sum(1 for x in arr if x > 0)
        negative_count = sum(1 for x in arr if x < 0)
        zero_count = sum(1 for x in arr if x == 0)

        # Calculate ratios
        positive_ratio = positive_count / n
        negative_ratio = negative_count / n
        zero_ratio = zero_count / n

        # Print ratios to 6 decimal places
        print(f"{positive_ratio:.6f}")
        print(f"{negative_ratio:.6f}")
        print(f"{zero_ratio:.6f}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero. The array must contain at least one element.")

# Execute the function
plusMinus()
