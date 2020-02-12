# Borealsummit (IADLMC)

"""
Simple python script to set an alarm for an especific time.
When the alarm goes off, a sound will be played or a youtube video opened
You can set the possible youtube videos in a config file
"""

import datetime
#  import os
import time
import random
import webbrowser


def convert_to_seconds(alarm_time_parts):
    seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second
    return sum(
        [a * b for a, b in zip(seconds_hms[: len(alarm_time_parts)], alarm_time_parts)]
    )


def get_time_diff_seconds_from_now(alarm_time_parts):
    alarm_seconds = convert_to_seconds(alarm_time_parts)
    print(f"Alarm set to trigger at {alarm_seconds} seconds of the day")
    now = datetime.datetime.now()
    current_time_seconds = convert_to_seconds([now.hour, now.minute, now.second])
    print(f"Current time seconds are: {current_time_seconds}")
    return alarm_seconds - current_time_seconds

def open_random_video():
    # Load list of possible video URLs
    with open("youtube_alarm_videos.txt", "r") as alarm_file:
        videos = alarm_file.readlines()

    # Open a random video from the list
    webbrowser.open(random.choice(videos))

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
    return hours_and_minutes(alarm_time) or hours_and_minutes_and_seconds(alarm_time)


if __name__ == "__main__":
    print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")

    while True:
        ALARM_INPUT = input(">> ")
        try:
            ALARM_TIME = [int(n) for n in ALARM_INPUT.split(":")]
            if check_alarm_input(ALARM_TIME):
                time_diff_seconds = get_time_diff_seconds_from_now(ALARM_TIME)
                print(
                    "Alarm set to go off in %s"
                    % datetime.timedelta(seconds=time_diff_seconds)
                )

                # Sleep until the alarm goes off
                time.sleep(time_diff_seconds)

                # Time for the alarm to go off
                print("Wake Up!")
                open_random_video()
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")
