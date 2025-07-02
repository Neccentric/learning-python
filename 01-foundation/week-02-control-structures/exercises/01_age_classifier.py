# Exercise 1: Age Category Classifier
# TODO: Create a program that classifies people into age categories

# Ask user for their age
# age = int(input("Enter your age: "))

# TODO: Classify the age into categories:
# - 0-2: Toddler
# - 3-12: Child
# - 13-19: Teenager
# - 20-64: Adult
# - 65+: Senior

# TODO: Print the appropriate category
# Example: "You are a teenager."

# Bonus: Add additional information for each category
# Your code here:

print("Welcome to the Age Category Classifier!")
print("Please enter your age to find out which category you belong to.") 

age = int(input("Enter your age: "))

# Validate age input
try:
    age = int(age)
    if age < 0 or age > 150:
        print("Please enter a valid age between 0 and 150.")
except ValueError:
    print("Invalid input. Please enter a number for your age.")

# Display the age category

# print("   ╔══════════════════════════════════════╗ ")
# print("   ║          AGE CATEGORY CLASSIFIER     ║ ")
# print("   ╠══════════════════════════════════════╣ ") 
# print(  f"  ║ Your Age is: {age}                   ║ ")
# print("   ╚══════════════════════════════════════╝ ")

if age < 0:
    print("Age cannot be negative.")
elif age == 0:
    category = "Newborn"
    print("You are a newborn.  Welcome to the world!")
 
elif age > 0 and age <= 3:
    category = "Toddler"
    print("You are a toddler.")

elif age > 3 and age <= 12:
    category = "Child"
    print("You are a child.")

elif age > 12 and age <= 19:
    category = "Teenager"
    print("You are a teenager.  Enjoy your youth!")

elif age > 19 and age <= 64:
    category = "Adult"
    print("You are an adult.  Welcome to the real world!")

elif age > 64 and age >= 65:
    category = "Senior"
    print("You are a senior.  Enjoy your retirement!")

else:
    print("Invalid age input.")
#Additional information for each category


print(" ╔══════════════════════════════════════╗ ")
print(" ║          ADDITIONAL INFORMATION      ║ ")

if age > 0 and age <= 2:
    print("Toddlers are learning to walk and talk.")
    print("They are curious about the world around them.")
    print("They need a lot of care and attention.")
    print("They are starting to explore their environment.")
    print("Pleasse learn how to walk before running a program!😂")

elif age > 3 and age <= 12:
    print("Children are full of energy and curiosity.")
    print("They are learning new skills every day.")
    print("They need guidance and support from adults.")
    print("They are starting to develop their own interests.")
    print("Please learn how to read your Multiplication table before running a program!😂")

elif age > 12 and age <= 19:
    print("Teenagers are discovering their identity.")
    print("They are becoming more independent.")
    print("They are facing new challenges and responsibilities.")
    print("They are starting to think about their future.")
    print("Please learn how to Opueh before running a program!😂")

elif age > 19 and age <= 64:
    print("Adults are balancing work and personal life.")
    print("They are often responsible for family and community.")
    print("They are making important decisions about their future.")
    print("They continue to learn and grow.")
    print("Please learn how to stop overthinking before running a program!😂")

elif age > 64 and age >= 65:
    print("Seniors are enjoying their retirement.")
    print("They have a wealth of experience and knowledge.")
    print("They often have more time for hobbies and interests.")
    print("They are valued members of the community.")
    print("Please learn how to relax before running a program!😂")

else:
    print("Invalid age input.")
    print("Please learn how to input your age before running a program!😂")
print("Thank you for using the Age Category Classifier!")
print("Have a great day! 😊")

print(" ║          END OF PROGRAM              ║ ")
print(" ╚══════════════════════════════════════╝ ")
    # End of code