print("#########################################")
print("Calculate your pet's age in human years!")
print("#########################################")
print("Choose your pet type:")
print("1.DOG ")
print("2.CAT ")
print("3.EXIT ")
n=int(input("Enter your choice:" ))

if n==1:
    age = int(input("Please enter your dog's age in years:"))
    if age<0:
        print("Age cannot be negative. Please enter a valid age.")
    else:
        human_age = age * 7
        print(f"Your dog's age in human years is: {human_age}")
elif n==2:
    age = int(input("Please enter your cat's age in years:"))
    if age<0:
        print("Age cannot be negative. Please enter a valid age.")
    else:
        human_age = (age - 2)*4 + 24 if age > 2 else age * 12
        print(f"Your cat's age in human years is: {human_age}")
elif n==3:
    print("Exiting the program. Goodbye!")
    
else:
    print("Invalid choice. Please select a valid option.")