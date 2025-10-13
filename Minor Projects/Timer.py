import time

t = int(input("Enter the time in seconds: "))

for x in reversed(range (0, t + 1)):
    secs = x % 60
    mins = (x / 60) % 60
    hrs = x / 3600
    print(f"{int(hrs):02d}:{int(mins):02d}:{secs:02d}")
    time.sleep(1)
print("Time's up!")
