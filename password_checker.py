# ==================================================
# Password Strength Checker
# DecodeLabs Internship - Week 1 Project
#
# Developed by: Miracle Godwin Ogbo
#
# Description:
# This program evaluates the strength of a user's
# password based on six security requirements:
#
# 1. Minimum length of 12 characters
# 2. Contains uppercase letters
# 3. Contains lowercase letters
# 4. Contains numbers
# 5. Contains special characters
# 6. Checks whether the password is a commonly used
#    password to help prevent dictionary attacks.
#
# ==================================================


# ==================================================
# USER INPUT
# ==================================================

password = input("Enter your password: ")

# Calculate password length
password_length = len(password)


# ==================================================
# COMMON PASSWORD LIST
# ==================================================

common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "abc123",
    "admin",
    "welcome",
    "letmein",
    "football"
]

# Convert the password to lowercase before checking
# so that Password123, PASSWORD123 and password123
# are all treated as the same password.
is_common_password = password.lower() in common_passwords


# ==================================================
# INITIALIZE VARIABLES
# ==================================================

has_uppercase = False
has_lowercase = False
has_number = False
has_symbol = False

score = 0


# ==================================================
# PASSWORD ANALYSIS
# ==================================================

# Check each character in the password
for character in password:

    if character.isupper():
        has_uppercase = True

    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_number = True

    if not character.isalnum():
        has_symbol = True


# ==================================================
# PASSWORD SCORING
# ==================================================

if password_length >= 12:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1


# ==================================================
# DISPLAY RESULTS
# ==================================================

print("\n=========================================")
print("      PASSWORD STRENGTH CHECKER")
print("=========================================")

print(f"\nPassword Length : {password_length}")

if has_uppercase:
    print("Uppercase       : ✓")
else:
    print("Uppercase       : ✗")

if has_lowercase:
    print("Lowercase       : ✓")
else:
    print("Lowercase       : ✗")

if has_number:
    print("Number          : ✓")
else:
    print("Number          : ✗")

if has_symbol:
    print("Special Symbol  : ✓")
else:
    print("Special Symbol  : ✗")

if is_common_password:
    print("Common Password : Yes ⚠️")
else:
    print("Common Password : No ✅")

print(f"\nScore           : {score}/5")


# ==================================================
# PASSWORD STRENGTH
# ==================================================

# Any password found in the common password list is
# automatically classified as WEAK regardless of score.

if is_common_password:
    print("\nPassword Strength : 🔴 WEAK")

elif score <= 2:
    print("\nPassword Strength : 🔴 WEAK")

elif score <= 4:
    print("\nPassword Strength : 🟡 MEDIUM")

else:
    print("\nPassword Strength : 🟢 STRONG")


# ==================================================
# RECOMMENDATIONS
# ==================================================

if is_common_password or score < 5:

    print("\nRecommendations:")

    if password_length < 12:
        print("- Increase the password length to at least 12 characters.")

    if not has_uppercase:
        print("- Add at least one uppercase letter.")

    if not has_lowercase:
        print("- Add at least one lowercase letter.")

    if not has_number:
        print("- Add at least one number.")

    if not has_symbol:
        print("- Add at least one special character.")

    if is_common_password:
        print("- Avoid using common passwords.")
        print("- Choose a unique password that is difficult to guess.")
        print("- Common passwords are vulnerable to dictionary attacks.")

else:
    print("\nExcellent! Your password meets all the recommended security requirements.")
