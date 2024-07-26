import test2
from threading import Timer
import setTimeOut

child = test2.Child("Alice", 10)

child.greet()

def hello():
    print ("hello, world")

t = Timer(3.0, hello)
#t.start()  # after 30 seconds, "hello, world" will be printed

def start_timer(delay, func): 
    t = Timer(float(delay), func).start();
    
#start_timer(1, hello)
setTimeOut(1,hello)