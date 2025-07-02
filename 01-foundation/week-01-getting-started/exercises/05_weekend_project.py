# Exercise 5: Personal Information Collector (Weekend Project)
# TODO: Create a comprehensive personal information collector

# This program should:
# 1. Ask for user's personal information
# 2. Validate and format the data
# 3. Display a formatted summary
# 4. Calculate some interesting statistics

print("=== Personal Information Collector ===")
print("Please provide the following information:\n")

# TODO: Collect the following information from user input:
# - Full name
# - Age
# - City
# - Favorite color
# - Favorite number
# - Email address
# - Phone number (optional)

# TODO: Validate the data:
# - Check if age is a valid number
# - Check if email contains @ symbol
# - Handle any input errors gracefully

# TODO: Calculate and display:
# - Birth year (current year - age)
# - Days lived (approximate: age * 365)
# - Name initials
# - Email username (part before @)

# TODO: Create a formatted summary display
# Example output:
# ╔══════════════════════════════════════╗
# ║           PERSONAL PROFILE           ║
# ╠══════════════════════════════════════╣
# ║ Name: John Doe (J.D.)               ║
# ║ Age: 25 years (born ~1998)          ║
# ║ Location: New York                   ║
# ║ Contact: john@email.com              ║
# ║ Favorites: Blue, Number 7            ║
# ║ Days Lived: ~9,125 days              ║
# ╚══════════════════════════════════════╝

# Your implementation here:

from datetime import datetime

# Collect information with error handling
try:
    # Basic information
    full_name = input("Enter your full name: ").strip()
    if not full_name:
        raise ValueError("Full name cannot be empty.")
    # Validate full name
    if not all(part.isalpha() or part.isspace() for part in full_name):
        raise ValueError("Full name can only contain letters and spaces.")
    full_name = " ".join(part.capitalize() for part in full_name.split())
    if len(full_name) < 3:
        raise ValueError("Full name must be at least 3 characters long.")
    if len(full_name) > 50:
        raise ValueError("Full name must not exceed 50 characters.")
    print(f"Hello, {full_name}!")
    print("Let's gather some more information about you.\n")
    
    # Age with validation
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                print("Please enter a valid age between 0 and 150.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for age.")
    
    city = input("Enter your city: ").strip()
    if not city:
        raise ValueError("City cannot be empty.")

    favorite_color = input("Enter your favorite color: ").strip()
    if not favorite_color:
        raise ValueError("Favorite color cannot be empty.")
    # Validate favorite color
    if not all(char.isalpha() or char.isspace() for char in favorite_color):
        raise ValueError("Favorite color can only contain letters and spaces.")
    
    # Favorite number with validation
    while True:
        try:
            favorite_number = int(input("Enter your favorite number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Email with basic validation
    while True:
        email = input("Enter your email address: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Please enter a valid email address (must contain @ and .)")
    
    # Optional phone number
    phone = input("Enter your phone number (optional): ").strip()
    if not phone:
        phone = "Not provided"

    # Calculate statistics
    current_year = datetime.now().year
    birth_year = current_year - age
    days_lived = age * 365  # Approximate
    
    # Extract initials
    name_parts = full_name.split()
    initials = "".join([part[0].upper() for part in name_parts if part])
    
    # Extract email username
    email_username = email.split("@")[0]
    
    # Create formatted display
    print("\n" + "="*50)
    print("╔══════════════════════════════════════════════════╗")
    print("║                PERSONAL PROFILE                  ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║ Name: {full_name:<25} ({initials:<4})           ║")
    print(f"║ Age: {age} years (born ~{birth_year})           ║")
    print(f"║ Location: {city:<35}                            ║")
    print(f"║ Contact: {email:<32}                            ║")
    if phone != "Not provided":
        print(f"║ Phone: {phone:<37}                          ║")
    print(f"║ Favorites: {favorite_color}, Number {favorite_number:<20}      ║")
    print(f"║ Days Lived: ~{days_lived:,} days{' '*(25-len(str(days_lived)))}║")
    print(f"║ Email Username: {email_username:<27}      ║")
    print("╚══════════════════════════════════════════════════╝")
    
    # Additional fun facts
    print(f"\n🎉 Fun Facts about {name_parts[0]}:")
    print(f"   • You've been alive for approximately {days_lived * 24:,} hours!")
    print(f"   • Your name has {len(full_name.replace(' ', ''))} characters (without spaces)")
    print(f"   • Your name has {len(name_parts)} parts (e.g., first, middle, last)")
    print(f"   .Your name has {len(full_name)} characters (including spaces)")
    print(f"   • You were born in the {birth_year}s")
    print(f"   • Your initials spell: {initials}")
    
    # Name analysis
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in full_name if char in vowels)
    consonant_count = sum(1 for char in full_name if char.isalpha() and char not in vowels)
    
    print(f"   • Your name contains {vowel_count} vowels and {consonant_count} consonants")
    
    if len(full_name) > 15:
        print(f"   • You have a long name! ({len(full_name)} characters)")
    
    # Lucky number calculation
    lucky_number = (age + favorite_number) % 10
    print(f"   • Your lucky number today is: {lucky_number}")
    
    print(f"\nThank you for using the Personal Information Collector!")
    print("Your information has been processed successfully! 🎊")

except KeyboardInterrupt:
    print("\n\nProgram interrupted by user. Goodbye!")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    print("Please try running the program again.")
