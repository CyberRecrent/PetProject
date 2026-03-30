print("HEllo, Tis is my pet-project")

Name = input("Your name: ")
Second_name = input("Your second name: ")
Age = int(input("Your age: "))
Mail = input("Email")
Subscribe = input("Your plan")

if Subscribe == "Pro":
    print(f"Dear {Name} {Second_name} you have Pro subscribe, you can go boxing, gym")
elif Subscribe == "Standart":
    print(f"Dear {Name} {Second_name} you can go gym. If you want boxing please upgrade your Subscribe")
else:
    print("Please buy subscribtion. For more information you can address to our support")

print("Thanks for using app")

print("This is my pull. And first commit from job")

print("Imagine that i added database like postgre")