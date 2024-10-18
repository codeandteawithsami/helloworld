import os

# Get the input from the environment variable
user_input = os.getenv("USER_INPUT", "default")  # Default value if not set

if user_input == "sami":
    print("Hello from Samiullah!")
else:
    for i in range(7):
        print("Samiullah is a good boy")
