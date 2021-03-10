import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from tkinter import *
import sys

def res_fun():
    if r.get() == 2:
        main_frm = LabelFrame(window).grid(row = 3, column = 0,padx = 10, pady = 10)
        
        ping_label = Label(main_frm,text = 'Enter your ip ===>')
        
        global ping_entry
        ping_entry = Entry(main_frm)
        pingSubmit_btn = Button(window,text = 'Submit',command = ping_res)
    
        ping_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        ping_entry.grid(row = 3, column = 1, padx = 10, pady = 10)
        pingSubmit_btn.grid(row = 4, column = 0, padx = 10, pady = 10)
    
    elif r.get() == 1:
        main_frm = LabelFrame(window).grid(row = 3, column = 0,padx = 10, pady = 10)
        
        ping_label = Label(main_frm,text = 'Enter your ip ===>')
        
        global ping_ent
        ping_ent = Entry(main_frm)
        pingSubmit_btn = Button(window,text = 'Submit',command = ping_check)
    
        ping_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        ping_ent.grid(row = 3, column = 1, padx = 10, pady = 10)
        pingSubmit_btn.grid(row = 4, column = 0, padx = 10, pady = 10)

def ping_check():
    pingGet = ping_ent.get()
    
    if len(pingGet) > 15:
        messagebox.showinfo('Result','You ave entered an incorrect ip')

def ping_res():
    res = ping()
    
    if res == True:
        messagebox.showinfo('Result','The ip is live.')
    elif res == False:
        messagebox.showinfo('Result','The ip is dead.')


def ping():
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    ping_get = ping_entry.get()

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ping_get]

    return subprocess.call(command) == 0


window = Tk()

r = IntVar()

Radiobutton(window,text = '1- Check an ip length validity.',variable = r,value = 1).grid(row = 0, column = 0, pady = 10, padx = 10)
Radiobutton(window,text = '2- Ping an IP.',variable = r,value = 2).grid(row = 1, column = 0, pady = 10, padx = 10)
submit_btn = Button(window,text = 'Submit',width = 20, height = 3,command = res_fun).grid(row = 2, column = 0, padx = 10,pady = 10)

window.mainloop()