Your_name = input("Enter Your Name:").strip().capitalize()
Your_age = int(input("Enter Your Age:"))
City = input("Enter Your City:").strip()
Food = input("Your Favorite Food:").strip()
Color = input("Your Favorite Color:").strip()
Animal = input("Your Spirit Animal:").strip()
Doing = input("One Thing You LOVE Doing:").strip()

import time
time.sleep(2)
print("Generate My Personality")

print("🧠 Known Your Personality")
print("✨ Let's discover who you really are with some fun data magic!")
print("*"*100)

import time
time.sleep(3)
print("🔍 Scanning colors, foods, and animal energies...")
time.sleep(3)
print("💫 Calculating your personality type using complex non-scientific logic...")
time.sleep(3)
print(f"🎉 Hey {Your_name}, here's your fun personality report!")

time.sleep(3)

print(f"🌆 You're from {City}, a place of dreams!")
time.sleep(1)
print(f"🍿 You love {Food} and enjoy doing {Doing}.")
time.sleep(1)
print(f"🎨 You vibe with the color {Color} and your spirit animal is the {Animal}.")
time.sleep(1)
month = Your_age*12
print(f"📅 You've lived approximately {month} months already.")
time.sleep(1)
if Your_age<18:
    print(f"🧩 You belong to the 'Young Explorer' tribe.")
elif 18<=Your_age<=30:
    print(f" You belong to the 'Adventurer' tribe.")
elif Your_age>30:
    print(f"🧩 You belong to the 'Wise Owl' tribe.")

time.sleep(1)

print("🔐 Your Secret Personality Code is: 💡", Your_name[:2]+str(Your_age)[-1]+Animal[0].upper()+Color[0].upper() )

print("✨ You seem deeply passionate — that hobby says a lot about your vibe!")
print("🌈 You are officially certified as: FUNKY AND FABULOUS! 😎")