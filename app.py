from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import random
from PIL import Image,ImageTk
import cx_Oracle
import tempfile


class BillApp:
    
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        
        self.root.title("Retail Management")

        

        # ====================Variable==================
        
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.choice(list(range(1000)))
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.product=StringVar()
        self.sub_tot=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.price=IntVar()
        self.qty=IntVar()
        self.search_bill=StringVar()
        self.Tax=10
        


        # =================Product==========================
        self.Category=["select option","snacks","lifestyle","milk products"]
        #==================snacks===========================
        self.subcatsnacks=["Biscuits","Chips","Soft-drinks"]

        self.Biscuits=["Sunfeast","Britannia","Parle"]
        self.price_sunfeast=10
        self.price_britania=10
        self.price_parle=10

        self.chips=["Bingo","Lays","Haldirams"]
        self.price_bingo=10
        self.price_lays=5
        self.price_haldirans=15

        self.softdrinks=["Sprite","Thums-up","Limca"]
        self.price_sprite=90
        self.price_thumsup=65
        self.price_limca=20
        #===================lifestyle==============================
        self.subcatlifestyle=["Bath soap","Dish wash soap","detergents","Face cream"]

        self.Bathsoap=["Santoor","Cinthol","Rexona"]
        self.price_santoor=20
        self.price_cinthol=40
        self.price_rexona=30

        self.dishwasher=["Vim","Exo","Sabena"]
        self.price_vim=10
        self.price_exo=20
        self.price_sabena=40

        self.detergents=["Rin","Surf excel","Tide"]
        self.price_rin=20
        self.price_surfexcel=25
        self.price_tide=30

        self.facecream=["Fair&lovely","Ponds","Fair&handsome"]
        self.price_fair_love=20
        self.price_ponds=10
        self.price_fair_handsome=25

        #=======================Milk===============================
        self.subcatmilk=["milk","curd","paneer"]

        self.milk=["Heritage","Vijaya","Amul"]
        self.price_milk_heritage=30
        self.price_milk_vijaya=26
        self.price_milk_amul=25

        self.curd=["hEritage","vIjaya","aMul"]
        self.price_curd_heritage=15
        self.price_curd_vijaya=20
        self.price_curd_amul=10



        self.paneer=["heritage","vijaya","amul"]
        self.price_paneer_heritage=108
        self.price_paneer_vijaya=100
        self.price_paneer_amul=89


        #Image 1
        img1=Image.open("rh1.jpg")
        img1=img1.resize((420,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(self.root,image=self.photoimage1)
        lbl_img1.place(x=0,y=0,width=420,height=130)
        #Image 2
        img2=Image.open("rh2.jpg")
        img2=img2.resize((420,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(self.root,image=self.photoimage2)
        lbl_img2.place(x=420,y=0,width=420,height=130)
        #Image 3
        img3=Image.open("RH3.jpg")
        img3=img3.resize((420,130),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(self.root,image=self.photoimage3)
        lbl_img3.place(x=843,y=0,width=440,height=130)
        
        

        lbl_tit=Label(self.root,text="RETAIL STORE MANAGEMENT SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red" )
        lbl_tit.place(x=-50,y=130,width=1530,height=50)
        
        

        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=175,width=1520,height=610)

        #Image 4
        img4=Image.open("rh4.jpg")
        img4=img4.resize((420,130),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lbl_img4=Label(Main_frame,image=self.photoimage4)
        lbl_img4.place(x=0,y=155,width=420,height=130)

        #Image 5
        img5=Image.open("rh5.jpg")
        img5=img5.resize((420,130),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        lbl_img5=Label(self.root,image=self.photoimage5)
        lbl_img5.place(x=430,y=340,width=420,height=130)

        #Customer label frame
        cust_frame=LabelFrame(Main_frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="red" )
        cust_frame.place(x=10,y=5,width=350,height=140)
       
        # For Mobile number
        self.lbl_mob=Label(cust_frame,text="Mobile Number:",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2) 
        self.enter_mob=ttk.Entry(cust_frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.enter_mob.grid(row=0,column=1)
       
        # For Name
        self.lbl_name=Label(cust_frame,text="Customer Name:",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=2) 
        self.enter_name=ttk.Entry(cust_frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.enter_name.grid(row=1,column=1)
       
        #For Email
        self.lbl_email=Label(cust_frame,text="Customer Email:",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=2) 
        self.enter_email=ttk.Entry(cust_frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.enter_email.grid(row=2,column=1)

        #Product Label Frame
        prod_frame=LabelFrame(Main_frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="red" )
        prod_frame.place(x=370,y=5,width=540,height=140)
        
        # Category Selection
        self.lbl_category=Label(prod_frame,text="Select Category",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_category.grid(row=0,column=0,sticky=W,padx=5,pady=2) 
        self.combo_categ=ttk.Combobox(prod_frame,font=("arial",12,"bold"),value=self.Category,width=14,state="readonly")
        self.combo_categ.current(0)
        self.combo_categ.grid(row=0,column=1,sticky=W,padx=5,pady=5)
        self.combo_categ.bind("<<ComboboxSelected>>",self.Categoriesfun)
        
        # sub Category Selection
        self.lbl_subcategory=Label(prod_frame,text="Select sub Category",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2) 
        self.combo_subcateg=ttk.Combobox(prod_frame,values=[''],font=("arial",12,"bold"),width=14,state="readonly")
        self.combo_subcateg.grid(row=1,column=1,sticky=W,padx=5,pady=5)
        self.combo_subcateg.bind("<<ComboboxSelected>>",self.productfun)

        # product Selection
        self.lbl_product=Label(prod_frame,text="Select Product",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_product.grid(row=2,column=0,sticky=W,padx=5,pady=2) 
        self.combo_product=ttk.Combobox(prod_frame,textvariable=self.product,font=("arial",12,"bold"),width=14,state="readonly")
        self.combo_product.grid(row=2,column=1,sticky=W,padx=5,pady=5)
        self.combo_product.bind("<<ComboboxSelected>>",self.pricefun)
        
        # price
        self.lbl_price=Label(prod_frame,text="Price",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_price.grid(row=0,column=2,sticky=W,padx=5,pady=2) 
        self.combo_price=ttk.Combobox(prod_frame,textvariable=self.price,font=("arial",12,"bold"),width=10,state="readonly")
        self.combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=5)
        
        # Quantity
        self.lbl_quant=Label(prod_frame,text="Quantity",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_quant.grid(row=1,column=2,sticky=W,padx=5,pady=2) 
        self.combo_quant=ttk.Entry(prod_frame,textvariable=self.qty,font=("arial",12,"bold"),width=10)
        self.combo_quant.grid(row=1,column=3,sticky=W,padx=5,pady=5)

        # search
        search_frame=Frame(Main_frame,bd=5,bg="white")
        search_frame.place(x=910,y=5,width=500,height=300)


        # self.lbl_bill=Label(search_frame,font=("arial",12,"bold"),bg="red",fg="white",text="Bill number")
        # self.lbl_bill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_search=ttk.Entry(search_frame,textvariable=self.search_bill,font=("arial",12,"bold"),width=20)
        self.txt_search.grid(row=0,column=0,padx=2)

        self.btnSearch=Button(search_frame,text="Search bill",command=self.searchfun,font=("arial",15,"bold"),width=10,bg="red",fg="white")
        self.btnSearch.grid(row=0,column=1,sticky=W)

        # Right Frame Bill Area
        Right_label_Frame=LabelFrame(Main_frame,text="Bill Area",font=("times new roman",15,"bold"),bg="white",fg="red")
        Right_label_Frame.place(x=920,y=60,width=340,height=300)
        
        # Scroll bar
        
        scrol_y=Scrollbar(Right_label_Frame,orient=VERTICAL)
        self.textarea=Text(Right_label_Frame,yscrollcommand=scrol_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview())
        self.textarea.pack(fill=BOTH,expand=1) 

        #Billcounter Label Frame
        
        billcount_frame=LabelFrame(Main_frame,font=("times new roman",15,"bold"),bg="white",fg="red" )
        billcount_frame.place(x=0,y=305,width=1520,height=140)
        
        img6=Image.open("rh6.jpg")
        img6=img6.resize((300,150),Image.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)
        lbl_img6=Label(billcount_frame,image=self.photoimage6)
        lbl_img6.place(x=0,y=0,width=300,height=150)
        #Sub total
        
        # self.lbl_subtotal=Label(billcount_frame,text="Sub Total",font=("arial",12,"bold"),bg="white",fg="black")
        # self.lbl_subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2) 
        # enty_quant=ttk.Entry(billcount_frame,font=("arial",12,"bold"),width=10)
        # enty_quant.grid(row=0,column=1,sticky=W,padx=5,pady=5)
        
        # # TAX
        
        # self.lbl_tax=Label(billcount_frame,text="Tax",font=("arial",12,"bold"),bg="white",fg="black")
        # self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2) 
        # enty_tax=ttk.Entry(billcount_frame,font=("arial",12,"bold"),width=10,)
        # enty_tax.grid(row=1,column=1,sticky=W,padx=5,pady=5) 

        # # Amount
        # self.lbl_amntotal=Label(billcount_frame,text="Total Amount",font=("arial",12,"bold"),bg="white",fg="black")
        # self.lbl_amntotal.grid(row=2,column=0,sticky=W,padx=5,pady=2) 
        # enty_amount=ttk.Entry(billcount_frame,font=("arial",12,"bold"),width=10)
        # enty_amount.grid(row=2,column=1,sticky=W,padx=5,pady=5) 

        #Button Frame
        btn_frame=Frame(billcount_frame,bd=5,bg="white")
        btn_frame.place(x=300,y=0)

        self.btnAddtocart=Button(btn_frame,command=self.Additemfun,height=2,text="Add to cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnAddtocart.grid(row=0,column=0 )
        
        self.btnGenBill=Button(btn_frame,command=self.genbillfun,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnGenBill.grid(row=0,column=1 )

        self.btnsavebil=Button(btn_frame,command=self.savebillfun,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnsavebil.grid(row=0,column=2 )

        self.btnPrint=Button(btn_frame,command=self.iprintfun,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnPrint.grid(row=0,column=3 )

        self.btnClear=Button(btn_frame,height=2,command=self.clearfun,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnClear.grid(row=0,column=4 )

        self.btnExit=Button(btn_frame,height=2,text="Exit",command=root.quit,font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnExit.grid(row=0,column=5)
        self.welcomefun()
        self.lis=[]
        # =========================FUNCTIONS==========================================
    def Additemfun(self,event=""):
        
        self.n=self.price.get()
        self.m=self.qty.get()*self.n
        self.lis.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error,Please select product name")
        else:
            self.textarea.insert(END, f" {self.product.get()}\t\t\t{self.qty.get()}\t{self.m}\n")
            self.sub_tot.set(str('Rs.%.2f'%(sum(self.lis))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.lis))-(self.price.get()))*self.Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.lis))+((((sum(self.lis))-(self.price.get()))*self.Tax)/100)))))
    def genbillfun(self):
        if self.product.get()=="":
            messagebox.showerror("Error, please add to cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.lis))))
            self.welcomefun()
            self.textarea.insert(END,f"\n==================================")
            self.textarea.insert(END, f"\n Sub Amount:\t\t{self.sub_tot.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t{self.total.get()}")
            self.textarea.insert(END,f"\n==================================")

    def welcomefun(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\tWelcome to Retail manager")
        self.textarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Email ID: {self.c_email.get()}")
        self.textarea.insert(END,f"\n==================================")
        self.textarea.insert(END,f"\n PRODUCTS\t\t\tQTY\tPrice")
        self.textarea.insert(END,f"\n==================================\n")

    def Categoriesfun(self,event=""):
        if self.combo_categ.get()=="snacks":
            self.combo_subcateg.config(value=self.subcatsnacks)
            self.combo_subcateg.current(0)

        if self.combo_categ.get()=="lifestyle":
            self.combo_subcateg.config(value=self.subcatlifestyle)
            self.combo_subcateg.current(0)
        
        if self.combo_categ.get()=="milk products":
            self.combo_subcateg.config(value=self.subcatmilk)
            self.combo_subcateg.current(0)


    def productfun(self,event=""):
        if self.combo_subcateg.get()=="Biscuits":
            self.combo_product.config(values=self.Biscuits)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="Chips":
            self.combo_product.config(values=self.chips)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="Soft-drinks":
            self.combo_product.config(values=self.softdrinks)
            self.combo_product.current(0)
# ===========lifestyle===============
        if self.combo_subcateg.get()=="Bath soap":
            self.combo_product.config(values=self.Bathsoap)
            self.combo_product.current(0)
        
        if self.combo_subcateg.get()=="Dish wash soap":
            self.combo_product.config(values=self.dishwasher)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="detergents":
            self.combo_product.config(values=self.detergents)
            self.combo_product.current(0)
        
        if self.combo_subcateg.get()=="Face cream":
            self.combo_product.config(values=self.facecream)
            self.combo_product.current(0)
#================milk products=================
        if self.combo_subcateg.get()=="milk":
            self.combo_product.config(values=self.milk)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="curd":
            self.combo_product.config(values=self.curd)
            self.combo_product.current(0)
        if self.combo_subcateg.get()=="paneer":
            self.combo_product.config(values=self.paneer)
            self.combo_product.current(0)
    def pricefun(self,event=""):
        #snacks
        if self.combo_product.get()=="Sunfeast":
            self.combo_price.config(values=self.price_sunfeast)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Britannia":
            self.combo_price.config(values=self.price_britania)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Parle":
            self.combo_price.config(values=self.price_parle)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Bingo":
            self.combo_price.config(values=self.price_bingo)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Lays":
            self.combo_price.config(values=self.price_lays)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Haldirams":
            self.combo_price.config(values=self.price_haldirans)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Sprite":
            self.combo_price.config(values=self.price_sprite)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Thums-up":
            self.combo_price.config(values=self.price_thumsup)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Limca":
            self.combo_price.config(values=self.price_limca)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Santoor":
            self.combo_price.config(values=self.price_santoor)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Cinthol":
            self.combo_price.config(values=self.price_cinthol)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Rexona":
            self.combo_price.config(values=self.price_rexona)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Vim":
            self.combo_price.config(values=self.price_vim)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Exo":
            self.combo_price.config(values=self.price_exo)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Sabena":
            self.combo_price.config(values=self.price_sabena)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Rin":
            self.combo_price.config(values=self.price_rin)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Surf excel":
            self.combo_price.config(values=self.price_surfexcel)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Tide":
            self.combo_price.config(values=self.price_tide)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Fair&lovely":
            self.combo_price.config(values=self.price_fair_love)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Ponds":
            self.combo_price.config(values=self.price_ponds)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Fair&handsome":
            self.combo_price.config(values=self.price_fair_handsome)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Heritage":
            self.combo_price.config(values=self.price_milk_heritage)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Vijaya":
            self.combo_price.config(values=self.price_milk_vijaya)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="Amul":
            self.combo_price.config(values=self.price_milk_amul)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="hEritage":
            self.combo_price.config(values=self.price_curd_heritage)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="vIjaya":
            self.combo_price.config(values=self.price_curd_vijaya)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="aMul":
            self.combo_price.config(values=self.price_curd_amul)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="heritage":
            self.combo_price.config(values=self.price_paneer_heritage)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="vijaya":
            self.combo_price.config(values=self.price_paneer_vijaya)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="amul":
            self.combo_price.config(values=self.price_paneer_amul)
            self.combo_price.current(0)
            self.qty.set(1)
    def savebillfun(self):
        c1_name=self.c_name.get()
        c1_email=self.c_email.get()
        c1_phon=self.c_phon.get()
        total1=self.total.get()
        billno1=self.bill_no.get()
        try:
            con=cx_Oracle.connect("system/sai123#S@localhost:1521/orcl")
            self.cursor=con.cursor()
            self.cursor.execute("insert into customer values(eid_seq.nextval,:1,:2,:3)",(c1_name,c1_email,c1_phon))
            con.commit()
            self.cursor.execute("select * from customer")
            e=self.cursor.fetchall()
            eid=e[-1]
            eid1=eid[0]
            self.cursor.execute("insert into bill values(:1,:2,:3)",(billno1,total1,eid1))
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("there is a problem with oracle",e)
        finally:
            if self.cursor:
                self.cursor.close() 
            if con:
                con.close()
    def searchfun(self):
        try:
            con=cx_Oracle.connect("system/sai123#S@localhost:1521/orcl")
            self.cursor=con.cursor()
            search1=self.search_bill.get()
            self.cursor.execute("select c.cid,c.cname,c.cmail,c.cmob,b.total from customer c,bill b where c.cid=b.cid and b.bid=:value",{'value':search1})
            ans=self.cursor.fetchone()
            
        except cx_Oracle.DatabaseError as e:
            print("there is a problem with oracle",e)
        finally:
            if self.cursor:
                self.cursor.close() 
            if con:
                con.close()
        q1=ans[0]
        q2=ans[1]
        q3=ans[2]
        q4=ans[3]
        q5=ans[4]
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\tDetails of customer")
        self.textarea.insert(END,f"\n==================================")
        self.textarea.insert(END, f"\nCUSTOMER ID            :{q1}")
        self.textarea.insert(END, f"\nCUSTOMER NAME          :{q2}")
        self.textarea.insert(END, f"\nCUSTOMER MAIL          :{q3}")
        self.textarea.insert(END, f"\nCUSTOMER PHONE NUMBER  :{q4}")
        self.textarea.insert(END, f"\nTOTAL BILL             :{q5}")
        self.textarea.insert(END,f"\n==================================")
            
    def iprintfun(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def clearfun(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        self.bill_no.set(random.choice(list(range(1000))))
        self.search_bill.set("")
        self.product.set("")
        self.price.set(0)
        self.qty.set(0)
        self.lis=[0]
        self.total.set("")
        self.sub_tot.set("")
        self.tax_input.set("")
        self.welcomefun()



if __name__=='__main__':
    root=Tk()
    
    obj=BillApp(root)

    root.mainloop()        




