Task=str(input("Enter your Task: "))
Priority=str(input("Priority (high/medium/low): "))
Timebound=str(input("Is it time-bound?(yes/no): "))

match Priority:
    case "high" if Timebound == "yes":  # Fixed syntax
        print(f"Reminder: {Task} is a high priority Task that requires immediate attention today!")
    case "high" if Timebound == "no":
        print(f"Reminder: {Task} is a high priority Task, but not time-bound.")
    case "medium" if Timebound == "yes":
        print(f"Reminder: {Task} is a medium priority Task with a deadline.")
    case "medium" if Timebound == "no":
        print(f"Reminder: {Task} is a medium priority Task, no urgent deadline.")
    case "low" if Timebound == "yes":
        print(f"Reminder: {Task} is a low priority Task, but has a deadline.")
    case "low" if Timebound == "no":
        print(f"Reminder: {Task} is a low priority Task. Consider completing it when you have free time.")
    case _:
        print("Error: Unexpected priority value.")