import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Timer completed!")

# User se input lena
t = int(input("Enter the time in seconds: "))

# Function call karna
countdown(t)
