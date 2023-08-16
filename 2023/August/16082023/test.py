from datetime import datetime, timedelta

# User input day and time
user_input = input("Enter the schedule (e.g., Every Wednesday at 06:00 AM): ").lstrip(
    "Every "
)

# Parse user input for day and time
user_input_day, user_input_time = user_input.split(" at ")
user_time = datetime.strptime(user_input_time, "%I:%M %p").time()

# Get current date and time
current_date_time = datetime.now()

# Calculate the number of days until the desired day
days_until_day = (
    [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ].index(user_input_day.lower())
    - current_date_time.weekday()
) % 7

# Calculate the date of the desired day
desired_date = current_date_time.date() + timedelta(
    days=days_until_day + (days_until_day <= 0) * 7
)

# Combine the desired date with user input time
desired_date_time = datetime.combine(desired_date, user_time)

# Compare with current date and time
if desired_date_time <= current_date_time:
    desired_date = current_date_time.date() + timedelta(days=7)
    desired_date_time = datetime.combine(desired_date, user_time)

# Format the output date and time
output_text = desired_date_time.strftime("%A, %B %d, %Y %I:%M %p")

print("Scheduled event:", output_text)
