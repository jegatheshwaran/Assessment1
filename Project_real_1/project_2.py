print("1. Your Profile")
Name = input("Enter your Name:").strip().title()
Age = int(input("Enter your age:"))
Gender = input("Enter your gender:").strip().title()
City = input("Enter your city:").strip().title()

print("2. Health Inputs")
print("Main symptom: Choose from fever, cough, fatigue, headache, chest pain, breathlessness")
Main_Symptom = input("Enter Symptom:").strip().lower()

Body_Temp = float(input("Body temperature in Fahrenheit:"))
Number_of_sick_days = int(input("Number of sick days:"))
Smoking_habit = input("Do you smoke? (yes/no):").strip().title()
Sleep_hours = int(input("Sleep hours:"))
Mood = input("Mood (choose from: Calm, Anxious, Sad, Irritable):").strip().title()
Pre_existing_conditions = input("Pre-existing conditions? (yes/no):").strip().title()

print("3. Risk Scoring Logic")
rating = 0

# Health risk scoring
if Body_Temp >= 102 or Number_of_sick_days > 3:
    rating += 3
if Age >= 60 and Body_Temp >= 102:
    rating += 2
if Main_Symptom == "cough" and Number_of_sick_days > 5:
    rating += 2
if Age > 30:
    rating += 2
if Main_Symptom == "headache" and Body_Temp >= 100:
    rating += 2
if Main_Symptom == "chest pain":
    rating += 3
if Main_Symptom == "breathlessness":
    rating += 4
if Smoking_habit == "Yes":
    rating += 2
if Sleep_hours < 6:
    rating += 1
if Mood in ["Anxious", "Sad", "Irritable"]:
    rating += 1
if Pre_existing_conditions == "Yes":
    rating += 2

print("4. Health Risk Result")
if rating <= 3:
    print("Low Risk")
elif 4 <= rating <= 6:
    print("Moderate Risk")
elif rating >= 7:
    print("High Risk")

print("5. Personalized Advice")
if Gender == "Female" and Age >= 45:
    print("Recommendation: Consider regular health screenings.")
if Gender == "Male" and Smoking_habit == "Yes":
    print("Suggestion: Quitting smoking would improve health.")
if Sleep_hours < 6:
    print("Advice: Get more rest for better recovery.")
if Mood == "Anxious":
    print("Tip: Try relaxation techniques like deep breathing.")
if Pre_existing_conditions == "Yes":
    print("Warning: Seek medical attention.")

print(f"Consider visiting urgent care near {City} if needed.")

print("6. Mental Health Tip")
if Mood == "Calm":
    print("Encouragement: Stay positive and maintain good habits.")
if Mood == "Sad":
    print("Support: Talking to someone might help.")
if Mood == "Anxious":
    print("Technique: Practice box breathing for relaxation.")
if Mood == "Irritable":
    print("Advice: Take a break and unwind.")