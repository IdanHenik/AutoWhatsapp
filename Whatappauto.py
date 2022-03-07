from dis import Instruction, show_code
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import dialog 
from PIL import Image,ImageTk
from xmlrpc.client import DateTime
import pyautogui as pg
import webbrowser as web
import time
root = tk.Tk()
root.title("Whatapp automation by iHenik")


canvas=tk.Canvas(root,height=300,width=600)
canvas.grid(columnspan=3,rowspan=3)

#logo
logo= Image.open('Whatapp.png')
logo =ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

def Delay(hour,min): 
    if hour not in range(25) or min not in range(60):
        raise Warning("Invalid Time Format!")
    current_time = time.localtime()
    delaymin=min-current_time.tm_min #descrease the time user input - current time
    delayhour=hour-current_time.tm_hour #etc
    delaytime=time.strptime(f"{delayhour}:{delaymin}:0","%H:%M:%S")
    return delaytime

def main_program():
    print("Enter the time you want to send the messege\n")
    input_time=input("For Example 17:40:\n")
    user_time=input_time.split(":") #Split time to hours and mins
    hour=int(user_time[0])
    min=int(user_time[1])
    print("Enter the Contact number")
    phone=input("for Example +972526262287:")
    text=input("Enter the messege: ")
    delaytime=Delay(hour,min) 
    delaytime_insec= (delaytime.tm_min*60)+(delaytime.tm_hour*3600) #Sum the delay time in seconds
    time.sleep(delaytime_insec)
    web.open(f"https://web.whatsapp.com/send?phone={phone}&text={text}", new=1)
    time.sleep(32)
#print(pg.position()) #Cursor on x= 1873 y=891
#pg.moveTo(1873,891,3)
    pg.click(1873,891,1,0,button="left")
    
    


#instrucations
Instructions = tk.Label(root,text="Send automaticalliy whatsapp messege to a specific contact",font="Raleway")
Instructions.grid(columnspan=3,column=0,row=1)



canvas=tk.Canvas(root,height=250,width=600)
canvas.grid(columnspan=3,)
root.after(3000,main_program)
root.mainloop()