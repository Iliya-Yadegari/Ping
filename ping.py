import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from tkinter import *
import sys

def ping():
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ping_entry.get()]

    return subprocess.call(command) == 0

def res_fun():
    if r == 2:
        main_frm = LabelFrame(window).grid(row = 1, column = 0,padx = 10, pady = 10)
        
        ping_label = Label(main_frm,text = 'Enter your ip ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
        ping_entry = Entry(main_frm).grid(row = 2, column = 1, padx = 10, pady = 10)
        
        ping_get = ping_entry.get()
    
        res = ping()
    
        if res == True:
            messagebox.askquestion('Result','The ip is live.')
        elif res == False:
            messagebox.askquestion('Result','The ip is dead.')

    if len(ping_get) > 15:
        res_label = Label(window,text = 'You have entered a wrong number try again.')
        sys.exit()

window = Tk()

r = IntVar()

Radiobutton(window,text = '1- Check an ip length validity.',variable = r,value = 1).grid(row = 0, column = 0, pady = 10, padx = 10)
Radiobutton(window,text = '2- Ping an IP.',variable = r,value = 2).grid(row = 1, column = 0, pady = 10, padx = 10)


window.mainloop()