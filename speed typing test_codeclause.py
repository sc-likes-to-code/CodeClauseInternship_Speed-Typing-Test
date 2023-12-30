#Importing all desired libraries
from tkinter import *
from timeit import default_timer as timer
import random

#Creating window using GUI
win1 = Tk()

#Naming the GUI interface window
win1.title("Speed Typing Test")

#Defining the dimensions of the window
win1.geometry("450x200")

x = 0

#Defining the function for the test
def speed_typing_test():
	global x

	#Loop for destroying the window after test
	if x == 0:
		win1.destroy()
		x = x+1

	#Defining function for results of test
	def check_result():
		if entry.get() == w1[w]:

			#Here start time is when the window is opened and end time is when window is destroyed
			end = timer()

			#We deduct the start time from end time and calculate results using timeit function
			print(end-start)
		else:
			print("Wrong Input")

	w1 = ['programming', 'coding', 'algorithm', 'systems', 'python', 'software', 'artificial', 'intelligence', 'machine', 'learning', 'language', 'speed', 'typing', 'test', 'computer']

	#Give random words for testing the speed of user
	w = random.randint(0, (len(w1)-1))

	#Start timer using timeit function
	start = timer()
	win2 = Tk()
	#Naming the GUI interface window
	win2.title("Speed Typing Test")
	win2.geometry("450x200")

	#Use label method of tkinter for labeling in window
	x2 = Label(win2, text=w1[w], font="times 20")

	#Place of labeling in window
	x2.place(x=150, y=10)
	x3 = Label(win2, text="Start Typing", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(win2)
	entry.place(x=280, y=55)

	#Buttons to submit output and check results
	b2 = Button(win2, text="Done", command=check_result, width=12, bg='grey')
	b2.place(x=150, y=100)

	b3 = Button(win2, text="Try Again", command=speed_typing_test, width=12, bg='grey')
	b3.place(x=250, y=100)
	win2.mainloop()


x1 = Label(win1, text="Lets start playing..", font="times 20")
x1.place(x=10, y=50)

b1 = Button(win1, text="Go", command=speed_typing_test, width=12, bg='grey')
b1.place(x=150, y=100)

#Calling window
win1.mainloop()
