import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from tkinter import *
#import sys

def ping():
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    ping_get = ping_ent.get()

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ping_get]

    return subprocess.call(command) == 0


def res_fun():
    
    # if Ip ping requested
    if r.get() == 2:
        
        #Call the ip pinger function
        res = ping()
        
        if res == True:
            messagebox.showinfo('Result','The ip is live.')
        elif res == False:
            messagebox.showinfo('Result','The ip is dead.')
            
    # if Ip validation requested    
    elif r.get() == 1:

        pingGet = ping_ent.get()
        
        if len(pingGet) > 15:
            messagebox.showinfo('Result','You have entered an incorrect ip')
        else:
            messagebox.showinfo('Result','You have entered an correct ip')


############################################################
#                        GLOBAL SECTION                    #
############################################################


window = Tk()

r = IntVar()

frame_1 = LabelFrame(window,text = 'Options')

Radiobutton(frame_1,text = '1- Check an ip length validity.',variable = r,value = 1).grid(row = 0, column = 0, pady = 10, padx = 10, sticky="W")
Radiobutton(frame_1,text = '2- Ping an IP.',variable = r,value = 2).grid(row = 1, column = 0, pady = 10, padx = 10, sticky="W")

ping_label = Label(frame_1,text = 'Enter your ip ===>',bg = 'yellow')
    
ping_ent = Entry(frame_1)
    
ping_label.grid(row = 3, column = 0, padx = 10, pady = 10, sticky="W")
ping_ent.grid(row = 3, column = 1, padx = 10, pady = 10 )

submit_btn = Button(window,text = 'Submit',width = 20, height = 3,command = res_fun,bg = '#00e6e6').grid(row = 2, column = 0, padx = 10,pady = 10)

frame_1.grid(row = 0, column = 0, padx = 10, pady = 10)

window.mainloop()