import webbrowser
import time

break_time=3
print("Program started on "+time.ctime())
for i in range(1,break_time+1):
    time.sleep(10)
    print("Current time:"+time.ctime())
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

print("Program ended")
