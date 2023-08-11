
import os
import tkinter as tk
import threading
#import imutils
import web
import portscanner
import dir_search
import waybackurl
import sys

from tkinter import messagebox

# from functools import partial
def show_help():
    help_text = "Enter the website you want to get informations:\n\n"
    help_text += "1. PortScan: This scan uses packets to determine open ports.\n"
    help_text += "2. Email scramper:Searches random email and generates info.\n"
    help_text += "3. Comprehensive Scan: This scan performs a comprehensive scan including both TCP and UDP ports.\n"
    help_text += "4. Subdomain : It will find and generate subdomain of that webpage.\n"
    help_text += "5. Directory search: Searching hidden directories.\n"
    messagebox.showinfo("Help", help_text)

root = tk.Tk()
root.geometry('1000x700')


# Create Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=show_help)

set_width = 50
set_height = 50
root.title('Web Enumeration Tools')
root.minsize(600,300)
# root.configure()
# Colors
m1c = "#00ee00"
bgc = "#222222"
dbg = "#000000"
fgc = "#111111"
root.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc, activeForeground=bgc, highlightColor=m1c,
                  highlightBackground=m1c)
                  
def print_search():
    l1.config(text=f"Target: {search.get()}")
    pass


search = tk.StringVar()
f1 = tk.Frame(root)
tk.Entry(f1, textvariable=search, width=55, font="comicsansms 10 italic").pack(side='left', padx=6)
tk.Button(f1, text="Print", command=print_search, font="comicsansms 9 italic", anchor='e').pack()
l1 = tk.Label(root, text="Target:", font="comicsansms 13 italic", padx=6)
f1.pack(anchor='w', pady=5, padx=6)
l1.pack(anchor='w')

from1 = tk.StringVar()
to1 = tk.StringVar()
thread1 = tk.StringVar()
email_link = tk.StringVar()
Checkbutton1 = tk.IntVar()
x11 = 0
x12 = 0
x13 = 0
x14 = 0
x15 = 0
x16 = 0


def port_scanner_btn():
    assert search.get(), "Please enter a target website."
    assert from1.get().isdigit() and to1.get().isdigit() and thread1.get().isdigit(), "Please enter valid numbers."
    s = search.get()
    if s.startswith("http://"):
        s = s[7:]
    if s.startswith("https://"):
        s = s[8:]
    portscanner.target = s
    a = int(from1.get())
    b = int(to1.get())
    x = int(thread1.get())
    t1 = threading.Thread(target=portscanner.portscanner, args=(x, a, b))
    t1.start()

    global x11
    if x11 == 0:
        x11 = 0
        t1.start()
def Port_Scan():
    global from1, to1, thread1
    f2 = tk.Frame(root)
    tk.Label(f2, text="1= Port Scan", font="comicsansms 11 bold", pady="1").pack()
    tk.Label(f2, text="Port Range:", font="comicsansms 11").pack(side='left')
    tk.Label(f2, text="From=", font="comicsansms 11").pack(side='left')
    tk.Entry(f2, textvariable=from1, width=8, font="comicsansms 11 italic").pack(side='left')
    tk.Label(f2, text="To=", font="comicsansms 11").pack(side='left')
    tk.Entry(f2, textvariable=to1, width=8, font="comicsansms 11 italic").pack(side='left')
    tk.Label(f2, text="Threads=", font="comicsansms 11").pack(side='left')
    tk.Entry(f2, textvariable=thread1, width=8, font="comicsansms 11 italic").pack(side='left')
    tk.Label(f2, text="", font="comicsansms 11").pack(side='left')
    tk.Button(f2, text="Scan", command=port_scanner_btn, font="comicsansms 9 italic").pack()
    f2.pack()

def email_btn():
    web.a1 = search.get()
    web.argument = int(email_link.get())
    t1 = threading.Thread(target=web.scrap_emails)  # email scraping
    global x12
    if x12 == 0:
        x12 = 0
        t1.start()

