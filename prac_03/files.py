# 1. Ask the user for their name and write it to name.txt
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# 2. Read the name from name.txt and print "Hi [Name]!"
with open("name.txt", "r") as file:
    saved_name = file.read().strip()  # Remove any trailing newline
print(f"Hi {saved_name}!")

# 3. Read the first two numbers from numbers.txt, add them, and print the sum
with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())  # Read first line
    second_number = int(file.readline().strip())  # Read second line
sum_two_numbers = first_number + second_number
print(sum_two_numbers)  # Expected output: 59

# 4. Read all numbers from numbers.txt, sum them, and print the total
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())  # Convert each line to int and add to total
print(total)  # Should print the sum of all numbers in the file
