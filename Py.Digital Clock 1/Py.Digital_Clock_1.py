#Py.DigitalClock
from tkinter import *
import time

window = Tk()
window.title('digital clock')
window.geometry('600x400')


def myTime():
    hour  = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p") 
    day = time.strftime("%A")
    zone = time.strftime("%Z")

    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + zone
    myLabel.config(text=myText)
    myLabel2.config(text=myText2)
    myLabel.after(1000 , myTime)

myLabel = Label(window, text="Hello Arshak", font=('Arial', 56),  fg='Brown', bg='Blue', background='yellow')
myLabel.pack()
myLabel2 = Label(window, text="", font=("Arial", 24))
myLabel2.pack()




myTime()


window.mainloop()

# sonoteller.ai
# www.craiyon.com

