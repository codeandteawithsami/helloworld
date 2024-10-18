try:
    user_input = input("Enter Your value!")
except EOFError:
    user_input = "default"  # Use a default value if no input is provided

if user_input == "sami":
    print("Hello from Samiullah!")
else:
    for i in range(7):
        print("Samiullah is a good boy")
