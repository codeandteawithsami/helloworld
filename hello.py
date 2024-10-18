import os

# Get the input from the environment variable
user_input = os.getenv("USER_INPUT", "default")  # Default value if not set
user_input1 = os.getenv("USER_INPUT", "default")

if user_input == user_input1:
    print("Hello from Samiullah!")
else:
    for i in range(7):
        print("Samiullah is a good boy")
