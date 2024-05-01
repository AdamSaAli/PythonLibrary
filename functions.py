from customtkinter import *

#I think I should rename this file as it mostly has the gui stuff the user interacts with
app = CTk()
app.geometry("500x400")

def getUserDate():
 
    new=CTkToplevel(app)
    textbox=CTkEntry(master=new,placeholder_text="Input date in the form of xx/xxx/xxxx to xx/xxx/xxxx")
    textbox.pack(anchor="center",expand=True,pady=100)
    #Double check the way the date is actually stored
    print("hihihih")
    

checkbox = CTkCheckBox(master=app,text="Choose which unit(s)")
button = CTkButton(master=app,text="submit",command=getUserDate)
# I need to somehow add more boxes to this depending on how many units the user has
checkbox.place(relx=0.5,rely=0.5,anchor="center")
button.pack(anchor="n",expand=True,)
#I will probably need  a function thats called when the user submits the amount of units they want that can fetch the data needed

#in this setup the window that asks how many unit sthey want and the window that asks the date range they want are both open, maybe I should close the first one after getting how many units they want or maybe I should keep it open in case they want to change which units they have selected
app.mainloop()
