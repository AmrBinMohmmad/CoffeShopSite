from playsound import playsound
import time
Clear = "\33[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapsed = 0
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        min_left = time_left // 60
        sec_left = time_left % 60
        print(f"Time's up!{CLEAR_AND_RETURN} {min_left:02d}:{sec_left:02d} seconds have passed.")
    playsound("Documents/nasheed.mp3")

prommt = int(input("Enter the time in seconds: "))
if prommt <= 0:
    print("Please enter a valid time in seconds.")
else:
    print("Alarm is set for", prommt, "seconds.")
    alarm(prommt)