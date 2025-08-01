common_password = {"123456", "money", "key", "happy", "password", }
special_characters = "@!#$%^&*"
uppercase = False
lowercase = False
digits = False
special_char = False
longpassword = False
uncommon = False
points = 0
correction = []

password = input("Enter your password: ")
for char in password: 
    if len(password) >= 8:
        longpassword = True
    if char.isupper() :
        uppercase = True
    elif char.islower() :
        lowercase = True
    elif char.isdigit() :
        digits = True
    elif char in special_characters:
        special_char = True

if password not in common_password:
    uncommon = True

criteria = [digits, lowercase, uppercase, longpassword, special_char, uncommon]
words = ["digits", "lowercase", "uppercase", "atleast 8 characters", "special characters", "to be uncommon"]

for  criterion, word in zip(criteria, words):
    if criterion == True:
        points += 20
    else:
        message = f"your password should have {word}"
        correction.append(message)
    
if points > 100:
    print(f"score: {points}/120 (excellent)")
elif points > 80:
    print(f"score: {points}/120 (strong) \nKey improvements are:")
    print(correction)
elif points > 60:
    print(f"score: {points}/120 (good) \nKey improvements are:")
    print(correction)
elif points > 40:
    print(f"score: {points}/120 (fair) \nKey improvements are:")
    print(correction)
else:
    print(f"score: {points}/120 (weak) \nKey improvements are:")
    print(f"{correction}")

