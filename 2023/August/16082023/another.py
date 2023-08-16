from datetime import datetime

toady_day_name = datetime.now().strftime("%A")

# User-provided time in the format "HH:MM AM/PM"
user_input_time = input("Enter a time (HH:MM AM/PM): ")

# Convert user input time to a datetime object
user_time = datetime.strptime(user_input_time, "%I:%M %p").time()

# Get the current time
current_time = datetime.now().time()
# Compare user's time with current time
if user_time <= current_time:
    print("User's time has already passed.")
else:
    print("User's time has not passed yet.")
