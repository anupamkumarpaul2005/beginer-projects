import time
import threading
from win10toast import ToastNotifier

print("""
            CLOCK
            
    1. Current Time
    2. Timer
    3. Alarm
    4. Stopwatch
    
""")

def currentTime():
    t=time.asctime(time.localtime(time.time()))
    print(f"The current date and time is- {t}")

def timer(n):
    time.sleep(n)
    hr=n//3600
    min=(n-(hr*3600))//60
    sec=(n-(hr*3600)%60)
    ToastNotifier().show_toast(title="Timer", msg=f"Time is up! It has been {hr} hr {min} min {sec} sec.", duration=10)

def alarm():
    pass

threading.Thread(target=timer, args=(10,)).start()
threading.Thread(target=currentTime).start()
