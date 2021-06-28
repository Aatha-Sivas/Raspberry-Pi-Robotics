import time
import tty
import sys
import termios

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	tty.setraw(sys.stdin.fileno())
	ch = sys.stdin.read(1)
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

var = "n"

while var!= "q":
	var = getch()
	if var == "l":
		print("you pressed the button L")
	if var == "h":
		print("you pressed the button H")
	if var == "b":
		print("WOW THIS WORKS?!")
	time.sleep(0.1)
