from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now()
    return current_date
def  calculate_future_date(num_of_days):
    current_date=display_current_datetime()
    future_date=current_date+timedelta(days=num_of_days)
    formated=future_date.strftime("%Y-%m-%d-%H-%M-%S")
    return formated

date=display_current_datetime()
num_of_days=int(input("Enter the number of days to add to the current date: "))
future_date=calculate_future_date(num_of_days)
print(future_date)