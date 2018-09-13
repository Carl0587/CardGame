from tkinter import *



root = Tk()
theLabel = Label(root, text="WAR GAME!!", fg= "blue")
theLabel.pack()
photo = PhotoImage(file ="2_of_clubs.png")
smallerPhoto=photo.subsample(6,8)

label=Label(root,bd=8, image=smallerPhoto)
label.pack()


root.mainloop()