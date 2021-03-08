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
    ping_get = ping_entry.get()
    if len(ping_get) > 15:
        res_label = Label(window,text = 'You have entered a wrong number try again.')
        sys.exit()
    res = ping()

    if res == True:
        messagebox.askquestion('Result','The ip is live.')
    elif res == False:
        messagebox.askquestion('Result','The ip is dead.')


window = Tk()

Radiobutton(window,text = '1- Check an ip length validity.',variable)

window.mainloop()