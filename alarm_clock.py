# Borealsummit (IADLMC)

"""
Simple python script to set an alarm for an especific time.
When the alarm goes off, a sound will be played or a youtube video opened
You can set the possible youtube videos in a config file
"""

#  import datetime
#  import os
#  import time
#  import random
#  import webbrowser


def valid_hours(hours):
    return hours < 24 and hours >= 0


def valid_minutes_or_seconds(minutes):
    return 0 <= minutes < 60


def only_hours(alarm_time):
    return len(alarm_time) == 1 and valid_hours(alarm_time[0])


def hours_and_minutes(alarm_time):
    return (
        len(alarm_time) == 2
        and valid_hours(alarm_time[0])
        and valid_minutes_or_seconds(alarm_time[1])
    )


def hours_and_minutes_and_seconds(alarm_time):
    return (
        len(alarm_time) == 3
        and valid_hours(alarm_time[0])
        and valid_minutes_or_seconds(alarm_time[1])
        and valid_minutes_or_seconds(alarm_time[2])
    )


def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    return (
        hours_and_minutes(alarm_time)
        or hours_and_minutes_and_seconds(alarm_time)
    )


if __name__ == "__main__":
    print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")

    while True:
        ALARM_INPUT = input(">> ")
        try:
            ALARM_TIME = [int(n) for n in ALARM_INPUT.split(":")]
            if check_alarm_input(ALARM_TIME):
                print("You entered a valid alarm")
                break
            raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")
