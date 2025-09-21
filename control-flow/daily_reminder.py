Task=str(input("Enter your Task: "))
Priority=str(input("Priority (high/medium/low): "))
time_bound=str(input("Is it time-bound?(yes/no): "))

match Priority:
    case "high" :
        if time_bound == "yes":
            print(f'Reminder: "{Task}" is a high priority task that requires immediate attention today! ')
