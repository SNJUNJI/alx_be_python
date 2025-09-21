size = int(input("Enter the size of the pattern: "))
if size <= 0:
    print("Error: Please enter a positive integer")
else:
    row = 0
    while row < size:  # Outer while loop for rows
        for col in range(size):  # Nested for loop for columns
            print("*", end="")  # Print asterisk without newline
        print()  # Newline after each row
        row += 1