# This runs test() function in intervals of 1 second
from re import I
from threading import Timer
run = True
def test():
	global run
    
	print(1)
	if run:
		Timer(1, test).start()


test()