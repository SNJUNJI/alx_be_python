task=str(input("Enter a task description."))
priority=str(input("Select a priority for the task: (high,medium,low):"))
time_bound=str(input("IS the task time bound? (yes or no)"))

match priority:
    case "high" if time_bound == "yes":
        print (f'Reminder: "{task}" is a high priority task that requires immediate attention today!')
    
    case "low" if time_bound == "no":
        print(f'Reminder: "{task}" is a low priority task. Consider completing it when you have free time.')