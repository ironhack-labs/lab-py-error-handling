try:
    # Request user input for a number
    number = input("Enter a number: ")
    number = float(number)  # Convert input to a float
    print(f"You entered the number: {number}")
except KeyboardInterrupt:
    print("\nInput was canceled by the user.")
except ValueError:
    print("Error: The entered value is not a number.")
