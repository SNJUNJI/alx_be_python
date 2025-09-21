Task=str(input("Enter your task: "))
Priority=str(input("Priority (high/medium/low): "))
Timebound=str(input("Is it time-bound?(yes/no): "))

match priority:
    case high if time_bound == "yes":
        print (f'Reminder: "{Task}" is a high priority task that requires immediate attention today!')
    
    case low if time_bound == "no":
        print(f'Reminder: "{Task}" is a low priority task. Consider completing it when you have free time.')