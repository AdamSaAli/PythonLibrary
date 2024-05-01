from customtkinter import *

app = CTk()
app.geometry("500x400")
def user_input():
    print(entry.get())

entry = CTkEntry(master=app, placeholder_text="Input",width=300)
button = CTkButton(master=app,text="submit",command=user_input)
#entry.place(relx=0.5,rely=0.5,anchor="center")

entry.pack(anchor="s",expand=True,pady=10)
button.pack(anchor="n",expand=True)

app.mainloop()