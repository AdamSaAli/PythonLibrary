from customtkinter import *

#I think I should rename this file as it mostly has the gui stuff the user interacts with
app = CTk()
app.geometry("500x400")

def getUserData():
    print(checkbox.get())
checkbox = CTkCheckBox(master=app,text="Choose which unit(s)")
button = CTkButton(master=app,text="submit",command=getUserData)
# I need to somehow add more boxes to this depending on how many units the user has
checkbox.place(relx=0.5,rely=0.5,anchor="center")
button.pack(anchor="n",expand=True)
#I will probably need  a function thats called when the user submits the amount of units they want that can fetch the data needed

app.mainloop()