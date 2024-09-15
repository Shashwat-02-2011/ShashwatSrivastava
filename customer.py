from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox 

class Customer_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+0+0")


        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_postal_code=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        


        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("ALGERIAN", 18, "bold"), bg="black", fg="gold", bd=3, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        
        
        Labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("ALGERIAN", 12, "bold"), padx=2,)
        Labelframeleft.place(x=5,y=50,width=425,height=490)
        
        
        lbl_customer_reference=Label(Labelframeleft, text="Customer Ref:", font=("ALGERIAN",12,"bold"),padx=2,pady=6)
        lbl_customer_reference.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_ref, width=29, font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
        
        cname = Label(Labelframeleft, text="Customer Name:", font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(Labelframeleft,textvariable=self.var_name, width=29,font=("times new roman", 13, "bold"))
        txtcname.grid(row=1, column=1)

        lblmname = Label(Labelframeleft, text="Mother Name:" ,font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(Labelframeleft,textvariable=self.var_mother, width=29,font=("times new roman", 13, "bold"))
        txtmname.grid(row=2, column=1)
        
        lbl_gender = Label(Labelframeleft, text="Gender:", font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gender=ttk.Combobox(Labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=3,column=1)
         

        lblPostCode = Label(Labelframeleft, text="Post Code:", font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(Labelframeleft,textvariable=self.var_postal_code, width=29,font=("times new roman", 13, "bold"))
        txtPostCode.grid(row=4, column=1)
        
        lblMobile = Label(Labelframeleft, text="Mobile:", font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(Labelframeleft,textvariable=self.var_mobile, width=29,font=("times new roman", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        lblEmail = Label(Labelframeleft, text="Email:",font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(Labelframeleft,textvariable=self.var_email, width=29,font=("times new roman", 13, "bold"))
        txtEmail.grid(row=6, column=1)
        
        lblNationality = Label(Labelframeleft, text="Nationality:", font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W) 
        combo_Nationality=ttk.Combobox(Labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),state="readonly")
        combo_Nationality["value"]=("Indian","Other")
        combo_Nationality.grid(row=7,column=1)
        
        lblId = Label(Labelframeleft, text="ID Proof ",font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lblId.grid(row=8, column=0, sticky=W)
        combo_Id=ttk.Combobox(Labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),state="readonly")
        combo_Id["value"]=("Aadhar","PAN Card","Passport")
        combo_Id.grid(row=8,column=1)
        
        
        lblIdno = Label(Labelframeleft, text="ID NO.:", font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lblIdno.grid(row=9, column=0, sticky=W)
        txtIDno = ttk.Entry(Labelframeleft,textvariable=self.var_idnumber, width=29,font=("times new roman", 13, "bold"))
        txtIDno.grid(row=9, column=1)
        
        lbladdress = Label(Labelframeleft, text="Address:",font=("ALGERIAN", 12, "bold"), padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky=W)
        txtaddress = ttk.Entry(Labelframeleft,textvariable=self.var_address, width=29,font=("times new roman", 13, "bold"))
        txtaddress.grid(row=10, column=1)
        
        
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd = Button(btn_frame, text="ADD",command=self.add_data, font=("times new roman", 13, "bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update,font=("times new roman", 13, "bold"), bg="black", fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btn_delete = Button(btn_frame, text="Delete", command=self.mDelete,font=("times new roman", 13, "bold"), bg="black", fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1)
        
        btn_reset = Button(btn_frame, text="Reset", command=self.reset,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1)                                                  

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details", font=("ALGERIAN", 12, "bold"), padx=2,)
        Table_Frame.place(x=435, y=50, width=860, height=490)
        
        self.search_var=StringVar()
        lblSearchBy = Label(Table_Frame, textvariable=self.search_var,text="Search By",font=("ALGERIAN", 12, "bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)
        
        combo_Search = ttk.Combobox(Table_Frame, font=("arial", 12, "bold"), state="readonly")
        combo_Search["value"] = ("Mobile", "Reference NO.")
        combo_Search.grid(row=0, column=1)
        
        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search,width=24,font=("times new roman", 13, "bold"))
        txtSearch.grid(row=0, column=2,padx=2)
        
        btnSearch = Button(Table_Frame, text="SEARCH", command=self.search,font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="SHOW ALL", command=self.fetch_data,font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        Det_frame = Frame(Table_Frame, bd=2, relief=RIDGE)
        Det_frame.place(x=0, y=50, width=860, height=350)
        
        scroll_x=ttk.Scrollbar(Det_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Det_frame, orient=VERTICAL)
        
        self.Customer_Details_Table=ttk.Treeview(Det_frame,column=("Ref","Name","Mother Name","Gender","Postal Code","Email","Mobile","Nationality","IdProof","IdNo.","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Customer_Details_Table.xview)
        scroll_y.config(command=self.Customer_Details_Table.yview)
        
        self.Customer_Details_Table.heading("Ref",text="Ref No.")
        self.Customer_Details_Table.heading("Name",text="Name") 
        self.Customer_Details_Table.heading("Mother Name",text="Mother Name")
        self.Customer_Details_Table.heading("Gender",text="Gender")
        self.Customer_Details_Table.heading("Mobile",text="Mobile   ")
        self.Customer_Details_Table.heading("Postal Code",text="Postal Code")
        self.Customer_Details_Table.heading("Email",text="Email")
        self.Customer_Details_Table.heading("Nationality",text="Nationality")
        self.Customer_Details_Table.heading("IdProof",text="IdProof")
        self.Customer_Details_Table.heading("IdNo.",text="IdNo.")
        self.Customer_Details_Table.heading("Address",text="Address")
        
        self.Customer_Details_Table["show"]="headings"
        self.Customer_Details_Table.pack(fill=BOTH,expand=1)
        self.Customer_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    def add_data(self):
        if(): 
            self.var_mobile.get() == "" or self.var_mother.get() == ""
            messagebox.showerror("Error","Fill all the fields",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect( host="localhost", username="root", password="1234", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                    self.var_ref.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_mother.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_postal_code.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_idproof.get(),
                                                                                    self.var_idnumber.get(),
                                                                                    self.var_address.get()
                                                                                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Information Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Fill All The Fields :{str(es)}", parent=self.root)
            
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Customer_Details_Table.delete(*self.Customer_Details_Table.get_children())
            for i in rows:
                self.Customer_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
            
    def get_cursor(self,event=""):
        cursor_row=self.Customer_Details_Table.focus() 
        content=self.Customer_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_ref.set(row[1]),
        self.var_ref.set(row[2]),
        self.var_ref.set(row[3]),
        self.var_ref.set(row[4]),
        self.var_ref.set(row[5]),
        self.var_ref.set(row[6]),
        self.var_ref.set(row[7]),
        self.var_ref.set(row[8]),
        self.var_ref.set(row[9]),
        self.var_ref.set(row[10])
               
      

    def update (self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost", username="root",password="1234" ,database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s, Mother=%s, Gender=%s, Mobile=%s,Postal Code=%s,  Email=%s, Nationalty=%s,IdProof=%s,IdNo.=%s, Address=%s where Ref No.=%s", (
                                                                                                                                                                                            
                                                                                                                                                                                    self.var_ref.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                                    self.var_postal_code.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                                    self.var_idproof.get(),
                                                                                                                                                                                    self.var_idnumber.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            
            
    def mDelete(self):
        mDelete=messagebox.askyesno ("Hotel Management System", "Do you want delete this customer", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect (host="localhost", username="root", password="1234", database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref No. = %s"
            value=(self.var_ref.get(), )
            my_cursor.execute(query, value)    
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()     
        
        
    
    def reset(self):
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set(""),
        self.var_ref.set("")
    
    
    
    def search (self):
        conn=mysql.connector.connect (host="localhost", username="root", password="1234", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get()+"LIKE '%"+str(self.txt_search.get())+"%'" ))
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.Customer_Details_Table.delete(*self.Customer_Details_Table.get_children())
            for i in rows:
                self.Customer_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
if __name__ == "__main__":
    root=Tk()
    obj=Customer_Window(root)
    root.mainloop()