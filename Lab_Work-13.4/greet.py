def greet(name):
    print(f"Hello, {name}! Welcome to the program.")


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print("This script is being run directly.")
    greet(user_name)
else:
    print("This script is being imported as a module.")