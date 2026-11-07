print("Day planner")
print("Aswer the questions and have a plan created!")

day      =  input("What's the day? (Monday 2 Sunday):").strip().capitalize()
weather  = input("What's the weather lookin' like? (sunny / rainy / cloudy):").strip().lower()
homework = input("Any pending homework? (yes/no):").strip().lower() 

print()
print("Your plan for the day is as follows:")


if day in ("Saturday", "Sunday"):
    print("It's the weekend! Time to relax and enjoy your day off!")
elif day == "Monday":
    print("It's Monday! Start your week off strong and stay productive!")
elif day == "Friday":
    print("It's Friday! Finish your tasks and get ready for the weekend!")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("It's a weekday! Stay focused and keep pushing through your tasks!")
else:
    print("Invalid day entered. Please enter a valid day of the week.")


if weather == "sunny" and homework == "yes":
    print("After doing the homework: head outside.")

if not (homework == "yes"):
    print("Since you have homework, do it first")
if weather == "rainy" or weather == "cloudy":
    print("Since the weather is not ideal, stay indoors and focus on your tasks.")



if weather == "rainy" and not (homework == "yes"):
    print("Since the weather is rainy, stay indoors and focus on your tasks.")
elif weather == "sunny" and homework =="yes" and not (day in ("Saturday", "Sunday")):
    print("Since the weather is sunny, you can go outside.")
else:
    print("idk what else to say bruv")