# a,
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    elif 50 <= percentage < 60:
        return 'E'
    else:
        return 'Fail'

def main(): # function for error handling and accepting user input
    
    try:
        percentage = float(input("Enter the percentage grade: "))
        if 0 <= percentage <= 100:
            grade = calculate_grade(percentage)
            print("The corresponding grade is:", grade)
        else:
            print("Percentage grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

# ii,
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Main function to convert temperatures
def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")

    elif choice == '2':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Temperature in Celsius: {celsius:.2f} °C")

   # else:
        #print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()

#b(i),
def calculate_triangle_area(base, height):
    # Calculate the area of the triangle
    area = 1/2 * base * height
    return area

def main():
    print("Triangle Area Calculator")
    
    # Prompt the user to enter the base and height of the triangle
    base = float(input("2"))
    height = float(input("3"))
    
    # Call the function to calculate the area
    area = calculate_triangle_area(base, height)
    
    # Print the calculated area
    print(f"The area of the triangle with base {2} and height {3} is: {area}")

if __name__ == "__main__":
    main()

#b ii,
def sum_list_numbers(num_list):
    total_sum = 0  # Initialize a variable to hold the sum
    
    # Iterate over each number in the list
    for num in num_list:
        total_sum += num  # Add the current number to the total sum
    
    return total_sum

# Example usage:
numbers = [9, 2, 3, 5, 8]
result = sum_list_numbers(numbers)
print("Sum of numbers in the list:", result)
