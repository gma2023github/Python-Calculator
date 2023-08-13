# Function to perform calculator operations
def calculator_operations():
    print(name + ", you selected Calculator.\n")
    print("1. Add\n")
    print("2. Subtract\n")
    print("3. Multiply\n")
    print("4. Divide\n")
    print("5. Check if a number is odd or even\n")
    print("6. Check if a number is positive or negative\n")
    print("7. Factorize a number\n")
    print("8. Back to main menu\n")

    while True:
        # Take operator choice from the user
        operator = input(name + ", enter choice (1/2/3/4/5/6/7/8): \n")

        if operator == '8':  # If operator(choice) is 8, go back to the main menu
            break

        if operator in ['5', '6', '7']:  # If user chooses options 5, 6, or 7
            num1 = get_number_input("Enter a number: \n")
        else:
            num1 = get_number_input("Enter the first number: \n")  # If user chooses options 1, 2, 3, or 4
            num2 = get_number_input("Enter the second number: \n")

        # Perform the selected operation
        if operator == '1':
            print("Result: \n", num1 + num2)  # Addition
        elif operator == '2':
            print("Result: \n", num1 - num2)  # Subtraction
        elif operator == '3':
            print("Result: \n", num1 * num2)  # Multiplication
        elif operator == '4':
            if num2 != 0:  # If num2 is not equal to 0
                print("Result: \n", num1 / num2)  # Division
            else:
                print("Cannot divide by zero!\n")  # Division by zero error handling
        elif operator == '5':
            if num1 % 2 == 0:  # If the remainder of the operation is 0
                print("Number is even\n")  # If the number is even which means it can be divisible by two
            else:
                print("Number is odd\n")  # If the number is odd which means it can't be divisible by two
        elif operator == '6':
            if num1 > 0:  # If number is positive
                print("Number is positive\n")
            elif num1 < 0:  # If the number is negative
                print("Number is negative\n")
            else:
                print("Number is zero\n")  # If the number is zero
        elif operator == '7':  # If the operator is '7'
            factors = []  # Create an empty list to store the factors
            for i in range(1, int(num1 ** 0.5) + 1):  # Iterate over the numbers from 1 to the square root of num1 (inclusive)
                if num1 % i == 0:  # If num1 is divisible by i
                    factors.append(i)  # Add i to the factors list
                    if i != num1 // i:  # If i is not the square root of num1
                        factors.append(num1 // i)  # Add the quotient of num1 divided by i to the factors list
            factors.sort()  # Sort the factors list in ascending order
            print("\nFactors of", num1, "are:", factors)  # Print the factors
        else:
            print("Invalid choice. Please try again.\n")

# Function to get a valid number input from the user
def get_number_input(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.\n")

#Main program
def main:
 print("Welcome to the Python Calculator!\n")
 name = input("Enter your name: \n")
 print("\nHi", name + "!")

 while True:
    print("\nMain Menu:")
    print("1. Calculator with additional functions")
    print("2. Exit")
    option = input(name + ", enter your choice (1/2): \n")

    if option == '1':
        calculator_operations()
    elif option == '2':
        print("Thank you for using the Python Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
main()
    
   

