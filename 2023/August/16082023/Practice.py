from datetime import datetime, timedelta
import re

# User input day
user_input = "Every Wednesday at 08:56 PM"  # For example, "Thursday"

# Regular Expression to identify the day name and time from the given string
day_name_pattern = r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
time_pattern = r"\d{2}:\d{2} [APap][Mm]"

# Verify if today is the day, then check if time has already passed or not
toady_day_name = datetime.now().strftime("%A").lower()
user_input_day = re.search(day_name_pattern, user_input, re.IGNORECASE).group().lower()
user_input_time_ = re.search(time_pattern, user_input).group()
user_input_time = datetime.strptime(user_input_time_, "%I:%M %p").time()

if toady_day_name == user_input_day and user_input_time > datetime.now().time():
    date = datetime.now().strftime("%A, %B %d, %Y ")
    print(date + "04:00 AM")
else:
    # Get the current date
    current_date = datetime.now().date()

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
        - current_date.weekday()
    ) % 7

    # Calculate the date of the desired day
    desired_date = current_date + timedelta(
        days=days_until_day + (days_until_day <= 0) * 7
    )

    # Format the output date
    output_date = desired_date.strftime("%A, %B %d, %Y %I:%M %p")

    print("Next", user_input_day, "is:", output_date)
