from tkinter import* 
import datetime as dt
import time
import winsound as ws
#defining the function for the alarm clock
def alarm(set_AlarmTimer):
    while True:
        time.sleep(1)
        actualTime=dt.datetime.now()
        currentTime=actualTime.strftime("%H:%M:%S")
        currentDate=actualTime.strftime("%d/%m/%y")
        the_message="Current Time:"+str(currentTime)
        print(the_message)
        if currentTime==set_AlarmTimer:
            ws.PlaySound("sound.wav", ws.SND_ASYNC)
            break

def getAlarmTime():
    alarmSetTime=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(alarmSetTime)

root=Tk()
root.title("The Alarm Clock")
root.geometry("400x500")
root.config(bg="#CACAFF")
root.resizable(width=False,height=False)
time_format=Label(root,text="Enter time in 24 hours format only!!!", fg="white", bg="red", font="Arial").place(x=50,y=280)

addTime=Label(root, text="Hour:", fg="green", relief="sunken",font=("Helevetica",13, "bold")).place(x=80, y=120)
addTime=Label(root, text="Min :  ", fg="green", relief="sunken",font=("Helevetica",13, "bold")).place(x=80, y=150)
addTime=Label(root, text="Sec :  ",fg="green", relief="sunken",font=("Helevetica",13, "bold")).place(x=80, y=180)
setYourAlarm=Label(root,text="Set Alarm Time",width="15", fg="blue",relief="raised",font="italic").place(x=130, y=60)
setYourAlarm=Label(root,text="Alarm Clock with GUI",width="20", fg="brown",relief="raised",font="italic").place(x=95, y=10)


#variables required to set the alarm

hour=StringVar()
min=StringVar()
sec=StringVar()

#time required to set the alarm clock

hourTime=Entry(root, textvariable=hour, bg="pink", width=20).place(x=150,y=120)
minTime=Entry(root, textvariable=min,bg="pink", width=20).place(x=150, y=150)
secTime=Entry( root,textvariable=sec, bg="pink", width=20).place(x=150, y=180)

#to take the time input by user

submit=Button(root, text="SET ALARM",fg="red", width=10,relief="solid", font=("Helevetica",13, "bold"), command=getAlarmTime).place(x=150, y=340)
root.mainloop()