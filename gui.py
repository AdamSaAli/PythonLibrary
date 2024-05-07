from customtkinter import *


app = CTk()
app.geometry("500x400")

def getUserDate():
 
    dateWindow=CTkToplevel(app)
    dateWindow.title("This is the window to retrieve the date")
    textbox=CTkEntry(master=dateWindow,placeholder_text="Input date in the form of xx/xxx/xxxx to xx/xxx/xxxx")
    textbox.pack(anchor="center",expand=True,pady=100)
    #Double check the way the date is actually stored
    submitDate = CTkButton(master=dateWindow,text="submit",command=getUserPollutant)
    submitDate.pack(anchor="center",expand=True)
    #make the window nicer by changin colours, centering stuff better and just improve the overall appearance 
    return
# not done with this function

def getUserPollutant():
    PollutantWindow=CTkToplevel(app)
    PollutantWindow.title("This is the window to retrieve the Pollutant")
    gasCheckBox=CTkCheckBox(master=PollutantWindow,text="Gas")
    PMCheckBox=CTkCheckBox(master=PollutantWindow,text="PM")
    #maybe I should use a drop down menu rather than checkboxes so the user can only chose one option
    gasCheckBox.pack(anchor="n")
    PMCheckBox.pack(anchor="n")
    PollutantSubmit = CTkButton(master=PollutantWindow,text="submit")
    PollutantSubmit.pack(anchor="n")
    
    return
#not done with this function


checkbox = CTkCheckBox(master=app,text="Choose which unit(s)")

button = CTkButton(master=app,text="submit",command=getUserDate)
# I need to somehow add more boxes to this depending on how many units the user has
checkbox.pack(anchor="center",expand=True)
button.pack(anchor="n",expand=True)

#I will probably need  a function thats called when the user submits the amount of units they want that can fetch the data needed

#in this setup the window that asks how many unit sthey want and the window that asks the date range they want are both open, maybe I should close the first one after getting how many units they want or maybe I should keep it open in case they want to change which units they have selected
app.mainloop()
