from tkinter import*
from PIL import Image,ImageTk
from customer import Customer_Window
from room import Room
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root 
        self.root.title("Hotel Management System")
        self.root.geometry("1550x700+0+0")
        
        img1 = Image.open(r"C:\Users\Shashwat\OneDrive\Desktop\hotel management\images\hotel2.jpeg")
        img1 = img1.resize((1500,200), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=200)


        img2 = Image.open(r"C:\Users\Shashwat\OneDrive\Desktop\hotel management\images\hotel4.jpeg")
        img2 = img2.resize((230,100), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("ALGERIAN",30,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=200,width=1280,height=50)
        
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=250,width=1550,height=620)
        
        
        lbl_menu = Label(main_frame, text="MENU", font=("ALGERIAN", 20, "bold"), bg="black", fg="gold", bd=3, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)


        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=95)

        
        customer_btn = Button(btn_frame, text="CUSTOMER", command=self.customer_det, width=20, font=("ALGERIAN", 12, "bold"), bg="blue", fg="white",bd=0,cursor="hand2")
        customer_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.room,width=20, font=("ALGERIAN", 12, "bold"), bg="blue", fg="white", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)
        
        details_btn = Button(btn_frame, text="DETAILS", width=20, command=self.details_room,font=("ALGERIAN", 12, "bold"), bg="blue", fg="white", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)
        
        #report_btn = Button(btn_frame, text="REPORT", width=20, font=( "ALGERIAN", 12, "bold"), bg="blue", fg="white", bd=0, cursor="hand2")
        #report_btn.grid(row=3, column=0, pady=1)

        #logout_btn = Button(btn_frame, text="LOG OUT", width=20, font=("ALGERIAN", 12, "bold"), bg="blue", fg="white", bd=0, cursor="hand2")
        #logout_btn.grid(row=4, column=0, pady=1)
        
        img3 = Image.open(r"C:\Users\Shashwat\OneDrive\Desktop\hotel management\images\hotel1.jpg")
        img3=img3.resize((1310,990),Image.Resampling.LANCZOS )
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=250,width=1305,height=590)
        
        img5 = Image.open(r"C:\Users\Shashwat\OneDrive\Desktop\hotel management\images\hotel3.jpeg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(self.root, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=445, width=230, height=210)

        
    def customer_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_Window(self.new_window)
        
    def room(self):
        self.new_window=Toplevel(self.root) 
        self.app=Room(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
    
             