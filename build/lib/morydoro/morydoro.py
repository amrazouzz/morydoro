import time
from termcolor import colored
from plyer import notification

def morydoro(pomodoro_duration, break_duration):
    print(colored("Starting a 25-minute pomodoro.", 'green'))
    time.sleep(pomodoro_duration)
    print(colored("Pomodoro complete!", 'red'))
    notification.notify(
        title='Morydoro',
        message='Pomodoro complete!',
        app_name='Morydoro',
    )
    print(colored("Starting a 5-minute break.", 'yellow'))
    time.sleep(break_duration)
    print(colored("Break complete!", 'red'))
    notification.notify(
        title='Morydoro',
        message='Break complete!',
        app_name='Morydoro',
    )

def main():
    pomodoro_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60  # 5 minutes in seconds
    while True:
        morydoro(pomodoro_duration, break_duration)

if __name__ == "__main__":
    main()