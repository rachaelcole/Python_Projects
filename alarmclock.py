# Importing all the necessary libraries
from tkinter import *  # stdlib GUI in Python
import datetime  
import time
import winsound  # sound playing machinery for Windows

# Create a while loop
def alarm(set_alarm_timer):
	while True:
		time.sleep(1)
		current_time = datetime.datetime.now()
		now = current_time.strftime("%H:%M:%S")
		date = current_time.strftime("%d/%m/%Y")
		print('The set date is:', date)
		print(now)
		if now == set_alarm_timer:
			print('Time to wake up!')

		winsound.Playsound('sound.wav', winsound.SND_ASYN)
		break

def actual_time():
	set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
	alarm(set_alarm_timer)

clock = Tk()

clock.title('Rachael\'s Alarm Clock')
clock.geometry('400x200')
time_format = Label(clock, text = 'Enter time in 24 hour format!',
					fg='red', bg='black', font='Arial').place(x = 60, y = 100)
addTime =  Label(clock, text = 'When to wake you up', fg = 'blue', relief = 'solid',
				font=('Helvetica', 7, 'bold')).place(x = 0, y = 29)

# The variables required to set the alarm (initialisation)
hour = StringVar()
mins = StringVar()
sec = StringVar()

# Time required to set the alarm clock
hourTime = Entry(clock, textvariable = hour, bg = 'pink', width = 15).place(x = 110, y = 30)
minTime = Entry(clock, textvariable = mins, bg = 'pink', width = 15).place(x=150,y=30)
secTime = Entry(clock, textvariable = sec, bg = 'pink', width = 15).place(x=200, y=30)

# To take the time input by user:
submit = Button(clock, text = 'Set alarm', fg='red', width=10, command=actual_time).place(x=110, y=70)
clock.mainloop()
# Execution of the window.