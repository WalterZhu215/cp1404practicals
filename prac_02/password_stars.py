"""
function main
    get password

    while len(password) < PASSWORD_LENGTH:
        display "Password must be at least {10} characters long."

    display '*' * len(password)
"""

PASSWORD_LENGTH = 10
def main():
    password = input("Enter your password: ")

    while len(password) < PASSWORD_LENGTH:
        print(f"Password must be at least {PASSWORD_LENGTH} characters long.")
        password = input("Enter your password: ")

    print('*' * len(password))

main()

# PASSWORD_LENGTH = 10
#
# password = input("Enter password: ")
# while password <= PASSWORD_LENGTH:
#     print("Invalid Password")
#     password = input("Enter password: ")
#
# length = len(password)
#
# print(length * "*")

