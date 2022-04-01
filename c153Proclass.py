from tkinter import *
import random
root=Tk()
root.title("Random Password Generator")
root.geometry("400x400")
root.configure(background="yellow")
shownew_password_label=Label(root)
old_password=Label(root)
old_entry=Entry(root)

array_3d=[[["1","2","3","4","5","6","7","8"],["Surf","Wave"],["A","B","C","D","E","G","H","I","J"]]]
print(array_3d[0][2][3])
def showPassword():
    get_password=old_entry.get()
    old_password['text']="Old password: "+get_password
    Random_num1=random.randint(0,7)
    Random_num2=random.randint(0,1)
    Random_num3=random.randint(0,8)
    word1=str(array_3d[0][0][Random_num1])
    word2=array_3d[0][1][Random_num2]
    word3=array_3d[0][2][Random_num3]
    shownew_password_label['text']="Generated New Password: "+word1+""+word2+""+word3
    
    
    



btn=Button(root,text="Show Generated Password",bg="black",fg="white",command=showPassword)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
shownew_password_label.place(relx=0.5,rely=0.8,anchor=CENTER)
old_password.place(relx=0.5,rely=0.4,anchor=CENTER)
old_entry.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()