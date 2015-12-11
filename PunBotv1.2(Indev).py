# -*- coding: utf-8 -*-
#PunBot
from Tkinter import *
import ttk
import tkMessageBox
import smtplib
import os

def start_spam(*args):
    try:
        login_user = str(username.get())
        login_pass = str(password.get())
        spam = int(spam_amount.get())
        msg = str(message.get())
        victim = str(to_address.get())

        while spam > 0:
            if "gmail" in username.get():
                server = smtplib.SMTP("smtp.gmail.com", 587)
            else:
                server = smtplib.SMTP("smtp.live.com", 587)
            server.ehlo()
            server.starttls()
            server.login(login_user, login_pass)
            server.sendmail(login_user, victim, msg)
            server.quit
            spam = spam - 1

        messagebox.showinfo("Complete" , "Victim has successfully been sent {0} emails!" . format(spam))
         
        os.exit(1)

    except smptlib.SMTPxception:
        spam = 0
        messagebox.showerror("Error Sending!" , """Failed to send mail!
This error usually aries from:
    -Your email account reaching a sending limit.   
    -Your email being banned or suspended.""")

    except smtplib.SMTPServerDisconnected:
        spam = 0
        messagebox.showerror("Error Sending", """
Failed to send email!
This error usually arises from:
    - Your email already being suspended or banned.
    - Not having a valid internet connection.
    - If the email server is offline or unavailable.
""")
        

root = Tk()
root.title("Punbot Version 1.1 Alpha")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

username = StringVar()
password = StringVar()

spam_amount = IntVar()
to_address = StringVar()
message = StringVar()


# Entrys
username_entry = ttk.Entry(mainframe, width = 10, textvariable = username)
username_entry.grid(column = 2, row = 1, sticky = W)

password_entry = ttk.Entry(mainframe, width = 10, textvariable = password)
password_entry.grid(column = 2, row = 2, sticky = W)

message_entry = ttk.Entry(mainframe, width = 15, textvariable = message)
message_entry.grid(column = 2, row = 3, sticky = W)

spam_entry = ttk.Entry(mainframe, width = 10, textvariable = spam_amount)
spam_entry.grid(column = 2, row = 4, sticky = W)

to_address_entry = ttk.Entry(mainframe, width = 10, textvariable = to_address)
to_address_entry.grid(column = 2, row = 5, sticky = W) 

# Labels

ttk.Label(mainframe, text = "Login Email:").grid(column = 1, row = 1, sticky = W)
ttk.Label(mainframe, text = "Login Password:").grid(column = 1, row = 2, sticky = W)
ttk.Label(mainframe, text = "Message:").grid(column = 1, row = 3, sticky = W)
ttk.Label(mainframe, text = "# of Messages:").grid(column = 1, row = 4, sticky = W)
ttk.Label(mainframe, text = "Recipient:").grid(column = 1, row = 5, sticky = W)

# Buttons

ttk.Button(mainframe, text = "Send puns!", command = start_spam).grid(column = 4, row = 2, sticky = W)


for child in mainframe.winfo_children(): child.grid_configure(padx = 5, pady = 5)
username_entry.focus()
root.mainloop()