from customtkinter import *


app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")
app.title("User input")

frame1=CTkFrame(master=app,fg_color="red",height=20,width=20)
frame1.pack()

Checkbox

frame2=CTkFrame(master=app,fg_color="blue")
frame2.pack()

frame3 = CTkFrame(master=app,fg_color="white")
frame3.pack(expand=True)
pollutant =CTkComboBox(master=frame3,values=["PM","Gas"])
#maybe we would like to add specific PM's or a specific gas
pollutant.pack(expand=True)

app.mainloop()
