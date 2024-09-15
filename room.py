from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Room :
        def __init__(self, root):
                self.root = root
                self.root.title("Hotel Management System")
                self.root.geometry("1295x550+230+220")
               

# ==========varibales=================
                self.var_contact = StringVar()
                self.var_checkin=StringVar()
                self.var_checkout = StringVar()
                self.var_roomtype = StringVar()
                self.var_roomavailable = StringVar()
                self.var_meal = StringVar()
                self.var_noofdays = StringVar()
                self.var_paidtax = StringVar()
                self.var_actualtotal = StringVar()
                self.var_total = StringVar()

                lbl_title=Label(self.root, text="ROOM BOOKING", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=3, relief=RIDGE)
                lbl_title.place(x=0, y=0, width=1295, height=50)


                img2 = Image.open(r"C:\Users\Shashwat\OneDrive\Desktop\hotel management\images\hotel4.jpeg")
                img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
                self.photoimg2=ImageTk.PhotoImage(img2)

        
                lblimg=Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
                lblimg.place(x=5, y=2, width=100, height=40)

        
                labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("arial", 12, "bold"), padx=2,)
                labelframeleft.place(x=5, y=50, width=425, height=490)

# Customer Contact

                lbl_customer_contact = Label(labelframeleft, text="Customer Contact:", font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
                lbl_customer_contact.grid(row=0, column=0, sticky=W)
                entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact,width=20, font=("times new roman", 13, "bold"))
                entry_contact.grid(row=0, column=1,sticky=W)
        
#Fetch Data Button
      
                btnFetchData = Button(labelframeleft, text="FETCH DATA", font=("times new roman", 8, "bold"), bg="black", fg="gold", width=9)
                btnFetchData.place(x=345,y=4)
        

        
#Check in Date

                check_in_date=Label(labelframeleft, font=("arial", 12, "bold"), text="Check in Date:",padx=2,pady=6) 
                check_in_date.grid(row=1, column=0, sticky=W) 
                txtcheck_in_date=ttk.Entry(labelframeleft, textvariable=self.var_checkin,font=("arial", 13, "bold"), width=29)
                txtcheck_in_date.grid(row=1, column=1)
        


                lbl_Check_out=Label(labelframeleft, font=("arial", 12, "bold"), text="Check Out Date:",padx=2,pady=6)
                lbl_Check_out.grid(row=2,column=0, sticky=W)
                txt_Check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("arial", 13, "bold"), width=29)
                txt_Check_out.grid(row=2,column=1)



#Room Type

                label_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6) 
                label_RoomType.grid(row=3, column=0, sticky=W)
                Combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=27, state="readonly")
                Combo_RoomType["value"] = ("single", "Double", "luxary") 
                Combo_RoomType.current(0)
                Combo_RoomType.grid(row=3, column=1)




#Available Room

                labelRoomAvailable=Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6) 
                labelRoomAvailable.grid(row=4, column=0, sticky=W) 
                txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
                txtRoomAvailable.grid(row=4, column=1)

#Meal

                labelMeal=Label(labelframeleft, font=("arial", 12, "bold"),text="Meal:", padx=2, pady=6)
                labelMeal.grid(row=5, column=0, sticky=W) 
                txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=( "arial", 13, "bold"), width=29)
                txtMeal.grid(row=5, column=1)

#No.of Days

                labelNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"),text="No of Days:", padx=2, pady=6)
                labelNoOfDays.grid(row=6, column=0, sticky=W) 
                txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial", 13, "bold"), width=29)
                txtNoOfDays.grid(row=6, column=1)

#Paid Tax

                labelNoOfDays1=Label(labelframeleft, font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6) 
                labelNoOfDays1.grid(row=7, column=0,sticky=W)
                txtNoOfDays1 = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
                txtNoOfDays1.grid(row=7,column=1)

# Sub Total

                lblNoOfDays2=Label(labelframeleft, font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6) 
                lblNoOfDays2.grid(row=8, column=0, sticky=W)
                txtNoOfDays2 = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=29)
                txtNoOfDays2.grid(row=8, column=1)


