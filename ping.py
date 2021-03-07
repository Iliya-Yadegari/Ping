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
    res = ping()
    ping_get = ping_entry.get()
    
    if len(ping_get) > 15:
        res_label = Label(window,text = 'You have entered a wrong number try again.')
        sys.exit()
    
    if res == True:
        res_label = Label(window,text = 'The ip is live').grid(row = 3, column = 0)
    elif res == False:
        res_label = Label(window,text = 'The ip is dead').grid(row = 3, column = 0)


window = Tk()

ping_label = Label(window,text = 'Enter your ip ===>')
ping_entry = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = ping)
res_btn = Button(window,text = 'Press for your result',width = 20, height = 3,command = res_fun).grid(row = 2, column = 0)

ping_label.grid(row = 0, column = 0, padx = 10, pady = 10)
ping_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
submit_btn.grid(row = 1, column = 0, padx = 10, pady = 10)

window.mainloop()