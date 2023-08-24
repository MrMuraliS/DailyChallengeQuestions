import calendar
from termcolor import colored


def display_amazing_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    header = colored(f" {month_name} {year} ", "white", "on_cyan", ["bold"])
    day_names = colored("Su Mo Tu We Th Fr Sa", "red", attrs=["bold"])
    separator = colored("-" * 50, "yellow")

    print(header.center(50))
    print(day_names)
    print(separator)

    for week in cal:
        week_str = " ".join(
            (
                colored(str(day).rjust(2), "magenta", attrs=["bold"])
                if day != 0
                else "  "
            )
            for day in week
        )
        print(week_str)


if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    display_amazing_calendar(year, month)