def email():
    global email_link
    f3 = tk.Frame(root)
    tk.Label(f3, text="2= Email Scraper", font="comicsansms 13 bold", pady=1).pack()
    tk.Label(f3, text="Number of Links you want to search=", font="comicsansms 13").pack(side='left')
    tk.Entry(f3, textvariable=email_link, width=8, font="comicsansms 13 italic").pack(side='left')
    tk.Label(f3, text="", font="comicsansms 13").pack(side='left')
    tk.Button(f3, text="Search", command=email_btn, font="comicsansms 9 italic").pack()
    f3.pack()


def cert():
    s = search.get()
    if s.startswith("http://"):
        s = s[7:]
    if s.startswith("https://"):
        s = s[8:]
    web.a1 = s
    t1 = threading.Thread(target=web.subdomain_crtsh)  
    global x13
    if x13 == 0:
        x13 = 0
        t1.start()
def dns_dumpster():
    s = search.get()
    if s.startswith("http://"):
        s = s[7:]
    if s.startswith("https://"):
        s = s[8:]
    if s.startswith("www."):
        s = s[4:]
    web.a1 = s
    t1 = threading.Thread(target=web.dns_dumpster) 
    global x14
    if x14 == 0:
        x14 = 0
        t1.start()

def subdomain():
    f4 = tk.Frame(root)
    tk.Label(f4, text="3= Find subdomain", font="comicsansms 13 bold", pady=1).pack()
    tk.Button(f4, text="Find from cert.sh", command=cert, font="comicsansms 11 italic").pack(side='left')
    tk.Label(f4, text=" ", font="comicsansms 13 bold", pady=1).pack(side='left')
    tk.Button(f4, text="Find from DNSDumpster", command=dns_dumpster, font="comicsansms 11 italic").pack(side='left')
    f4.pack()


def way_back_btn():
    waybackurl.a1 = search.get()
    t1 = threading.Thread(target=waybackurl.way_back_url)  # web.archive.org  way back urls
    global x15
    if x15 == 0:
        x15 = 0
        t1.start()
def way_back():
    f5 = tk.Frame(root)
    tk.Label(f5, text="4= Way Back urls: ", font="comicsansms 13 bold", pady=1).pack(side='left')
    tk.Button(f5, text="Find", command=way_back_btn, font="comicsansms 11 italic").pack()
    f5.pack()

def dirsearch_btn():
    dir_search.url = search.get()
    x = Checkbutton1.get()
    if x == 1:
        s = "apache-user-enum-1.0"
    elif x == 2:
        s = "directory-list-1.0"
    elif x == 3:
        s = "directory-list-lowercase-2.3-medium"
    elif x == 4:
        s = "directory-list-lowercase-2.3-small"
    else:
        s = "directory-list-2.3-small_edited"
    dir_search.s = s
    dir_search.run()

def dir_search11():
    f6 = tk.Frame(root)
    tk.Label(f6, text="5= Directory search", font="comicsansms 13 bold", pady=1).pack()
    tk.Label(f6, text="wordlist:", font="comicsansms 11", pady=1).pack(side='left')
    global Checkbutton1

    tk.Radiobutton(f6, text="apache-user-enum-1.0", variable=Checkbutton1, value=1, indicator=0,
                   ).pack()
    tk.Radiobutton(f6, text="directory-list-1.0", variable=Checkbutton1, value=2, indicator=0,
                   ).pack()
    tk.Radiobutton(f6, text="directory-list-lowercase-2.3-medium", variable=Checkbutton1, value=3, indicator=0,
                   ).pack()
    tk.Radiobutton(f6, text="directory-list-lowercase-2.3-small", variable=Checkbutton1, value=4, indicator=0,
                   ).pack()
    tk.Button(f6, text="dirsearch", command=dirsearch_btn, font="comicsansms 11 italic").pack(side='right')
    f6.pack()


output_text = tk.Text(root, font=("Arial", 9))
output_text.pack(side=tk.BOTTOM,fill=tk.NONE, expand=True)
output_text.config(width=50, height=10)

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
       
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)


    def flush(self):
        pass
sys.stdout = StdoutRedirector(output_text)

if __name__ == "__main__":
    assert os.name == 'nt', "This program is intended to run on a Windows system."
   

Port_Scan()
email()
subdomain()
way_back()
dir_search11()
root.mainloop()