# Total Cost

                lblTotal=Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
                lblTotal.grid(row=9, column=0, sticky=W)
                txtTotal = ttk.Entry(labelframeleft, textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
                txtTotal.grid(row=9, column=1)
#Bill Button
                
                btnBill = Button(labelframeleft, text="Bill", command=self.total,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
                btnBill.grid(row=10, column=0, padx=1,sticky=W)
                

                # ============= =======btns==== ====
                btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
                btn_frame.place(x=0, y=400, width=412, height=40)
                
                btnAdd=Button(btn_frame, text="Add", command=self.add_data,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
                btnAdd.grid(row=0, column=0, padx=1)
                
                btnUpadate = Button(btn_frame, text="Update", command=self.update,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
                btnUpadate.grid(row=0, column=1, padx=1)
                
                btnDelete = Button(btn_frame, text="Delete", command=self.mDelete,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
                btnDelete.grid(row=0, column=2, padx=1)
                
                btnReset=Button(btn_frame, text="Reset", command=self.reset,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
                btnReset.grid(row=0, column=3, padx=1)
                
#Table Frame
                
                Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details", font=("ALGERIAN", 12, "bold"), padx=2,)
                Table_Frame.place(x=435, y=50, width=860, height=490)

                self.search_var = StringVar()
                lblSearchBy = Label(Table_Frame, textvariable=self.search_var, text="Search By", font=("ALGERIAN", 12, "bold"), bg="red", fg="white")
                lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

                combo_Search = ttk.Combobox(Table_Frame, font=("arial", 12, "bold"), state="readonly")
                combo_Search["value"] = ("Contact", "Room")
                combo_Search.grid(row=0, column=1)

                self.txt_search = StringVar()
                txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("times new roman", 13, "bold"))
                txtSearch.grid(row=0, column=2, padx=2)

                btnSearch = Button(Table_Frame, text="SEARCH",command=self.search,font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
                btnSearch.grid(row=0, column=3, padx=1)

                btnShowAll = Button(Table_Frame, text="SHOW ALL", command=self.fetch_data,font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
                btnShowAll.grid(row=0, column=4, padx=1)
                
#Show data Table
                
                Det_frame = Frame(Table_Frame, bd=2, relief=RIDGE)
                Det_frame.place(x=0, y=50, width=860, height=350)

                scroll_x = ttk.Scrollbar(Det_frame, orient=HORIZONTAL)
                scroll_y = ttk.Scrollbar(Det_frame, orient=VERTICAL)

                self.room_table = ttk.Treeview(Det_frame, column=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)

                scroll_x.config(command=self.room_table.xview)
                scroll_y.config(command=self.room_table.yview)

                self.room_table.heading("contact", text="Contact")

                self.room_table.heading("checkin", text="Check-in ")
                self.room_table.heading("checkout", text="Check-out")
                self.room_table.heading("roomtype", text="Room Type")
                self.room_table.heading("roomavailable", text="Room No")
                self.room_table.heading("meal", text="Meal")
                self.room_table.heading("noofdays", text="NoOfDays")

                self.room_table["show"] = "headings"
                self.room_table.column("contact", width=100)
                self.room_table.column("checkin", width=100)
                self.room_table.column("checkout",width=100)
                self.room_table.column("roomtype",width=100)
                self.room_table.column("roomavailable",width=100)
                self.room_table.column("meal", width=100)
                self.room_table.column("noofdays",width=100)
                self.room_table.pack(fill=BOTH, expand=1)
                
                self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
                self.fetch_data()
                
        def add_data(self):
                if(): 
                        self.var_contact.get() == "" or self.var_checkin.get() == ""
                        messagebox.showerror("Error","Fill all the fields",parent=self.root)
                else:
                        try:
                                conn = mysql.connector.connect( host="localhost", username="root", password="1234", database="management")
                                my_cursor = conn.cursor()
                                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(),
                                                                                                    self.var_meal.get(),
                                                                                                    self.var_noofdays.get()
                                                                                                
                                                                                                ))
                
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success", "Information Added", parent=self.root)
                        except Exception as es:
                                messagebox.showwarning("Warning", f"Fill All The Fields :{str(es)}", parent=self.root)                
        
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost", username="root", password="1234", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room")
                rows=my_cursor.fetchall()
                if len (rows) !=0:
                    self.room_table.delete (*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
                
        def get_cursor(self,event=""):
                cursor_row=self.room_table.focus() 
                content=self.room_table.item(cursor_row)
                row=content["values"]
        
                self.var_contact.set(row[0]),
                self.var_checkin.set(row[1]),
                self.var_checkout.set(row[2]),
                self.var_roomtype.set(row[3]),
                self.var_roomavailable.set(row[4]),
                self.var_meal.set(row[5]),
                self.var_noofdays.set(row[6])
                
                
        def update (self):
            if self.var_contact.get()=="":
                    messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            else:
                    conn=mysql.connector.connect(host="localhost", username="root",password="1234" ,database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update room set check_in=%s, check_out=%s, roomtype=%s,roomavailable=%s,  meal=%s, noOfdays=%s where Contact=%s", (
                                                                                                                                                                                            
                                                                                                                                                           self.var_checkin.get(),
                                                                                                                                                           self.var_checkout.get(),
                                                                                                                                                           self.var_roomtype.get(),
                                                                                                                                                           self.var_roomavailable.get(),
                                                                                                                                                           self.var_meal.get(),
                                                                                                                                                           self.var_noofdays.get(),
                                                                                                                                                           self.var_contact.get()
                                                                                                                                                           
                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()        
            messagebox.showinfo("Update", "Room details has been updated successfully", parent=self.root)
       
       
        def mDelete(self):
                mDelete=messagebox.askyesno ("Hotel Management System", "Do you want delete this customer", parent=self.root)
                if mDelete>0:
                        conn=mysql.connector.connect (host="localhost", username="root", password="1234", database="management")
                        my_cursor=conn.cursor()
                        query="delete from room where Contact = %s"
                        value=(self.var_contact.get(), )
                        my_cursor.execute(query, value)    
                else:
                        if not mDelete:
                                return
                conn.commit()
                self.fetch_data()
                conn.close() 
                
        def reset (self):
                self.var_contact.set("")
                self.var_checkin.set("")
                self.var_checkout.set("")
                self.var_roomtype.set("")
                self.var_roomavailable.set("")
                self.var_meal.set("")
                self.var_noofdays.set("")        
                self.var_paidtax.set("") 
                self.var_actualtotal.set("") 
                self.var_total.set("") 

       # def Fetch_contact(self): 
        #        if  self.var_contact.get()=="":
         #               messagebox.showerror("Error","Please Enter Contact",parent=self.root)
          #      else:
           #             conn=mysql.connector.connect(host="localhost", username="root", password="1234", database="management")
            #            my_cursor=conn.cursor()
             #           query=("select Name from customer where Mobile=%s")
              #          value=(self.var_conatct.get(),)
               #         my_cursor.execute(query, value)
                #        row=my_cursor.fetchone()
                 #       if row==None:
                  #              messagebox.showerror("Error", "THis number Not Found", parent=self.root)
                   #     else:
                    #            conn.commit()
                     #           conn.close()
                      #          
                       #         showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                        #        showDataframe.place(x=455, y=55,width=300,height=180)
                         #       
                          #      lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                           #     lblName.place(x=0,y=0)
        
        def search (self):
                conn=mysql.connector.connect (host="localhost", username="root", password="1234", database="management")
                my_cursor=conn.cursor()
        
                my_cursor.execute("select * from room where "+str(self.search_var.get()+"LIKE '%"+str(self.txt_search.get())+"%'" ))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.room_table.delete(*self.room_table.get_children())
                        for i in rows:
                                self.room_table.insert("", END, values=i)
                        conn.commit()
                conn.close()
        
        
        def total(self):
                inDate=self.var_checkin.get()
                outDate=self.var_checkout.get()
                inDate=datetime.strptime(inDate,"%d/%m/%Y")
                outDate=datetime.strptime(outDate,"%d/%m/%Y")
                self.var_noofdays.set(abs(outDate-inDate).days)
                
                
                if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="luxary"):
                        q1=float(300)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST = "Rs."+str("%.2f" % ((q5)))
                        TT = "Rs."+str("%.2f" %(q5+((q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actualtotal.set(ST)
                        self.var_total.set(TT)
                        
                elif(self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "single"):
                    q1 = float(300)
                    q2 = float(700)
                    q3 = float(self.var_noofdays.get())
                    q4 = float(q1+q2)
                    q5 = float(q3+q4)
                    Tax = "Rs."+str("%.2f" % ((q5)*0.1))
                    ST = "Rs."+str("%.2f" % ((q5)))
                    TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
                    self.var_paidtax.set(Tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)


if __name__ == "__main__":
        root = Tk()
        obj = Room(root)
        root.mainloop()
