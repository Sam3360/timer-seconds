import time

def timer(seconds):
    """
    Counts down from a specified number of seconds, printing each second on a new line.
    """
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display) 
        time.sleep(1)  
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    try:
        duration = int(input("Enter the duration of the timer in seconds: "))
        if duration <= 0:
            print("Please enter a positive number of seconds.")
        else:
            timer(duration)
    except ValueError:
        print("Invalid input. Please enter an integer.")
